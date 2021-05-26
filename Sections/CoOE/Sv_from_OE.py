from numpy import pi
from math import atan,cos,sin

def atan2d_0_360(y,x):
    if x == 0:
        if y == 0:
            t = 0
        elif y > 0:
            t = 90
        else:
            t = 270
    elif x > 0:
        if y>= 0:
            t = atan(y/x)
        else:
            t = atan(y/x) + 2*pi
    elif x < 0:
        if y == 0:
            t = 2*pi
        else:
            t = atan(y/x) + pi
    return t

def sv_from_OE(mag_h, mag_e, omega, inc, ohm, nu, mu):
    r_per = (mag_h^2/mu) * (1/(1 + mag_e*cos(nu))) * (cos(nu)*)
