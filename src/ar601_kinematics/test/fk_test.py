#!/usr/bin/env python
import rospy
import unittest
from ar601_kinematics.srv import FK
from ar601_kinematics.srv import FKRequest
from ar601_api.topics import FK_SERVICE
from ik_test import assert_float_lists_equal


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


class TestFK(unittest.TestCase):
    def test_fk_left(self):
        # 0, 0, 0, 0, 0, 0, -0.02, -0.088, 0.7615, 0, 0, 0
        req = make_request(True, [-0, 0, -1.82501e-08, 3.65002e-08, -1.82501e-08, 0])
        fk_resp_left = fk_call(req).positions
        assert_float_lists_equal(self, [-0.02, -0.088, 0.7615], fk_resp_left)

        # # 0, 0, 0, 0, -.1, -.1, -0.1, -0.07, 0.7, -.1, -.1, -0.1,
        # req = make_request(True, [9.22518e-20, 0.10334171876565033, -0.48736335282347215,
        #                           0.9659896992142543, -0.47862634639078205, -0.0033417187656503288])
        # fk_resp_left = fk_call(req).positions
        # assert_float_lists_equal(self, [-0.1, -0.07, 0.7], fk_resp_left)

        # # 0, 0, 0, 0, -.01, -.01, -0.01, -0.075, 0.72, -.01, -.01, -.01
        # req = make_request(True, [-8.675711879108144e-19, -0.013059073726849493, -0.3544968765178264,
        #                           0.778298453718839, -0.4238015772010127, 0.023059073726849493])
        # fk_resp_left = fk_call(req).positions
        # assert_float_lists_equal(self, [-0.01, -0.075, 0.72], fk_resp_left)

        # 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0,
        req = make_request(True, [-0.0, -0.17472941706619638, -0.40075532150841026, 0.8804885112539778,
                                  -0.47973318974556756, 0.17472941706619635])
        fk_resp_left = fk_call(req).positions
        assert_float_lists_equal(self, [0, 0, 0.7], fk_resp_left)

        # 0, 0, 0, 0, 0, 0, 0, -0.088, 0.7, 0, 0, 0,
        req = make_request(True, [-0.0, 0.0, -0.4313862566518265, 0.9429702240201357, -0.5115839673683092, 0.0])
        fk_resp_left = fk_call(req).positions
        assert_float_lists_equal(self, [0, -0.088, 0.7], fk_resp_left)

    def test_fk_right(self):
        # 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0,
        req = make_request(False, [-0.0, 0.17472941706619638, -0.40075532150841026, 0.8804885112539778,
                                   -0.47973318974556756, -0.17472941706619635])
        fk_resp_right = fk_call(req).positions
        assert_float_lists_equal(self, [0, 0, 0.7], fk_resp_right)

        # 0, 0, 0, 0, 0, 0, -0.02, -0.088, 0.7, 0, 0, 0
        req = make_request(False, [0, 0.339397540742941, -0.336153635008036, 0.672307270016072, -0.336153635008036,
                                   -0.339397540742941])
        fk_resp_right = fk_call(req).positions
        assert_float_lists_equal(self, [-0.02, -0.088, 0.7], fk_resp_right)

        # # 0,0,0,0,.1,.1,0.01,-0.07,0.7,-.1,-.1,-.01
        # req = make_request(False, [0.0447843360067726, 0.427051901032257, -0.148159299394971, 0.556309619469387,
        #                            -0.20215182312532, -0.322833762970801])
        # fk_resp_right = fk_call(req).positions
        # assert_float_lists_equal(self, [0.01, -0.07, 0.7], fk_resp_right)

        # # 0, 0, 0, 0, -.01, -.01, -0.01, -0.075, 0.72, -.01, -.01, -.01
        # req = make_request(False, [0.04478433600677259, 0.4270519010322574, -0.1481592993949721,
        #                            0.5563096194693885, -0.20215182312532048, -0.3228337629708014])
        # fk_resp_right = fk_call(req).positions
        # assert_float_lists_equal(self, [-0.01, -0.075, 0.72], fk_resp_right)


if __name__ == "__main__":
    rospy.init_node('fk_test')

    rospy.wait_for_service(FK_SERVICE)
    global fk_call
    fk_call = rospy.ServiceProxy(FK_SERVICE, FK)

    import rostest

    rostest.rosrun('ar601_kinematics', 'fk_test', TestFK)
