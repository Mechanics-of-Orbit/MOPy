from numpy import transpose, asarray, pi
from math import cos,sin


class OE_to_SV():
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2

    @classmethod
    def calculate(cls, mag_h, mag_e, ohm, inc, omega, nu, major_body):
        mu = 398600 #self.G * major_body
        pos_vec_peri = (mag_h**2/mu) * (1/(1 + mag_e*cos(nu))) * (cos(nu) * transpose(cls.I) + sin(nu) * transpose(cls.J))
        vel_vec_peri = (mu/mag_h) * (-sin(nu) * transpose(cls.I) + (mag_e + cos(nu)) * transpose(cls.J))

        R3_omega = asarray([[cos(omega), sin(omega), 0],[-sin(omega), cos(omega), 0],[0, 0, 1]]) #Rotation Matrix about the z-axis through the angle w
        Rl_i = asarray([[1, 0, 0],[0, cos(inc), sin(inc)],[0, -sin(inc), cos(inc)]]) #Rotation Matrix about the x-axis through the angle i
        R3_Omega = asarray([[cos(ohm), sin(ohm), 0], [-sin(ohm), cos(ohm), 0],[0, 0, 1]]) #Rotation Matrix about the z-axis through the angle nu

        Q_px = transpose(R3_omega*Rl_i*R3_Omega) # Matrix of the transformation from the perifocal to geocentric equatorial frame
        pos_vec = transpose(Q_px*pos_vec_peri)
        vel_vec = transpose(Q_px*vel_vec_peri)
        return [pos_vec, vel_vec]

a = OE_to_SV.calculate(80000, 1.4, 40*pi/180, 30*pi/180, 60*pi/180, 30*pi/180, "Earth")
print(transpose(a))


