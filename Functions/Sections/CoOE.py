from numpy.linalg import norm
from numpy import dot, pi, cross, multiply as multi
from math import acos

class Calculate:
    def __init__(self,major_body, pos_vec, vel_vec):
        self.I = [1, 0, 0]
        self.J = [0, 1, 0]
        self.K = [0, 0, 1]
        self.G = 6.67e-20 #units are in km3 kg-1 s-2
        self.major_body = major_body
        self.pos_vec = pos_vec
        self.vel_vec = vel_vec
    
    def OrbitalElements(self):
        if Calculate.possibility(self) is True:
            [a, e, inc] = Calculate.OE()
            [Ohm_Pi, omega_l, nu_u] = Calculate.ACOE()
            OE_labels = [self.OE1, self.OE2, self.OE3, self.OE4, self.OE5, self.OE6]
            return[a, e, inc, Ohm_Pi, omega_l, nu_u, OE_labels]
        else:
            return "The Orbit is not possible as radius of perigee is less than radius of the major Body"

    def muvalue(self):
        # LINK DATA BASE HERE
        G = 6.67e-20
        major_body_mass = 5.972e24
        major_body_radius = 6378
        mu = G * major_body_mass
        return [major_body_radius, mu]
    
    def correct_ohm(self, ohm, n_vec):
        if n_vec[0] > 0 and n_vec[1] > 0: 
            GraphChara = "This is a Prograde Elliptical Orbit and is in first Quadrant."
            if ohm >90:
                ohm -= 360
        elif n_vec[0] < 0 and n_vec[1] > 0:
            GraphChara = "This is a Retrograde Elliptical Orbit and is in second Quadrant."
            if ohm > 180:
                ohm -= 360
        elif n_vec[0] < 0 and n_vec[1] < 0:
            GraphChara = "This is a Retrograde Elliptical Orbit and is in Third Quadrant."
            if ohm < 180:
                ohm -= 360
        elif n_vec[0] > 0 and n_vec[1] < 0:
            GraphChara = "This is a Prograde Elliptical Orbit and is in fourth Quadrant."
            if ohm < 90:
                ohm -= 360
        return [GraphChara, ohm]

    def other_var(self):
        h_vec = cross(self.pos_vec, self.vel_vec)
        n_vec = cross(self.K,h_vec)
        return [h_vec, n_vec]

    def OE(self):
        [h_vec, n_vec] = Calculate.other_var(self.pos_vec, self.vel_vec)
        [mu, major_body_radius] = Calculate.muvalue(major_body)
        e_vec = (multi((norm(self.vel_vec)*norm(self.vel_vec)-(mu/norm(self.pos_vec))),self.pos_vec)- multi(dot(self.pos_vec,self.vel_vec),self.vel_vec))/(mu)
        inc = (acos((dot(h_vec, self.K))/norm(h_vec))) * 180/pi
        sma = 1/((2/norm(self.pos_vec))-((norm(self.vel_vec)*norm(self.vel_vec))/mu))
        self.OE1 = "Semi-Major Axis"
        self.OE2 = "Eccentricity"
        self.OE3 = "Inclination"
        return [sma, inc, e_vec]
    
    def ACOE(self, e_vec, inc):
        [h_vec, n_vec] = Calculate.other_var(self.pos_vec, self.vel_vec)
        if inc != 0 or 180 and norm(e_vec) > 0: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Nothing is Zero/180
            ohm = (acos((dot(self.I,n_vec))/norm(n_vec)))
            [self.OE4, ohm] = ["RAAN", Calculate.correct_ohm(ohm, n_vec)]
            [self.OE6, nu] = ["True Anomaly", (acos((dot(e_vec,self.pos_vec))/(norm(e_vec)*norm(self.pos_vec))))]
            [self.OE5, omega] = ["Argument of Perigee", (acos((dot(n_vec,e_vec))/multi(norm(n_vec),norm(e_vec))))]
            return [ohm, omega, nu]
        elif inc == 0 or 180: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Inclination is Zero
            if norm(e_vec) > 0: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Elliptical Orbit
                nu = (acos((dot(e_vec,self.pos_vec))/(norm(e_vec)*norm(self.pos_vec))))
                Long_of_peri_pi = acos(dot(self.I,e_vec)/(norm(self.I)*norm(e_vec)))
                [self.OE5, self.OE6] = ["Longitude of Perigee","True Anomaly"]
                self.OE4 = "Not Defined"
                return [Long_of_peri_pi, nu]
            elif norm(e_vec) == 0: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Circular Orbit
                Tr_long_l = acos(dot(self.I,self.pos_vec)/(norm(self.pos_vec)*norm(self.I)))
                self.OE5 = "True Longitude"
                self.OE4 = self.OE6 = "Not Defined"
                return [Tr_long_l]
        elif norm(e_vec) == 0: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Circular orbit with inclination non-zero/pi
            Arg_of_lattitude_u = acos(dot(n_vec,self.pos_vec)/(norm(n_vec)*norm(self.pos_vec)))
            self.OE6 = "Argument of Latitude"
            self.OE4 = self.OE5 = "Not Defined"
            return [Arg_of_lattitude_u]

    def possibility(self):
        [mu, major_body_radius] = Calculate.muvalue(major_body)
        pos = norm(self.pos_vec)
        vel = norm(self.vel_vec)
        sma = 1/((2/pos)-(vel*vel/mu))
        e_vec = (multi((norm(self.vel_vec)*norm(self.vel_vec)-(mu/norm(self.pos_vec))),self.pos_vec)- multi(dot(self.pos_vec,self.vel_vec),self.vel_vec))/(mu)
        r_peri = sma*(1-norm(e_vec))
        if r_peri <= major_body_radius:
            return False
        return True

if __name__ == '__main__':
    pos_vec = [8250, 390, 6900]
    vel_vec = [-0.7, 6.6, -0.6]
    major_body = "Earth"
    OEM = Calculate(major_body, pos_vec, vel_vec)
    a = OEM.OrbitalElements()
    try:
        [a, e, inc, Ohm_Pi, omega_l, nu_u, OE_labels] = a
        print(OE_labels)
    except:
        print(a)
    print(">>>>>>>>>>>>>>>>>OrbitalElements<<<<<<<<<<<<<<<<<< \n")
    print(f"|->{OE_labels(1)} = {a}\n")
    print(f"|->{OE_labels(2)} = {e}\n")
    print(f"|->{OE_labels(3)} = {inc}\n")
    print(f"|->{OE_labels(4)} = {Ohm_Pi}\n")
    print(f"|->{OE_labels(5)} = {omega_l}\n")
    print(f"|->{OE_labels(6)} = {nu_u}\n")


