AR601_PREFIX = "a600"

IK_SERVICE = "ik_server"
FK_SERVICE = "fk_server"
TRAJECTORY_SERVICE = "get_trajectory"

LEFT_LEG_FORCE_TORQUE = '/' + AR601_PREFIX + '/LAnkleRoll_ft'
RIGHT_LEG_FORCE_TORQUE = '/' + AR601_PREFIX + '/RAnkleRoll_ft'

JOINT_STATES = '/' + AR601_PREFIX + "/joint_states"
Imu_Topic = '/' + AR601_PREFIX + "/imu"
Pressure_Topic = '/' + AR601_PREFIX + "/pressure"
Temperature_Topic = '/' + AR601_PREFIX + "/temperature"
MagneticField_Topic = '/' + AR601_PREFIX + "/magnetic_field"
SetAudioOn_Topic = '/' + AR601_PREFIX + "/set_audio_on"
CalibrateUchs_Topic = '/' + AR601_PREFIX + "/calibrate_uchs"

ForceTorqueLAnkleRoll_Topic = '/' + AR601_PREFIX + '/LAnkleRoll_ft'
ForceTorqueRAnkleRoll_Topic = '/' + AR601_PREFIX + '/RAnkleRoll_ft'


def joint_topic(joint, command, suffix=""):
    return "/" + AR601_PREFIX + "/" + joint + suffix + "/" + command


def joint_command_topic(joint):
    return joint_topic(joint, "command", "_position_controller")


def joint_pid_topic(joint):
    return joint_topic(joint, "pid", "_position_controller")


def joint_set_status_topic(joint):
    return joint_topic(joint, "set_status")
