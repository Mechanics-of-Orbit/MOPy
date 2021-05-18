import numpy as np
from math import *

# allthe units should be km
class CalculateValues:
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2

    @classmethod
    def semiecc(cls, sma, mag_e, major_body):
        r_per = sma * (1 - mag_e)
        r_apo = sma * (1 + mag_e)
        [mean_motion, T_period, mag_h, sme, slr] = CalculateValues.orb_const(r_per, sma, mag_e, major_body)
        return [r_per, r_apo, mean_motion, T_period, mag_h, sme, slr]
    
    @classmethod
    def perapo(cls, r_per, r_apo, major_body):
        sma = (r_per + r_apo)/2
        mag_e = (r_apo - r_per)/(r_apo + r_per)
        [mean_motion, T_period, mag_h, sme, slr] = CalculateValues.orb_const(r_per, sma, mag_e, major_body)
        return [mag_e, sma, mean_motion, T_period, mag_h, sme, slr]
    
    @classmethod
    def orb_const(cls, r_per, sma, mag_e, major_body):
        major_body_mass = 1
        mu = cls.G * major_body_mass
        slr = sma*(1-mag_e**2)
        mag_h = (r_per*(1+e)*mu)**0.5
        T_period = sqrt(((4*pi**2)/mu)*sma**3)
        mean_motion = sqrt(mu/sma**3)
        sme = -mu/(2* sma)
        return [mean_motion, T_period, mag_h, sme, slr]
    
    @classmethod
    def force_at_this_point(cls, r, theta):
        pass