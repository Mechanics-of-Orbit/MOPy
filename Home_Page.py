#import math as m
#import numpy as np
from sympy import *

x = Symbol('x')
print(diff(x**5 + sin(x)*cos(x)-tan(x)))

class Integrations():

    @classmethod
    def NewtonRhapson(cls, f_x):
        
        pass