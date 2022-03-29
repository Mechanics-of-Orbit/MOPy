from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Custom Properties
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
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
       
        
        # Set Default size without layout
        self.resize(self.width, self.height)

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
            margin = self.progress_width / 2
            value = self.value * 360 / self.max_value

            # Create a Painter
            paint = QPainter()
            paint.begin(self)
            paint.setRenderHint(QPainter.Antialiasing) # To remove pixelated edges and smoothen the render/animation
            paint.setFont(QFont(self.font_family, self.font_size))

            # Create a Rectangle
            rect = QRect(0, 0, self.width, self.height)
            paint.setPen(Qt.NoPen) # Removes the border of the Rectangle
            paint.drawRect(rect)

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
                penn.setWidth(10)
                penn.setColor(QColor(self.bg_color))
                paint.setPen(penn)
                paint.drawArc(margin, margin, width, height, 0, 360 * 16)

            # Create the arc of the circular bar
            paint.setPen(pen)
            
            paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)

            # Create text
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")


            # End Painting
            paint.end()


