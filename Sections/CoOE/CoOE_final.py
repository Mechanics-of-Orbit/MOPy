import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from numpy.linalg import norm
from numpy import dot,pi,cross,multiply as multi
import pandas
# If I want to import every thing inside a module the type-'from numpy import *' then there is no need to use numpy.function instead directly type function name
from math import acos

#Constants
I = [1, 0, 0]
J = [0, 1, 0]
K = [0, 0, 1]
G = 6.67e-20 #units are km3 kg-1 s-2

#Unit Conversion
def convert_unit(len,Radius,unit1,unit2):
    i = len
    if unit1 == 'km' and unit2 == 'km':
        out = [element * 2 for element in i]
        return(out)
    elif unit1 == 'km' and unit2 == 'miles':
        out = [element * 0.621371 for element in i]
        return(out)
    elif unit1 == 'km' and unit2 == 'AU':
        out = [element * 6.6846e-9 for element in i]
        return(out)
    elif unit1 == 'km' and unit2 == 'DU':
        out = [element / Radius for element in i]
        return(out)
    elif unit1 == 'miles' and unit2 == 'miles':
        out = i
        return(out)
    elif unit1 == 'miles' and unit2 == 'km':
        out = [element / 0.621371 for element in i]
        return(out)
    elif unit1 == 'miles' and unit2 == 'AU':
        out = [element * 1.07578e-8 for element in i]
        return(out)
    elif unit1 == 'miles' and unit2 == 'DU':
        out = [element *0.621371/Radius for element in i]
        return(out)
    if unit1 == 'AU' and unit2 == 'AU':
        out = i
        return(out)
    elif unit1 == 'AU' and unit2 == 'miles':
        out = [element /1.07578e-8 for element in i]
        return(out)
    elif unit1 == 'AU' and unit2 == 'km':
        out = [element * 6.6806e-9 for element in i]
        return(out)
    elif unit1 == 'AU' and unit2 == 'DU':
        out = [element *Radius/6.6846e-9 for element in i]
        return(out)


#function for the calculate_button
def Calculate_function():
    pos_vec_str = [call.pos_vec_i.text(), call.pos_vec_j.text(), call.pos_vec_k.text()]
    vel_vec_str = [call.vel_vec_i.text(), call.vel_vec_j.text(), call.vel_vec_k.text()]
    Major_Body = call.major_body.currentText()
    
    pos_vec = list(map(float, pos_vec_str))
    vel_vec = list(map(float, vel_vec_str))

    #calling values from the csv
    if Major_Body != "Other":
        major_body_list = pandas.read_csv("Major_and_Minor_Bodies.csv")
        major_bodies_mass = list(major_body_list.Mass)
        major_bodies_radius = list(major_body_list.Radius)
        major_bodies = list(major_body_list.Major_Body)
        sel_major_body = major_bodies.index(Major_Body)
        major_body_mass = major_bodies_mass[sel_major_body]
        major_body_radius = major_bodies_radius[sel_major_body]
    else:
        major_body_mass = float(call.other_major_body_mass.text())
        major_body_radius = float(call.other_major_body_radius.text())
    
    if call.pos_vec_unit.currentText() and call.vel_vec_unit.currentText() == "km":
        j = 1
    elif call.pos_vec_unit.currentText() == "Miles":
        pos_vec = convert_unit(pos_vec, major_body_radius, "miles", "km")
        if call.vel_vec_unit.currentText() == "Miles":
            vel_vec = convert_unit(pos_vec, major_body_radius, "miles", "km")
    elif call.pos_vec_unit.currentText() == "AU":
        pos_vec = convert_unit(pos_vec, major_body_radius, "AU", "km")
        if call.vel_vec_unit.currentText() == "AU":
            vel_vec = convert_unit(pos_vec, major_body_radius, "AU", "km")
    elif call.pos_vec_unit.currentText() == "DU" and call.vel_vec_unit.currentText() == "DU/TU":
        pos_vec = convert_unit(pos_vec, major_body_radius, "DU", "km")
        vel_vec = convert_unit(pos_vec, major_body_radius, "DU", "km")


    #Standard Formulae
    if call.pos_vec_unit.currentText() == "DU" and call.vel_vec_unit.currentText() == "DU/TU":
        mu = 1
    elif call.pos_vec_unit.currentText() == "DU" or call.vel_vec_unit.currentText() == "DU/TU":
        call.error_status.setText("Enter both in same units")
    else:
        mu = G * major_body_mass
    h_vec = cross(pos_vec,vel_vec)
    n_vec = cross(K,h_vec)
    e_vec= (multi((norm(vel_vec)*norm(vel_vec)-(mu/norm(pos_vec))),pos_vec)- multi(dot(pos_vec,vel_vec),vel_vec))/(mu)
    inc = (acos((dot(h_vec,K))/norm(h_vec))) * 180/pi
    ohm = (acos((dot(I,n_vec))/norm(n_vec))) * 180/pi
    omega = (acos((dot(n_vec,e_vec))/multi(norm(n_vec),norm(e_vec)))) * 180/pi
    nu = (acos((dot(e_vec,pos_vec))/(norm(e_vec)*norm(pos_vec)))) * 180/pi
    sma = 1/((2/norm(pos_vec))-((norm(vel_vec)*norm(vel_vec))/mu))
    c = sma*norm(e_vec)
    r_peri = sma*(1-norm(e_vec))
    r_apo = sma*(1+norm(e_vec))
       

    #Condtional Statements to check wheather orbit is possible or not and if possible what are values associated with it.
    if r_peri <= major_body_radius:
        call.error_status.setText("The Orbit is not possible as radius of perigee is less than radius of the major Body")        
    elif inc != 0 or 180 and norm(e_vec) > 0:
        if n_vec[0] > 0 and n_vec[1]:
            call.error_status.setText("This is a Prograde Elliptical Orbit and is in first Quadrant.")

            if ohm >90:
                ohm = 360 - ohm
                ohm_nom = ohm
            else:
                ohm_nom = ohm
        elif n_vec[0] < 0 and n_vec[1] > 0:
            call.error_status.setText("This is a Retrograde Elliptical Orbit and is in second Quadrant.")
            if ohm > 180:
                ohm = 360 - ohm
                ohm_nom = ohm
            else:
                ohm_nom = ohm 
        elif n_vec[0] < 0 and n_vec[1] < 0:
            call.error_status.setText("This is a Retrograde Elliptical Orbit and is in Third Quadrant.")
            if ohm < 180:
                ohm = 360 - ohm
                ohm_nom = ohm
            else: 
                ohm_nom = ohm
        elif n_vec[0] > 0 and n_vec[1] < 0:
            call.error_status.setText("This is a Prograde Elliptical Orbit and is in fourth Quadrant.")
            if ohm < 90:
                ohm = 360 - ohm
                ohm_nom = ohm
            else:
                ohm_nom = ohm
        call.ecc_o.setText(str(norm(e_vec)))
        call.inc_o.setText(str(inc))
        call.omega_l_o.setText(str(omega))
        call.nu_u_o.setText(str(nu))
        call.ohm_o.setText(str(ohm_nom))
        call.sma_o.setText(str(sma))
    elif inc != 0 or 180 and (e_vec) == 0:
        if n_vec[0] > 0 and n_vec[1] > 0: 
            call.error_status.setText("This is a Prograde Elliptical Orbit and is in first Quadrant.")
            if ohm >90:
                ohm = 360 - ohm
                call.ohm_o.setText(str(ohm))
            else:
                call.ohm_o.setText(str(ohm))
        elif n_vec[0] < 0 and n_vec[1] > 0:
            call.error_status.setText("This is a Retrograde Elliptical Orbit and is in second Quadrant.")
            if ohm >180:
                ohm = 360 - ohm
                call.ohm_o.setText(str(ohm))
            else:
                call.ohm_o.setText(str(ohm))

        elif n_vec[0] < 0 and n_vec[1] < 0:
            call.error_status.setText("This is a Retrorograde Elliptical Orbit and is in third Quadrant.")
            if ohm < 180:
                ohm = 360 - ohm
                call.ohm_o.setText(str(ohm))
            else: 
                call.ohm_o.setText(str(ohm))
        elif n_vec[0] > 0 and n_vec[1] < 0:
            call.error_status.setText("This is a Prograde Elliptical Orbit and is in fourth Quadrant.")
            if ohm < 90:
                ohm = 360 - ohm
                call.ohm_o.setText(str(ohm))
            else:
                call.ohm_o.setText(str(ohm))
        Arg_of_lattitude_u = acos(dot(n_vec,pos_vec)/(norm(n_vec)*norm(pos_vec)))
        call.nu_u_lab.setText(str("Argument Of Perigee"))
        call.nu_u_o.setText(str(Arg_of_lattitude_u))
        call.sma_o.setText(str(sma))
        call.ecc_o.setText(str(norm(e_vec)))
        call.inc_o.setText(str(inc))

    #When the orbit is Elliptical and it is parallel to equatorial Plane
    elif inc == 0 or 180 and e_vec > 0:
        call.inc_o.setText(str(inc))
        nu = acos((dot(e_vec,pos_vec))/(norm(e_vec)*norm(pos_vec)))
        Long_of_peri_pi = acos(dot(I,e_vec)/(norm(I)*norm(e_vec)))
        call.nu_u_o.setText(str(nu))
        call.sma_o.setText(str(sma))
        call.omega_l_lab.setText("Longitude of Perigee")
        call.omega_l_lab.setText(str(Long_of_peri_pi))
        call.ecc_o.setText(str(norm(e_vec)))

    # When the Orbit is Circular and it is Parallel to Equatorial Plane
    elif inc ==0 or 180 and e_vec == 0:
        call.inc_o.setText(str(inc))
        Tr_long_l = acos(dot(I,pos_vec)/(norm(pos_vec)*norm(I)))
        call.nu_u_o.setText(str(nu))
        call.sma_o.setText(str(sma))
        call.omega_l_o.setText(str(Tr_long_l))
        call.omega_l_lab.setText("True Longitude")
        call.ecc_o.setText(str(norm(e_vec)))
    

        


#main
app = QtWidgets.QApplication([])
call = uic.loadUi("GUI\CoOE\CoOE.ui")

call.calculate_button.clicked.connect(Calculate_function)

call.show()
app.exec_()
