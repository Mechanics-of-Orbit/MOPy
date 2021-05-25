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
class CalculateCircularElliptical:
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2
    def __init__(self, major_body):
    
        self.major_body = major_body
        return

    @classmethod
    def semiecc(cls, sma, mag_e, major_body):
        r_per = sma * (1 - mag_e)
        r_apo = sma * (1 + mag_e)
        [mean_motion, T_period, mag_h, sme, slr] = CalculateCircularElliptical.orb_const(r_per, sma, mag_e, major_body)
        return [r_per, r_apo, mean_motion, T_period, mag_h, sme, slr]
    
    @classmethod
    def perapo(cls, r_per, r_apo, major_body):
        sma = (r_per + r_apo)/2
        mag_e = (r_apo - r_per)/(r_apo + r_per)
        [mean_motion, T_period, mag_h, sme, slr] = CalculateCircularElliptical.orb_const(r_per, sma, mag_e, major_body)
        return [mag_e, sma, mean_motion, T_period, mag_h, sme, slr]
    
    @classmethod
    def orb_const(self, cls, r_per, sma, mag_e):
        major_body_mass = self.major_body * 1
        mu = cls.G * major_body_mass
        slr = sma*(1-mag_e**2)
        mag_h = (r_per*(1+e)*mu)**0.5
        T_period = sqrt(((4*pi**2)/mu)*sma**3)
        mean_motion = T_period/(2*pi)
        sme = -mu/(2* sma)
        return [mean_motion, T_period, mag_h, sme, slr]
    
    @classmethod
    def time_since_periapsis(cls, mag_e, theta, T_period):
        E_anomly = 2 * atan((sqrt((1 - mag_e)/(1 + mag_e)) * tan(theta/2)))
        M_anomly = E_anomly - mag_e * sin(E_anomly)
        t_since_perigee = T_period * M_anomly/(2*pi)
        return t_since_perigee
    
    # @classmethod
    # def theta_since_time(cls, mag_e, theta, T_period, t_since_perigee):
    #     M_anomly = 2 * pi * t_since_perigee/T_period
    #     return None
    
    @classmethod
    def velocity_at_any_point(cls, sma, r, major_body):
        major_body_mass = major_body * 1
        mu = cls.G * major_body_mass
        v_point = sqrt(((2 * mu)/r) - (mu/sma))
        return v_point

class CalculateParabola():

    def __init__(self):
        I = [1, 0, 0]
        J = [0, 1, 0]
        K = [0, 0, 1]
        G = 6.67e-20 #units are in km3 kg-1 s-2

    @classmethod
    def parabolicvalues(cls, r_per, major_body):
        major_body_mass = major_body * 1
        mu = major_body_mass * cls.G
        slr = 2 * r_per
        v_per = sqrt((2*mu)/r_per)
        mag_h = sqrt(mu*r_per * 2)
        return [slr, v_per, mag_h]

    @classmethod
    def vel_parabolic(self, cls, r, major_body):
        major_body_mass = major_body * 1
        mu = major_body_mass * self.G
        v = sqrt((2*mu)/r)
        return v
    
class CalculateHyperBola():
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2

    @classmethod
    def hyperbolic_values():
        pass


# major_body = 2

# x_obj = CalculateCircularElliptical(major_body)

# x_obj.orb_const()