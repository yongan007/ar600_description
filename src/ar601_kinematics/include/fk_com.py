# !/usr/bin/env python3.5
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




def fk_com(q1,q2,q3,q4,q5,q6,left):
  q1 = -q1
  q2 = -q2
  q3 = -q3
  q4 = -q4
  q5 = -q5
  q5 = -q6
  
  T_b = transl(0,0,foot_z)

  if left:
    T_t = transl(com_x,com_y,com_z)
  else:
    T_t =  transl(com_x,-com_y,com_z)
  T_1 = rotx(q6) @ transl(0,0,ankle_z)
  T_2 = roty(q5)@transl(0,0,leg_down)
  T_3 = roty(q4)@transl(0,0,leg_up)
  T_4 = roty(q3)
  T_5 = rotx(q2)
  T_6 = rotz(q1)

  T = T_b @ T_1 @ T_2 @ T_3 @ T_4 @ T_5 @ T_6 @ T_t

  position = np.array([T[0,3], T[1,3], T[2,3]]).reshape(3,1)
  orietation = np.array([T[0,0], T[0,1], T[0,2], 
                        T[1,0], T[1,1], T[1,2],
                        T[2,0], T[2,1], T[2,2]])
        
  return position,orietation.reshape(3,3)




if __name__ == "__main__":
  pos,orn = fk_com(0,0,0,0,0,0,True)
  print (pos,"\n",orn)



