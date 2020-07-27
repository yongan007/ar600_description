#!/usr/bin/env python
from __future__ import division
from ar601_hardware.device import *
from ar601_api.joints import *

# Legs
RAnkleRoll = JointDevice(joint=RAnkleRoll_Joint, p=1000, i=1, ilim=244, buf_num=1, reverse=True, min_pos=-1700,
                         max_pos=1700, device_num=1)
RAnklePitch = JointDevice(joint=RAnklePitch_Joint, p=1000, i=1, ilim=-352, buf_num=2, reverse=True, min_pos=-6000,
                          max_pos=3200, device_num=2)
RKneePitch = JointDevice(joint=RKneePitch_Joint, p=1000, i=1, ilim=3628, buf_num=3, reverse=True, min_pos=-500,
                         max_pos=9000, device_num=3)
RHipPitch = JointDevice(joint=RHipPitch_Joint, p=1000, i=1, ilim=2532, buf_num=4, reverse=False, min_pos=-6000,
                        max_pos=4000, device_num=4)
RHipRoll = JointDevice(joint=RHipRoll_Joint, p=1000, i=1, ilim=-1227, buf_num=5, reverse=False, min_pos=-1800,
                       max_pos=1100, device_num=5)
RHipYaw = JointDevice(joint=RHipYaw_Joint, p=1000, i=1, ilim=-4385, buf_num=6, reverse=False, min_pos=-1000,
                      max_pos=1000, device_num=6)
right_leg_joints = [RAnkleRoll, RAnklePitch, RKneePitch, RHipPitch, RHipRoll, RHipYaw]
LAnkleRoll = JointDevice(joint=LAnkleRoll_Joint, p=1000, i=1, ilim=3720, buf_num=7, reverse=True, min_pos=-1700,
                         max_pos=1700, device_num=7)
LAnklePitch = JointDevice(joint=LAnklePitch_Joint, p=1000, i=1, ilim=-115, buf_num=8, reverse=False, min_pos=-6000,
                          max_pos=3200, device_num=8)
LKneePitch = JointDevice(joint=LKneePitch_Joint, p=1000, i=1, ilim=-211, buf_num=9, reverse=False, min_pos=-500,
                         max_pos=9000, device_num=9)
LHipPitch = JointDevice(joint=LHipPitch_Joint, p=1000, i=1, ilim=7918, buf_num=10, reverse=True, min_pos=-6000,
                        max_pos=4000, device_num=10)
LHipRoll = JointDevice(joint=LHipRoll_Joint, p=1000, i=1, ilim=-236, buf_num=11, reverse=False, min_pos=-1100,
                       max_pos=1800, device_num=11)
LHipYaw = JointDevice(joint=LHipYaw_Joint, p=1000, i=1, ilim=-298, buf_num=12, reverse=False, min_pos=-1000,
                      max_pos=1000, device_num=12)
left_leg_joints = [LAnkleRoll, LAnklePitch, LKneePitch, LHipPitch, LHipRoll, LHipYaw]
legs_joints = left_leg_joints + right_leg_joints
# Arms
RElbowYaw = JointDevice(joint=RElbowYaw_Joint, p=600, i=1, ilim=-14264, buf_num=49, reverse=False, min_pos=-300,
                        max_pos=9000, device_num=17)
RElbowPitch = JointDevice(joint=RElbowPitch_Joint, p=600, i=1, ilim=3963, buf_num=50, reverse=False, min_pos=2000,
                          max_pos=5500, device_num=18)
RShoulderRoll = JointDevice(joint=RShoulderRoll_Joint, p=800, i=1, ilim=2544, buf_num=51, reverse=False, min_pos=-500,
                            max_pos=8000, device_num=19)
RShoulderPitch = JointDevice(joint=RShoulderPitch_Joint, p=800, i=1, ilim=7066, buf_num=52, reverse=False,
                             min_pos=-10500,
                             max_pos=550, device_num=20)
RForearmPitch = JointDevice(joint=RForearmPitch_Joint, p=5000, i=0, ilim=505, buf_num=53, reverse=True, min_pos=-500,
                            max_pos=543, device_num=21)
LElbowYaw = JointDevice(joint=LElbowYaw_Joint, p=600, i=1, ilim=16220, buf_num=24, reverse=False, min_pos=-9000,
                        max_pos=300, device_num=33)
LElbowPitch = JointDevice(joint=LElbowPitch_Joint, p=600, i=1, ilim=7696, buf_num=25, reverse=True, min_pos=-2000,
                          max_pos=5500, device_num=34)
LShoulderRoll = JointDevice(joint=LShoulderRoll_Joint, p=500, i=1, ilim=-7535, buf_num=26, reverse=False, min_pos=-8000,
                            max_pos=500, device_num=35)
LShoulderPitch = JointDevice(joint=LShoulderPitch_Joint, p=800, i=1, ilim=4523, buf_num=27, reverse=True,
                             min_pos=-10500,
                             max_pos=500, device_num=36)
LForearmPitch = JointDevice(joint=LForearmPitch_Joint, p=5000, i=0, ilim=161, buf_num=46, reverse=False, min_pos=-543,
                            max_pos=500, device_num=51)
right_arm_joints = [RElbowYaw, RElbowPitch, RShoulderRoll, RShoulderPitch, RForearmPitch]
left_arm_joints = [LElbowYaw, LElbowPitch, LShoulderRoll, LShoulderPitch, LForearmPitch]
# Right wrist
RWristRoll = JointDevice(joint=RWristRoll_Joint, p=-10000, i=2, ilim=1111, buf_num=54, reverse=True, min_pos=-100,
                         max_pos=250, device_num=22)
RWristYaw = JointDevice(joint=RWristYaw_Joint, p=-10000, i=2, ilim=1254, buf_num=55, reverse=False, min_pos=-140,
                        max_pos=170, device_num=23)
RPinky = JointDevice(joint=RPinky_Joint, p=4000, i=0, ilim=1854, buf_num=56, reverse=True, min_pos=-150, max_pos=1700,
                     device_num=24)
RRing = JointDevice(joint=RRing_Joint, p=9000, i=0, ilim=1943, buf_num=57, reverse=True, min_pos=-100, max_pos=1700,
                    device_num=25)
RMiddle = JointDevice(joint=RMiddle_Joint, p=9000, i=0, ilim=1767, buf_num=59, reverse=True, min_pos=-120, max_pos=1700,
                      device_num=27)
RIndex = JointDevice(joint=RIndex_Joint, p=9000, i=0, ilim=1713, buf_num=58, reverse=True, min_pos=-200, max_pos=2000,
                     device_num=26)
RThumb = JointDevice(joint=RThumb_Joint, p=9000, i=0, ilim=2038, buf_num=60, reverse=True, min_pos=0, max_pos=1700,
                     device_num=28)
right_wrist_joints = [RWristRoll, RWristYaw, RPinky, RRing, RMiddle, RIndex, RThumb]
# Left wrist
LWristRoll = JointDevice(joint=LWristRoll_Joint, p=10000, i=0, ilim=595, buf_num=29, reverse=False, min_pos=-120,
                         max_pos=90, device_num=52)
LWristYaw = JointDevice(joint=LWristYaw_Joint, p=10000, i=0, ilim=-1175, buf_num=30, reverse=True, min_pos=-90,
                        max_pos=250, device_num=53)
LPinky = JointDevice(joint=LPinky_Joint, p=9000, i=0, ilim=1826, buf_num=33, reverse=False, min_pos=-1700, max_pos=100,
                     device_num=56)
LRing = JointDevice(joint=LRing_Joint, p=9000, i=0, ilim=1729, buf_num=34, reverse=False, min_pos=-1700, max_pos=100,
                    device_num=57)
LMiddle = JointDevice(joint=LMiddle_Joint, p=9000, i=0, ilim=2041, buf_num=32, reverse=False, min_pos=-1700, max_pos=0,
                      device_num=55)
LIndex = JointDevice(joint=LIndex_Joint, p=9000, i=0, ilim=1397, buf_num=31, reverse=False, min_pos=-1700, max_pos=100,
                     device_num=54)
LThumb = JointDevice(joint=LThumb_Joint, p=9000, i=0, ilim=1964, buf_num=35, reverse=True, min_pos=-50, max_pos=1700,
                     device_num=58)
left_wrist_joints = [LWristRoll, LWristYaw, LPinky, LRing, LMiddle, LIndex, LThumb]
arms_joints = left_arm_joints + right_arm_joints + left_wrist_joints + right_wrist_joints
# Torso and head
NeckPitch = JointDevice(joint=NeckPitch_Joint, p=500, i=0, ilim=13262, buf_num=69, reverse=False, min_pos=-200,
                        max_pos=1500, device_num=46)
NeckYaw = JointDevice(joint=NeckYaw_Joint, p=1000, i=2, ilim=-933, buf_num=36, reverse=False, min_pos=-2000,
                      max_pos=2000, device_num=43)
HeadPitch = JointDevice(joint=HeadPitch_Joint, p=600, i=2, ilim=-7723, buf_num=37, reverse=False, min_pos=-1500,
                        max_pos=2000, device_num=44)
HeadRoll = JointDevice(joint=HeadRoll_Joint, p=600, i=2, ilim=4633, buf_num=38, reverse=True, min_pos=-1000,
                       max_pos=1000, device_num=45)
TorsoYaw = JointDevice(joint=TorsoYaw_Joint, p=800, i=1, ilim=1333, buf_num=19, reverse=False, min_pos=-2500,
                       max_pos=2500, device_num=49)

all_joint_devices = legs_joints + arms_joints + [NeckPitch, NeckYaw, HeadPitch, HeadRoll, TorsoYaw]

LFootFS = ForceSensor(device_name=LFoot_ForceSensor, device_num=16, buf_num=16, uch0=1568, uch1=1687, uch2=1633,
                      uch3=1540)
RFootFS = ForceSensor(device_name=RFoot_ForceSensor, device_num=15, buf_num=15, uch0=1551, uch1=1710, uch2=1757,
                      uch3=66)
LWristFS = ForceSensor(device_name=LWrist_ForceSensor, device_num=84, buf_num=47, uch0=24507, uch1=23862, uch2=23681,
                       uch3=32544)
RWristFS = ForceSensor(device_name=RWrist_ForceSensor, device_num=83, buf_num=70, uch0=-3070, uch1=30279, uch2=2720,
                       uch3=-1493)

all_force_sensors = [LFootFS, RFootFS, LWristFS, RWristFS]

Gyro = Device(device_name="Gyro", device_num=13, buf_num=23)
GyroPlus = Device(device_name="Gyro+", device_num=14, buf_num=14)

# not added devices 81, 82, 85, 86, 90, 91
