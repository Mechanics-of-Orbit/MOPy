from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def SoI(major_body, minor_body):
    MaB_mass = 1
    MiB_mass = 1
    MiB_radius = 1
    r_ai = 1
    rSOI = (r_ai*(MiB_mass/MaB_mass)**(2/5))
    return [rSOI, rSOI/MiB_radius]