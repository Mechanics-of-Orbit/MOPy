
## ==> GUI FILE
import Home_Page_main
from Home_Page_main import *
from Functions.Sections.VPCO import CalculateCircularElliptical, CalculateParabola
from Functions.Sections.DB.call_database import *
from math import *

def Sliding_animation(self, maxHeight, enable):
    if enable and maxHeight == 400:
        self.ui.a_and_e_graph_VPCO.setCurrentIndex(0)
        self.dummy = 0
        # GET WIDTH
        height = self.ui.Bottom_slider_VPCO_Output.height()
        maxExtend = maxHeight
        standard = 0

        # SET MAX WIDTH
        if height == 0:
            heightExtended = maxExtend
            
            
        else:
            heightExtended = standard
            self.ui.VPCO_Input_Stack.setCurrentIndex(0)
            

        Semi_maj_ax = self.ui.VPCO_Input_a_lineedit.text()
        Eccentricity = self.ui.VPCO_Input_e_lineedit.text()

        try:
            Semi_maj_ax =  float(Semi_maj_ax)
            try:
                
                Eccentricity = float(Eccentricity)
                
                self.ui.Semi_maj_ax_err_label.setText("")
                self.ui.VPCO_Input_Stack.setCurrentIndex(1)
                self.ui.a_and_e_graph_VPCO.setCurrentIndex(1) 
                self.dummy = 1
                
            except:
                self.ui.Eccentricity_err_label.setText("Please Enter an integer value of Eccentricty")
                self.ui.Semi_maj_ax_err_label.setText("")

        except:
            try:
                Eccentricity = float(Eccentricity)
                self.ui.Semi_maj_ax_err_label.setText("Please Enter an integer value of Semi-major axis")
                self.ui.Eccentricity_err_label.setText("")
            except:
                self.ui.Semi_maj_ax_err_label.setText("Please Enter an integer value of Semi-major axis")
                self.ui.Eccentricity_err_label.setText("Please Enter an integer value of Eccentricty")

        if self.dummy == 1:
            Maj_Body = self.ui.Maj_Body__Drop_VPCO.currentText()
            m = planet_data(Maj_Body, "Mass")
            Maj_Body_Mass = m[0]
            vpco = CalculateCircularElliptical.semiecc(Semi_maj_ax, Eccentricity, Maj_Body_Mass)
            
            self.ui.VPCO_Radius_of_Peri_Label.setText(str(round(vpco[0], 4)))
            self.ui.VPCO_Radius_of_Apo_Label.setText(str(round(vpco[1], 4)))
            self.ui.VPCO_Sp_Mech_Energy_Label.setText(str(round(vpco[5], 4)))
            self.ui.VPCO_Time_Period_Label.setText(str(round(vpco[3], 4)))
            self.ui.VPCO_Sp_Angular_Mome_Label.setText(str(round(vpco[4], 4)))
            self.ui.VPCO_Mean_Motion_Label.setText(str(round(vpco[2], 4)))
            self.ui.VPCO_Semi_latus_Rectum_Label.setText(str(round(vpco[6], 4)))

            Vel_peri = CalculateCircularElliptical.velocity_at_any_point(Semi_maj_ax, vpco[0], Maj_Body_Mass)
            self.ui.VPCO_Velocity_at_Periapis_Label.setText(str(round(Vel_peri, 4)))

            Vel_apo = CalculateCircularElliptical.velocity_at_any_point(Semi_maj_ax, vpco[1], Maj_Body_Mass)
            self.ui.VPCO_Velocity_of_Apoapsis_Label.setText(str(round(Vel_apo, 4)))

            Vel_at_Semi_latus_Rectum = CalculateCircularElliptical.velocity_at_any_point(Semi_maj_ax, vpco[6], Maj_Body_Mass)
            self.ui.VPCO_Vel_at_Semi_latus_re_Label.setText(str(round(Vel_at_Semi_latus_Rectum, 4)))

            self.ui.VPCO_Esc_Velocity_at_Periapsis_Label.setText(str(round(sqrt((2*G*Maj_Body_Mass)/vpco[0]), 4)))
            self.ui.VPCO_Esc_Velocity_at_Apoapsis_Label.setText(str(round(sqrt((2*G*Maj_Body_Mass)/vpco[1]), 4)))
        
            self.ui.Bottom_slider_VPCO_Output.show()

            
    elif enable and maxHeight == 522:

        # ACOE = PECalculation()
        JD = calendar_time(self, 2)
        print(JD)

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