# from Home_Page_main import *
from PySide2.QtCore import *
from PySide2 import QtCore, QtGui, QtWidgets



def toggle_slider(self, longwide, var_name, standard, maxExtent):
    if longwide == "long":
        height = var_name.height()
        
        if height == standard:
            height_to_extend = maxExtent
        else:
            height_to_extend = standard
        
        return[var_name, longwide, height, height_to_extend]
        
        
    elif longwide == "wide":
        width = var_name.width()
        if width == standard:
            width_to_extend = maxExtent
        else:
            width_to_extend = standard
        
        return[var_name, longwide, width, width_to_extend]
        



def Animation_Home_Eulers_Angle(self, longwide, var_name, standard, maxExtent):
    r1 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_1 = QPropertyAnimation(var_name, b"minimumWidth")
    self.animation_1.setDuration(400)
    self.animation_1.setStartValue(r1[2])
    self.animation_1.setEndValue(r1[3])
    self.animation_1.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_1.start()

def Animation_Home_VPCO(self, longwide, var_name, standard, maxExtent):
    r2 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_2 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_2.setDuration(200)
    self.animation_2.setStartValue(r2[2])
    self.animation_2.setEndValue(r2[3])
    self.animation_2.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_2.start()

def Animation_Home_Julian_Day(self, longwide, var_name, standard, maxExtent):
    r3 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_3 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_3.setDuration(200)
    self.animation_3.setStartValue(r3[2])
    self.animation_3.setEndValue(r3[3])
    self.animation_3.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_3.start()

def Animation_Orbital_Elements(self, longwide, var_name, standard, maxExtent):
    r4 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_4 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_4.setDuration(200)
    self.animation_4.setStartValue(r4[2])
    self.animation_4.setEndValue(r4[3])
    self.animation_4.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_4.start()    

def Animation_Home_SOI(self, longwide, var_name, standard, maxExtent):
    r5 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_5 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_5.setDuration(200)
    self.animation_5.setStartValue(r5[2])
    self.animation_5.setEndValue(r5[3])
    self.animation_5.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_5.start() 

def Animation_Home_Orbit_Visualization(self, longwide, var_name, standard, maxExtent):
    r6 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_6 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_6.setDuration(200)
    self.animation_6.setStartValue(r6[2])
    self.animation_6.setEndValue(r6[3])
    self.animation_6.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_6.start()

def Animation_Home_Ground_Track(self, longwide, var_name, standard, maxExtent):
    r7 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_7 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_7.setDuration(200)
    self.animation_7.setStartValue(r7[2])
    self.animation_7.setEndValue(r7[3])
    self.animation_7.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_7.start()

def Animation_Home_Planet_in_Shadow(self, longwide, var_name, standard, maxExtent):
    r8 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_8 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_8.setDuration(200)
    self.animation_8.setStartValue(r8[2])
    self.animation_8.setEndValue(r8[3])
    self.animation_8.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_8.start()

def Animation_Home_Planetary_Ephemeris(self, longwide, var_name, standard, maxExtent):
    r9 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_9 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_9.setDuration(200)
    self.animation_9.setStartValue(r9[2])
    self.animation_9.setEndValue(r9[3])
    self.animation_9.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_9.start()

def Animation_Home_Numerical_Methods(self, longwide, var_name, standard, maxExtent):
    r10 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_10 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_10.setDuration(200)
    self.animation_10.setStartValue(r10[2])
    self.animation_10.setEndValue(r10[3])
    self.animation_10.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_10.start()

def Animation_Home_Orbital_Transfer(self, longwide, var_name, standard, maxExtent):
    r11 = toggle_slider(self, longwide, var_name, standard, maxExtent)
    self.animation_11 = QPropertyAnimation(var_name, b"minimumHeight")
    self.animation_11.setDuration(200)
    self.animation_11.setStartValue(r11[2])
    self.animation_11.setEndValue(r11[3])
    self.animation_11.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    self.animation_11.start()



    