#!/usr/bin/env python
import rospy
import unittest
from ar601_kinematics.srv import IK
from ar601_kinematics.srv import IKRequest
from ar601_api.topics import IK_SERVICE


def assert_float_lists_equal(tc, exp, act):
    tc.assertEqual(len(exp), len(act), "lens should be equal")
    for i in range(len(exp)):
        tc.assertAlmostEqual(exp[i], act[i], 9,  # accuracy for test
                             "on index {0} numbers are not equals, expected: {1}, actual: {2}".format(i, exp, act))


class TestIK(unittest.TestCase):
    def test_ik_left(self):
        # 0, 0, 0, 0, 0, 0, -0.02, -0.088, 0.7615, 0, 0, 0
        ik_req = IKRequest()
        ik_req.left = True
        ik_req.x_t = -0.02
        ik_req.y_t = -0.088
        ik_req.z_t = 0.7615
        ik_resp_left = ik_call(ik_req).angles
        assert_float_lists_equal(self, [-0, 0, -1.82501e-08, 3.65002e-08, -1.82501e-08, 0], ik_resp_left)
        # 0, 0, 0, 0, -.1, -.1, -0.1, -0.07, 0.7, -.1, -.1, -0.1,
        ik_req = IKRequest()
        ik_req.left = True
        ik_req.phi_y = -0.1
        ik_req.phi_z = -0.1
        ik_req.x_t = -0.1
        ik_req.y_t = -0.07
        ik_req.z_t = 0.7
        ik_req.phi_x_t = -0.1
        ik_req.phi_y_t = -0.1
        ik_req.phi_z_t = -0.1
        ik_resp_left = ik_call(ik_req).angles
        assert_float_lists_equal(self, [9.22518e-20, 0.10334171876565033, -0.48736335282347215,
                                        0.9659896992142543, -0.47862634639078205, -0.0033417187656503288], ik_resp_left)
        # 0, 0, 0, 0, -.01, -.01, -0.01, -0.075, 0.72, -.01, -.01, -.01
        ik_req = IKRequest()
        ik_req.left = True
        ik_req.phi_y = -0.01
        ik_req.phi_z = -0.01
        ik_req.x_t = -0.01
        ik_req.y_t = -0.075
        ik_req.z_t = 0.72
        ik_req.phi_x_t = -0.01
        ik_req.phi_y_t = -0.01
        ik_req.phi_z_t = -0.01
        ik_resp_left = ik_call(ik_req).angles
        assert_float_lists_equal(self, [-8.675711879108144e-19, -0.013059073726849493, -0.3544968765178264,
                                        0.778298453718839, -0.4238015772010127, 0.023059073726849493], ik_resp_left)
        # 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0,
        ik_req = IKRequest()
        ik_req.left = True
        ik_req.z_t = 0.7
        ik_resp_left = ik_call(ik_req).angles
        assert_float_lists_equal(self, [-0.0, -0.17472941706619638, -0.40075532150841026, 0.8804885112539778,
                                        -0.47973318974556756, 0.17472941706619635], ik_resp_left)
        # 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0,
        ik_req = IKRequest()
        ik_req.left = True
        ik_req.y_t = -0.088
        ik_req.z_t = 0.7
        ik_resp_left = ik_call(ik_req).angles
        assert_float_lists_equal(self, [-0.0, 0.0, -0.4313862566518265, 0.9429702240201357, -0.5115839673683092, 0.0],
                                 ik_resp_left)

    def test_ik_right(self):
        # 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0,
        ik_req = IKRequest()
        ik_req.left = False
        ik_req.z_t = 0.7
        ik_resp_right = ik_call(ik_req).angles
        assert_float_lists_equal(self, [-0.0, 0.17472941706619638, -0.40075532150841026, 0.8804885112539778,
                                        -0.47973318974556756, -0.17472941706619635], ik_resp_right)
        # 0, 0, 0, 0, 0, 0, -0.02, -0.088, 0.7, 0, 0, 0
        ik_req = IKRequest()
        ik_req.left = False
        ik_req.x_t = -0.02
        ik_req.y_t = -0.088
        ik_req.z_t = 0.7
        ik_resp_right = ik_call(ik_req).angles
        assert_float_lists_equal(self, [0, 0.339397540742941, -0.336153635008036, 0.672307270016072, -0.336153635008036,
                                        -0.339397540742941], ik_resp_right)
        # 0,0,0,0,.1,.1,0.01,-0.07,0.7,-.1,-.1,-.01
        ik_req = IKRequest()
        ik_req.left = False
        ik_req.phi_y = 0.1
        ik_req.phi_z = 0.1
        ik_req.x_t = 0.01
        ik_req.y_t = -0.07
        ik_req.z_t = 0.7
        ik_req.phi_x_t = -0.1
        ik_req.phi_y_t = -0.1
        ik_req.phi_z_t = -0.01
        ik_resp_right = ik_call(ik_req).angles
        assert_float_lists_equal(self, [0.0447843360067726, 0.427051901032257, -0.148159299394971, 0.556309619469387,
                                        -0.20215182312532, -0.322833762970801], ik_resp_right)
        # 0, 0, 0, 0, -.01, -.01, -0.01, -0.075, 0.72, -.01, -.01, -.01
        ik_req = IKRequest()
        ik_req.left = False
        ik_req.phi_y = -0.01
        ik_req.phi_z = -0.01
        ik_req.x_t = -0.01
        ik_req.y_t = -0.075
        ik_req.z_t = 0.72
        ik_req.phi_x_t = -0.01
        ik_req.phi_y_t = -0.01
        ik_req.phi_z_t = -0.01
        assert_float_lists_equal(self, [0.04478433600677259, 0.4270519010322574, -0.1481592993949721,
                                        0.5563096194693885, -0.20215182312532048, -0.3228337629708014], ik_resp_right)


if __name__ == "__main__":
    rospy.init_node('ik_test')

    rospy.wait_for_service(IK_SERVICE)
    global ik_call
    ik_call = rospy.ServiceProxy(IK_SERVICE, IK)

    import rostest

    rostest.rosrun('ar601_kinematics', 'ik_test', TestIK)
