#!/usr/bin/env python
# license removed for brevity
# this file jist publish to joint states in gazebo. you launch the gazebo2.launch first and then rosrun this file rosrun control control_dynamic

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


from sensor_msgs.msg import JointState
from dynamic_reconfigure.msg import Config
from dynamic_reconfigure.server import Server

import math
from dynamic_reconfigure.msg import Config
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
# global positions

def callback(data):
    global positions

    msgs = data.doubles
    names = [msg.name for msg in msgs]
    positions =[round(msg.value* math.pi/180,2) for msg in msgs]

    sort_order = [ 4, 5, 7, 3, 1, 10, 8, 9 ,2, 0, 11,6]

    positions =[msg.value for msg in msgs]

    new_positions =[]
    for i in sort_order:
        new_positions.append(positions[i])
    positions = new_positions
    # return positions

def talker():
    
    # global positions

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rospy.Subscriber("/listener/parameter_updates", Config, callback)


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

    while not rospy.is_shutdown():
            

            # rate.sleep()

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