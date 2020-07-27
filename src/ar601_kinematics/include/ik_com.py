#!/usr/bin/env python3.5
import numpy as np 
from numpy import sin, cos, arctan2,abs,linalg
from math import sqrt, radians, sin, cos, degrees, acos, isnan,pi, atan2
from utility import * 

foot_z = 0.1455# distance between floor and foot joints intersection
ankle_z = 0.030# distance between foot and ankle joints intersection 
leg_up = 0.277# upper leg link length
leg_down = 0.28# lower leg link length
com_x = -0.006#  com coordinates in hip CS
com_y = -0.088#
com_z = 0.006#


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

def foot_joints(x_f,y_f,z_f,Rf,x_c,y_c,z_c,Rc):

    def I_xyz(Tf,Rf,Tt,Rt):
      I = np.linalg.inv(Rf) @ np.linalg.inv(Tf) @ Tt @ Rt
      return I[0,3], I[1,3], I[2,3]

    Tf = transl(x_f,y_f,z_f)
    Tc = transl(x_c,y_c,z_c)

    x_I,y_I,z_I = I_xyz(Tf,Rf,Tc,Rc)

    T_I = transl(x_I,y_I,z_I)
    R_I = np.linalg.inv(Rf) @ Rc
    T_b_inv = transl(0,0,-foot_z)
    T_t_inv = transl(-com_x,-com_y,-com_z)  

    def T_xyz(T_b_inv,T_I,R_I,T_t_inv):
      T = T_b_inv @ T_I @ R_I @ T_t_inv
      return T[2,3],T[1,3],T[0,3]

    xx,yy,zz = T_xyz(T_b_inv,T_I,R_I,T_t_inv)
    q6 = atan2(yy,xx)
    q4 = -acos((sqrt(xx**2+yy**2-ankle_z)-leg_up**2 - leg_down**2)/(2*leg_down*leg_up))

    q5 = -atan2(leg_up*sin(q4), (leg_down + leg_up*cos(q4))) + atan2(zz , sqrt(xx**2 + yy**2-ankle_z))

    T1 = rotx(q6)*transl(0,0,ankle_z)
    T2 = roty(q5)*transl(0,0,leg_down)
    T3 = roty(q4)*transl(0,0,leg_up)

    T46 = np.linalg.inv(T1@T2@T3)@(T_b_inv @ T_I @ R_I @ T_t_inv)
    q1,q2,q3 = wrist(T46)
    angles = [q1,q2,q3,q4,q5,q6]

    return angles

def orientation(x,y,z,phi_x,phi_y,phi_z,x_t,y_t,z_t,phi_x_t,phi_y_t,phi_z_t,left):
  Rx = roty(phi_x)
  Ry = roty(phi_y)
  Rz = rotz(phi_z)

  R = Rx @ Ry @ Rz 

  Rx_t = roty(phi_x_t)
  Ry_t = roty(phi_y_t)
  Rz_t = rotz(phi_z_t)

  R_t = Rx_t @ Ry_t @ Rz_t 

  if left == False :
    Rt = np.array (R_t[0,0],R_t[0,1],R_t[0,2],
                    R_t[1,0],R_t[1,1],R_t[1,2],
                    R_t[2,0],R_t[2,1],R_t[2,2])

    temp = np.array([0,-2*com_y,0]).reshape(3,1)
    dr = Rt*temp 
    x = x + dr[0]
    y = y + dr[1]
    z = z + dr[2]



if __name__ == "__main__":
    A = rotx(0)
    B = roty(30)
    C = rotz(10)

    D= A@B@C

    a = foot_joints(0,0,0,A,0,0,0,A)
    print(a)







