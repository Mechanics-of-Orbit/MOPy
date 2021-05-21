import numpy as np
from math import *

class GlobalCalculation():
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2

    @classmethod
    def force_at_this_point(cls, r, major_body_mass, minor_body_mass):
        F_r = cls.G * major_body_mass * minor_body_mass / r ** 2
        return F_r

# all the units should be km
class CalculateCircEllip:
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2

    @classmethod
    def semiecc(cls, sma, mag_e, major_body):
        r_per = sma * (1 - mag_e)
        r_apo = sma * (1 + mag_e)
        [mean_motion, T_period, mag_h, sme, slr] = CalculateCircEllip.orb_const(r_per, sma, mag_e, major_body)
        return [r_per, r_apo, mean_motion, T_period, mag_h, sme, slr]
    
    @classmethod
    def perapo(cls, r_per, r_apo, major_body):
        sma = (r_per + r_apo)/2
        mag_e = (r_apo - r_per)/(r_apo + r_per)
        [mean_motion, T_period, mag_h, sme, slr] = CalculateCircEllip.orb_const(r_per, sma, mag_e, major_body)
        return [mag_e, sma, mean_motion, T_period, mag_h, sme, slr]
    
    @classmethod
    def orb_const(cls, r_per, sma, mag_e, major_body):
        major_body_mass = major_body * 1
        mu = cls.G * major_body_mass
        slr = sma*(1-mag_e**2)
        mag_h = (r_per*(1+e)*mu)**0.5
        T_period = sqrt(((4*pi**2)/mu)*sma**3)
        mean_motion = T_period/(2*pi)
        sme = -mu/(2* sma)
        return [mean_motion, T_period, mag_h, sme, slr]
    
    @classmethod
    def time_since_perigee(cls, mag_e, theta, T_period):
        E_anomly = 2 * atan((sqrt((1 - mag_e)/(1 + mag_e)) * tan(theta/2)))
        M_anomly = E_anomly - mag_e * sin(E_anomly)
        t_since_perigee = T_period * M_anomly/(2*pi)
        return t_since_perigee
    
    @classmethod
    def theta_since_time(cls, mag_e, theta, T_period, t_since_perigee):
        M_anomly = 2 * pi * t_since_perigee/T_period
        return None
    
    @classmethod
    def velocity_at_any_point(cls, mag_e, theta, mag_h, major_body):
        pass
        

    