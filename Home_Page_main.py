
from sys import path
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sqlite3
from math import *
from Functions.Sections.soi import SoI

from jsontrial import fun_fact

from numpy.linalg import norm
from numpy import dot, pi, cross, multiply as multi
from math import acos

from UI_Functions.ui_splash_screen import Ui_SplashScreen

from SOI3Dviz import SOI

from Functions.Sections.VPCO import CalculateCircularElliptical, CalculateParabola

from Functions.SOI3D import SOI

#from SOI3Dviz import SOI

from Functions.Sections.CoOE import Calculate

from Functions.Sections.DB.call_database import call,raund

# GUI FILE
from UI_Functions.Home_Page import Ui_MainWindow

# IMPORT FUNCTIONS
from UI_Functions.Home_Page_functions import *

path.append('..\Functions\Sections')

# GLOBALS
counter = 0
progress_val = 0
class MainWindow(QMainWindow):
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Getting and storing the window properties in desktoprect 
        desktoprect = QApplication.desktop().availableGeometry(self)

        # Getting the center of the window
        center = desktoprect.center()

        # Moving the window to the center of the screen
        self.move(center.x() - (self.width() * 0.5), center.y() - (self.height() * 0.5)) 

        

        # Hidding some of the widgets in VPCO output
        self.ui.semi_major_axis_toggle_menu_spinbox.hide()
        self.ui.eccentricity_toggle_menu_spinbox.hide()
        self.ui.inclination_toggle_menu_spinbox.hide()
        self.ui.RAAN_toggle_menu_spinbox.hide()
        self.ui.arg_of_per_toggle_menu_spinbox.hide()
        self.ui.tru_ano_toggle_menu_spinbox.hide()

        self.ui.semi_major_axis_toggle_menu_slider.hide()
        self.ui.eccentricity_toggle_menu_slider.hide()
        self.ui.inclination_toggle_menu_slider.hide()
        self.ui.RAAN_toggle_menu_slider.hide()
        self.ui.arg_of_per_toggle_menu_slider.hide()
        self.ui.tru_ano_toggle_menu_slider.hide()


        # Connecting the toggle menu btn to the expand function
        self.ui.toggle_menu_btn.clicked.connect(lambda: UIFunctions.expand(self, 150, True))

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

    

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    # Screen switching defination
    def search(self):
        index = self.ui.combosearchbox.currentIndex()
        if index == 9:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif index == 3:
            self.ui.stackedWidget.setCurrentIndex(2)
        elif index == 1:
            self.ui.stackedWidget.setCurrentIndex(5)
        elif index == 13:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.Orbit_type_stack.setCurrentIndex(0)

    # vpco go button(selecting type of input)
    def vpco_go_btn(self):
        selct_body = self.ui.vpco_major_body.currentIndex()

        
           
        index1 = self.ui.vpco_input_type.currentIndex()
        if index1 == 1:
            if selct_body == 0:
                self.ui.error_selct_body.setText("Please Select Major Body")
            else:
                self.ui.Orbit_type_stack.setCurrentIndex(1)
        elif index1 == 2:
            if selct_body == 0:
                    self.ui.error_selct_body.setText("Please Select Major Body")
            else:
                self.ui.Orbit_type_stack.setCurrentIndex(2)
        elif index1 == 3:
            if selct_body == 0:
                    self.ui.error_selct_body.setText("Please Select Major Body")
            else:
                self.ui.Orbit_type_stack.setCurrentIndex(3)
        elif index1 == 4:
            if selct_body == 0:
                    self.ui.error_selct_body.setText("Please Select Major Body")
            else:
                self.ui.Orbit_type_stack.setCurrentIndex(4)
        elif index1 == 5:
            if selct_body == 0:
                    self.ui.error_selct_body.setText("Please Select Major Body")
            else:
                self.ui.Orbit_type_stack.setCurrentIndex(5)

    #VPCO_a_e_calculate_btn
    def vpco_ae_cal_btn(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        index1 = self.ui.vpco_input_type.currentIndex()
        if index1 == 1:
            self.ui.VPCO_output_stack.setCurrentIndex(0)
            
        elif index1 == 2:
            self.ui.VPCO_output_stack.setCurrentIndex(1)
            
        elif index1 == 3:
            self.ui.VPCO_output_stack.setCurrentIndex(2)
            
        elif index1 == 4:
            self.ui.VPCO_output_stack.setCurrentIndex(3)
            
        elif index1 == 5:
            self.ui.VPCO_output_stack.setCurrentIndex(4)
            
        e = self.ui.eccentricity_inpt_ae.text()
        e = float(e)
        a = self.ui.semimajor_axis_input_ae.text()
        a = float(a)
        maj_body = self.ui.vpco_major_body.currentText()
        maj_body_mass = call.data(maj_body,'mass')
        
        if e == 0 or 0 < e < 1: 
            [r_per, r_apo, mean_motion, T_period, mag_h, sme, slr] = CalculateCircularElliptical.semiecc(a, e, maj_body_mass[0])

            v_per = CalculateCircularElliptical.velocity_at_any_point(a, r_per, maj_body_mass[0])
            v_apo = CalculateCircularElliptical.velocity_at_any_point(a, r_apo, maj_body_mass[0])
            v_slr = CalculateCircularElliptical.velocity_at_any_point(a, slr, maj_body_mass[0])

            esc_vp = CalculateParabola.velocity_at_any_point(r_per, maj_body_mass[0])
            esc_va = CalculateParabola.velocity_at_any_point(r_apo, maj_body_mass[0])
            self.ui.rp_ae.setText(str(round(r_per,4)))
            self.ui.ra_ae.setText(str(round(r_apo,4)))
            self.ui.mu_ae.setText(str(round(sme,4)))
            self.ui.p_ae.setText(str(round(slr,4)))
            self.ui.h_ae.setText(str(round(mag_h,4)))
            self.ui.T_ae.setText(str(round(T_period,4)))
            self.ui.n_ae.setText(str(round(mean_motion,4)))
            self.ui.vp_ae.setText(str(round(v_per,4)))
            self.ui.va_ae.setText(str(round(v_apo,4)))
            self.ui.vlatus_ae.setText(str(round(v_slr,4)))
            self.ui.escvp_ae.setText(str(round(esc_vp,4)))
            self.ui.escva_ae.setText(str(round(esc_va,4)))
        
        #elif e == 1:
            

        
        
    # vpco feature back btn
    def vpco_feature_back_btn(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.Orbit_type_stack.setCurrentIndex(1)          

    # vpco input ae screen
    def vpco_a_e(self):
        e = self.ui.eccentricity_inpt_ae.text()
        e = float(e)
        at = self.ui.semimajor_axis_input_ae.text()
        try:
            a = float(at)
        except:
            self.ui.orbit_type_ae.setText("")
            self.ui.Error_parabola.setText("Please Enter Valid Semimajor Axis Value")
            self.ui.Error_parabola.setStyleSheet(u"color:red;")
        if e == 1 and a < inf:
            self.ui.Error_parabola.setText("It is not Possible\nbecause if the eccentricity is 1 then the\nSemimajor Axis should be infinity or vice versa")
            self.ui.orbit_type_ae.setText("")
            self.ui.Error_parabola.setStyleSheet(u"color:red;")
        elif e == 0 and 0 < a < inf:
            self.ui.orbit_type_ae.setText("Circular")
            self.ui.Error_parabola.setText("")
        elif e == 1 and (at == "infinite" or "inf" or "Infinite" or "Inf" or 'infinity' or 'Infinity'):
            self.ui.orbit_type_ae.setText("Parabola")
            self.ui.Error_parabola.setText("")
        elif 0 < e < 1 and 0 < a < inf:
            self.ui.orbit_type_ae.setText("Ellipse")
            self.ui.Error_parabola.setText("")
        elif e > 1 and 0 < a < inf:
            self.ui.orbit_type_ae.setText("Hyperbola")
            self.ui.Error_parabola.setText("")
        elif (e == 0 or e < 1 or e > 1) and (at == "infinite" or "inf" or "Infinite" or "Inf" or 'infinity' or 'Infinity'):
            self.ui.orbit_type_ae.setText("")
            self.ui.Error_parabola.setText("Please enter a finite Semimajor axis value")
            self.ui.Error_parabola.setStyleSheet(u"color:red;")
        
            
        
    # vpco home_btn_2
    def homebtn2(self):
        self.ui.Orbit_type_stack.setCurrentIndex(0)
        self.ui.Error_parabola.setText("")
    
    # COE n AOE Calculation
    def coeNaoe(self):
        Ri = self.ui.Ri_coe_n_aoe.text()
        Rj = self.ui.Rj_coe_n_aoe.text()
        Rk = self.ui.Rk_coe_n_aoe.text()
        Vi = self.ui.Vi_coe_n_aoe.text()
        Vj = self.ui.Vj_coe_n_aoe.text()
        Vk = self.ui.Vk_coe_n_aoe.text()
        pos_vec = [float(Ri), float(Rj), float(Rk)]
        vel_vec = [float(Vi), float(Vj) ,float(Vk)] 
        Major_Body = self.ui.maj_body_CoOE.currentText()
        Major_Body = Major_Body.strip()

        if Major_Body != 'Other':
            self.ui.otherbody_stack.setCurrentIndex(0)
            [mu, major_body_radius] = Calculate.muvalue(self,Major_Body)
        
        elif Major_Body == 'Other':
            self.ui.otherbody_stack.setCurrentIndex(1)
            Body_mass = self.ui.other_body_mass_coe_n_aoe.text()
            try:
                Body_mass = Body_mass.split('e')
            except:
                Body_mass = Body_mass
            if len(Body_mass) == 1:
                Body_mass = int(Body_mass[0])
                
            elif len(Body_mass) == 2:
                b1 = int(Body_mass[0])
                b2 = int(Body_mass[1])
                Body_mass = b1 * 10**b2  
            
            major_body_radius = self.ui.other_body_radius_coe_n_aoe.text()
            major_body_radius = float(major_body_radius)
            mu = float(self.G) * float(int(Body_mass))

        OE_values, ACOE_values = Calculate.OE(pos_vec, vel_vec, mu)
        
        
        sma = float(OE_values['Semi-Major Axis'])
        inc_deg = float(OE_values['Inclination'])*(180/pi)
        e_vec = OE_values['Vec_Eccentricity']
        e_norm = float(OE_values['Norm_Eccentricity'])

        self.ui.semimajor_axis_coe_n_aoe.setText(str(round(sma, 4)))
        self.ui.inclination_coe_n_aoe.setText(str(round(inc_deg, 4)))
        self.ui.eccentricity_coe_n_aoe.setText(str(round(e_norm, 4)))

        [h_vec, n_vec] = Calculate.other_var(pos_vec, vel_vec)
        
        r_peri = sma*(1-norm(e_vec))
        
        if r_peri < major_body_radius:
            self.ui.CoOE_output_stack.setCurrentIndex(0)
            self.ui.CoOE_output_lbl_error.setText('Satellite will crash into the planets surface')
        else:
            self.ui.CoOE_output_stack.setCurrentIndex(1)
            self.ui.CoOE_output_lbl_error.setText('')

        
        quad = Calculate.position_of_n_vector(n_vec)
        self.ui.CoOE_output_para_lbl.setText(quad)
        keys = list(ACOE_values.keys())
        values = list(ACOE_values.values()) 
        self.ui.RAAN_CoOE_lbl.setText(keys[0])
        self.ui.RAAN_coe_n_aoe.setText(str(round(values[0] * (180/pi), 4)))
        self.ui.arg_of_per_CoOE_lbl.setText(keys[1])
        self.ui.arg_of_per_coe_n_aoe.setText(str(round(values[1] * (180/pi), 4)))
        self.ui.tru_ano_CoOE_lbl.setText(keys[2])
        self.ui.tru_ana_coe_n_aoe.setText(str(round(values[2] * (180/pi), 4))) 

        

    # SOI
    def SEARCH(self):
        planet_name = self.ui.SOI_planet_name.currentText()
        planet_mass = call.data(planet_name,'mass')
        dist_frm_sun = call.data(planet_name,'dist_frm_sun')
        self.ui.lbl_mass.setText("Mass of " + str(planet_mass[1])+":")
        self.ui.soi_mass.setText(str(planet_mass[0]))
        self.ui.dist_frm_sun.setText(str(dist_frm_sun[0]))
       
            
    def SOI(self):
        planet_name = self.ui.SOI_planet_name.currentText()
        self.ui.rSOI_of_planet_lbl.setText("Radius of SOI of " + str(planet_name.strip()) + ":")
        Mass_of_Sun = call.data('Sun','mass')
        Minor_body_mass = self.ui.soi_mass.text() 
        distance_bt_sun_plnt = self.ui.soi_mass.text()
        rSOI = (float(distance_bt_sun_plnt)*(float(Minor_body_mass)/Mass_of_Sun[0])**(2/5))
        self.ui.soi_rad.setText(raund(rSOI,4))
    
       
    # SOI Graph
    def soi_graph(self):
        planet_name1 = self.ui.SOI_planet_name.currentText()
        planet_name = planet_name1.strip()
        planet_name = planet_name.lower()
        rSOI = self.ui.soi_rad.text()

        r_planet = call.data(planet_name1,'radius')[0]
        r_soimb = float(rSOI)/r_planet
        graph3d = SOI(planet_name,rSOI,r_soimb)
        graph3d.run()
            

  
    
    # Home_btn
    def meth_Home_btn(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    # Julian Day Calculation
    def calendar_time(self):
        selected_date = self.ui.calendarWidget.selectedDate()
        year = selected_date.year()
        month = selected_date.month()
        day = selected_date.day()
        selected_time = self.ui.timeEdit.time()
        hour = selected_time.hour()
        minutes = selected_time.minute()
        seconds = selected_time.second()
        accuracy = self.ui.digits_accuracy.value()
        calendar = self.ui.type_of_calendar.currentText()
        if calendar == "  Gregorian Calendar":
            self.ui.Error_state.setText("")
            #julian day number from Gregorian calender date
            JDN = int((1461 * (year + 4800 + (month - 14)/12))/4) + int((367 * month - 2 - 12 * ((month - 14)/12))/12) - int((3 * ((year + 4900 + (month - 14)/12)/100))/4) + day - 32075
        elif calendar == "  Julian Calendar":
            self.ui.Error_state.setText("")
            #julian day number from julian calender date
            JDN = 367 * year - int((7 * (year + 5001 + (month - 9)/7))/4) + int((275 * month)/9) + day + 1729777
        elif calendar == "  Select the Type Of Calendar":
            self.ui.Error_state.setText("Please select the type of calendar")
                
        #JDN to JD
        JD = JDN + round(((hour - 12)/24),accuracy) + round((minutes/1440), accuracy) + round((seconds/86400), accuracy)
        
        self.ui.JulianDay_Result.setText(str(round(JD, accuracy))+ str(' Julian Days'))
    
    def slider_released(self,event):
        changed_slidervalue = self.ui.semi_major_axis_toggle_menu_slider.value()
        #print(changed_slidervalue)
        #current_slidervalue = self.slider_pressed()
        #print(current_slidervalue, changed_slidervalue)
        current_spinvalue = self.ui.semi_major_axis_toggle_menu_spinbox.value()
        if changed_slidervalue > current_slidervalue:
            remain = changed_slidervalue - current_slidervalue
            #print(remain)
            self.ui.semi_major_axis_toggle_menu_spinbox.setValue(current_spinvalue + remain)
        else:
            add = -changed_slidervalue + current_slidervalue
            #print(add)
            self.ui.semi_major_axis_toggle_menu_spinbox.setValue(current_spinvalue - add)

    def slider_pressed(self, event):
        print(event)
        self.ui.semi_major_axis_toggle_menu_spinbox.setValue(event)
        #print(current_slidervalue)
        return event

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(50)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.app_description_lbl.setText("WELCOME TO <strong>MOPy</strong>")

        # Change Texts
        QtCore.QTimer.singleShot(1200, lambda: self.ui.app_description_lbl.setText("<strong>Initializing</strong> Database"))
        QtCore.QTimer.singleShot(2500, lambda: self.ui.app_description_lbl.setText("<strong>Pulling</strong> Resources"))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.app_description_lbl.setText("<strong>Arranging</strong> User Interface "))
        QtCore.QTimer.singleShot(4700, lambda: self.ui.app_description_lbl.setText("Ready to <strong>Takeoff</strong> "))
        QtCore.QTimer.singleShot(6000, lambda: self.ui.app_description_lbl.setText(" "))

        # Fun Facts
        
        self.ui.loading_lbl.setText("<strong>Do you know: </strong>"+ fun_fact())

        ### Spiral Progress BAR

        # Setting the Minimum value 
        self.ui.progressBar_2.spb_setMinimum((0, 0, 0))

        # Setting the maximum value 
        self.ui.progressBar_2.spb_setMaximum((120, 220, 320))

        # Set progress value
        x = 100
        self.ui.progressBar_2.spb_setValue((x, x*2, x*3))

        #Set Progress Color
        self.ui.progressBar_2.spb_lineColor(((233, 152, 6), (6, 201, 233), (233, 6, 88)))

        # Setting the initial position of the progress bar
        self.ui.progressBar_2.spb_setInitialPos(('West', 'South', 'East'))

        # Setting the direction of Progress of ProgressBar
        self.ui.progressBar_2.spb_setDirection(('Clockwise', 'Clockwise', 'Clockwise'))

        # Set line width of Progressbar
        self.ui.progressBar_2.spb_lineWidth(4)

        # Setting the gap width between the progress Bar
        self.ui.progressBar_2.spb_setGap(4)

        # Set line Style
        self.ui.progressBar_2.spb_lineStyle(('SolidLine', 'SolidLine', 'SolidLine'))

        # Set end cap to progress Bar
        self.ui.progressBar_2.spb_lineCap(('RoundCap','RoundCap', 'RoundCap'))

        # Hide the path followed by the progress Bar
        self.ui.progressBar_2.spb_setPathHidden(True)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        self.timer_2 = QtCore.QTimer() 
        self.timer_2.timeout.connect(self.progress_2)
        self.timer_2.start(5)

        # Set all the progress bar to zero on start
        QtCore.QTimer.singleShot(0, lambda: self.ui.progressBar_2.spb_setValue((0, 0, 0)))

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1  

    def progress_2(self):
            global progress_val
            # Set Progress Values
            self.ui.progressBar_2.spb_setValue((progress_val, progress_val*2, progress_val*3))

            # Reset Progresses if the maximum value is reached
            if progress_val > 120:
                progress_val = 0

            # Increase progress value by one, every 60ms

            progress_val += 1
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
