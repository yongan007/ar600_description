
import numpy as np 
from numpy import sin, cos, arctan2,abs,linalg
from math import sqrt, radians, sin, cos, degrees, acos, isnan,pi, atan2


def transl(px,py,pz):
  return np.array([[1, 0, 0, px], [0, 1, 0, py], [0, 0, 1, pz], [0, 0, 0, 1]])

def rotx(theta):
    c, s = _return_sin_and_cos(theta)
    return np.array([[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]])


def roty(theta):
    c, s = _return_sin_and_cos(theta)
    return np.array([[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]])


def rotz(theta):
    c, s = _return_sin_and_cos(theta)
    return np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


def _return_sin_and_cos(theta):
    # d= theta
    d = theta
    c = cos(d)
    s = sin(d)
    return c, s

# print(_return_sin_and_cos(np.pi))
