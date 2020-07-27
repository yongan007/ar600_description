#!/usr/bin/env python3.5
import numpy as np 
from numpy import sin, cos, arctan2,abs,linalg,matmul
from math import sqrt, radians, sin, cos, degrees, acos, isnan,pi, atan2
from utility import * 
from fk_com import * 

foot_z = 0.1455# distance between floor and foot joints intersection
ankle_z = 0.030# distance between foot and ankle joints intersection 
leg_up = 0.277# upper leg link length
leg_down = 0.28# lower leg link length
com_x = -0.006#  com coordinates in hip CS
com_y = -0.088#
com_z = -0.006#


def tiny_dec(x): return np.around(x, decimals=2)

def wrist(A):
  if abs(abs(A[1, 2]) - 1) < 0.0001 :
    q1 = 0
    q2 = 0
    q3 = 0

  q1 = arctan2(A[1,0],A[1,1])
  q3 = atan2(A[0, 2], A[2, 2])

  if abs(A[2, 2]) >= 0.0001:
      q2 = atan2(-A[1, 2] * cos(q3), A[2, 2])
  else:
      q2 = atan2(-A[1, 2] * sin(q3), A[0, 2])
  
  return q1, q2, q3

def foot_joint(x,y,z):

  q6 = atan2(-y,z)
  
  D= ((z-ankle_z*cos(q6))**2+(-y-ankle_z*sin(q6))**2 +x**2-leg_up**2 - leg_down**2)/(2*leg_down*leg_up)
  D = tiny_dec(D)

  q4 = atan2(sqrt(1-D**2),D)
  q5 = atan2(leg_up*sin(q4), leg_down + leg_up*cos(q4)) + atan2(x,sqrt((z-ankle_z*cos(q6))**2+(-y-ankle_z*sin(q6))**2))

  return q4,q5,q6


def inv_kin(R,T):
   
    T_0 = R@T
    T_b_inv = np.linalg.inv(transl(0,0,foot_z))
    T_t_inv = np.linalg.inv(transl(com_x,com_y,com_z)) 
    
    T_I = T_b_inv @ T_0 @ T_t_inv

    #position of robot respected to foot_z
    px = T_I[0,3]
    py = T_I[1,3]
    pz =  T_I[2,3]

    q4,q5,q6 = foot_joint(px,py,pz)

    #q1,q2,q3 
    T1 = rotx(q6)@transl(0,0,ankle_z)
    T2 = roty(q5)@transl(0,0,leg_down)
    T3 = roty(q4)@transl(0,0,leg_up)
    T13_inv = np.linalg.inv(T1@T2@T3) 
    T46 = T_b_inv @ T13_inv @ T_I @ T_t_inv 

    q1,q2,q3 = wrist(T46)
    angles = [q1,q2,q3,q4,q5,q6]

    return angles

if __name__ == "__main__":
  # pose = fk_com(0,0,0,0,0,0,True)

  T = transl(-0.006 ,-0.088,0.70)
  R = np.diag(np.ones(4))

  angles = inv_kin(R,T)
  print(angles)







