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
import math

from sensor_msgs.msg import JointState
# from sensor_msgs.msg import Jo
def talker():

    rospy.init_node('joint_state_publisher')

    joint_state = JointState()

    joint_pub = rospy.Publisher("joint_states", JointState, queue_size=1)
    
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        s = socket.socket()

        # lab ip
        # host = "192.168.31.146"
        # home ip
        host = '10.91.53.160'

        port = 9999
        s.connect((host, port))
        rate = rospy.Rate(50)
        while True:

            json_length = struct.unpack(">I", s.recv(4))[0]
            # now read the JSON data of the given size and JSON decode it
            json_data = b""  # initiate an empty bytes structure
            while len(json_data) < json_length:
                chunk = s.recv(min(4096, json_length - len(json_data)))
                if not chunk:  
                    break  
                json_data += chunk

            data = json.loads(json_data.decode())["slaves"]
            
            RhipR_pos =data[1]["position"]
            RhipS_pos =data[2]["position"]
            RhipF_pos =data[3]["position"]

            RKnee_pos = data[4]["position"]
            RFootF_pos = data[5]["position"]
            RFootS_pos = data[6]["position"]

            LhipR_pos =data[8]["position"]
            LhipS_pos =data[9]["position"]
            LhipF_pos =data[10]["position"]

            LKnee_pos = data[11]["position"]
            LFootF_pos = data[12]["position"]
            LFootS_pos = data[13]["position"]

            RhipR_vel =data[1]["velocity"]
            RhipS_vel =data[2]["velocity"]
            RhipF_vel =data[3]["velocity"]

            RKnee_vel = data[4]["velocity"]
            RFootF_vel = data[5]["velocity"]
            RFootS_vel = data[6]["velocity"]

            LhipR_vel =data[8]["velocity"]
            LhipS_vel =data[9]["velocity"]
            LhipF_vel =data[10]["velocity"]

            LKnee_vel = data[11]["velocity"]
            LFootF_vel = data[12]["velocity"]
            LFootS_vel = data[13]["velocity"] 

            joint_name = ["R.HipR", "R.HipS","R.HipF","R.Knee", 
                          "R.FootF","R.FootS","R.HipR", "R.HipS",
                          "L.HipF","L.Knee", "L.FootF","L.FootS"]

            # joint_names = [R_HipR, R_HipS, R_Knee_Upper, R_Knee_Lower, R_FootR, R_FootS, L_HipR, L_HipS, L_Knee_upper,
            # L_Knee_Lower, L_FootR, L_FootS]
            joint_names= ['R_HipR', 'R_HipS', 'R_Knee_Upper', 'R_Knee_Lower', 
                        'R_FootR', 'R_FootS', 'L_HipR', 'L_HipS', 
                        'L_Knee_upper', 'L_Knee_Lower', 'L_FootR', 'L_FootS', ]

            positions = [RhipR_pos,RhipS_pos,RhipF_pos,RKnee_pos, RFootF_pos,
                        RFootS_pos,LhipR_pos, LhipS_pos,LhipF_pos,LKnee_pos,
                        LFootF_pos,LFootS_pos]

            velocity = [RhipR_vel,RhipS_vel,RhipF_vel,RKnee_vel, RFootF_vel,
                        RFootS_vel,LhipR_vel, LhipS_vel,LhipF_vel,LKnee_vel,
                        LFootF_vel,LFootS_vel]

            positions = [round(pos*math.pi/180,2) for pos in positions]
            velocity = [round(vel) for vel in velocity]

            print(positions)

            joint_state = JointState()
            joint_state.header.stamp = rospy.Time.now()
            joint_state.name += joint_names
            joint_state.effort+= []
            joint_state.position+= positions

            joint_pub.publish(joint_state)

            rate.sleep()

        return pub5

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass