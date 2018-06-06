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
    #rospy.loginfo(data)
    x = data.linear.x
    angular = data.angular.z
    sense.clear([int(data.linear.x), int(data.linear.y), int(data.linear.z)])


rospy.init_node('motor_output', anonymous=True)
rospy.Subscriber('/cmd_vel', Twist, get_cmd_vel)

sense.show_message("Started")


while not rospy.is_shutdown():
    try:
        
    
    except (KeyboardInterrupt, SystemExit):
        raise 
    except:
        traceback.print_exc()
