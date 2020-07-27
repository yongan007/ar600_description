#!/usr/bin/env python
import rospy
import unittest
from ar601_kinematics.srv import FK
from ar601_kinematics.srv import FKRequest
from ar601_api.topics import FK_SERVICE
# from ik_test import assert_float_lists_equal


def make_request(left, arr):
    req = FKRequest()
    req.left = left
    req.q1 = arr[0]
    req.q2 = arr[1]
    req.q3 = arr[2]
    req.q4 = arr[3]
    req.q5 = arr[4]
    req.q6 = arr[5]
    return req



def test_fk_left():
    # 0, 0, 0, 0, 0, 0, -0.02, -0.088, 0.7615, 0, 0, 0
    req = make_request(True, [0.0, 0.0, 0, 0, 0, 0.0])
    fk_resp_left = fk_call(req).positions
    print(fk_resp_left)

if __name__ == "__main__":
    rospy.init_node('fk_test')

    rospy.wait_for_service(FK_SERVICE)
    global fk_call
    fk_call = rospy.ServiceProxy(FK_SERVICE, FK)

    test_fk_left()