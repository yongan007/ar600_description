import rospy
from ar601_api.topics import JOINT_STATES
from sensor_msgs.msg import JointState
from ar601_api.constants import LOOP_RATE


class JointStatesWrapper:
    def __init__(self, js_msg):
        self.js_msg = js_msg
        self.names_map = {}
        for i in range(len(js_msg.name)):
            self.names_map[js_msg.name[i]] = i

    def position(self, joint):
        if joint not in self.names_map:
            raise KeyError("joint (" + joint + ") not found in names: " + str(self.js_msg.name))
        return self.js_msg.position[self.names_map[joint]]


def get_joint_states():
    return JointStatesWrapper(rospy.wait_for_message(JOINT_STATES, JointState, timeout=4))


def move_to_target(target_pos, publishers, velocity=0.009):
    """
     Read joint_states and publish commands to move to target_pos
     :param target_pos: Dict, where key is joint name and value - target position
     :param publishers: Dict, where key is joint name and value - command publisher
     """
    joint_states = get_joint_states()
    max_value = 0
    for joint in target_pos:
        max_value = max(max_value, abs(target_pos[joint] - joint_states.position(joint)))

    if velocity > 0.009:  # max and default velocity
        velocity = 0.009
    steps = int(max_value / velocity)

    rate = rospy.Rate(LOOP_RATE)
    for i in range(steps):
        for joint in target_pos:
            init_pos = joint_states.position(joint)
            next_v = init_pos + (target_pos[joint] - init_pos) * (i + 1) / steps
            publishers[joint].publish(next_v)
        rate.sleep()
