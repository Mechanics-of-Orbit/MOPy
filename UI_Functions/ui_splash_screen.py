# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenRDGnQM.ui'
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
        SplashScreen.resize(850, 474)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(50, 47, 111, 220), stop:0.488636 rgba(28, 30, 72, 220));\n"
"\n"
"\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 50px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.logo_frame = QFrame(self.dropShadowFrame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMaximumSize(QSize(16777215, 250))
        self.logo_frame.setStyleSheet(u"background-color:transparent;")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.logo_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(262, 0, 262, 0)
        self.logo = QLabel(self.logo_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(286, 254))
        self.logo.setMaximumSize(QSize(338, 300))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.logo.setFont(font)
        self.logo.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color:transparent;")
        self.logo.setPixmap(QPixmap(u"UI_Functions/Resources/MOPy Cover_transparent.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logo)


        self.verticalLayout_2.addWidget(self.logo_frame)

        self.ProgressBarContainer = QFrame(self.dropShadowFrame)
        self.ProgressBarContainer.setObjectName(u"ProgressBarContainer")
        self.ProgressBarContainer.setMinimumSize(QSize(500, 60))
        self.ProgressBarContainer.setMaximumSize(QSize(16777215, 60))
        self.ProgressBarContainer.setStyleSheet(u"background:transparent")
        self.ProgressBarContainer.setFrameShape(QFrame.StyledPanel)
        self.ProgressBarContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ProgressBarContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_2.addWidget(self.ProgressBarContainer)

        self.app_description_lbl = QLabel(self.dropShadowFrame)
        self.app_description_lbl.setObjectName(u"app_description_lbl")
        self.app_description_lbl.setMinimumSize(QSize(500, 40))
        self.app_description_lbl.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.app_description_lbl.setFont(font1)
        self.app_description_lbl.setStyleSheet(u"color: rgb(98, 114, 164);\n"
"background-color:transparent;")
        self.app_description_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.app_description_lbl)

        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 25))
        self.progressBar.setMaximumSize(QSize(16777215, 25))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164,200);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 12px;\n"
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

        self.verticalLayout_2.addWidget(self.progressBar)

        self.loading_lbl = QLabel(self.dropShadowFrame)
        self.loading_lbl.setObjectName(u"loading_lbl")
        self.loading_lbl.setMinimumSize(QSize(500, 70))
        self.loading_lbl.setMaximumSize(QSize(16777215, 70))
        font2 = QFont()
        font2.setPointSize(11)
        self.loading_lbl.setFont(font2)
        self.loading_lbl.setStyleSheet(u"background:transparent;")
        self.loading_lbl.setAlignment(Qt.AlignCenter)
        self.loading_lbl.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.loading_lbl)


        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.logo.setText("")
        self.app_description_lbl.setText(QCoreApplication.translate("SplashScreen", u"<strong>APP</strong> DESCRIPTION", None))
        self.loading_lbl.setText("")
    # retranslateUi

