from __future__ import division

M_PI = 3.14159265358979323846

RADIAN_TO_GRADUS_COEF = 180 / M_PI

GRAVITATIONAL_CONSTANT = 9.80665

LOOP_RATE_MAX = 250
LOOP_RATE = 50
# be careful that control manager module cuts LOOP_RATE_MAX/LOOP_RATE to int.
# So for 40 we have int(250/40)*40 = 240 HZ from control manager


EPSILON3 = 0.001
PREVIEW_TIME = 1.5

BAD_RESPONSE = Exception('BAD RESPONSE')

PID_P_KEY = "p"
PID_I_KEY = "i"
PID_D_KEY = "d"

# robot specific (AR601):
HEIGHT_OF_MASS_CENTER = 0.55
FOOT_DIFF = 0.09  # for zero angles 0.088

def in_radians(gradus):
    return gradus / RADIAN_TO_GRADUS_COEF / 100


def in_gradus(radians):
    return radians * RADIAN_TO_GRADUS_COEF * 100


def max_radian_per_tick(p):
    if p < 500:
        return 0.056
    if p < 1000:
        return 0.056 - 0.008 * (p - 500) / 500
    if p < 1200:
        return 0.048 - 0.018 * (p - 1000) / 200
    if p < 2000:
        return 0.030 - 0.008 * (p - 1200) / 800
    if p < 3000:
        return 0.022 - 0.004 * (p - 2000) / 1000
    return 0.018
