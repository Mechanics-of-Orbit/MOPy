import sys
from math import *
from numpy import *
from VPCO import *

class Hohmann():
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2

    @classmethod
    def values(cls,r_apo, r_per, major_body):
        major_body_mass = major_body * 1
        mu = cls.G * major_body_mass
        mag_h = sqrt(2*mu)*sqrt((r_apo+r_per)/(r_per*r_apo))
        v_per = mag_h/r_per
        v_apo = mag_h/r_apo
        return [v_per, v_apo]

    @classmethod
    def hohmann_method(cls, major_body, r_apo_1, r_per_1, r_per_2, r_apo_2):
        [v_per_1, v_apo_1] = Hohmann.values(r_apo_1, r_per_1, major_body)
        [v_per_2, v_apo_2] = Hohmann.values(r_apo_2, r_per_2, major_body)
        #case-a r_per_t = r_per_1
        r_per_ta = r_per_1
        r_apo_ta = r_apo_2
        [v_per_ta, v_apo_ta] = Hohmann.values(r_apo_ta, r_per_ta, major_body)
        delta_v_1a = v_per_ta - v_per_1
        delta_v_2a = v_apo_2 - v_apo_ta
        total_delta_va = abs(delta_v_1a) + abs(delta_v_2a)
        #case-b r_per_t = r_apo_1
        r_per_tb = r_apo_1
        r_apo_tb = r_per_2
        [v_per_tb, v_apo_tb] = Hohmann.values(r_apo_tb, r_per_tb, major_body)
        delta_v_1b = v_per_tb - v_apo_1
        delta_v_2b = v_per_2 - v_apo_tb
        total_delta_vb = abs(delta_v_1b) + abs(delta_v_2b)
        return [total_delta_va, total_delta_vb]

    @classmethod
    def bi_elliptical_hohmann_transfer(cls, major_body, r_apo_1, r_per_1, r_per_2, r_apo_2):
        pass
    




