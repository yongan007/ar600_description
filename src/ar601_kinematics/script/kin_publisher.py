#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String

from numpy import zeros
import ik_call

from ik_call import FkIkCalculation
from ar601_api.topics import joint_command_topic


class PubSub:

    def __init__(self):
        pass

    def publisher(self,position):
        pub = zeros(6)

        for i in range(1,7):
            joint = joint_command_topic("joint"+str(i))
            pub[i-1] = rospy.Publisher(joint, Float64, queue_size=10)
        
        while not rospy.is_shutdown():
            print("position is", positions)
            for i in range(6):
                pub[i].publish(positions[i])  
            rate.sleep()


def main():
    position = {"x": 0.0,"y": 0.0,"z": 0.0}
    oriantation = {"phi_x": 0.0 ,"phi_y":0.0, "phi_z": 0.0}
        
    pose = {"x_t": -0.02,"y_t": -0.088,"z_t": 0.7615}
    ornt = {"phi_x_t": 0.0 ,"phi_y_t":0.0, "phi_z_t": 0.0}

    cal = FkIkCalculation()
    angle = cal.ik_left(position,oriantation,pose,ornt)

    PubSub.publisher(angle)


if __name__ == '__main__':
    # main(sys.argv)
    a = joint_command_topic("joint1")
 

