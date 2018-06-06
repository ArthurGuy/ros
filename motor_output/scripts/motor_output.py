#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu, MagneticField
import serial
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
sense.clear()

class driver:
    def __init__(self):
        # init ros
        rospy.init_node('car_driver', anonymous=True)
        rospy.Subscriber('/cmd_vel', Twist, self.get_cmd_vel)
        
        sense.show_message("Started")
        
        #self.ser = serial.Serial('/dev/ttyUSB0', 115200)
        #self.get_arduino_message()
        
        pub_heading = rospy.Publisher('~bearing', Float32, queue_size=1)
        
        self.get_bearing()

    # get cmd_vel message, and get linear velocity and angular velocity
    def get_cmd_vel(self, data):
        x = data.linear.x
        angular = data.angular.z
        sense.clear([x, angular, 0])
        #self.send_cmd_to_arduino(x, angular)
        
    def get_bearing(self):
        dir = sense.get_compass()
        msg_dir = Float32()
        msg_dir.data = float(dir)
        pub_heading.publish(msg_dir)

    # translate x, and angular velocity to PWM signal of each wheels, and send to arduino
    def send_cmd_to_arduino(self, x, angular):
        # calculate right and left wheels' signal
        right = int((x + angular) * 50)
        left = int((x - angular) * 50)
        # format for arduino
        message = "{},{},{},{},{},{}*".format(right, left, right, left, right, left)
        print message
        # send by serial 
        self.ser.write(message)

    # receive serial text from arduino and publish it to '/arduino' message
    def get_arduino_message(self):
        pub = rospy.Publisher('arduino', String, queue_size=10)
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            message = self.ser.readline()
            pub.publish(message)
            r.sleep()

if __name__ == '__main__':
    try:
        d = driver()
    except rospy.ROSInterruptException: 
        pass
