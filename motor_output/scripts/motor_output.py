#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu, MagneticField, Temperature
import serial
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(0)
sense.clear()



def get_cmd_vel(data):
    #rospy.loginfo(data)
    x = data.linear.x
    angular = data.angular.z
    sense.clear([int(data.linear.x), int(data.linear.y), int(data.linear.z)])

def get_new_temp(data):
	sense.show_message(str(int(data.temperature)))
	#sense.set_pixel(0, 0, int(data.temperature), 0, 255)



rospy.init_node('motor_output', anonymous=True)
rospy.Subscriber('/cmd_vel', Twist, get_cmd_vel)
rospy.Subscriber('/Temperature', Temperature, get_new_temp)

sense.show_message("Started")


while not rospy.is_shutdown():
    try:
        time.sleep(1)
    
    except (KeyboardInterrupt, SystemExit):
        raise 
    except:
        traceback.print_exc()
