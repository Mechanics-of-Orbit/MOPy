from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from numpy.linalg import norm
from numpy import dot, pi, cross, multiply as multi
from math import acos
import pandas

class MainWindow:
    def Calculate_function(self):
        pos_vec_str = [call.pos_vec_i.text(), call.pos_vec_j.text(), call.pos_vec_k.text()]
        vel_vec_str = [call.vel_vec_i.text(), call.vel_vec_j.text(), call.vel_vec_k.text()]
        Major_Body = call.major_body.currentText()
        pos_vec = list(map(float, pos_vec_str))
        vel_vec = list(map(float, vel_vec_str))
        if Major_Body != "Other":
            [mu, major_body_radius] = Calculate.muvalue(Major_Body)
        else:
            major_body_mass = float(call.other_major_body_mass.text())
            major_body_radius = float(call.other_major_body_radius.text())
            mu = self.G * major_body_mass
        if Calculate.possibility(Major_Body, pos_vec, vel_vec) is True:
            [mu, major_body_radius] = Calculate.muvalue(Major_Body)
            [sma, inc, e_vec] = Calculate.OE(pos_vec, vel_vec, mu)
            oon = Calculate.ACOE(pos_vec, vel_vec, e_vec, inc)
        
class Calculate:
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2

    @classmethod
    def muvalue(cls, major_body):
        major_body_list = pandas.read_csv("Major_and_Minor_Bodies.csv")
        major_bodies = list(major_body_list.Major_Body)
        major_bodies_mass = list(major_body_list.Mass)
        major_bodies_radius = list(major_body_list.Radius)        
        sel_major_body = major_bodies.index(major_body)
        major_body_mass = major_bodies_mass[sel_major_body]
        major_body_radius = major_bodies_radius[sel_major_body]
        mu = cls.G * major_body_mass
        return [mu, major_body_radius]
    
    @classmethod
    def correct_ohm(cls, ohm, n_vec):
        if n_vec[0] > 0 and n_vec[1] > 0: 
            call.error_status.setText("This is a Prograde Elliptical Orbit and is in first Quadrant.")
            if ohm >90:
                ohm -= 360
        elif n_vec[0] < 0 and n_vec[1] > 0:
            call.error_status.setText("This is a Retrograde Elliptical Orbit and is in second Quadrant.")
            if ohm > 180:
                ohm -= 360
        elif n_vec[0] < 0 and n_vec[1] < 0:
            call.error_status.setText("This is a Retrograde Elliptical Orbit and is in Third Quadrant.")
            if ohm < 180:
                ohm -= 360
        elif n_vec[0] > 0 and n_vec[1] < 0:
            call.error_status.setText("This is a Prograde Elliptical Orbit and is in fourth Quadrant.")
            if ohm < 90:
                ohm -= 360
        return ohm

    @classmethod
    def other_var(cls, pos_vec, vel_vec):
        h_vec = cross(pos_vec, vel_vec)
        n_vec = cross(cls.K,h_vec)
        return [h_vec, n_vec]

    @classmethod
    def OE(cls, pos_vec, vel_vec, mu):
        [h_vec, n_vec] = Calculate.other_var(pos_vec, vel_vec)
        e_vec = (multi((norm(vel_vec)*norm(vel_vec)-(mu/norm(pos_vec))),pos_vec)- multi(dot(pos_vec,vel_vec),vel_vec))/(mu)
        call.ecc_o.setText(str(norm(e_vec)))
        inc = (acos((dot(h_vec, cls.K))/norm(h_vec))) * 180/pi
        call.inc_o.setText(str(inc))
        sma = 1/((2/norm(pos_vec))-((norm(vel_vec)*norm(vel_vec))/mu))
        call.sma_o.setText(str(sma))
        return [sma, inc, e_vec]
    
    @classmethod
    def ACOE(cls, pos_vec, vel_vec, e_vec, inc):
        [h_vec, n_vec] = Calculate.other_var(pos_vec, vel_vec)
        if inc != 0 or 180 and norm(e_vec) > 0: #Nothing is Zero/180
            ohm = (acos((dot(cls.I,n_vec))/norm(n_vec)))
            ohm = Calculate.correct_ohm(ohm, n_vec)
            call.ohm_o.setText(str(ohm))
            nu = (acos((dot(e_vec,pos_vec))/(norm(e_vec)*norm(pos_vec))))
            call.nu_u_o.setText(str(nu))
            omega = (acos((dot(n_vec,e_vec))/multi(norm(n_vec),norm(e_vec))))
            call.omega_l_o.setText(str(omega))
            return [ohm, omega, nu]
        elif inc == 0 or 180: #Inclination is Zero
            if norm(e_vec) > 0: #Elliptical Orbit
                nu = (acos((dot(e_vec,pos_vec))/(norm(e_vec)*norm(pos_vec))))
                call.nu_u_o.setText(str(nu))
                Long_of_peri_pi = acos(dot(cls.I,e_vec)/(norm(cls.I)*norm(e_vec)))
                call.omega_l_lab.setText("Longitude of Perigee")
                call.omega_l_lab.setText(str(Long_of_peri_pi))
                call.ohm_lab.setText("NA")
                call.ohm_o.setText("NA")
                return [Long_of_peri_pi, nu]
            elif norm(e_vec) == 0: #Circular Orbit
                Tr_long_l = acos(dot(cls.I,pos_vec)/(norm(pos_vec)*norm(cls.I)))
                call.omega_l_o.setText(str(Tr_long_l))
                call.omega_l_lab.setText("True Longitude")
                call.ohm_lab.setText("NA")
                call.ohm_o.setText("NA")
                call.nu_u_lab.setText("NA")
                call.nu_u_o.setText("NA")
                return [Tr_long_l]
        elif norm(e_vec) == 0: #Circular orbit with inclination non-zero/pi
            Arg_of_lattitude_u = acos(dot(n_vec,pos_vec)/(norm(n_vec)*norm(pos_vec)))
            call.nu_u_lab.setText(str("Argument Of Perigee"))
            call.nu_u_o.setText(str(Arg_of_lattitude_u))
            call.ohm_lab.setText("NA")
            call.ohm_o.setText("NA")
            call.nu_u_lab.setText("NA")
            call.nu_u_o.setText("NA")
            return [Arg_of_lattitude_u]

    @classmethod
    def possibility(cls, major_body, pos_vec, vel_vec):
        [mu, major_body_radius] = Calculate.muvalue(major_body)
        pos = norm(pos_vec)
        vel = norm(vel_vec)
        sma = 1/((2/pos)-(vel*vel/mu))
        e_vec = (multi((norm(vel_vec)*norm(vel_vec)-(mu/norm(pos_vec))),pos_vec)- multi(dot(pos_vec,vel_vec),vel_vec))/(mu)
        r_peri = sma*(1-norm(e_vec))
        if r_peri <= major_body_radius:
            call.error_status.setText("The Orbit is not possible as radius of perigee is less than radius of the major Body")
            return False
        return True
        
#main
app = QtWidgets.QApplication([])
call = uic.loadUi("GUI\CoOE\CoOE.ui")
call.calculate_button.clicked.connect(MainWindow.Calculate_function)
call.show()
app.exec_()









