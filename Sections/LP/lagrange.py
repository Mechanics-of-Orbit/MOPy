from math import pi
import matplotlib.pyplot as plt
from numpy import arange
from scipy.optimize import root_scalar

major_body = 'Earth'
minor_body = 'Moon'

class LagPoints():
    G = 6.67408e-11 # m^3 / (kg * s^2)
    
    @classmethod
    def calculate(cls, dist_major_to_minor, major_body, minor_body):
        major_body_mass = 5.972e24 #cls.major_body * 1
        minor_body_mass = 0.07346e24 #cls.minor_body * 1
        x1 = minor_body_mass * dist_major_to_minor/ (minor_body_mass + major_body_mass)
        x2 = major_body_mass * dist_major_to_minor/ (minor_body_mass + major_body_mass)
        velocity = (cls.G * (minor_body_mass + major_body_mass)/ dist_major_to_minor) ** 0.5
        period = 2 * pi * dist_major_to_minor / velocity
        theta_dot = 2*pi / period
        return [x1, x2, velocity, period, theta_dot]

    @classmethod
    def x_eq(cls, xs, dist_major_to_minor,major_body, minor_body):
        major_body_mass = 5.972e24 #cls.major_body * 1
        minor_body_mass = 0.07346e24 #cls.minor_body * 1
        [x1, x2, velocity, period, theta_dot] = LagPoints.calculate(dist_major_to_minor, major_body, minor_body)
        x_sol = -cls.G*major_body_mass/((xs + x1) * abs(xs +x1)) - cls.G * minor_body_mass / ((xs - x2)*abs(xs-x2)) + theta_dot**2 * xs
        return [x_sol, x1, x2]


l = 384400000 #m, distance from earth to moon

xvals = arange(-2*l, 2*l, 1000)
[x_eqn, x1, x2] = LagPoints.x_eq(xvals, l, major_body, minor_body)
yvals = x_eqn(xvals)

L1 = root_scalar(x_eqn, bracket=[2e8, 3.5e8])
print(L1.root+x1)

L2 = root_scalar(x_eqn, bracket=[3.9e8, 5e8])
print(L2.root+x1)

L3 = root_scalar(x_eqn, bracket=[-4e8, -2e8])
print(L3.root+x1)

plt.plot(xvals, yvals)
plt.grid()
plt.ylim(-0.01, 0.01)
plt.show()
