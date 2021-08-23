from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys

class CircularProgress(QWidget):
    def __init__(self, parent = None):
        super(CircularProgress, self).__init__(parent)

        # Custom Properties
        self.value = 0
        self.width = 100
        self.height = 100
        self.progress_width = 6
        self.progress_rounded_cap = True
        self.progress_color = "#ff79c6"
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x498BD1

        # Set Background
        self.enable_bg = True
        self.bg_color = 0x44475a
       
        self.dial = QDial(self)
        self.dial.move(self.width/120, self.height/450)
        self.dial.valueChanged.connect(lambda:self.dial_changed())
        self.dial.setMaximum(360)
        self.dial.setMinimum(0)
        self.dial.setWrapping(1)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set Default size without layout
        # self.resize(self.width, self.height)
        self.show()

    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 220))
            self.setGraphicsEffect(self.shadow)

    def set_value(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, event):
            # Set progress Parameters
            width = self.width - self.progress_width
            height = self.height - self.progress_width
            margin_x = self.width/20
            margin_y = self.height/18
            value = self.dial.value()

            # Create a Painter
            paint = QPainter()
            paint.begin(self)
            paint.setRenderHint(QPainter.Antialiasing) # To remove pixelated edges and smoothen the render/animation
            paint.setFont(QFont(self.font_family, self.font_size))

        
            # PEN TO set the progress bar style
            pen = QPen()
            pen.setColor(QColor(self.progress_color))
            pen.setWidth(self.progress_width)
            
            # Set round cap to the progress bar
            if self.progress_rounded_cap:
                pen.setCapStyle(Qt.RoundCap)

            # Enable Backgground
            if self.enable_bg:
                penn = QPen()
                penn.setWidth(self.progress_width)
                penn.setColor(QColor(self.bg_color))
                paint.setPen(penn)
                paint.drawArc(margin_x, margin_y, width-5, height-5, 0, 360 * 16)

            # Create the arc of the circular bar
            paint.setPen(pen)
            
            paint.drawArc(margin_x, margin_y, width-5, height-5, -90 * 16, -value * 16)
            # End Painting
            paint.end()
    
    def dial_changed(self):
        self.value = self.dial.value()
        print(self.value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircularProgress()
    window.show()
    sys.exit(app.exec_())