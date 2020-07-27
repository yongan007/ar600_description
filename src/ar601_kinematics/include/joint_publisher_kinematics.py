#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState


from numpy import zeros
import ik_com_fix
# import ik_call

# from ik_call import FkIkCalculation
from ar601_api.topics import joint_command_topic


def publisher(angles):
    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    pub =[]
    for i in range(6):
        joint = joint_command_topic("joint"+str(i+1))
        # print(type(joint))
        p = rospy.Publisher(joint, Float64, queue_size=10)
        pub.append(p)

    print("Angle of each joint is", angles)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        for i in range(6):
            pub[i].publish(angles[i])  
        rate.sleep()

            
            
    # return pub5


if __name__ == '__main__':

    
    T = transl(-0.006 ,-0.088,0.70)
    R = np.diag(np.ones(4))

    angles = inv_kin(R,T)
    print(angles)

    try:
        publisher(angle)
    except rospy.ROSInterruptException:
        pass