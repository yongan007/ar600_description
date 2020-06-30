#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from numpy import pi 
import socket
import os
import subprocess
import json
from ast import literal_eval
import yaml
import struct
import re

from sensor_msgs.msg import JointState
from dynamic_reconfigure.msg import Config
from dynamic_reconfigure.server import Server
from dynamic_reconf_joints.cfg import DynamicConfig
import math
from dynamic_reconfigure.msg import Config
import rospy
from std_msgs.msg import String

def callback(data):
    global positions
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.doubles)
    msgs = data.doubles
    # print(msgs[0].value)
    names = [msg.name for msg in msgs]
    positions =[round(msg.value,2)* (3*math.pi/180) for msgs in msgs]
    print(positions)


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/listener/parameter_updates", Config, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
def talker():
    
    # rospy.init_node('talker', anonymous=True)
    rospy.init_node('talker')

    
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():

        pub1 = rospy.Publisher('/a600/joint1_position_controller/command', Float64, queue_size=10)
        pub2 = rospy.Publisher('/a600/joint2_position_controller/command', Float64, queue_size=10)
        pub3 = rospy.Publisher('/a600/joint3_position_controller/command', Float64, queue_size=10)  
        pub4 = rospy.Publisher('/a600/joint4_position_controller/command', Float64, queue_size=10)
        pub5 = rospy.Publisher('/a600/joint5_position_controller/command', Float64, queue_size=10)
        pub6 = rospy.Publisher('/a600/joint6_position_controller/command', Float64, queue_size=10)    
        pub7 = rospy.Publisher('/a600/joint7_position_controller/command', Float64, queue_size=10)
        pub8 = rospy.Publisher('/a600/joint8_position_controller/command', Float64, queue_size=10)
        pub9 = rospy.Publisher('/a600/joint9_position_controller/command', Float64, queue_size=10)    
        pub10 = rospy.Publisher('/a600/joint10_position_controller/command', Float64, queue_size=10)
        pub11 = rospy.Publisher('/a600/joint11_position_controller/command', Float64, queue_size=10)
        pub12 = rospy.Publisher('/a600/joint12_position_controller/command', Float64, queue_size=10)      
        
        rate = rospy.Rate(10) # 10hz

        # rate.sleep()

        pub1.publish(positions[0])
        pub2.publish(positions[1])
        pub3.publish(positions[2])
        pub4.publish(positions[3])
        # rate.sleep()
        pub5.publish(positions[4])
        pub6.publish(positions[5])

        pub7.publish(positions[6])
        pub8.publish(positions[7])
        pub9.publish(positions[8])
        pub10.publish(positions[9])
        pub11.publish(positions[11])
        pub12.publish(positions[12])

                
        rate.sleep()

    # return pub5

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass