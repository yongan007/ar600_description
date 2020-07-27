#!/usr/bin/env python
import rospy
import unittest
from ar601_kinematics.srv import IK
from ar601_kinematics.srv import IKRequest
from ar601_api.topics import IK_SERVICE

from ar601_kinematics.srv import FK
from ar601_kinematics.srv import FKRequest
from ar601_api.topics import FK_SERVICE


def fk_request(left, arr):
    req = FKRequest()
    req.left = left
    req.q1 = arr[0]
    req.q2 = arr[1]
    req.q3 = arr[2]
    req.q4 = arr[3]
    req.q5 = arr[4]
    req.q6 = arr[5]
    return req

def ik_request(left, position,oriantation,pose,ornt):
    ik_req = IKRequest()
    ik_req.x = position["x"]
    ik_req.y = position["y"]
    ik_req.z = position["z"]
    ik_req.phi_x = oriantation["phi_x"]
    ik_req.phi_y = oriantation["phi_y"]
    ik_req.phi_z = oriantation["phi_z"]
    ik_req.x_t = pose["x_t"]
    ik_req.y_t = pose["y_t"]
    ik_req.z_t = pose["z_t"]
    ik_req.phi_x_t = ornt["phi_x_t"]
    ik_req.phi_y_t = ornt["phi_y_t"]
    ik_req.phi_z_t = ornt["phi_z_t"]
    return ik_req 



class FkIkCalculation(object):
    
    def __init__(self):
        rospy.init_node('ik_test')
        rospy.wait_for_service(IK_SERVICE)
        rospy.wait_for_service(FK_SERVICE)  
        # rospy.loginfo
        self.fk_call = rospy.ServiceProxy(FK_SERVICE, FK)
        self.ik_call = rospy.ServiceProxy(IK_SERVICE, IK)


    def ik_left(self,position,oriantation,pose,ornt):
        ik_req = ik_request(True, position,oriantation,pose,ornt)
        ik_resp_left = self.ik_call(ik_req).angles
        print("IK angle is ", ik_resp_left)
        return ik_resp_left

    def fk_left(self,position,oriantation,pose,ornt):
        angle = list(FkIkCalculation().ik_left(position,oriantation,pose,ornt))
        print("IK angle is ",angle)
        req = fk_request(True, angle)
        fk_resp_left = self.fk_call(req).positions
        print("Fk is : ", fk_resp_left)  

def main():
    rospy.init_node('ik_test')
    position = {"x": 0.0,"y": 0.0,"z": 0.0}
    oriantation = {"phi_x": 0.0 ,"phi_y":0.0, "phi_z": 0.0}
    # 0, 0, 0, 0, 0, 0, -0.02, -0.088, 0.7615, 0, 0, 0
    pose = {"x_t": -0.006,"y_t": -0.088,"z_t": 0.7385}
    ornt = {"phi_x_t": 0.0 ,"phi_y_t":0.0, "phi_z_t": 0.0}

    fkcal = FkIkCalculation()
    fkcal.ik_left(position,oriantation,pose,ornt)

      

if __name__ == "__main__":
    main()

