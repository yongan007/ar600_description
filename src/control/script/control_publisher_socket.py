#!/usr/bin/env python

# this file uses dynamic reconf to publish to joint states in gazebo. It works with client_new 


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

import socket
import sys
import json
import struct

from std_msgs.msg import Float64
from numpy import pi 
from ast import literal_eval
from sensor_msgs.msg import JointState
from dynamic_reconfigure.msg import Config
from dynamic_reconfigure.server import Server
from dynamic_reconfigure.msg import Config
from std_msgs.msg import String

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        global conn
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

        conn, address = s.accept()
        print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))


    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)


def callback(data):

    global positions
    global names
    global msgs
    msgs = data.doubles

    names = [msg.name for msg in msgs]
    # joints =["RHipR", "RHipS","RHipF","RKnee", "RFootF","RFootS","LHipR", "LHipS","LHipF","LKnee", "LFootF","LFootS"]
    
    # joints=['LKnee',0 'RFootF',1 'LHipF'2, 'RKnee'3, 'RHipR'4, 'RHipS'5, 'LFootS'6, 'RHipF'7, 'LHipR'8, 'LHipS'9, 'RFootS'10, 'LFootF'11]
    
    positions =[round(msg.value* math.pi/180,2) for msg in msgs]
    sort_order = [ 4, 5, 7, 3, 1, 10, 8, 9 ,2, 0, 11,6]

    # positions =[msg.value for msg in msgs]

    new_positions =[]
    for i in sort_order:
        new_positions.append(positions[i])
    positions = new_positions

def talker():
    create_socket()
    bind_socket()
    
    rospy.init_node('talker', anonymous=True)


    rospy.Subscriber("/listener/parameter_updates", Config, callback)

    # s = socket.socket()
    # host = ""
    # port = 9999

    # s.bind((host, port))
    # s.listen(5)
    # conn, address = s.accept()
    # print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))


    rate = rospy.Rate(20) # 10hz

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
        # socket_accept()
        send_commands(conn)
        # print(names)
        # print(msgs)

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

        send_commands(conn)
        rate.sleep()

    conn.shutdown()
    conn.close()
    


# Send commands to client/victim or a friend
def send_commands(conn):
    # while True:
    joints =["R.HipR", "R.HipS","R.HipF","R.Knee", "R.FootF","R.FootS","L.HipR", "L.HipS","L.HipF","L.Knee", "L.FootF","L.FootS"]

    data ={"slaves":[{"name": joints[0], "mode": "position", "target":positions[0],"velocity": 1, "acceleration": 0.001},
            {"name": joints[1], "mode": "position", "target":positions[1],"velocity": 1, "acceleration": 0.001},
            {"name": joints[2], "mode": "position", "target": positions[2],"velocity": 1, "acceleration": 0.001},
            {"name": joints[3], "mode": "position", "target":positions[3],"velocity": 1, "acceleration": 0.001},
            {"name": joints[4], "mode": "position", "target": positions[4],"velocity": 1, "acceleration": 0.001},
            {"name": joints[5], "mode": "position", "target":positions[5],"velocity": 1, "acceleration": 0.001},
            {"name": joints[6], "mode": "position", "target": positions[6],"velocity": 1, "acceleration": 0.001},
            {"name": joints[7], "mode": "position", "target":positions[7],"velocity": 1, "acceleration": 0.001},
            {"name": joints[8], "mode": "position", "target": positions[8],"velocity": 1, "acceleration": 0.001},
            {"name": joints[9], "mode": "position", "target":positions[9],"velocity": 1, "acceleration": 0.001},
            {"name": joints[10], "mode": "position", "target": positions[10],"velocity": 1, "acceleration": 0.001},
            {"name": joints[11], "mode": "position", "target":positions[11],"velocity": 1, "acceleration": 0.001}
            ]}

    # conn.send(json.dumps(data).encode())
    data = json.dumps(data).encode()
    conn.sendall(struct.pack(">I", len(data)))  # pack as BE 32-bit unsigned int
    # now send the JSON payload itself
    conn.sendall(data)



if __name__ == '__main__':
    try:
        talker()
 
    except rospy.ROSInterruptException:
        pass