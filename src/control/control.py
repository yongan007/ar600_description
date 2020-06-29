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

# def client():
#     s = socket.socket()
#     host = '10.91.53.160'
#     # host = "192.168.31.146"
#     port = 9999
#     s.connect((host, port))
#     while True:
#         json_length = struct.unpack(">I", s.recv(4))[0]
#         # now read the JSON data of the given size and JSON decode it
#         json_data = b""  # initiate an empty bytes structure
#         while len(json_data) < json_length:
#             chunk = s.recv(min(4096, json_length - len(json_data)))
#             if not chunk:  # no data, possibly broken connection/bad protocol
#                 break  # just exit for now, you should deal with this case in production
#             json_data += chunk
#         payload = json.loads(json_data.decode())["slaves"][1]["position"]
#         # print(type(payload))
#         return payload
# from joint_receiver import 

        # return message
def talker():
    
    rospy.init_node('talker', anonymous=True)

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
        s = socket.socket()
        host = '10.91.53.160'
        # host = "192.168.31.146"
        port = 9999
        s.connect((host, port))
        while True:
            json_length = struct.unpack(">I", s.recv(4))[0]
            # now read the JSON data of the given size and JSON decode it
            json_data = b""  # initiate an empty bytes structure
            while len(json_data) < json_length:
                chunk = s.recv(min(4096, json_length - len(json_data)))
                if not chunk:  
                    break  
                json_data += chunk
            data = json.loads(json_data.decode())["slaves"][1]["position"]
            print(" I received {} and I am sending it for publishing".format(data))
            position1 = data
            position2 = data
            position3 = data

            rate.sleep()

            pub1.publish(position1)
            pub2.publish(position1)
            pub3.publish(position1)
            pub4.publish(position1)
            # rate.sleep()
            pub5.publish(position1)
            pub6.publish(position1)

            pub7.publish(position2)
            pub8.publish(position2)
            pub9.publish(position2)
            pub10.publish(position2)
            pub11.publish(position2)
            pub12.publish(position2)

            
            rate.sleep()

        return pub5

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass