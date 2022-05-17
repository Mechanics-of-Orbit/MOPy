from Home_Page_main import *

def toggle_slider(self, longwide, var_name, standard, maxExtent):
    if longwide == "long":
        height = self.ui.var_name.height()
        if height == standard:
            height_to_extend = maxExtent
        else:
            height_to_extend = standard
        
        self.animation_x = QPropertyAnimation(self.ui.var_name, b"maximumHeight")
        self.animation_x.setDuration(600)
        self.animation_x.setStartValue(height)
        self.animation_x.setEndValue(height_to_extend)
        self.animation_x.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.animation_x.start()
        
    elif longwide == "wide":
        width = self.ui.var_name.width()
        if width == standard:
            width_to_extend = maxExtent
        else:
            width_to_extend = standard
        
        self.animation_x = QPropertyAnimation(self.ui.var_name, b"minimumHeight")
        self.animation_x.setDuration(600)
        self.animation_x.setStartValue(width)
        self.animation_x.setEndValue(width_to_extend)
        self.animation_x.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.animation_x.start()
        
    



    