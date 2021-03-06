from numpy.linalg import norm
from numpy import dot, pi, cross, multiply as multi
from math import acos

if __name__ == '__main__':
    from DB.call_database import *
else:
    from Functions.Sections.DB.call_database import *

class Calculate:
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2
    def muvalue(self,major_body):
        major_body_radius = planet_data(major_body,'Radius') #major_bodies_radius[sel_major_body]
        major_body_mass = planet_data(major_body,'Mass')[0]
        mu = self.G * major_body_mass
        return [mu, major_body_radius]
    
    def correct_ohm(ohm, n_vec):
        if n_vec[0] > 0 and n_vec[1] > 0: 
            if ohm > pi/2:
                ohm = 2*pi - ohm
        elif n_vec[0] < 0 and n_vec[1] > 0:
            if ohm > pi:
                ohm = 2*pi - ohm
        elif n_vec[0] < 0 and n_vec[1] < 0:
            if ohm < pi:
                ohm = 2*pi - ohm
        elif n_vec[0] > 0 and n_vec[1] < 0:
            if ohm < pi/2:
                ohm = 2*pi - ohm
        return ohm

    def position_of_n_vector(n_vec):
        if n_vec[0] == 0 and n_vec[1] == 0:
            quad = "The n vector doesn't exist as there is no Orbital Inclination"
        elif n_vec[0] == 0 or n_vec[1] == 0:
            if n_vec[0] < 0:
                quad = "This is a Retrograde Orbit and the n-vector lies on negative x-axis"
            elif n_vec[0] > 0:
                quad = "This is a Prograde Orbit and the n-vector lies on Positive x-axis"
            elif n_vec[1] > 0:
                quad = "This is a Prograde Orbit and the n-vector lies on Positive y-axis"
            elif n_vec[1] < 0:
                quad = "This is a Retrograde Orbit and the n-vector lies on Negative y-axis"
        elif n_vec[0] > 0 and n_vec[1] > 0: 
            quad = ("This is a Prograde Orbit and the n-vector lies in first Quadrant.")
        elif n_vec[0] < 0 and n_vec[1] > 0:
            quad = ("This is a Retrograde Orbit and the n-vector lies in second Quadrant.")
        elif n_vec[0] < 0 and n_vec[1] < 0:
            quad = ("This is a Retrograde Orbit and the n-vector lies in Third Quadrant.")
        elif n_vec[0] > 0 and n_vec[1] < 0:
            quad = ("This is a Prograde Orbit and the n-vector lies in fourth Quadrant.")
        return quad
        
    def other_var(pos_vec, vel_vec):
        h_vec = cross(pos_vec, vel_vec)
        K = [0, 0, 1]
        n_vec = cross(K,h_vec)
        return [h_vec, n_vec]
    
    def OE(pos_vec, vel_vec, mu):
        [h_vec, n_vec] = Calculate.other_var(pos_vec, vel_vec)
        e_vec = (multi((norm(vel_vec)*norm(vel_vec)-(mu/norm(pos_vec))),pos_vec)- multi(dot(pos_vec,vel_vec),vel_vec))/(mu)
        K = [0, 0, 1]
        inc = (acos((dot(h_vec, K))/norm(h_vec))) 
        sma = 1/((2/norm(pos_vec))-((norm(vel_vec)*norm(vel_vec))/mu))
        e_norm = norm(e_vec)
        ACOE_values = Calculate.ACOE(pos_vec, vel_vec, e_vec, inc)
        OE_values = {"Semi-Major Axis": sma, "Inclination": inc, "Vec_Eccentricity": e_vec, "Norm_Eccentricity": e_norm}
        return [OE_values, ACOE_values]
        
        
    def ACOE(pos_vec, vel_vec, e_vec, inc):
        [h_vec, n_vec] = Calculate.other_var(pos_vec, vel_vec)
        I = [1, 0, 0]
        if (inc != 0 or 180) and norm(e_vec) > 0: #Nothing is Zero/180
            ohm = (acos((dot(I,n_vec))/norm(n_vec)))
            ohm = Calculate.correct_ohm(ohm, n_vec)
            
            nu = (acos((dot(e_vec,pos_vec))/(norm(e_vec)*norm(pos_vec))))
            
            omega = (acos((dot(n_vec,e_vec))/multi(norm(n_vec),norm(e_vec))))
            
            return {"RAAN":ohm, "Argument of Perigee":omega, "True Anomaly":nu}
      
        elif (inc == 0 or 180): #Inclination is Zero
            
            if norm(e_vec) > 0: #Elliptical Orbit
                nu = (acos((dot(e_vec,pos_vec))/(norm(e_vec)*norm(pos_vec))))
                Long_of_peri_pi = acos(dot(I,e_vec)/(norm(I)*norm(e_vec)))
                return {"Longitude of Perigee":Long_of_peri_pi, "True Anomaly":nu, "nothing":'NA'}
            elif norm(e_vec) == 0: #Circular Orbit
                Tr_long_l = acos(dot(I,pos_vec)/(norm(pos_vec)*norm(I)))
                return {"True Longitude": Tr_long_l, "NA":'NA', "NA":'NA'}
        
        elif (inc != 0 or 180) and norm(e_vec) == 0: #Circular orbit with inclination non-zero/pi
            ohm = (acos((dot(I,n_vec))/norm(n_vec)))
            ohm = Calculate.correct_ohm(ohm, n_vec)
            Arg_of_lattitude_u = acos(dot(n_vec,pos_vec)/(norm(n_vec)*norm(pos_vec)))
            return {"Argument of Latitude": Arg_of_lattitude_u, "RAAN": ohm, "NA":'NA'}

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
    pos_vec = [8250.0, 390.0, 6900.0]
    vel_vec = [-0.7, 6.6, -0.6]
    # e_vec = [0.140621, 0.12893, 0.117342]
    # inc = 39.94
    # manju = Calculate.ACOE(pos_vec, vel_vec, e_vec, inc)
    # print(manju)
    Major_Body = "Earth"
    # [mu, major_body_radius] = Calculate.muvalue(Major_Body)
    mu = 3.986e5
    test = Calculate.muvalue("Earth")
    OE = Calculate.OE(pos_vec, vel_vec, mu)
    print(OE)
    
