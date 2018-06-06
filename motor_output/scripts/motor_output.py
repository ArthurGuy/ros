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



def get_cmd_vel(data):
    x = data.linear.x
    angular = data.angular.z
    sense.clear([x, angular, 0])
    #self.send_cmd_to_arduino(x, angular)

def get_bearing():
    dir = sense.get_compass()
    msg_dir = Float32()
    msg_dir.data = float(dir)
    pub_heading.publish(msg_dir)
    
    
rospy.init_node('car_driver', anonymous=True)
rospy.Subscriber('/cmd_vel', Twist, get_cmd_vel)
pub_heading = rospy.Publisher('~bearing', Float32, queue_size=1)

sense.show_message("Started")


while not rospy.is_shutdown():
    try:
        get_bearing()
    
    except (KeyboardInterrupt, SystemExit):
        raise 
    except:
        traceback.print_exc()
