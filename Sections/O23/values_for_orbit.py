import numpy as np
from math import *

class CalculateValues:
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2

    @classmethod
    def semiecc(cls, sma, ecc, major_body):
        mu = cls.G * major_body
        rp = sma*(1 - ecc)
        ra = sma * (1 + e)
        return [ra, rp]
    
    @classmethod
    def perapo(cls, r_per, r_apo, major_body):
        mu = cls.G * major_body
        sma = (r_per + r_apo)/2
        mag_e = (r_apo - r_per)/(r_apo + r_per)
        return [mag_e, sma]

