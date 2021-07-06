# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenXBLbsI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(750, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(50, 47, 111, 220), stop:0.488636 rgba(28, 30, 72, 220));	\n"
"	\n"
"\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 50px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.app_description_lbl = QLabel(self.dropShadowFrame)
        self.app_description_lbl.setObjectName(u"app_description_lbl")
        self.app_description_lbl.setGeometry(QRect(0, 230, 731, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        self.app_description_lbl.setFont(font)
        self.app_description_lbl.setStyleSheet(u"color: rgb(98, 114, 164);\n"
"background-color:transparent;")
        self.app_description_lbl.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 631, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164,200);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	/*background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));*/\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.977273, y2:1, stop:0 rgba(177, 45, 85, 255), stop:1 rgba(255, 170, 0, 220));\n"
"\n"
"	\n"
"	\n"
"	\n"
"\n"
"}")
        self.progressBar.setValue(24)
        self.loading_lbl = QLabel(self.dropShadowFrame)
        self.loading_lbl.setObjectName(u"loading_lbl")
        self.loading_lbl.setGeometry(QRect(0, 320, 731, 21))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.loading_lbl.setFont(font1)
        self.loading_lbl.setStyleSheet(u"background-color:transparent;\n"
"color: rgb(98, 114, 164);")
        self.loading_lbl.setAlignment(Qt.AlignCenter)
        self.logo_frame = QFrame(self.dropShadowFrame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setGeometry(QRect(0, -1, 731, 221))
        self.logo_frame.setStyleSheet(u"background-color:transparent;")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.logo_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(232, -1, 232, 0)
        self.logo_lbl = QLabel(self.logo_frame)
        self.logo_lbl.setObjectName(u"logo_lbl")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(40)
        self.logo_lbl.setFont(font2)
        self.logo_lbl.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color:transparent;")
        self.logo_lbl.setPixmap(QPixmap(u"UI_Functions/Resources/MOPy Cover_transparent.png"))
        self.logo_lbl.setScaledContents(True)
        self.logo_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logo_lbl)

        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(570, 330, 47, 41))
        self.label.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.app_description_lbl.setText(QCoreApplication.translate("SplashScreen", u"<strong>APP</strong> DESCRIPTION", None))
        self.loading_lbl.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.logo_lbl.setText("")
        self.label.setText("")
    # retranslateUi

