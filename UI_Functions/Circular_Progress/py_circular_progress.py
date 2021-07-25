# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
import time
import sys


from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class PyCircularProgress(QMainWindow):
    def __init__(
        self,
        value=0,
        progress_width=20,
        is_rounded=True,
        max_value=100,
        progress_color="#ff79c6",
        enable_text=False,
        font_family="Segoe UI",
        font_size=12,
        suffix="%",
        text_color="#ff79c6",
        enable_bg=True,
        bg_color="#44475a",
        animate=False,
        customText="",
        speed=10,
        try_me=False,
        finished_text="",
        
    ):
        
        QMainWindow.__init__(self)

        # CUSTOM PROPERTIES
        self.width = 40
        self.height = 40
        self.value = value
        self.progress_width = progress_width
        self.progress_rounded_cap = is_rounded
        self.max_value = max_value
        self.progress_color = progress_color
        # Text
        self.enable_text = enable_text
        self.font_family = font_family
        self.font_size = font_size
        self.customText = customText
        self.suffix = suffix
        self.text_color = text_color
        self.finished_text = finished_text
        # BG
        self.enable_bg = enable_bg
        self.bg_color = bg_color

        self.animate = animate
        self.resize(self.width, self.height)

        
        if not self.max_value:
            self.animate = True
        self.plus = True
        self.size_idle = 5
        self.smol = 0

        if not self.customText and not max_value:
            self.customText = "Cargando..."

        self.turning = 1

        if self.animate:
            self.timer = QTimer(self)
            self.timer.setSingleShot(False)
            #self.timer.setInterval(speed)
            self.timer.timeout.connect(self.idle_move)
            self.timer.start(25)

        self.stopper = 0
        if try_me:
            self.value = 0
            self.timer = QTimer(self)
            self.timer.setSingleShot(False)
            self.timer.setInterval(100)
            self.timer.timeout.connect(self.try_me)
            self.timer.start()
        self.show()
    def try_me(self):
        if self.value == self.max_value - 1:
            self.stopper = 0

        if self.value == self.max_value:
            if not self.stopper:
                self.set_value(0)
            else:
                self.stopper -= 1
        else:
            self.set_value(round(self.value + 1, 2))

    def idle_move(self):
        self.turning += 1
        if self.plus:
            if self.smol > 20:
                self.size_idle += 1
            elif self.smol == 20:
                self.size_idle += 1
                self.smol += 1
            else:
                self.smol += 1
        else:
            self.size_idle -= 1
            self.turning += 1
        self.repaint()

    # ADD DROPSHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 80))
            self.setGraphicsEffect(self.shadow)

    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint()  # Render progress bar after change value

    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, e):
        # SET PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        if self.max_value:
            value = self.value * 360 / self.max_value
        else:
            value = self.turning * 360 / 360

        
        # PAINTER
        paint = QPainter(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        
        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)####

        # PEN
        pen1 = QPen()  
        pen1.setColor(QColor('#FF9933'))           
        pen1.setWidth(self.progress_width)
        
        pen2 = QPen()  
        pen2.setColor(QColor('#FFFFFF'))           
        pen2.setWidth(self.progress_width)

        pen3 = QPen()  
        pen3.setColor(QColor('#138808'))           
        pen3.setWidth(self.progress_width)

        # Set Round Cap
        if self.progress_rounded_cap:
            pen1.setCapStyle(Qt.RoundCap)
            pen2.setCapStyle(Qt.RoundCap)
            pen3.setCapStyle(Qt.RoundCap)

        # ENABLE BG
        # if self.enable_bg:
        #     pen.setColor(QColor(self.bg_color))
        #     paint.setPen(pen)  
        #     paint.drawArc(margin, margin, width, height, 0, 360 * 16) 

        # CREATE ARC / CIRCULAR PROGRESS
        
        
        
        if self.animate:
            if self.max_value:
                paint.setPen(pen1)
                paint.drawArc(margin , margin , width , height , -(self.turning * 16) + 30, -value * 16)
                paint.setPen(pen2)
                paint.drawArc(margin + 5 , margin + 5, width - 10 , height - 10, -2 *(self.turning * 16), -value  * 16)
                paint.setPen(pen3)
                paint.drawArc(margin + 10, margin + 10, width - 20 , height - 20, -3 *(self.turning * 16), -value  * 16)
            else:
                paint.setPen(pen1)
                paint.drawArc(margin , margin, width, height, -(self.turning  * 16) , - self.size_idle * 16)
                paint.setPen(pen2)
                paint.drawArc(margin + 5 , margin + 5, width - 10, height - 10, -2 *(self.turning * 16), - self.size_idle * 16)
                paint.setPen(pen3)
                paint.drawArc(margin + 10 , margin + 10, width - 20 , height - 20, -3 *(self.turning * 16), - self.size_idle * 16)
                if self.size_idle > 280:
                    self.size_idle = 280
                    self.plus = False
                elif self.size_idle < 5:
                    self.size_idle = 4
                    self.plus = True
                    if self.smol == 21:
                        self.smol = 0
        else:
            paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)

        # CREATE TEXT
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            if self.value == self.max_value and self.finished_text:
                paint.drawText(rect, Qt.AlignCenter, self.finished_text)
            elif not self.customText:
                paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")
            else:
                if self.max_value:
                    paint.drawText(rect, Qt.AlignCenter, f"{self.customText} {self.value}{self.suffix}")
                else:
                    paint.drawText(rect, Qt.AlignCenter, self.customText)

        # END
        paint.end()


