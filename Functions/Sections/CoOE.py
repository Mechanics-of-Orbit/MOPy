from numpy.linalg import norm
from numpy import dot, pi, cross, multiply as multi
from math import acos
import sqlite3

class Calculate():
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2

    def muvalue(self, major_body):
        db = sqlite3.connect("Functions/Sections/DB/MajorBody_data.db")
        cursor = db.cursor()
        major_body = "  " + major_body
        
        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[major_body])
        
        for row_number, row_data in enumerate(result):
            major_body_radius = row_data[2]/2
            major_body_mass = row_data[1]
             
        mu = self.G * major_body_mass
        return [mu, major_body_radius]
    
    def correct_ohm(ohm, n_vec):
        if n_vec[0] > 0 and n_vec[1] > 0: 
            quad = ("This is a Prograde Elliptical Orbit and n vector lies in first Quadrant.")
            if ohm >90:
                ohm = 360 - ohm
        elif n_vec[0] < 0 and n_vec[1] > 0:
            quad = ("This is a Retrograde Elliptical Orbit and n vector lies in second Quadrant.")
            if ohm > 180:
                ohm = 360 - ohm
        elif n_vec[0] < 0 and n_vec[1] < 0:
            quad = ("This is a Retrograde Elliptical Orbit and n vector lies in Third Quadrant.")
            if ohm < 180:
                ohm = 360 - ohm
        elif n_vec[0] > 0 and n_vec[1] < 0:
            quad = ("This is a Prograde Elliptical Orbit and n vector lies in fourth Quadrant.")
            if ohm < 90:
                ohm = 360 - ohm
        return [ohm, quad]
    
    def other_var(self, pos_vec, vel_vec):
        h_vec = cross(pos_vec, vel_vec)
        n_vec = cross(self.K,h_vec)
        return [h_vec, n_vec]
    
    def OE(self, pos_vec, vel_vec, mu):
        [h_vec, n_vec] = Calculate.other_var(self, pos_vec, vel_vec)
        e_vec = (multi((norm(vel_vec)*norm(vel_vec)-(mu/norm(pos_vec))),pos_vec)- multi(dot(pos_vec,vel_vec),vel_vec))/(mu)
        inc = (acos((dot(h_vec, self.K))/norm(h_vec))) * 180/pi
        sma = 1/((2/norm(pos_vec))-((norm(vel_vec)*norm(vel_vec))/mu))
        e_norm = norm(e_vec)
        return [sma, inc, e_vec, e_norm]
    
    def ACOE(self, pos_vec, vel_vec, e_vec, inc):
        [h_vec, n_vec] = Calculate.other_var(pos_vec, vel_vec)
        if inc != 0 or 180 and norm(e_vec) > 0: #Nothing is Zero/180
            ohm = (acos((dot(self.I,n_vec))/norm(n_vec)))
            ohm = Calculate.correct_ohm(ohm, n_vec)
            nu = (acos((dot(e_vec,pos_vec))/(norm(e_vec)*norm(pos_vec))))
            omega = (acos((dot(n_vec,e_vec))/multi(norm(n_vec),norm(e_vec))))
            return [ohm, omega, nu]
        elif inc == 0 or 180: #Inclination is Zero
            if norm(e_vec) > 0: #Elliptical Orbit
                nu = (acos((dot(e_vec,pos_vec))/(norm(e_vec)*norm(pos_vec))))
                Long_of_peri_pi = acos(dot(self.I,e_vec)/(norm(self.I)*norm(e_vec)))
                return [Long_of_peri_pi, nu]
            elif norm(e_vec) == 0: #Circular Orbit
                Tr_long_l = acos(dot(self.I,pos_vec)/(norm(pos_vec)*norm(self.I)))
                return [Tr_long_l]
        elif norm(e_vec) == 0: #Circular orbit with inclination non-zero/pi
            Arg_of_lattitude_u = acos(dot(n_vec,pos_vec)/(norm(n_vec)*norm(pos_vec)))
            return [Arg_of_lattitude_u]

    def possibility(cls, major_body, pos_vec, vel_vec):
        [mu, major_body_radius] = Calculate.muvalue(major_body)
        pos = norm(pos_vec)
        vel = norm(vel_vec)
        sma = 1/((2/pos)-(vel*vel/mu))
        e_vec = (multi((norm(vel_vec)*norm(vel_vec)-(mu/norm(pos_vec))),pos_vec)- multi(dot(pos_vec,vel_vec),vel_vec))/(mu)
        r_peri = sma*(1-norm(e_vec))
        if r_peri <= major_body_radius:
            # status = ("The Orbit is not possible as radius of perigee is less than radius of the major Body")
            return False
        return True

if __name__ == '__main__':
    pos_vec = [1, 2, 3]
    vel_vec = [4, 5, 6]
    Major_Body = "Earth"
    [mu, major_body_radius] = Calculate.muvalue(Major_Body)
    [sma, inc, e_vec] = Calculate.OE(pos_vec, vel_vec, mu)
    oon = Calculate.ACOE(pos_vec, vel_vec, e_vec, inc)
