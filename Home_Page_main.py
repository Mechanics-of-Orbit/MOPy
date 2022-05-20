from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QParallelAnimationGroup, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import sys
from math import *
from sys import path
from numpy.linalg import norm
from numpy import dot, pi, cross, multiply as multi,linspace
from math import acos


from orbit3d import OrbitPlot
import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure



# IMPORT FUNCTIONS 
from jsontrial import fun_fact
from UI_Functions.Circular_Progress.py_circular_progress import PyCircularProgress
from UI_Functions.ui_splash_screen import Ui_SplashScreen
from Functions.Sections.VPCO import CalculateCircularElliptical, CalculateParabola
from Functions.SOI3D import SOI3D
from Functions.Sections.soi import *
from Functions.Sections.CoOE import Calculate
from Functions.Sections.DB.call_database import *
from UI_Functions.Home_Page import Ui_MainWindow
from UI_Functions.Home_Page_functions import *
from Hover_Slide_animation_functn import *





# from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

path.append('..\Functions\Sections')

# GLOBALS
counter = 0
slider_pressed = 0

a = 0

class MainWindow(QMainWindow):
    I = [1, 0, 0]
    J = [0, 1, 0]
    K = [0, 0, 1]
    G = 6.67e-20 #units are in km3 kg-1 s-2
    def __init__(self, parent=None):
        super().__init__(parent)
        #QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Getting and storing the window properties in desktoprect 
        desktoprect = QApplication.desktop().availableGeometry(self)

        # Getting the center of the window
        center = desktoprect.center()

        # Moving the window to the center of the screen
        self.move(center.x() - (self.width() * 0.5), center.y() - (self.height() * 0.5)) 


        self.ui.Semi_dial.setNotchesVisible(1)
        self.ui.ecce_dial.setNotchesVisible(1)


        self.ui.Orbtl_tranf_Out_frame.hide()
        self.ui.Orbtl_tranf_Inp_n_Out_frames_container.hide()
        self.ui.Plot_frame_for_Orbital_transfer.hide()
        
        
        
        # Assigning hover signal to the squares in the home screen
        self.ui.Home_VPCO.installEventFilter(self)
        self.ui.Home_Julian_Day.installEventFilter(self)
        self.ui.Home_Orbital_Elements.installEventFilter(self)
        self.ui.Home_SOI.installEventFilter(self)
        self.ui.Home_Orbit_Visualization.installEventFilter(self)
        self.ui.Home_Ground_Track.installEventFilter(self)
        self.ui.Home_Planet_in_Shadow.installEventFilter(self)
        self.ui.Home_Planetary_Ephimeris.installEventFilter(self)
        self.ui.Home_Numerical_integ.installEventFilter(self)
        self.ui.Home_Orbital_transfer.installEventFilter(self)
        self.ui.Home_Eulers_Angle.installEventFilter(self)
        self.ui.Home_VPCO_Label.installEventFilter(self)
        self.ui.Hohmn_transf_label.installEventFilter(self)

        
###################################_______Plotting Graphs_______#########################################

#
# 1
# ########-----------------------------------VPCO_Graph-----------------------------------------##########
        VPCO_Graph_Layout = QtWidgets.QVBoxLayout(self.ui.graph_widget)
        VPCO_Static_Canvas = FigureCanvas(Figure(facecolor = "#36375c"))
        VPCO_Graph_Layout.addWidget(NavigationToolbar(VPCO_Static_Canvas, self))
        VPCO_Graph_Layout.addWidget(VPCO_Static_Canvas)
        self._static_ax = VPCO_Static_Canvas.figure.add_subplot(111,facecolor='black', title = "Orbit")
        
        # ji = OrbitPlot.plotOrbitMPL(3.986e5, 12000, 12000, 0, 2*np.pi)
        self._static_ax.axis('equal')
        # self._static_ax.plot(ji[0], ji[1])

        # jo = OrbitPlot.hohmannTransfer(7178, 6878, 22378, 22378, 3.986e5, 6378)
        # self._static_ax.plot(jo[0][0], jo[0][1], "r")
        # self._static_ax.plot(jo[1][0], jo[1][1], "yellow", LineStyle = "dotted")
        # self._static_ax.plot(jo[2][0], jo[2][1],"green")
        MajorBodyPlot = OrbitPlot.plotOrbitMPL(3.986e5,6378, 6378, 0, 2*np.pi)
        self._static_ax.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        Orbit = OrbitPlot.plotOrbitMPL(3.986e5, 37500 ,12500, 0, 2*np.pi)
        self._static_ax.plot(Orbit[0], Orbit[1], "r")
        

        self._static_ax.tick_params(axis='x', colors='white') 
        self._static_ax.tick_params(axis='y', colors='white')

#
# 2
# ########-----------------------------------Orbital_Transfer_Graph-----------------------------------------##########
#
# 2------1
# ########--------------------------Orbital_Transfer_Graph - Hohmann Transfer-------------------------------##########
        Orbital_Transfer_Graph_Layout = QtWidgets.QVBoxLayout(self.ui.Plot_Widget_for_Orbital_Transfer)
        Orbital_Transfer_Static_Canvas = FigureCanvas(Figure(facecolor = "#36375c"))
        Orbital_Transfer_Graph_Layout.addWidget(NavigationToolbar(Orbital_Transfer_Static_Canvas, self))
        Orbital_Transfer_Graph_Layout.addWidget(Orbital_Transfer_Static_Canvas)
        self._static_ax = Orbital_Transfer_Static_Canvas.figure.add_subplot(111,facecolor='black',title="Phasing Maneuver")
        self._static_ax.axis('equal')
       
        jo = OrbitPlot.phasingManeuver(3.986e5, 6378, 13600, 6800, 0, np.pi/2)
        self._static_ax.plot(jo[0][0], jo[0][1], "r", label = 'Initial Orbit')
        self._static_ax.plot(jo[1][0], jo[1][1], "yellow", linestyle = "dotted", label = 'Phasing Orbit')
        
        MajorBodyPlot = OrbitPlot.plotOrbitMPL(3.986e5,6378, 6378, 0, 2*np.pi)
        self._static_ax.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        self._static_ax.tick_params(axis='x', colors='white') 
        self._static_ax.tick_params(axis='y', colors='white')
        self._static_ax.legend(loc="upper right")
#
# 2------2
# ########---------------------Orbital_Transfer_Graph - Bielliptical Hohmann Transfer---------------------##########
        # Orbital_Transfer_Graph_Layout = QtWidgets.QVBoxLayout(self.ui.Plot_Widget_for_Orbital_Transfer)
        # Orbital_Transfer_Static_Canvas = FigureCanvas(Figure(facecolor = "#36375c"))
        # Orbital_Transfer_Graph_Layout.addWidget(NavigationToolbar(Orbital_Transfer_Static_Canvas, self))
        # Orbital_Transfer_Graph_Layout.addWidget(Orbital_Transfer_Static_Canvas)
        # self._static_ax = Orbital_Transfer_Static_Canvas.figure.add_subplot(111,facecolor='black',title="Bi-Elliptical Hohmann transfer")
        # self._static_ax.axis('equal')
        # Orbit = OrbitPlot.biellipticalHohmannTransfer(3.986e5, 6378, 7000, 7000, 105000, 105000, rt1a = 210000)
        # self._static_ax.plot(Orbit[0][0], Orbit[0][1], "r", label = 'Initial Orbit')
        # self._static_ax.plot(Orbit[1][0], Orbit[1][1], "y", label = 'Final Orbit')
        # self._static_ax.plot(Orbit[2][0], Orbit[2][1], "b", label = 'Initial Transfer Orbit', LineStyle = "dotted")
        # self._static_ax.plot(Orbit[3][0], Orbit[3][1], "m", label = 'Final Transfer Orbit', LineStyle = "dotted")
        # self._static_ax.legend(loc="best", fancybox=True, framealpha = 0.5)

        
        # MajorBodyPlot = OrbitPlot.plotOrbitMPL(3.986e5,6378, 6378, 0, 2*np.pi)
        # self._static_ax.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        # self._static_ax.tick_params(axis='x', colors='white') 
        # self._static_ax.tick_params(axis='y', colors='white')


#
# 2------3
# ########---------------------Orbital_Transfer_Graph - Hohmann Transfer---------------------##########
        # Orbital_Transfer_Graph_Layout = QtWidgets.QVBoxLayout(self.ui.Plot_Widget_for_Orbital_Transfer)
        # Orbital_Transfer_Static_Canvas = FigureCanvas(Figure(facecolor = "#36375c"))
        # Orbital_Transfer_Graph_Layout.addWidget(NavigationToolbar(Orbital_Transfer_Static_Canvas, self))
        # Orbital_Transfer_Graph_Layout.addWidget(Orbital_Transfer_Static_Canvas)
        # self._static_ax = Orbital_Transfer_Static_Canvas.figure.add_subplot(111,facecolor='black',title="Hohmann transfer")
        # self._static_ax.axis('equal')
        # Orbit = OrbitPlot.hohmannTransfer(7178, 6878, 22378, 22378, 3.986e5, 6378)
        # self._static_ax.plot(Orbit[0][0], Orbit[0][1], "r", label = 'Initial Orbit')
        # self._static_ax.plot(Orbit[1][0], Orbit[1][1], "y", label = 'Final Orbit')
        # self._static_ax.plot(Orbit[2][0], Orbit[2][1], "b", label = 'Initial Transfer Orbit', LineStyle = "dotted")
        
        # self._static_ax.legend(loc="upper right")

        
        # MajorBodyPlot = OrbitPlot.plotOrbitMPL(3.986e5,6378, 6378, 0, 2*np.pi)
        # self._static_ax.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        # self._static_ax.tick_params(axis='x', colors='white') 
        # self._static_ax.tick_params(axis='y', colors='white')

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

    def trial(self):
        self.ui.Orbtl_tranf_Out_frame.show()
        self.ui.Plot_frame_for_Orbital_transfer.show()
        self.ui.Container_for_Type_of_Orbital_Transfer.hide()
    
    def eventFilter(self, source, event):
        if (source == self.ui.Home_VPCO and event.type() == QEvent.Enter):
            Animation_Home_VPCO(self,"long", self.ui.Home_VPCO_Slider, 91, 182)
        elif source == self.ui.Home_VPCO and event.type() == QEvent.Leave:
            Animation_Home_VPCO(self,"long", self.ui.Home_VPCO_Slider, 91, 91)

        elif (source == self.ui.Home_Julian_Day and event.type() == QEvent.Enter):
            Animation_Home_Julian_Day(self,"long", self.ui.Home_Julian_Day_Slider, 91, 182)
        elif source == self.ui.Home_Julian_Day and event.type() == QEvent.Leave:
            Animation_Home_Julian_Day(self,"long", self.ui.Home_Julian_Day_Slider, 91, 91) 


        elif (source == self.ui.Home_Orbital_Elements and event.type() == QEvent.Enter):
            Animation_Orbital_Elements(self,"long", self.ui.Home_Orbital_Elements_Slider, 91, 182)
        elif source == self.ui.Home_Orbital_Elements and event.type() == QEvent.Leave:
            Animation_Orbital_Elements(self,"long", self.ui.Home_Orbital_Elements_Slider, 91, 91)

        elif (source == self.ui.Home_SOI and event.type() == QEvent.Enter):
            Animation_Home_SOI(self,"long", self.ui.Home_SOI_Slider, 91, 182)
        elif source == self.ui.Home_SOI and event.type() == QEvent.Leave:
            Animation_Home_SOI(self,"long", self.ui.Home_SOI_Slider, 91, 91)
        
        elif (source == self.ui.Home_Orbit_Visualization and event.type() == QEvent.Enter):
            Animation_Home_Orbit_Visualization(self,"long", self.ui.Home_Orbit_Visualization_Slider, 91, 182)
        elif source == self.ui.Home_Orbit_Visualization and event.type() == QEvent.Leave:
            Animation_Home_Orbit_Visualization(self,"long", self.ui.Home_Orbit_Visualization_Slider, 91, 91)
        
        elif (source == self.ui.Home_Ground_Track and event.type() == QEvent.Enter):
            Animation_Home_Ground_Track(self,"long", self.ui.Home_Ground_Track_Slider, 91, 182)
        elif source == self.ui.Home_Ground_Track and event.type() == QEvent.Leave:
            Animation_Home_Ground_Track(self,"long", self.ui.Home_Ground_Track_Slider, 91, 91)

        elif (source == self.ui.Home_Planet_in_Shadow and event.type() == QEvent.Enter):
            Animation_Home_Planet_in_Shadow(self,"long", self.ui.Home_Planet_in_Shadow_Slider, 91, 182)
        elif source == self.ui.Home_Planet_in_Shadow and event.type() == QEvent.Leave:
            Animation_Home_Planet_in_Shadow(self,"long", self.ui.Home_Planet_in_Shadow_Slider, 91, 91)
        
        elif (source == self.ui.Home_Planetary_Ephimeris and event.type() == QEvent.Enter):
            Animation_Home_Planetary_Ephemeris(self,"long", self.ui.Home_Planetary_Ephimeris_Slider, 91, 182)
        elif source == self.ui.Home_Planetary_Ephimeris and event.type() == QEvent.Leave:
            Animation_Home_Planetary_Ephemeris(self,"long", self.ui.Home_Planetary_Ephimeris_Slider, 91, 91)
        
        elif (source == self.ui.Home_Numerical_integ and event.type() == QEvent.Enter):
            Animation_Home_Numerical_Methods(self,"long", self.ui.Home_Numerical_integ_Slider, 91, 182)
        elif source == self.ui.Home_Numerical_integ and event.type() == QEvent.Leave:
            Animation_Home_Numerical_Methods(self,"long", self.ui.Home_Numerical_integ_Slider, 91, 91)
        
        elif (source == self.ui.Home_Orbital_transfer and event.type() == QEvent.Enter):
            Animation_Home_Orbital_Transfer(self,"long", self.ui.Home_Orbital_transfer_Slider, 91, 182)
        elif source == self.ui.Home_Orbital_transfer and event.type() == QEvent.Leave:
            Animation_Home_Orbital_Transfer(self,"long", self.ui.Home_Orbital_transfer_Slider, 91, 91)

        elif (source == self.ui.Home_Eulers_Angle and event.type() == QEvent.Enter):
            Animation_Home_Eulers_Angle(self,"wide", self.ui.Home_Eulers_Angle_Slider, 237, 490)
        elif source == self.ui.Home_Eulers_Angle and event.type() == QEvent.Leave:
            Animation_Home_Eulers_Angle(self,"wide", self.ui.Home_Eulers_Angle_Slider, 237, 237)

        elif (source == self.ui.Home_VPCO and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.label_title.setText(" MOPy - Various Parameters at a given point in Orbit")
        
        elif (source == self.ui.Home_Orbital_transfer and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(6)
            self.ui.label_title.setText(" MOPy - Orbital Transfer")

        
        elif (source == self.ui.Home_Julian_Day and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.label_title.setText(" MOPy - Julian Day Calculation")
        
        elif (source == self.ui.Home_Orbital_Elements and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(5)
            self.ui.label_title.setText(" MOPy - Orbital Elements of an Orbit")
        
        elif (source == self.ui.Home_SOI and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.label_title.setText(" MOPy - Sphere Of Influence")
        
        elif (source == self.ui.Home_Orbit_Visualization and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(8)
            self.ui.label_title.setText(" MOPy - Orbit Visualization")

        elif (source == self.ui.Home_Ground_Track and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(8)
            self.ui.label_title.setText(" MOPy - Ground Track")
        
        elif (source == self.ui.Home_Planet_in_Shadow and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(8)
            self.ui.label_title.setText(" MOPy - Planet in Shadow")
        
        elif (source == self.ui.Home_Planetary_Ephimeris and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(7)
            self.ui.label_title.setText(" MOPy - Planetary Ephemeris")
        
        elif (source == self.ui.Home_Numerical_integ and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(8)
            self.ui.label_title.setText(" MOPy - Numerical Integration")
        
        elif (source == self.ui.Home_Eulers_Angle and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(8)
            self.ui.label_title.setText(" MOPy - Eulers Angle of an Spacecraft")
        
        elif (source == self.ui.Home_Orbital_transfer and event.type() == QtCore.QEvent.MouseButtonPress):
            self.ui.stackedWidget.setCurrentIndex(6)
            self.ui.label_title.setText(" MOPy - Orbital Transfer")
        
    


    def Sliding_animation(self, maxHeight, enable):
        if enable and maxHeight == 300:

            # GET WIDTH
            height = self.ui.Bottom_slider_VPCO_Output.height()
            maxExtend = maxHeight
            standard = 0
            
            

            # SET MAX WIDTH
            if height == 0:
                heightExtended = maxExtend
                self.ui.VPCO_Input_Stack.setCurrentIndex(1)
                self.ui.btn_go_back.show()
                
            else:
                heightExtended = standard
                self.ui.VPCO_Input_Stack.setCurrentIndex(0)
                self.ui.btn_go_back.hide()
                
            # ANIMATION
            self.animation_x = QPropertyAnimation(self.ui.Bottom_slider_VPCO_Output, b"maximumHeight")
            self.animation_x.setDuration(600)
            self.animation_x.setStartValue(height)
            self.animation_x.setEndValue(heightExtended)
            self.animation_x.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
            self.animation_x.start()
            
        elif enable and maxHeight == 522:
    
            # GET WIDTH
            width = self.ui.Plot_frame_for_Orbital_transfer.width()
            maxExtend = maxHeight
            standard = 0
            
            

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                
            else:
                widthExtended = standard
            
                
            # ANIMATION
            self.animaton_r = QPropertyAnimation(self.ui.Plot_frame_for_Orbital_transfer, b"maximumWidth")
            self.animaton_r.setDuration(600)
            self.animaton_r.setStartValue(width)
            self.animaton_r.setEndValue(widthExtended)
            self.animaton_r.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
            

            self.animaton_l = QPropertyAnimation(self.ui.Type_of_Orbital_transfer_frame, b"maximumWidth")
            self.animaton_l.setDuration(600)
            self.animaton_l.setStartValue(width)
            self.animaton_l.setEndValue(0)
            self.animaton_l.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
            
            self.animation_group = QParallelAnimationGroup(self)
            self.animation_group.addAnimation(self.animaton_r)
            self.animation_group.addAnimation(self.animaton_l)
            self.animation_group.start()

        elif enable and maxHeight == 200:
    
            # GET WIDTH
            height = self.ui.Bottom_slider_PE_Output.height()
            maxExtend = maxHeight
            standard = 0
            
            

            # SET MAX WIDTH
            if height == 0:
                heightExtended = maxExtend
            else:
                heightExtended = standard
                
            # ANIMATION
            self.animation_x = QPropertyAnimation(self.ui.Bottom_slider_PE_Output, b"maximumHeight")
            self.animation_x.setDuration(600)
            self.animation_x.setStartValue(height)
            self.animation_x.setEndValue(heightExtended)
            self.animation_x.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
            self.animation_x.start()
            
  

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

#########################################################################################################################

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
        index_dict = {1:0, 2:1, 3:2, 4:3, 5:4}
        index1 = self.ui.vpco_input_type.currentIndex()
        setIndex = index_dict[index1]
        self.ui.VPCO_output_stack.setCurrentIndex(setIndex)
            
        e = self.ui.eccentricity_inpt_ae.text()
        e = float(e)
        a = self.ui.semimajor_axis_input_ae.text()
        a = float(a)
        maj_body = self.ui.vpco_major_body.currentText()
        maj_body_mass = planet_data(maj_body,'Mass')
        
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
    
#########################################################################################################################

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

#########################################################################################################################        

    # SOI
    def SEARCH(self):
        planet_name = self.ui.SOI_planet_name.currentText()
        planet_mass = planet_data(planet_name,'Mass')
        dist_frm_sun = planet_data(planet_name,'Distance_from_sun')
        self.ui.lbl_mass.setText("Mass of " + str(planet_mass[1])+":")
        self.ui.soi_mass.setText(str(planet_mass[0]))
        self.ui.dist_frm_sun.setText(str(dist_frm_sun[0]))
       
            
    def SOI(self):
        planet_name = self.ui.SOI_planet_name.currentText()
        self.ui.rSOI_of_planet_lbl.setText("Radius of SOI of " + str(planet_name.strip()) + ":")
        Mass_of_Sun = planet_data('Sun','Mass')
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

        r_planet = planet_data(planet_name1,'Radius')[0]
        r_soimb = float(rSOI)/r_planet
        SOI3D(planet_name)
        
            
#########################################################################################################################
  
    # Home_btn

    def meth_Home_btn(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.label_title.setText(" MOPy ")

#########################################################################################################################

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
        
        self.ui.JulianDay_Result.setText(str(round(JD, accuracy)))

#########################################################################################################################
                                             ##---->>((( New VPCO )))<<----##

    # Slider pressed and released functions for sliders in the VPCO toggle menu

    def semi_slider_changed(self):
        semi_step_dict = {0:10, 1:100, 2:1000, 3:10000, 4:100000, 5:1000000}
        semi_slider_value = self.ui.semi_major_axis_toggle_menu_slider.value()
        semi_step = semi_step_dict[semi_slider_value]
        return semi_step

    def ecce_slider_changed(self):
        ecce_step_dict = {0:0.01, 1:0.05, 2:0.1, 3:0.5, 4:1, 5:2, 6:5, 7:10}
        ecce_slider_value = self.ui.eccentricity_toggle_menu_slider.value()
        ecce_step = ecce_step_dict[ecce_slider_value]
        return ecce_step

    def semi_dial_changed(self):
        semi_step = MainWindow.semi_slider_changed(self)
        sma = self.ui.semi_major_axis_toggle_menu_spinbox.value()
        direction = MainWindow.semi_dial_direction(self)
        if direction == "Clockwise":
            sma += semi_step 
        elif direction == "Anti-Clockwise":
            sma -= semi_step
        else:
            sma = sma
        self.ui.semi_major_axis_toggle_menu_spinbox.setValue(sma)
    
    def semi_slider_single_step(self):
        semi_step = MainWindow.semi_slider_changed(self)
        self.ui.semi_major_axis_toggle_menu_single_step.setValue(semi_step)
        
    def ecce_slider_single_step(self):
        ecce_step = MainWindow.ecce_slider_changed(self)
        self.ui.eccentricity_toggle_menu_single_step.setValue(ecce_step)
    
    def ecce_dial_changed(self):
        ecce_step = MainWindow.ecce_slider_changed(self)
        ecce = self.ui.eccentricity_toggle_menu_spinbox.value()
        direction = MainWindow.ecce_dial_direction(self)
        if direction == "Clockwise":
            ecce += ecce_step 
        elif direction == "Anti-Clockwise":
            ecce -= ecce_step 
        else:
            ecce = ecce
        self.ui.eccentricity_toggle_menu_spinbox.setValue(ecce)
        self.ui.eccentricity_toggle_menu_single_step.setValue(ecce_step)

    def semi_dial_direction(self):
        global a
        current_value = self.ui.Semi_dial.value()
        difference = current_value - a
        previous_value = current_value - difference
        a = current_value
        minimum_dial = self.ui.Semi_dial.maximum()
        maximum_dial = self.ui.Semi_dial.minimum()
        corner_case = [minimum_dial, maximum_dial]
        direction = self.direction_of_dial(current_value,corner_case,previous_value, difference)
        return direction

    def ecce_dial_direction(self):
        global a
        current_value = self.ui.ecce_dial.value()
        difference = current_value - a
        previous_value = current_value - difference
        a = current_value
        minimum_dial = self.ui.ecce_dial.maximum()
        maximum_dial = self.ui.ecce_dial.minimum()
        corner_case = [minimum_dial, maximum_dial]
        direction = self.direction_of_dial(current_value,corner_case,previous_value, difference)
        return direction

    def direction_of_dial(self, current_value,corner_case,previous_value, difference):
        if current_value in corner_case and previous_value in corner_case:
            if difference < 0:
                direction = 'Clockwise'
            elif difference > 0:
                direction = 'Anti-Clockwise'
            else:
                direction = "No Change"
        elif difference < 0:
            direction = "Anti-Clockwise"
        elif difference > 0:
            direction = "Clockwise"
        elif current_value:
            direction = "No Change"
        return direction

    def toggle_option_index(self):
        toggle_dict = {0:1,1:2,2:3, 3:4, 4:5, 5:6}
        dropdown_toggle_index = self.ui.type_of_input_toggle.currentIndex()
        print(dropdown_toggle_index)
        screen_toggle_menu = toggle_dict[dropdown_toggle_index]
        self.ui.stackedWidget_2.setCurrentIndex(screen_toggle_menu)

    ########################################################################################
                                    ##--->>((( Test )))---##
    # def test_dial_changed(self):
    #     test_step = MainWindow.ecce_slider_changed(self)
    #     test = self.ui.eccentricity_toggle_menu_spinbox.value()
    #     direction = MainWindow.test_dial_direction(self)
    #     if direction == "Clockwise":
    #         test += test_step 
    #     elif direction == "Anti-Clockwise":
    #         test -= test_step 
    #     else:
    #         test = test
    #     self.ui.eccentricity_toggle_menu_spinbox.setValue(test)
    #     self.ui.eccentricity_toggle_menu_single_step.setValue(test_step)

    # def test_dial_direction(self):
    #     global a
    #     current_value = self.ui.test_dial.value()
    #     difference = current_value - a
    #     previous_value = current_value - difference
    #     a = current_value
    #     minimum_dial = self.ui.test_dial.maximum()
    #     maximum_dial = self.ui.test_dial.minimum()
    #     corner_case = [minimum_dial, maximum_dial]
    #     direction = self.direction_of_dial(current_value,corner_case,previous_value, difference)
    #     return direction

###########################################################################################################################################################
# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.windowsize = windowsize
        # self.setFixedSize(self.windowsize)
        # QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # screensize = app.desktop().availableGeometry().size()
        # window_size = screensize/1.6
        # sts = str(window_size)kk
        # window_height = int(sts[-4] + sts[-3] + sts[-2])
        # window_width = int(sts[-9] + sts[-8] + sts[-7])
        # logo_frame_height = window_height*21/38
        # self.ui.logo_frame.setFixedHeight(logo_frame_height)
        # self.ui.logo.setFixedWidth(logo_frame_height * 143/127)


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
        self.timer.start(5)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.app_description_lbl.setText("WELCOME TO <strong>MOPy</strong>")

        # Change Texts
        QtCore.QTimer.singleShot(1200, lambda: self.ui.app_description_lbl.setText("<strong>Initializing</strong> Database"))
        QtCore.QTimer.singleShot(2500, lambda: self.ui.app_description_lbl.setText("<strong>Pulling</strong> Resources"))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.app_description_lbl.setText("<strong>Arranging</strong> User Interface "))
        QtCore.QTimer.singleShot(4700, lambda: self.ui.app_description_lbl.setText("Ready to <strong>Takeoff</strong> "))
        QtCore.QTimer.singleShot(6000, lambda: self.ui.app_description_lbl.setText("3"))
        QtCore.QTimer.singleShot(7600, lambda: self.ui.app_description_lbl.setText("2"))
        QtCore.QTimer.singleShot(8200, lambda: self.ui.app_description_lbl.setText("1"))
        QtCore.QTimer.singleShot(9600, lambda: self.ui.app_description_lbl.setText("<strong>Lift</strong> Off"))

        # Fun Facts
        
        self.ui.loading_lbl.setText("<strong>Do you know: </strong>"+ fun_fact())

        # Defining Spin Loader
        self.circular_progress_1 = PyCircularProgress(
            value=45,
            progress_width=4,
            animate=True,
            speed=120,
            try_me=True,
            
        )
        self.circular_progress_1.add_shadow("true")

        self.circular_progress_1.setMinimumSize(self.circular_progress_1.width, self.circular_progress_1.height)
        self.circular_progress_1.setMinimumSize(QSize(60, 60))
        self.circular_progress_1.setMaximumSize(QSize(60, 60))

        self.ui.horizontalLayout_2.addWidget(self.circular_progress_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        

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
    # window = MainWindow()
    window.show()
    sys.exit(app.exec_())
