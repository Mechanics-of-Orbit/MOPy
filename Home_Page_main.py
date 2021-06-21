
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

from UI_Functions.ui_splash_screen import Ui_SplashScreen

from SOI3Dviz import SOI

from Functions.Sections.VPCO import CalculateCircularElliptical, CalculateParabola

from SOI3Dviz import SOI

from Functions.Sections.CoOE import Calculate

# GUI FILE
from UI_Functions.Home_Page import Ui_MainWindow

# IMPORT FUNCTIONS
from UI_Functions.Home_Page_functions import *

path.append('..\Functions\Sections')

# GLOBALS
counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        

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
        db = sqlite3.connect("Functions/Sections/DB/MajorBody_data.db")
        cursor = db.cursor()
        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[maj_body])

       
        for row_number, row_data in enumerate(result):
            maj_body_mass = row_data[1]
        
        if e == 0 or 0 < e < 1: 
            [r_per, r_apo, mean_motion, T_period, mag_h, sme, slr] = CalculateCircularElliptical.semiecc(a, e, maj_body_mass)

            v_per = CalculateCircularElliptical.velocity_at_any_point(a, r_per, maj_body_mass)
            v_apo = CalculateCircularElliptical.velocity_at_any_point(a, r_apo, maj_body_mass)
            v_slr = CalculateCircularElliptical.velocity_at_any_point(a, slr, maj_body_mass)

            esc_vp = CalculateParabola.velocity_at_any_point(r_per, maj_body_mass)
            esc_va = CalculateParabola.velocity_at_any_point(r_apo, maj_body_mass)
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
        self.ui.Orbit_type_stack.setCurrentIndex(0)          

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
        if e == 1 and a < inf:
            self.ui.Error_parabola.setText("It is not Possible\nbecause if the eccentricity is 1 then the\nSemimajor Axis should be infinity or vice versa")
            self.ui.orbit_type_ae.setText("")
        elif e == 0 and 0 < a < inf:
            self.ui.orbit_type_ae.setText("Circular")
            self.ui.Error_parabola.setText("")
        elif e == 1 and (at == "infinity" or "inf" or "Infinity" or "Inf"):
            self.ui.orbit_type_ae.setText("Parabola")
            self.ui.Error_parabola.setText("")
        elif 0 < e < 1 and 0 < a < inf:
            self.ui.orbit_type_ae.setText("Ellipse")
            self.ui.Error_parabola.setText("")
        elif e > 1 and 0 < a < inf:
            self.ui.orbit_type_ae.setText("Hyperbola")
            self.ui.Error_parabola.setText("")
        elif (e == 0 or e < 1 or e > 1) and (at == "infinite" or "inf" or "Infinite" or "Inf"):
            self.ui.orbit_type_ae.setText("")
            self.ui.Error_parabola.setText("Please enter a finite Semimajor axis value")
        
            
        
    # vpco home_btn_2
    def homebtn2(self):
        self.ui.Orbit_type_stack.setCurrentIndex(0)
    
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
        print(pos_vec)
        print(vel_vec)


    # SOI
    def SEARCH(self):
        db = sqlite3.connect("Functions/Sections/DB/MajorBody_data.db")
        cursor = db.cursor()

        planet_name = self.ui.SOI_planet_name.currentText()
        
        self.ui.lbl_mass.setText("Mass of" + str(planet_name)+":")
       

        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[planet_name])

       
        for row_number, row_data in enumerate(result):
            self.ui.soi_mass.setText(str(row_data[1]))
            self.ui.dist_frm_sun.setText(str(row_data[8]))
            
    def SOI(self):
        planet_name = self.ui.SOI_planet_name.currentText()
        self.ui.label_18.setText("Radius of SOI of" + str(planet_name) + ":")
        Mass_of_Sun = 1.989e30
        Minor_body_mass = self.ui.soi_mass.text() 
        distance_bt_sun_plnt = self.ui.soi_mass.text()
        rSOI = (float(distance_bt_sun_plnt)*(float(Minor_body_mass)/Mass_of_Sun)**(2/5))
        self.ui.soi_rad.setText(str(rSOI))
    
       
    # SOI Graph
    def soi_graph(self):
        planet_name1 = self.ui.SOI_planet_name.currentText()
        planet_name = planet_name1.strip()
        planet_name = planet_name.lower()
        rSOI = self.ui.soi_rad.text()
        db = sqlite3.connect("Functions/Sections/DB/MajorBody_data.db")
        cursor = db.cursor()
        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[planet_name1])
        
        for row_number, row_data in enumerate(result):
            r_planet = row_data[2]/2
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
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("WELCOME TO <strong>MOPy</strong>")

        # Change Texts
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> Database"))
        QtCore.QTimer.singleShot(3800, lambda: self.ui.label_description.setText("<strong>LOADING</strong> Resources"))
        QtCore.QTimer.singleShot(5000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> User Interface "))
        QtCore.QTimer.singleShot(5500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> Completed "))
        QtCore.QTimer.singleShot(6000, lambda: self.ui.label_description.setText(" "))




        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

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
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
