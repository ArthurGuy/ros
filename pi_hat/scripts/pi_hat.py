#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu, MagneticField, Temperature
import serial
from sense_hat import SenseHat
import traceback

sense = SenseHat()
sense.set_rotation(0)
sense.clear()


def get_data():
	try:
    	dir = sense.get_orientation_degrees()
	    msg_dir = Float32()
    	msg_dir.data = float(dir)
	    pub_heading.publish(msg_dir)
	except TypeError:
		rospy.loginfo(dir)
	
    
    msg_humidity = Float32()
    msg_humidity.data = float(sense.get_humidity())
    pub_humidity.publish(msg_humidity)
    
    msg_temp = Temperature()
    msg_temp.temperature = sense.get_temperature()
    pub_temperature.publish(msg_temp)
    
    msg_pressure = Temperature()
    msg_pressure.temperature = sense.get_pressure()
    pub_pressure.publish(msg_pressure)
    
    rospy.loginfo(data)
    
    
rospy.init_node('pi_hat_sensors', anonymous=True)
pub_heading = rospy.Publisher('~bearing', Float32, queue_size=1)

pub_humidity = rospy.Publisher('~humidity', Float32, queue_size=1)

pub_pressure = rospy.Publisher('~pressure', Float32, queue_size=1)

pub_temperature = rospy.Publisher('Temperature', Temperature, queue_size=1)

sense.show_message("Started")


while not rospy.is_shutdown():
    try:
        get_data()
    
    except (KeyboardInterrupt, SystemExit):
        raise 
    except:
        traceback.print_exc()
