#!/usr/bin/env python

# this file uses dynamic reconf to publish to joint states in gazebo

import rospy
import socket
import os
import subprocess
import json
import yaml
import struct
import re
import math
import rospy


from std_msgs.msg import Float64
from numpy import pi 
from ast import literal_eval
from sensor_msgs.msg import JointState
from dynamic_reconfigure.msg import Config
from dynamic_reconfigure.server import Server
from dynamic_reconfigure.msg import Config
from std_msgs.msg import String



def callback(data):

    global positions 
    
    global names    
    msgs = data.doubles

    names = [msg.name for msg in msgs]
    print(names)
    positions =[round(msg.value* math.pi/180,2) for msg in msgs]



def talker():
    
    rospy.init_node('talker', anonymous=True)

    rospy.Subscriber("/listener/parameter_updates", Config, callback)

    # rospy.spin()
    rate = rospy.Rate(10) # 10hz


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


    while not rospy.is_shutdown():
        print("position is", positions)
        pub1.publish(positions[0])
        pub2.publish(positions[1])

        pub3.publish(positions[2])
        pub4.publish(positions[3])

        pub5.publish(positions[4])
        pub6.publish(positions[5])

        pub7.publish(positions[6])
        pub8.publish(positions[7])

        pub9.publish(positions[8])
        pub10.publish(positions[9])

        pub11.publish(positions[10])
        pub12.publish(positions[11])
                
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass