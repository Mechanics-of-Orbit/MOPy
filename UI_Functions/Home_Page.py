# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home_PagekXVlZx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1110, 663)
        MainWindow.setMinimumSize(QSize(750, 0))
        MainWindow.setMaximumSize(QSize(1198, 16777215))
        MainWindow.setStyleSheet(u"QToolTip{\n"
"border:none;\n"
"background-color:white;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color:rgb(54, 55, 92);\n"
"\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"	border-color:rgb(8, 255, 173);\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 45))
        self.title_bar.setMaximumSize(QSize(16777215, 55))
        self.title_bar.setStyleSheet(u"background-color: None")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font = QFont()
        font.setFamily(u"Rockwell Condensed")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setStyleSheet(u"background-color: rgb(78, 79, 132);\n"
"border:5px solid white;\n"
"border-color: rgb(54, 55, 92);")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_title)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(60, 0))
        self.frame_10.setMaximumSize(QSize(60, 16777215))
        self.frame_10.setStyleSheet(u"border:none;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(15, 4, -1, -1)
        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(30, 30))
        self.frame_16.setMaximumSize(QSize(30, 30))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.Home_btn = QPushButton(self.frame_16)
        self.Home_btn.setObjectName(u"Home_btn")
        self.Home_btn.setMinimumSize(QSize(30, 30))
        self.Home_btn.setMaximumSize(QSize(30, 30))
        self.Home_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px;\n"
"	image:url(UI_Functions/Resources/Home_btn.png);\n"
"	border:none;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 0.2em 0.2em 0.2em 0.2em;\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 0.5em 0.5em 0.5em 0.5em;\n"
"	\n"
"}\n"
"\n"
"QToolTip{\n"
"border-color: rgb(134, 86, 168);\n"
"color:white;\n"
"background-color:rgb(134, 86, 168);\n"
"border-radius:1px;\n"
"}")

        self.horizontalLayout_73.addWidget(self.Home_btn)


        self.verticalLayout_12.addWidget(self.frame_16)


        self.horizontalLayout_14.addWidget(self.frame_10)

        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(400, 0))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color:rgb(60, 235, 250);\n"
"border:none;")

        self.horizontalLayout_14.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(0, 40))
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamily(u"MS Serif")
        self.frame_btns.setFont(font2)
        self.frame_btns.setStyleSheet(u"background-color: rgb(78, 79, 132);\n"
"border:5px solid white;\n"
"border-color: rgb(54, 55, 92);")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(-1, 8, -1, 12)
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(20, 20))
        self.btn_minimize.setMaximumSize(QSize(20, 20))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:8px;\n"
"	image:url(UI_Functions/Resources/minimize.svg);\n"
"	padding: 0.2em 0.2em 0.2em 0.2em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 1px solid transparent;\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 0.5em 0.5em 0.5em 0.5em;\n"
"	\n"
"}")

        self.horizontalLayout_70.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setMaximumSize(QSize(20, 20))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	\n"
"	border-radius:8px;\n"
"	image:url(UI_Functions/Resources/close.svg);\n"
"	padding: 0.1em 0.1em 0.2em 0.1em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 1px solid transparent;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 0.5em 0.5em 0.5em 0.5em;\n"
"	\n"
"}")
        self.btn_close.setIconSize(QSize(12, 12))

        self.horizontalLayout_70.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: transparent;")
        self.content_bar.setFrameShape(QFrame.NoFrame)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget{\n"
"background-color:#36375c;\n"
"border:5px solid white;\n"
"border-color:#36375c;\n"
"border-radius:8px;}\n"
"")
        self.Home_Page_Screen = QWidget()
        self.Home_Page_Screen.setObjectName(u"Home_Page_Screen")
        self.Home_Page_Screen.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.Home_Page_Screen)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.Home_Page_Screen)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setStyleSheet(u"/*QSrollArea{\n"
"background-color:#4e4f84;}*/\n"
"\n"
"/*Vertical Scrollbar*/\n"
"QScrollBar:vertical{\n"
"border:none;\n"
"background-color:rgb(59, 59, 90);\n"
"width:8px;\n"
"margin: 15px 0 15px 0;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"/* Handle Bar Vertical */\n"
"QScrollBar::handle:vertical{\n"
"background-color: rgb(80, 80, 122);\n"
"min-height: 30px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vetical:hover{\n"
"background-color: rgb(108, 87, 134);\n"
"	\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - Scrollbar*/\n"
"QScrollBar::sub-line:vertical{\n"
"border:none;\n"
"background-color: rgb(59, 59, 90);\n"
"height:15px;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"background-color: rgb(185, 0"
                        ", 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - Scrollbar*/\n"
"QScrollBar::add-line:vertical{\n"
"border:none;\n"
"background-color: rgb(59, 59, 90);\n"
"height:15px;\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed{\n"
"background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW*/\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"border:none;\n"
"background: rgb(78, 79, 132);\n"
"}")
        self.frame_content_home.setFrameShape(QFrame.NoFrame)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_content_home)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color:transparent;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -57, 1072, 630))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 200))
        self.frame_2.setMaximumSize(QSize(16777215, 250))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.VPCO = QWidget(self.frame_2)
        self.VPCO.setObjectName(u"VPCO")
        self.VPCO.setMinimumSize(QSize(150, 150))
        self.VPCO.setMaximumSize(QSize(230, 200))
        self.VPCO.setStyleSheet(u"QWidget{\n"
"background-color:black;\n"
"image:url(UI_Functions/Resources/Orbits.jpg);\n"
"}	")
        self.verticalLayout_13 = QVBoxLayout(self.VPCO)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.filler_1 = QFrame(self.VPCO)
        self.filler_1.setObjectName(u"filler_1")
        self.filler_1.setStyleSheet(u"background-color:transparent;\n"
"image:none;")
        self.filler_1.setFrameShape(QFrame.StyledPanel)
        self.filler_1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.filler_1)

        self.slider_1 = QFrame(self.VPCO)
        self.slider_1.setObjectName(u"slider_1")
        self.slider_1.setMinimumSize(QSize(150, 80))
        self.slider_1.setMaximumSize(QSize(230, 200))
        self.slider_1.setStyleSheet(u"background-color: rgb(0, 0, 0,88%);\n"
"image:none;")
        self.slider_1.setFrameShape(QFrame.StyledPanel)
        self.slider_1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.slider_1)


        self.horizontalLayout_4.addWidget(self.VPCO)

        self.Julian_Day = QWidget(self.frame_2)
        self.Julian_Day.setObjectName(u"Julian_Day")
        self.Julian_Day.setMinimumSize(QSize(150, 150))
        self.Julian_Day.setMaximumSize(QSize(230, 200))
        self.Julian_Day.setStyleSheet(u"background-color:green;")
        self.verticalLayout_32 = QVBoxLayout(self.Julian_Day)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.filler_2 = QFrame(self.Julian_Day)
        self.filler_2.setObjectName(u"filler_2")
        self.filler_2.setStyleSheet(u"background-color:transparent;")
        self.filler_2.setFrameShape(QFrame.StyledPanel)
        self.filler_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_32.addWidget(self.filler_2)

        self.slider_2 = QFrame(self.Julian_Day)
        self.slider_2.setObjectName(u"slider_2")
        self.slider_2.setMinimumSize(QSize(150, 80))
        self.slider_2.setMaximumSize(QSize(230, 200))
        self.slider_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.slider_2.setFrameShape(QFrame.StyledPanel)
        self.slider_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_32.addWidget(self.slider_2)


        self.horizontalLayout_4.addWidget(self.Julian_Day)

        self.Orbital_Elements = QWidget(self.frame_2)
        self.Orbital_Elements.setObjectName(u"Orbital_Elements")
        self.Orbital_Elements.setMinimumSize(QSize(150, 150))
        self.Orbital_Elements.setMaximumSize(QSize(230, 200))
        self.Orbital_Elements.setStyleSheet(u"background-color:green;")
        self.verticalLayout_36 = QVBoxLayout(self.Orbital_Elements)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.filler_6 = QFrame(self.Orbital_Elements)
        self.filler_6.setObjectName(u"filler_6")
        self.filler_6.setStyleSheet(u"background-color:transparent;")
        self.filler_6.setFrameShape(QFrame.StyledPanel)
        self.filler_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_36.addWidget(self.filler_6)

        self.slider_6 = QFrame(self.Orbital_Elements)
        self.slider_6.setObjectName(u"slider_6")
        self.slider_6.setMinimumSize(QSize(150, 80))
        self.slider_6.setMaximumSize(QSize(230, 200))
        self.slider_6.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.slider_6.setFrameShape(QFrame.StyledPanel)
        self.slider_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_36.addWidget(self.slider_6)


        self.horizontalLayout_4.addWidget(self.Orbital_Elements)

        self.SOI = QWidget(self.frame_2)
        self.SOI.setObjectName(u"SOI")
        self.SOI.setMinimumSize(QSize(150, 150))
        self.SOI.setMaximumSize(QSize(230, 200))
        self.SOI.setStyleSheet(u"background-color:green;")
        self.verticalLayout_37 = QVBoxLayout(self.SOI)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.filler_7 = QFrame(self.SOI)
        self.filler_7.setObjectName(u"filler_7")
        self.filler_7.setStyleSheet(u"background-color:transparent;")
        self.filler_7.setFrameShape(QFrame.StyledPanel)
        self.filler_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_37.addWidget(self.filler_7)

        self.slider_7 = QFrame(self.SOI)
        self.slider_7.setObjectName(u"slider_7")
        self.slider_7.setMinimumSize(QSize(150, 80))
        self.slider_7.setMaximumSize(QSize(230, 200))
        self.slider_7.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.slider_7.setFrameShape(QFrame.StyledPanel)
        self.slider_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_37.addWidget(self.slider_7)


        self.horizontalLayout_4.addWidget(self.SOI)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 200))
        self.frame_8.setMaximumSize(QSize(16777215, 250))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Orbit_Visualization = QWidget(self.frame_8)
        self.Orbit_Visualization.setObjectName(u"Orbit_Visualization")
        self.Orbit_Visualization.setMinimumSize(QSize(150, 150))
        self.Orbit_Visualization.setMaximumSize(QSize(230, 200))
        self.Orbit_Visualization.setStyleSheet(u"background-color:red;")
        self.verticalLayout_33 = QVBoxLayout(self.Orbit_Visualization)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.filler_3 = QFrame(self.Orbit_Visualization)
        self.filler_3.setObjectName(u"filler_3")
        self.filler_3.setStyleSheet(u"background-color:transparent;")
        self.filler_3.setFrameShape(QFrame.StyledPanel)
        self.filler_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.filler_3)

        self.slider_3 = QFrame(self.Orbit_Visualization)
        self.slider_3.setObjectName(u"slider_3")
        self.slider_3.setMinimumSize(QSize(150, 80))
        self.slider_3.setMaximumSize(QSize(230, 200))
        self.slider_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.slider_3.setFrameShape(QFrame.StyledPanel)
        self.slider_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.slider_3)


        self.horizontalLayout_8.addWidget(self.Orbit_Visualization)

        self.Ground_Track = QWidget(self.frame_8)
        self.Ground_Track.setObjectName(u"Ground_Track")
        self.Ground_Track.setMinimumSize(QSize(150, 150))
        self.Ground_Track.setMaximumSize(QSize(230, 200))
        self.Ground_Track.setStyleSheet(u"background-color:red;")
        self.verticalLayout_34 = QVBoxLayout(self.Ground_Track)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.filler_4 = QFrame(self.Ground_Track)
        self.filler_4.setObjectName(u"filler_4")
        self.filler_4.setStyleSheet(u"background-color:transparent;")
        self.filler_4.setFrameShape(QFrame.StyledPanel)
        self.filler_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_34.addWidget(self.filler_4)

        self.slider_4 = QFrame(self.Ground_Track)
        self.slider_4.setObjectName(u"slider_4")
        self.slider_4.setMinimumSize(QSize(150, 80))
        self.slider_4.setMaximumSize(QSize(230, 200))
        self.slider_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.slider_4.setFrameShape(QFrame.StyledPanel)
        self.slider_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_34.addWidget(self.slider_4)


        self.horizontalLayout_8.addWidget(self.Ground_Track)

        self.Planet_in_Shadow = QWidget(self.frame_8)
        self.Planet_in_Shadow.setObjectName(u"Planet_in_Shadow")
        self.Planet_in_Shadow.setMinimumSize(QSize(150, 150))
        self.Planet_in_Shadow.setMaximumSize(QSize(230, 200))
        self.Planet_in_Shadow.setStyleSheet(u"background-color:red;")
        self.verticalLayout_35 = QVBoxLayout(self.Planet_in_Shadow)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.filler_5 = QFrame(self.Planet_in_Shadow)
        self.filler_5.setObjectName(u"filler_5")
        self.filler_5.setStyleSheet(u"background-color:transparent;")
        self.filler_5.setFrameShape(QFrame.StyledPanel)
        self.filler_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_35.addWidget(self.filler_5)

        self.slider_5 = QFrame(self.Planet_in_Shadow)
        self.slider_5.setObjectName(u"slider_5")
        self.slider_5.setMinimumSize(QSize(150, 80))
        self.slider_5.setMaximumSize(QSize(230, 200))
        self.slider_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.slider_5.setFrameShape(QFrame.StyledPanel)
        self.slider_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_35.addWidget(self.slider_5)


        self.horizontalLayout_8.addWidget(self.Planet_in_Shadow)

        self.Planetary_Ephimeris = QWidget(self.frame_8)
        self.Planetary_Ephimeris.setObjectName(u"Planetary_Ephimeris")
        self.Planetary_Ephimeris.setMinimumSize(QSize(150, 150))
        self.Planetary_Ephimeris.setMaximumSize(QSize(230, 200))
        self.Planetary_Ephimeris.setStyleSheet(u"background-color:red;")
        self.verticalLayout_40 = QVBoxLayout(self.Planetary_Ephimeris)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.filler_8 = QFrame(self.Planetary_Ephimeris)
        self.filler_8.setObjectName(u"filler_8")
        self.filler_8.setStyleSheet(u"background-color:transparent;")
        self.filler_8.setFrameShape(QFrame.StyledPanel)
        self.filler_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_40.addWidget(self.filler_8)

        self.slider_8 = QFrame(self.Planetary_Ephimeris)
        self.slider_8.setObjectName(u"slider_8")
        self.slider_8.setMinimumSize(QSize(150, 80))
        self.slider_8.setMaximumSize(QSize(230, 200))
        self.slider_8.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.slider_8.setFrameShape(QFrame.StyledPanel)
        self.slider_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_40.addWidget(self.slider_8)


        self.horizontalLayout_8.addWidget(self.Planetary_Ephimeris)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 200))
        self.frame_15.setMaximumSize(QSize(16777215, 250))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.Comparision_of_numerical_integ = QWidget(self.frame_15)
        self.Comparision_of_numerical_integ.setObjectName(u"Comparision_of_numerical_integ")
        self.Comparision_of_numerical_integ.setMinimumSize(QSize(150, 150))
        self.Comparision_of_numerical_integ.setMaximumSize(QSize(230, 200))
        self.Comparision_of_numerical_integ.setStyleSheet(u"background-color:yellow;")
        self.verticalLayout_38 = QVBoxLayout(self.Comparision_of_numerical_integ)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.filler_9 = QFrame(self.Comparision_of_numerical_integ)
        self.filler_9.setObjectName(u"filler_9")
        self.filler_9.setStyleSheet(u"background-color:transparent;")
        self.filler_9.setFrameShape(QFrame.StyledPanel)
        self.filler_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.filler_9)

        self.slider_9 = QFrame(self.Comparision_of_numerical_integ)
        self.slider_9.setObjectName(u"slider_9")
        self.slider_9.setMinimumSize(QSize(150, 80))
        self.slider_9.setMaximumSize(QSize(230, 200))
        self.slider_9.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.slider_9.setFrameShape(QFrame.StyledPanel)
        self.slider_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.slider_9)


        self.horizontalLayout_72.addWidget(self.Comparision_of_numerical_integ)

        self.Orbital_transfer_and_Eulers_angle = QWidget(self.frame_15)
        self.Orbital_transfer_and_Eulers_angle.setObjectName(u"Orbital_transfer_and_Eulers_angle")
        self.Orbital_transfer_and_Eulers_angle.setMinimumSize(QSize(150, 150))
        self.Orbital_transfer_and_Eulers_angle.setMaximumSize(QSize(230, 200))
        self.Orbital_transfer_and_Eulers_angle.setStyleSheet(u"background-color:yellow;")
        self.verticalLayout_39 = QVBoxLayout(self.Orbital_transfer_and_Eulers_angle)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.filler_10 = QFrame(self.Orbital_transfer_and_Eulers_angle)
        self.filler_10.setObjectName(u"filler_10")
        self.filler_10.setStyleSheet(u"background-color:transparent;")
        self.filler_10.setFrameShape(QFrame.StyledPanel)
        self.filler_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_39.addWidget(self.filler_10)

        self.slider_10 = QFrame(self.Orbital_transfer_and_Eulers_angle)
        self.slider_10.setObjectName(u"slider_10")
        self.slider_10.setMinimumSize(QSize(150, 80))
        self.slider_10.setMaximumSize(QSize(230, 200))
        self.slider_10.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.slider_10.setFrameShape(QFrame.StyledPanel)
        self.slider_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_39.addWidget(self.slider_10)


        self.horizontalLayout_72.addWidget(self.Orbital_transfer_and_Eulers_angle)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.frame_content_home)

        self.stackedWidget.addWidget(self.Home_Page_Screen)
        self.Julian_Day_Screen = QWidget()
        self.Julian_Day_Screen.setObjectName(u"Julian_Day_Screen")
        self.verticalLayout_5 = QVBoxLayout(self.Julian_Day_Screen)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_content_Julian_calculation = QFrame(self.Julian_Day_Screen)
        self.frame_content_Julian_calculation.setObjectName(u"frame_content_Julian_calculation")
        self.frame_content_Julian_calculation.setFrameShape(QFrame.StyledPanel)
        self.frame_content_Julian_calculation.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_content_Julian_calculation)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_content_Julian_calculation)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 25))
        self.frame_14.setMaximumSize(QSize(16777215, 25))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_title_2 = QLabel(self.frame_14)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setFont(font1)
        self.label_title_2.setStyleSheet(u"color:rgb(60, 235, 250);\n"
"")

        self.verticalLayout_14.addWidget(self.label_title_2)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.frame_9 = QFrame(self.frame_content_Julian_calculation)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(315, 40))
        self.frame_11.setMaximumSize(QSize(315, 50))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.type_of_calendar = QComboBox(self.frame_11)
        self.type_of_calendar.addItem("")
        self.type_of_calendar.addItem("")
        self.type_of_calendar.addItem("")
        self.type_of_calendar.setObjectName(u"type_of_calendar")
        self.type_of_calendar.setMinimumSize(QSize(305, 40))
        self.type_of_calendar.setMaximumSize(QSize(305, 40))
        self.type_of_calendar.setStyleSheet(u"QComboBox{\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.type_of_calendar, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame_18 = QFrame(self.frame_content_Julian_calculation)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 20))
        self.frame_18.setMaximumSize(QSize(16777215, 20))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_24 = QFrame(self.frame_18)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(0, 0, 16, 20))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_18)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 0, 500, 20))
        self.label_5.setMinimumSize(QSize(500, 0))
        self.label_5.setMaximumSize(QSize(500, 16777215))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"border: none;\n"
"color: white;")
        self.frame_34 = QFrame(self.frame_18)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(670, 0, 400, 16))
        self.frame_34.setMinimumSize(QSize(400, 0))
        self.frame_34.setMaximumSize(QSize(400, 16777215))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_34)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Error_state = QLabel(self.frame_34)
        self.Error_state.setObjectName(u"Error_state")
        font4 = QFont()
        font4.setPointSize(10)
        self.Error_state.setFont(font4)
        self.Error_state.setStyleSheet(u"color:rgb(255, 0, 0);")

        self.verticalLayout_17.addWidget(self.Error_state)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.frame = QFrame(self.frame_content_Julian_calculation)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 280))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(10, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_12)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(360, 0))
        self.frame_6.setMaximumSize(QSize(50, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(320, 250))
        self.frame_7.setMaximumSize(QSize(360, 250))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"\n"
"border: 5px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid white;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(6, 6, 6, 6)
        self.calendarWidget = QCalendarWidget(self.frame_7)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMinimumSize(QSize(320, 200))
        self.calendarWidget.setMaximumSize(QSize(320, 205))
        self.calendarWidget.setStyleSheet(u"\n"
"QCalendarWidget QToolButton{\n"
"\n"
"	\n"
"	height: 20px;\n"
"	width: 150px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	icon-size: 30px,30px;\n"
"	background-color: black;\n"
"	border: 5px solid rgb(34, 14, 36);\n"
"\n"
"}")

        self.horizontalLayout_13.addWidget(self.calendarWidget)


        self.verticalLayout_11.addWidget(self.frame_7)


        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 0, 0, 0)
        self.Date_time_frame = QFrame(self.frame_5)
        self.Date_time_frame.setObjectName(u"Date_time_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Date_time_frame.sizePolicy().hasHeightForWidth())
        self.Date_time_frame.setSizePolicy(sizePolicy1)
        self.Date_time_frame.setMinimumSize(QSize(320, 250))
        self.Date_time_frame.setMaximumSize(QSize(340, 250))
        font5 = QFont()
        font5.setPointSize(15)
        self.Date_time_frame.setFont(font5)
        self.Date_time_frame.setStyleSheet(u"QFrame{\n"
"\n"
"border: 5px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid white;\n"
"}")
        self.Date_time_frame.setFrameShape(QFrame.NoFrame)
        self.Date_time_frame.setFrameShadow(QFrame.Raised)
        self.digits_accuracy = QSpinBox(self.Date_time_frame)
        self.digits_accuracy.setObjectName(u"digits_accuracy")
        self.digits_accuracy.setGeometry(QRect(230, 120, 61, 31))
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(False)
        font6.setWeight(50)
        self.digits_accuracy.setFont(font6)
        self.digits_accuracy.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;  	\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-but"
                        "ton:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"")
        self.digits_accuracy.setAlignment(Qt.AlignCenter)
        self.digits_accuracy.setMaximum(8)
        self.label = QLabel(self.Date_time_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 111, 16))
        self.label.setFont(font3)
        self.label.setStyleSheet(u"border: none;\n"
"color: white;")
        self.timeEdit = QTimeEdit(self.Date_time_frame)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(130, 30, 141, 31))
        self.timeEdit.setFont(font5)
        self.timeEdit.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;  		\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:"
                        "pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }")
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.label_2 = QLabel(self.Date_time_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 35, 31, 21))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"border: none;\n"
"color: white;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.Date_time_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 70, 101, 16))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: white;")
        self.label_4 = QLabel(self.Date_time_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 171, 31))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"border: none;\n"
"color: white;")
        self.calculate_btn = QPushButton(self.Date_time_frame)
        self.calculate_btn.setObjectName(u"calculate_btn")
        self.calculate_btn.setGeometry(QRect(100, 192, 151, 31))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.calculate_btn.setFont(font7)
        self.calculate_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 14px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0,60%);\n"
"}")

        self.verticalLayout_10.addWidget(self.Date_time_frame)


        self.horizontalLayout_6.addWidget(self.frame_5)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_13)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_content_Julian_calculation)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 170))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_4)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 20))
        self.frame_20.setMaximumSize(QSize(16777215, 20))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(0, 0, 10, 20))
        self.frame_25.setMinimumSize(QSize(10, 0))
        self.frame_25.setMaximumSize(QSize(10, 16777215))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_20)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 0, 500, 20))
        self.label_6.setMinimumSize(QSize(500, 0))
        self.label_6.setMaximumSize(QSize(500, 16777215))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"border: none;\n"
"color: white;")

        self.verticalLayout_15.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_22)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(350, 0))
        self.frame_21.setMaximumSize(QSize(350, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.JulianDay_Result = QLabel(self.frame_21)
        self.JulianDay_Result.setObjectName(u"JulianDay_Result")
        self.JulianDay_Result.setMaximumSize(QSize(16777215, 40))
        self.JulianDay_Result.setStyleSheet(u"QLabel{\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.JulianDay_Result.setScaledContents(True)
        self.JulianDay_Result.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.JulianDay_Result)


        self.horizontalLayout_11.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_23)


        self.verticalLayout_15.addWidget(self.frame_19)


        self.verticalLayout_8.addWidget(self.frame_4)


        self.verticalLayout_5.addWidget(self.frame_content_Julian_calculation)

        self.stackedWidget.addWidget(self.Julian_Day_Screen)
        self.SOI_Screen = QWidget()
        self.SOI_Screen.setObjectName(u"SOI_Screen")
        self.horizontalLayout_17 = QHBoxLayout(self.SOI_Screen)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.SOI_frame_content = QFrame(self.SOI_Screen)
        self.SOI_frame_content.setObjectName(u"SOI_frame_content")
        self.SOI_frame_content.setFrameShape(QFrame.StyledPanel)
        self.SOI_frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.SOI_frame_content)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 10)
        self.frame_37 = QFrame(self.SOI_frame_content)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 40))
        self.frame_37.setMaximumSize(QSize(16777215, 40))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_37)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_title_3 = QLabel(self.frame_37)
        self.label_title_3.setObjectName(u"label_title_3")
        self.label_title_3.setMinimumSize(QSize(400, 0))
        self.label_title_3.setFont(font1)
        self.label_title_3.setStyleSheet(u"color:rgb(60, 235, 250);\n"
"")

        self.verticalLayout_19.addWidget(self.label_title_3)


        self.verticalLayout_16.addWidget(self.frame_37)

        self.frame_33 = QFrame(self.SOI_frame_content)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 30))
        self.frame_33.setMaximumSize(QSize(16777215, 30))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_33)
        self.label_7.setObjectName(u"label_7")
        font8 = QFont()
        font8.setPointSize(11)
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"color: white;")

        self.horizontalLayout_16.addWidget(self.label_7)


        self.verticalLayout_16.addWidget(self.frame_33)

        self.frame_32 = QFrame(self.SOI_frame_content)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 250))
        self.frame_32.setMaximumSize(QSize(16777215, 250))
        self.frame_32.setStyleSheet(u"")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_32)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(130, -1, 130, -1)
        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"QFrame{\n"
"\n"
"border: 5px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid white;\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_35)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(150, 50, 171, 21))
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"color: white;\n"
"border:none;")
        self.lbl_mass = QLabel(self.frame_35)
        self.lbl_mass.setObjectName(u"lbl_mass")
        self.lbl_mass.setGeometry(QRect(20, 130, 141, 21))
        self.lbl_mass.setFont(font8)
        self.lbl_mass.setLayoutDirection(Qt.RightToLeft)
        self.lbl_mass.setStyleSheet(u"color: white;\n"
"border:none;")
        self.SOI_planet_name = QComboBox(self.frame_35)
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.addItem("")
        self.SOI_planet_name.setObjectName(u"SOI_planet_name")
        self.SOI_planet_name.setGeometry(QRect(440, 40, 211, 41))
        self.SOI_planet_name.setStyleSheet(u"QComboBox{\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.lbl_dist_frm_sun = QLabel(self.frame_35)
        self.lbl_dist_frm_sun.setObjectName(u"lbl_dist_frm_sun")
        self.lbl_dist_frm_sun.setGeometry(QRect(410, 130, 221, 21))
        self.lbl_dist_frm_sun.setFont(font8)
        self.lbl_dist_frm_sun.setStyleSheet(u"color: white;\n"
"border:none;")
        self.label_11 = QLabel(self.frame_35)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(340, 130, 141, 21))
        self.label_11.setFont(font8)
        self.label_11.setStyleSheet(u"color: white;\n"
"border:none;")
        self.label_16 = QLabel(self.frame_35)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(740, 130, 141, 21))
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"color: white;\n"
"border:none;")
        self.soi_mass = QLabel(self.frame_35)
        self.soi_mass.setObjectName(u"soi_mass")
        self.soi_mass.setGeometry(QRect(170, 120, 161, 41))
        self.soi_mass.setStyleSheet(u"\n"
"\n"
"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.soi_mass.setAlignment(Qt.AlignCenter)
        self.dist_frm_sun = QLabel(self.frame_35)
        self.dist_frm_sun.setObjectName(u"dist_frm_sun")
        self.dist_frm_sun.setGeometry(QRect(570, 120, 161, 41))
        self.dist_frm_sun.setStyleSheet(u"\n"
"\n"
"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.dist_frm_sun.setAlignment(Qt.AlignCenter)
        self.soi_cal = QPushButton(self.frame_35)
        self.soi_cal.setObjectName(u"soi_cal")
        self.soi_cal.setGeometry(QRect(350, 170, 101, 41))
        font9 = QFont()
        font9.setPointSize(12)
        self.soi_cal.setFont(font9)
        self.soi_cal.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0,60%);\n"
"}")

        self.verticalLayout_18.addWidget(self.frame_35)


        self.verticalLayout_16.addWidget(self.frame_32)

        self.frame_26 = QFrame(self.SOI_frame_content)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 30))
        self.frame_26.setMaximumSize(QSize(16777215, 30))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_26)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"color: white;")

        self.horizontalLayout_19.addWidget(self.label_15)


        self.verticalLayout_16.addWidget(self.frame_26)

        self.frame_28 = QFrame(self.SOI_frame_content)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(270, 0, 270, 0)
        self.frame_36 = QFrame(self.frame_28)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"QFrame{\n"
"\n"
"border: 5px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid white;\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.get_3D_soi = QPushButton(self.frame_36)
        self.get_3D_soi.setObjectName(u"get_3D_soi")
        self.get_3D_soi.setGeometry(QRect(130, 100, 254, 41))
        self.get_3D_soi.setFont(font9)
        self.get_3D_soi.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0,60%);\n"
"}")
        self.label_17 = QLabel(self.frame_36)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(480, 20, 111, 41))
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"color: white;\n"
"border:none;")
        self.rSOI_of_planet_lbl = QLabel(self.frame_36)
        self.rSOI_of_planet_lbl.setObjectName(u"rSOI_of_planet_lbl")
        self.rSOI_of_planet_lbl.setGeometry(QRect(10, 30, 211, 21))
        self.rSOI_of_planet_lbl.setFont(font8)
        self.rSOI_of_planet_lbl.setStyleSheet(u"color: white;\n"
"border:none;")
        self.soi_rad = QLabel(self.frame_36)
        self.soi_rad.setObjectName(u"soi_rad")
        self.soi_rad.setGeometry(QRect(230, 20, 241, 41))
        self.soi_rad.setStyleSheet(u"\n"
"\n"
"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.soi_rad.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.frame_36)


        self.verticalLayout_16.addWidget(self.frame_28)


        self.horizontalLayout_17.addWidget(self.SOI_frame_content)

        self.stackedWidget.addWidget(self.SOI_Screen)
        self.VPCO_input = QWidget()
        self.VPCO_input.setObjectName(u"VPCO_input")
        self.verticalLayout_20 = QVBoxLayout(self.VPCO_input)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.VPCO_screen = QFrame(self.VPCO_input)
        self.VPCO_screen.setObjectName(u"VPCO_screen")
        self.VPCO_screen.setFrameShape(QFrame.StyledPanel)
        self.VPCO_screen.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.VPCO_screen)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_29 = QFrame(self.VPCO_screen)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_29)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.screen_heading_frame = QFrame(self.frame_29)
        self.screen_heading_frame.setObjectName(u"screen_heading_frame")
        self.screen_heading_frame.setMinimumSize(QSize(0, 30))
        self.screen_heading_frame.setMaximumSize(QSize(16777215, 30))
        self.screen_heading_frame.setFrameShape(QFrame.StyledPanel)
        self.screen_heading_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.screen_heading_frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_title_4 = QLabel(self.screen_heading_frame)
        self.label_title_4.setObjectName(u"label_title_4")
        self.label_title_4.setMinimumSize(QSize(400, 0))
        self.label_title_4.setFont(font1)
        self.label_title_4.setStyleSheet(u"color:rgb(60, 235, 250);\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_4)


        self.verticalLayout_21.addWidget(self.screen_heading_frame)

        self.frame_38 = QFrame(self.frame_29)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.Home_btn_2 = QPushButton(self.frame_38)
        self.Home_btn_2.setObjectName(u"Home_btn_2")
        self.Home_btn_2.setGeometry(QRect(980, 50, 41, 36))
        self.Home_btn_2.setMinimumSize(QSize(0, 36))
        self.Home_btn_2.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	image:url(UI_Functions/Resources/backk.svg);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 0.2em 0.2em 0.2em 0.2em;\n"
"	\n"
"}")

        self.verticalLayout_21.addWidget(self.frame_38)

        self.type_of_orbit_frame = QFrame(self.frame_29)
        self.type_of_orbit_frame.setObjectName(u"type_of_orbit_frame")
        self.type_of_orbit_frame.setMinimumSize(QSize(1050, 250))
        self.type_of_orbit_frame.setMaximumSize(QSize(1070, 300))
        self.type_of_orbit_frame.setFont(font9)
        self.type_of_orbit_frame.setStyleSheet(u"")
        self.type_of_orbit_frame.setFrameShape(QFrame.NoFrame)
        self.type_of_orbit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.type_of_orbit_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, 9, 9, 9)
        self.Orbit_type_stack = QStackedWidget(self.type_of_orbit_frame)
        self.Orbit_type_stack.setObjectName(u"Orbit_type_stack")
        self.Orbit_type_stack.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"border: 5px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")
        self.vpco_input_type_screen = QWidget()
        self.vpco_input_type_screen.setObjectName(u"vpco_input_type_screen")
        self.vpco_input_type = QComboBox(self.vpco_input_type_screen)
        self.vpco_input_type.addItem("")
        self.vpco_input_type.addItem("")
        self.vpco_input_type.addItem("")
        self.vpco_input_type.addItem("")
        self.vpco_input_type.addItem("")
        self.vpco_input_type.addItem("")
        self.vpco_input_type.setObjectName(u"vpco_input_type")
        self.vpco_input_type.setGeometry(QRect(310, 150, 391, 41))
        self.vpco_input_type.setStyleSheet(u"QComboBox{\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.label_9 = QLabel(self.vpco_input_type_screen)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 30, 671, 41))
        font10 = QFont()
        font10.setFamily(u"Arial")
        font10.setPointSize(12)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.label_9.setFont(font10)
        self.label_9.setStyleSheet(u"color: white;\n"
"border:none;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.vpco_major_body = QComboBox(self.vpco_input_type_screen)
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.addItem("")
        self.vpco_major_body.setObjectName(u"vpco_major_body")
        self.vpco_major_body.setGeometry(QRect(400, 90, 211, 41))
        self.vpco_major_body.setStyleSheet(u"QComboBox{\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.input_type_go_btn_vpco = QPushButton(self.vpco_input_type_screen)
        self.input_type_go_btn_vpco.setObjectName(u"input_type_go_btn_vpco")
        self.input_type_go_btn_vpco.setGeometry(QRect(450, 200, 101, 41))
        self.input_type_go_btn_vpco.setFont(font9)
        self.input_type_go_btn_vpco.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0,60%);\n"
"}")
        self.error_selct_body = QLabel(self.vpco_input_type_screen)
        self.error_selct_body.setObjectName(u"error_selct_body")
        self.error_selct_body.setGeometry(QRect(650, 90, 321, 41))
        self.error_selct_body.setFont(font10)
        self.error_selct_body.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"border:none;")
        self.error_selct_body.setAlignment(Qt.AlignCenter)
        self.Orbit_type_stack.addWidget(self.vpco_input_type_screen)
        self.a_e_screen = QWidget()
        self.a_e_screen.setObjectName(u"a_e_screen")
        self.label_13 = QLabel(self.a_e_screen)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(70, 40, 171, 21))
        self.label_13.setStyleSheet(u"border:none")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.a_e_screen)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(610, 40, 151, 21))
        self.label_14.setStyleSheet(u"border:none")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.a_e_screen)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(380, 40, 71, 21))
        self.label_19.setStyleSheet(u"border:none")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.orbit_type_ae = QLabel(self.a_e_screen)
        self.orbit_type_ae.setObjectName(u"orbit_type_ae")
        self.orbit_type_ae.setGeometry(QRect(370, 140, 261, 41))
        self.orbit_type_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"  	\n"
"}")
        self.orbit_type_ae.setAlignment(Qt.AlignCenter)
        self.orbit_type_btn_inpt_ae = QPushButton(self.a_e_screen)
        self.orbit_type_btn_inpt_ae.setObjectName(u"orbit_type_btn_inpt_ae")
        self.orbit_type_btn_inpt_ae.setGeometry(QRect(440, 90, 121, 41))
        self.orbit_type_btn_inpt_ae.setFont(font9)
        self.orbit_type_btn_inpt_ae.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0,60%);\n"
"}")
        self.go_btn_inpt_ae = QPushButton(self.a_e_screen)
        self.go_btn_inpt_ae.setObjectName(u"go_btn_inpt_ae")
        self.go_btn_inpt_ae.setGeometry(QRect(450, 190, 101, 41))
        self.go_btn_inpt_ae.setFont(font9)
        self.go_btn_inpt_ae.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0,60%);\n"
"}")
        self.semimajor_axis_input_ae = QLineEdit(self.a_e_screen)
        self.semimajor_axis_input_ae.setObjectName(u"semimajor_axis_input_ae")
        self.semimajor_axis_input_ae.setGeometry(QRect(240, 30, 131, 41))
        self.semimajor_axis_input_ae.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:black;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.semimajor_axis_input_ae.setAlignment(Qt.AlignCenter)
        self.eccentricity_inpt_ae = QDoubleSpinBox(self.a_e_screen)
        self.eccentricity_inpt_ae.setObjectName(u"eccentricity_inpt_ae")
        self.eccentricity_inpt_ae.setGeometry(QRect(751, 30, 131, 41))
        self.eccentricity_inpt_ae.setFont(font9)
        self.eccentricity_inpt_ae.setStyleSheet(u"    /*spinbox lift style*/\n"
"   QDoubleSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;  \n"
"		\n"
"		\n"
"    }\n"
"\n"
" \n"
"    QDoubleSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"   QDoubleSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QDoubleSpinBox::down-button:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"	QDoubleSpinBox{\n"
"		border: 5px solid rgb(84, 84, 19"
                        "7);\n"
"		border-radius: 20px;	\n"
"}\n"
"	QDoubleSpinBox:hover{\n"
"\n"
"		border: 4px solid rgb(2, 119, 189);\n"
"  		\n"
"}")
        self.eccentricity_inpt_ae.setAlignment(Qt.AlignCenter)
        self.eccentricity_inpt_ae.setSingleStep(0.100000000000000)
        self.Orbit_type_stack.addWidget(self.a_e_screen)
        self.ra_rp_screen = QWidget()
        self.ra_rp_screen.setObjectName(u"ra_rp_screen")
        self.ra_inpt_rarp = QLabel(self.ra_rp_screen)
        self.ra_inpt_rarp.setObjectName(u"ra_inpt_rarp")
        self.ra_inpt_rarp.setGeometry(QRect(270, 30, 161, 41))
        self.ra_inpt_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_12 = QLabel(self.ra_rp_screen)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 181, 41))
        self.label_12.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_32 = QLabel(self.ra_rp_screen)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(550, 30, 201, 41))
        self.label_32.setStyleSheet(u"border:none;\n"
"color:white;")
        self.rp_inpt_rarp = QLabel(self.ra_rp_screen)
        self.rp_inpt_rarp.setObjectName(u"rp_inpt_rarp")
        self.rp_inpt_rarp.setGeometry(QRect(760, 30, 161, 41))
        self.rp_inpt_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_34 = QLabel(self.ra_rp_screen)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(440, 30, 51, 41))
        self.label_34.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_35 = QLabel(self.ra_rp_screen)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(930, 30, 51, 41))
        self.label_35.setStyleSheet(u"border:none;\n"
"color:white;")
        self.orbit_type_rarp = QLabel(self.ra_rp_screen)
        self.orbit_type_rarp.setObjectName(u"orbit_type_rarp")
        self.orbit_type_rarp.setGeometry(QRect(380, 140, 241, 41))
        self.orbit_type_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.orbit_type_rarp.setAlignment(Qt.AlignCenter)
        self.Orbit_type_stack.addWidget(self.ra_rp_screen)
        self.r_v_gamma_screen = QWidget()
        self.r_v_gamma_screen.setObjectName(u"r_v_gamma_screen")
        self.distance_frm_cntr_of_body_inpt_rvgamma = QLabel(self.r_v_gamma_screen)
        self.distance_frm_cntr_of_body_inpt_rvgamma.setObjectName(u"distance_frm_cntr_of_body_inpt_rvgamma")
        self.distance_frm_cntr_of_body_inpt_rvgamma.setGeometry(QRect(550, 20, 141, 41))
        self.distance_frm_cntr_of_body_inpt_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_20 = QLabel(self.r_v_gamma_screen)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 5, 181, 21))
        self.label_20.setStyleSheet(u"color:rgb(205, 255, 193);\n"
"border:none;")
        self.label_21 = QLabel(self.r_v_gamma_screen)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(100, 20, 441, 41))
        self.label_21.setLayoutDirection(Qt.RightToLeft)
        self.label_21.setStyleSheet(u"border:none;")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_30 = QLabel(self.r_v_gamma_screen)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(100, 70, 441, 41))
        self.label_30.setLayoutDirection(Qt.RightToLeft)
        self.label_30.setStyleSheet(u"border:none;")
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_31 = QLabel(self.r_v_gamma_screen)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(690, 20, 51, 41))
        self.label_31.setLayoutDirection(Qt.RightToLeft)
        self.label_31.setStyleSheet(u"border:none;")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.v_at_point_inpt_rvgamma = QLabel(self.r_v_gamma_screen)
        self.v_at_point_inpt_rvgamma.setObjectName(u"v_at_point_inpt_rvgamma")
        self.v_at_point_inpt_rvgamma.setGeometry(QRect(550, 70, 141, 41))
        self.v_at_point_inpt_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_39 = QLabel(self.r_v_gamma_screen)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(690, 70, 51, 41))
        self.label_39.setLayoutDirection(Qt.RightToLeft)
        self.label_39.setStyleSheet(u"border:none;")
        self.label_39.setAlignment(Qt.AlignCenter)
        self.flt_path_angle_inpt_rvgamma = QLabel(self.r_v_gamma_screen)
        self.flt_path_angle_inpt_rvgamma.setObjectName(u"flt_path_angle_inpt_rvgamma")
        self.flt_path_angle_inpt_rvgamma.setGeometry(QRect(550, 120, 141, 41))
        self.flt_path_angle_inpt_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_41 = QLabel(self.r_v_gamma_screen)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(100, 120, 441, 41))
        self.label_41.setLayoutDirection(Qt.RightToLeft)
        self.label_41.setStyleSheet(u"border:none;")
        self.label_41.setAlignment(Qt.AlignCenter)
        self.label_42 = QLabel(self.r_v_gamma_screen)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(700, 120, 51, 41))
        self.label_42.setLayoutDirection(Qt.RightToLeft)
        self.label_42.setStyleSheet(u"border:none;")
        self.label_42.setAlignment(Qt.AlignCenter)
        self.orbit_type_rvgamma = QLabel(self.r_v_gamma_screen)
        self.orbit_type_rvgamma.setObjectName(u"orbit_type_rvgamma")
        self.orbit_type_rvgamma.setGeometry(QRect(430, 190, 211, 41))
        self.orbit_type_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.Orbit_type_stack.addWidget(self.r_v_gamma_screen)
        self.orbital_elements_screen = QWidget()
        self.orbital_elements_screen.setObjectName(u"orbital_elements_screen")
        self.semi_major_axis_inpt_orbitalElements = QLabel(self.orbital_elements_screen)
        self.semi_major_axis_inpt_orbitalElements.setObjectName(u"semi_major_axis_inpt_orbitalElements")
        self.semi_major_axis_inpt_orbitalElements.setGeometry(QRect(280, 10, 101, 41))
        self.semi_major_axis_inpt_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.eccentricity_inpt_orbitalElements = QLabel(self.orbital_elements_screen)
        self.eccentricity_inpt_orbitalElements.setObjectName(u"eccentricity_inpt_orbitalElements")
        self.eccentricity_inpt_orbitalElements.setGeometry(QRect(280, 70, 101, 41))
        self.eccentricity_inpt_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.inclination_inpt_orbitalElements = QLabel(self.orbital_elements_screen)
        self.inclination_inpt_orbitalElements.setObjectName(u"inclination_inpt_orbitalElements")
        self.inclination_inpt_orbitalElements.setGeometry(QRect(280, 130, 101, 41))
        self.inclination_inpt_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.raan_inpt_orbitalElements = QLabel(self.orbital_elements_screen)
        self.raan_inpt_orbitalElements.setObjectName(u"raan_inpt_orbitalElements")
        self.raan_inpt_orbitalElements.setGeometry(QRect(830, 10, 101, 41))
        self.raan_inpt_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.argment_of_peri__inpt_orbitalElements = QLabel(self.orbital_elements_screen)
        self.argment_of_peri__inpt_orbitalElements.setObjectName(u"argment_of_peri__inpt_orbitalElements")
        self.argment_of_peri__inpt_orbitalElements.setGeometry(QRect(830, 70, 101, 41))
        self.argment_of_peri__inpt_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.tru_anmly_inpt_orbitalElements = QLabel(self.orbital_elements_screen)
        self.tru_anmly_inpt_orbitalElements.setObjectName(u"tru_anmly_inpt_orbitalElements")
        self.tru_anmly_inpt_orbitalElements.setGeometry(QRect(830, 130, 101, 41))
        self.tru_anmly_inpt_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_73 = QLabel(self.orbital_elements_screen)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(50, 20, 201, 21))
        self.label_73.setStyleSheet(u"border:none;")
        self.label_73.setAlignment(Qt.AlignCenter)
        self.label_74 = QLabel(self.orbital_elements_screen)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(50, 80, 161, 21))
        self.label_74.setStyleSheet(u"border:none;")
        self.label_74.setAlignment(Qt.AlignCenter)
        self.label_75 = QLabel(self.orbital_elements_screen)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(50, 140, 161, 21))
        self.label_75.setStyleSheet(u"border:none;")
        self.label_75.setAlignment(Qt.AlignCenter)
        self.label_76 = QLabel(self.orbital_elements_screen)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(580, 140, 221, 21))
        self.label_76.setStyleSheet(u"border:none;")
        self.label_76.setAlignment(Qt.AlignCenter)
        self.label_77 = QLabel(self.orbital_elements_screen)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(640, 20, 161, 21))
        self.label_77.setStyleSheet(u"border:none;")
        self.label_77.setAlignment(Qt.AlignCenter)
        self.label_78 = QLabel(self.orbital_elements_screen)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(500, 80, 301, 21))
        self.label_78.setStyleSheet(u"border:none;")
        self.label_78.setAlignment(Qt.AlignCenter)
        self.label_107 = QLabel(self.orbital_elements_screen)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(390, 20, 61, 21))
        self.label_107.setStyleSheet(u"border:none;")
        self.label_107.setAlignment(Qt.AlignCenter)
        self.label_108 = QLabel(self.orbital_elements_screen)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(940, 20, 61, 21))
        self.label_108.setStyleSheet(u"border:none;")
        self.label_108.setAlignment(Qt.AlignCenter)
        self.label_109 = QLabel(self.orbital_elements_screen)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(390, 140, 61, 21))
        self.label_109.setStyleSheet(u"border:none;")
        self.label_109.setAlignment(Qt.AlignCenter)
        self.label_110 = QLabel(self.orbital_elements_screen)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(940, 80, 61, 21))
        self.label_110.setStyleSheet(u"border:none;")
        self.label_110.setAlignment(Qt.AlignCenter)
        self.label_111 = QLabel(self.orbital_elements_screen)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(940, 140, 61, 21))
        self.label_111.setStyleSheet(u"border:none;")
        self.label_111.setAlignment(Qt.AlignCenter)
        self.orbit_type_orbitalElements = QLabel(self.orbital_elements_screen)
        self.orbit_type_orbitalElements.setObjectName(u"orbit_type_orbitalElements")
        self.orbit_type_orbitalElements.setGeometry(QRect(390, 180, 231, 41))
        self.orbit_type_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.Orbit_type_stack.addWidget(self.orbital_elements_screen)
        self.stateVectors_screen = QWidget()
        self.stateVectors_screen.setObjectName(u"stateVectors_screen")
        self.position_vector_inpt_stateVector = QLabel(self.stateVectors_screen)
        self.position_vector_inpt_stateVector.setObjectName(u"position_vector_inpt_stateVector")
        self.position_vector_inpt_stateVector.setGeometry(QRect(280, 50, 131, 41))
        self.position_vector_inpt_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_150 = QLabel(self.stateVectors_screen)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setGeometry(QRect(100, 60, 141, 21))
        self.label_150.setStyleSheet(u"border:none;")
        self.label_150.setAlignment(Qt.AlignCenter)
        self.velocity_vector_inpt_stateVector = QLabel(self.stateVectors_screen)
        self.velocity_vector_inpt_stateVector.setObjectName(u"velocity_vector_inpt_stateVector")
        self.velocity_vector_inpt_stateVector.setGeometry(QRect(680, 50, 131, 41))
        self.velocity_vector_inpt_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_152 = QLabel(self.stateVectors_screen)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setGeometry(QRect(530, 60, 131, 21))
        self.label_152.setStyleSheet(u"border:none;")
        self.label_152.setAlignment(Qt.AlignCenter)
        self.label_153 = QLabel(self.stateVectors_screen)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setGeometry(QRect(420, 60, 41, 21))
        self.label_153.setStyleSheet(u"border:none;")
        self.label_153.setAlignment(Qt.AlignCenter)
        self.label_154 = QLabel(self.stateVectors_screen)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setGeometry(QRect(820, 60, 51, 21))
        self.label_154.setStyleSheet(u"border:none;")
        self.label_154.setAlignment(Qt.AlignCenter)
        self.orbit_type_stateVector = QLabel(self.stateVectors_screen)
        self.orbit_type_stateVector.setObjectName(u"orbit_type_stateVector")
        self.orbit_type_stateVector.setGeometry(QRect(410, 160, 191, 41))
        self.orbit_type_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.Orbit_type_stack.addWidget(self.stateVectors_screen)

        self.verticalLayout_22.addWidget(self.Orbit_type_stack)


        self.horizontalLayout_7.addLayout(self.verticalLayout_22)


        self.verticalLayout_21.addWidget(self.type_of_orbit_frame)

        self.frame_39 = QFrame(self.frame_29)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.Error_parabola = QLabel(self.frame_39)
        self.Error_parabola.setObjectName(u"Error_parabola")
        font11 = QFont()
        font11.setFamily(u"MS Shell Dlg 2")
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.Error_parabola.setFont(font11)
        self.Error_parabola.setStyleSheet(u"border:none;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_parabola.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.Error_parabola)


        self.verticalLayout_21.addWidget(self.frame_39)


        self.horizontalLayout_20.addWidget(self.frame_29)


        self.verticalLayout_20.addWidget(self.VPCO_screen)

        self.stackedWidget.addWidget(self.VPCO_input)
        self.VPCO_output = QWidget()
        self.VPCO_output.setObjectName(u"VPCO_output")
        self.horizontalLayout_21 = QHBoxLayout(self.VPCO_output)
        self.horizontalLayout_21.setSpacing(3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(6, 0, 6, 0)
        self.VPCO_menu_toggle_frame = QFrame(self.VPCO_output)
        self.VPCO_menu_toggle_frame.setObjectName(u"VPCO_menu_toggle_frame")
        self.VPCO_menu_toggle_frame.setMaximumSize(QSize(40, 16777215))
        self.VPCO_menu_toggle_frame.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 5px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background: transparent;\n"
"	min-height: 30px;\n"
"	border-radius: 2.4px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background:transparent;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
""
                        "	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background:transparent;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 5px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.VPCO_menu_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.VPCO_menu_toggle_frame.setFrameShadow(QFrame.Raised)
        self.VPCO_menu_toggle_frame.setMidLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.VPCO_menu_toggle_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_menu_btn_frame = QFrame(self.VPCO_menu_toggle_frame)
        self.toggle_menu_btn_frame.setObjectName(u"toggle_menu_btn_frame")
        self.toggle_menu_btn_frame.setMinimumSize(QSize(0, 40))
        self.toggle_menu_btn_frame.setMaximumSize(QSize(16777215, 40))
        self.toggle_menu_btn_frame.setStyleSheet(u"\n"
"\n"
"QFrame{\n"
"border:none;\n"
"background:transparent;\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(168, 128, 243, 70%), stop:1 rgba(108, 121, 240, 70%));\n"
"\n"
"}")
        self.toggle_menu_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.toggle_menu_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.toggle_menu_btn_frame)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.drop_frame_toggle = QFrame(self.toggle_menu_btn_frame)
        self.drop_frame_toggle.setObjectName(u"drop_frame_toggle")
        self.drop_frame_toggle.setMinimumSize(QSize(0, 40))
        self.drop_frame_toggle.setMaximumSize(QSize(16777215, 40))
        self.drop_frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.drop_frame_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.drop_frame_toggle)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.toggle_menu_btn = QPushButton(self.drop_frame_toggle)
        self.toggle_menu_btn.setObjectName(u"toggle_menu_btn")
        self.toggle_menu_btn.setMinimumSize(QSize(35, 20))
        self.toggle_menu_btn.setMaximumSize(QSize(35, 20))
        self.toggle_menu_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 0.1em 0.1em 0.1em 0.1em;\n"
"	\n"
"}")
        icon = QIcon()
        icon.addFile(u"UI_Functions/Resources/Toggle_menu_btn_VPCO_rounded.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_menu_btn.setIcon(icon)
        self.toggle_menu_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_36.addWidget(self.toggle_menu_btn)

        self.type_of_input_toggle = QComboBox(self.drop_frame_toggle)
        self.type_of_input_toggle.addItem("")
        self.type_of_input_toggle.addItem("")
        self.type_of_input_toggle.addItem("")
        self.type_of_input_toggle.addItem("")
        self.type_of_input_toggle.addItem("")
        self.type_of_input_toggle.addItem("")
        self.type_of_input_toggle.setObjectName(u"type_of_input_toggle")
        self.type_of_input_toggle.setMinimumSize(QSize(100, 30))
        self.type_of_input_toggle.setMaximumSize(QSize(100, 30))
        self.type_of_input_toggle.setLayoutDirection(Qt.LeftToRight)
        self.type_of_input_toggle.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	\n"
"	border: 3px solid rgb(34, 14, 36);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 15px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid white;\n"
"}\n"
"\n"
"")
        self.type_of_input_toggle.setEditable(False)

        self.horizontalLayout_36.addWidget(self.type_of_input_toggle)


        self.horizontalLayout_25.addWidget(self.drop_frame_toggle)


        self.verticalLayout_2.addWidget(self.toggle_menu_btn_frame)

        self.stackedWidget_2 = QStackedWidget(self.VPCO_menu_toggle_frame)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"border:none;")
        self.all_classic_orbital_elements_show_page = QWidget()
        self.all_classic_orbital_elements_show_page.setObjectName(u"all_classic_orbital_elements_show_page")
        self.verticalLayout_24 = QVBoxLayout(self.all_classic_orbital_elements_show_page)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 10)
        self.semi_major_axis_toggle_menu_lbl_2 = QLabel(self.all_classic_orbital_elements_show_page)
        self.semi_major_axis_toggle_menu_lbl_2.setObjectName(u"semi_major_axis_toggle_menu_lbl_2")
        self.semi_major_axis_toggle_menu_lbl_2.setFont(font7)
        self.semi_major_axis_toggle_menu_lbl_2.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.semi_major_axis_toggle_menu_lbl_2)

        self.eccentricity_toggle_menu_lbl_2 = QLabel(self.all_classic_orbital_elements_show_page)
        self.eccentricity_toggle_menu_lbl_2.setObjectName(u"eccentricity_toggle_menu_lbl_2")
        self.eccentricity_toggle_menu_lbl_2.setFont(font7)
        self.eccentricity_toggle_menu_lbl_2.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"}\n"
"\n"
"")
        self.eccentricity_toggle_menu_lbl_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.eccentricity_toggle_menu_lbl_2)

        self.inclination_toggle_menu_lbl_2 = QLabel(self.all_classic_orbital_elements_show_page)
        self.inclination_toggle_menu_lbl_2.setObjectName(u"inclination_toggle_menu_lbl_2")
        self.inclination_toggle_menu_lbl_2.setFont(font7)
        self.inclination_toggle_menu_lbl_2.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"}\n"
"\n"
"")
        self.inclination_toggle_menu_lbl_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.inclination_toggle_menu_lbl_2)

        self.RAAN_toggle_menu_lbl_2 = QLabel(self.all_classic_orbital_elements_show_page)
        self.RAAN_toggle_menu_lbl_2.setObjectName(u"RAAN_toggle_menu_lbl_2")
        self.RAAN_toggle_menu_lbl_2.setFont(font7)
        self.RAAN_toggle_menu_lbl_2.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"}\n"
"\n"
"")
        self.RAAN_toggle_menu_lbl_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.RAAN_toggle_menu_lbl_2)

        self.arg_of_per_toggle_menu_lbl_2 = QLabel(self.all_classic_orbital_elements_show_page)
        self.arg_of_per_toggle_menu_lbl_2.setObjectName(u"arg_of_per_toggle_menu_lbl_2")
        self.arg_of_per_toggle_menu_lbl_2.setFont(font7)
        self.arg_of_per_toggle_menu_lbl_2.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"}\n"
"\n"
"")
        self.arg_of_per_toggle_menu_lbl_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.arg_of_per_toggle_menu_lbl_2)

        self.tru_ano_toggle_menu_lbl_2 = QLabel(self.all_classic_orbital_elements_show_page)
        self.tru_ano_toggle_menu_lbl_2.setObjectName(u"tru_ano_toggle_menu_lbl_2")
        self.tru_ano_toggle_menu_lbl_2.setFont(font7)
        self.tru_ano_toggle_menu_lbl_2.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"}\n"
"\n"
"")
        self.tru_ano_toggle_menu_lbl_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.tru_ano_toggle_menu_lbl_2)

        self.stackedWidget_2.addWidget(self.all_classic_orbital_elements_show_page)
        self.Semi_major_axis_and_Eccentricity_page = QWidget()
        self.Semi_major_axis_and_Eccentricity_page.setObjectName(u"Semi_major_axis_and_Eccentricity_page")
        self.Semi_major_axis_and_Eccentricity_page.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    \n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"    border: 0px solid;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"	border-radius:5.4px;\n"
"	\n"
"    \n"
"    }\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.Semi_major_axis_and_Eccentricity_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Semi_major_axis_toggle_frame = QFrame(self.Semi_major_axis_and_Eccentricity_page)
        self.Semi_major_axis_toggle_frame.setObjectName(u"Semi_major_axis_toggle_frame")
        self.Semi_major_axis_toggle_frame.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}")
        self.Semi_major_axis_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Semi_major_axis_toggle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.Semi_major_axis_toggle_frame)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(8, 8, 8, 8)
        self.Semi_major_axis_toggle_menu_layout = QVBoxLayout()
        self.Semi_major_axis_toggle_menu_layout.setSpacing(0)
        self.Semi_major_axis_toggle_menu_layout.setObjectName(u"Semi_major_axis_toggle_menu_layout")
        self.Semi_major_axis_toggle_menu_layout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.semi_major_axis_toggle_menu_lbl = QLabel(self.Semi_major_axis_toggle_frame)
        self.semi_major_axis_toggle_menu_lbl.setObjectName(u"semi_major_axis_toggle_menu_lbl")
        self.semi_major_axis_toggle_menu_lbl.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl.setMaximumSize(QSize(16777215, 20))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setWeight(75)
        self.semi_major_axis_toggle_menu_lbl.setFont(font12)
        self.semi_major_axis_toggle_menu_lbl.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.semi_major_axis_toggle_menu_lbl)


        self.Semi_major_axis_toggle_menu_layout.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.semi_major_axis_toggle_menu_spinbox = QDoubleSpinBox(self.Semi_major_axis_toggle_frame)
        self.semi_major_axis_toggle_menu_spinbox.setObjectName(u"semi_major_axis_toggle_menu_spinbox")
        self.semi_major_axis_toggle_menu_spinbox.setMinimumSize(QSize(80, 0))
        self.semi_major_axis_toggle_menu_spinbox.setMaximumSize(QSize(80, 16777215))
        self.semi_major_axis_toggle_menu_spinbox.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;  	\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-but"
                        "ton:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"QDoubleSpinBox{\n"
"border: 2px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.semi_major_axis_toggle_menu_spinbox.setAlignment(Qt.AlignCenter)
        self.semi_major_axis_toggle_menu_spinbox.setMinimum(-999999996.000000000000000)
        self.semi_major_axis_toggle_menu_spinbox.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_27.addWidget(self.semi_major_axis_toggle_menu_spinbox)


        self.Semi_major_axis_toggle_menu_layout.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.Semi_dial = QDial(self.Semi_major_axis_toggle_frame)
        self.Semi_dial.setObjectName(u"Semi_dial")
        self.Semi_dial.setMinimumSize(QSize(75, 75))
        self.Semi_dial.setMaximumSize(QSize(75, 75))
        self.Semi_dial.setMouseTracking(False)
        self.Semi_dial.setStyleSheet(u"QDial::handle { background-color: black }")
        self.Semi_dial.setMinimum(0)
        self.Semi_dial.setMaximum(10)

        self.horizontalLayout_30.addWidget(self.Semi_dial)


        self.Semi_major_axis_toggle_menu_layout.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.semi_major_axis_toggle_menu_single_step = QDoubleSpinBox(self.Semi_major_axis_toggle_frame)
        self.semi_major_axis_toggle_menu_single_step.setObjectName(u"semi_major_axis_toggle_menu_single_step")
        self.semi_major_axis_toggle_menu_single_step.setMinimumSize(QSize(80, 0))
        self.semi_major_axis_toggle_menu_single_step.setMaximumSize(QSize(80, 16777215))
        self.semi_major_axis_toggle_menu_single_step.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow_white.svg);\n"
"        width: 12px;\n"
"        height: 20px;  	\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow_white.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinB"
                        "ox::down-button:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"QDoubleSpinBox{\n"
"border: 2px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.semi_major_axis_toggle_menu_single_step.setAlignment(Qt.AlignCenter)
        self.semi_major_axis_toggle_menu_single_step.setMinimum(10.000000000000000)
        self.semi_major_axis_toggle_menu_single_step.setMaximum(100000.000000000000000)

        self.horizontalLayout_42.addWidget(self.semi_major_axis_toggle_menu_single_step)


        self.Semi_major_axis_toggle_menu_layout.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.semi_major_axis_toggle_menu_slider = QSlider(self.Semi_major_axis_toggle_frame)
        self.semi_major_axis_toggle_menu_slider.setObjectName(u"semi_major_axis_toggle_menu_slider")
        self.semi_major_axis_toggle_menu_slider.setStyleSheet(u"")
        self.semi_major_axis_toggle_menu_slider.setMaximum(5)
        self.semi_major_axis_toggle_menu_slider.setPageStep(10)
        self.semi_major_axis_toggle_menu_slider.setValue(0)
        self.semi_major_axis_toggle_menu_slider.setSliderPosition(0)
        self.semi_major_axis_toggle_menu_slider.setOrientation(Qt.Horizontal)
        self.semi_major_axis_toggle_menu_slider.setTickPosition(QSlider.TicksAbove)
        self.semi_major_axis_toggle_menu_slider.setTickInterval(1)

        self.horizontalLayout_35.addWidget(self.semi_major_axis_toggle_menu_slider)


        self.Semi_major_axis_toggle_menu_layout.addLayout(self.horizontalLayout_35)


        self.horizontalLayout_26.addLayout(self.Semi_major_axis_toggle_menu_layout)


        self.verticalLayout_3.addWidget(self.Semi_major_axis_toggle_frame)

        self.Eccentricity_toggle_frame = QFrame(self.Semi_major_axis_and_Eccentricity_page)
        self.Eccentricity_toggle_frame.setObjectName(u"Eccentricity_toggle_frame")
        self.Eccentricity_toggle_frame.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}")
        self.Eccentricity_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Eccentricity_toggle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.Eccentricity_toggle_frame)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(8, 8, 8, 8)
        self.eccentricity_toggle_menu_layout = QVBoxLayout()
        self.eccentricity_toggle_menu_layout.setSpacing(0)
        self.eccentricity_toggle_menu_layout.setObjectName(u"eccentricity_toggle_menu_layout")
        self.eccentricity_toggle_menu_layout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.eccentricity_toggle_menu_lbl = QLabel(self.Eccentricity_toggle_frame)
        self.eccentricity_toggle_menu_lbl.setObjectName(u"eccentricity_toggle_menu_lbl")
        self.eccentricity_toggle_menu_lbl.setMinimumSize(QSize(0, 20))
        self.eccentricity_toggle_menu_lbl.setMaximumSize(QSize(16777215, 20))
        self.eccentricity_toggle_menu_lbl.setFont(font12)
        self.eccentricity_toggle_menu_lbl.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.eccentricity_toggle_menu_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.eccentricity_toggle_menu_lbl)


        self.eccentricity_toggle_menu_layout.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.eccentricity_toggle_menu_spinbox = QDoubleSpinBox(self.Eccentricity_toggle_frame)
        self.eccentricity_toggle_menu_spinbox.setObjectName(u"eccentricity_toggle_menu_spinbox")
        self.eccentricity_toggle_menu_spinbox.setMinimumSize(QSize(80, 0))
        self.eccentricity_toggle_menu_spinbox.setMaximumSize(QSize(80, 16777215))
        self.eccentricity_toggle_menu_spinbox.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;  	\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-but"
                        "ton:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"QDoubleSpinBox{\n"
"border: 2px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.eccentricity_toggle_menu_spinbox.setAlignment(Qt.AlignCenter)
        self.eccentricity_toggle_menu_spinbox.setMinimum(-50.000000000000000)
        self.eccentricity_toggle_menu_spinbox.setMaximum(50.000000000000000)

        self.horizontalLayout_28.addWidget(self.eccentricity_toggle_menu_spinbox)


        self.eccentricity_toggle_menu_layout.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.ecce_dial = QDial(self.Eccentricity_toggle_frame)
        self.ecce_dial.setObjectName(u"ecce_dial")
        self.ecce_dial.setMinimumSize(QSize(75, 75))
        self.ecce_dial.setMaximumSize(QSize(75, 75))
        self.ecce_dial.setMaximum(10)
        self.ecce_dial.setNotchesVisible(True)

        self.horizontalLayout_29.addWidget(self.ecce_dial)


        self.eccentricity_toggle_menu_layout.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.eccentricity_toggle_menu_single_step = QDoubleSpinBox(self.Eccentricity_toggle_frame)
        self.eccentricity_toggle_menu_single_step.setObjectName(u"eccentricity_toggle_menu_single_step")
        self.eccentricity_toggle_menu_single_step.setMinimumSize(QSize(80, 0))
        self.eccentricity_toggle_menu_single_step.setMaximumSize(QSize(80, 16777215))
        self.eccentricity_toggle_menu_single_step.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow_white.svg);\n"
"        width: 12px;\n"
"        height: 20px;  	\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow_white.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinB"
                        "ox::down-button:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"QDoubleSpinBox{\n"
"border: 2px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.eccentricity_toggle_menu_single_step.setAlignment(Qt.AlignCenter)
        self.eccentricity_toggle_menu_single_step.setMinimum(0.010000000000000)
        self.eccentricity_toggle_menu_single_step.setMaximum(10.000000000000000)

        self.horizontalLayout_44.addWidget(self.eccentricity_toggle_menu_single_step)


        self.eccentricity_toggle_menu_layout.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.eccentricity_toggle_menu_slider = QSlider(self.Eccentricity_toggle_frame)
        self.eccentricity_toggle_menu_slider.setObjectName(u"eccentricity_toggle_menu_slider")
        self.eccentricity_toggle_menu_slider.setStyleSheet(u"")
        self.eccentricity_toggle_menu_slider.setMaximum(7)
        self.eccentricity_toggle_menu_slider.setValue(0)
        self.eccentricity_toggle_menu_slider.setSliderPosition(0)
        self.eccentricity_toggle_menu_slider.setOrientation(Qt.Horizontal)
        self.eccentricity_toggle_menu_slider.setTickPosition(QSlider.TicksAbove)
        self.eccentricity_toggle_menu_slider.setTickInterval(1)

        self.horizontalLayout_34.addWidget(self.eccentricity_toggle_menu_slider)


        self.eccentricity_toggle_menu_layout.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_31.addLayout(self.eccentricity_toggle_menu_layout)


        self.verticalLayout_3.addWidget(self.Eccentricity_toggle_frame)

        self.stackedWidget_2.addWidget(self.Semi_major_axis_and_Eccentricity_page)
        self.Radius_of_apoapsis_and_periapsis_page = QWidget()
        self.Radius_of_apoapsis_and_periapsis_page.setObjectName(u"Radius_of_apoapsis_and_periapsis_page")
        self.verticalLayout_27 = QVBoxLayout(self.Radius_of_apoapsis_and_periapsis_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.Radius_of_Apoapsis_frame = QFrame(self.Radius_of_apoapsis_and_periapsis_page)
        self.Radius_of_Apoapsis_frame.setObjectName(u"Radius_of_Apoapsis_frame")
        self.Radius_of_Apoapsis_frame.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}")
        self.Radius_of_Apoapsis_frame.setFrameShape(QFrame.StyledPanel)
        self.Radius_of_Apoapsis_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.Radius_of_Apoapsis_frame)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(8, 8, 8, 8)
        self.Radius_of_Apoapsis_frame_layout = QVBoxLayout()
        self.Radius_of_Apoapsis_frame_layout.setSpacing(0)
        self.Radius_of_Apoapsis_frame_layout.setObjectName(u"Radius_of_Apoapsis_frame_layout")
        self.Radius_of_Apoapsis_frame_layout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.Radius_of_Apoapsis_frame_lbl = QLabel(self.Radius_of_Apoapsis_frame)
        self.Radius_of_Apoapsis_frame_lbl.setObjectName(u"Radius_of_Apoapsis_frame_lbl")
        self.Radius_of_Apoapsis_frame_lbl.setMinimumSize(QSize(0, 20))
        self.Radius_of_Apoapsis_frame_lbl.setMaximumSize(QSize(16777215, 20))
        self.Radius_of_Apoapsis_frame_lbl.setFont(font12)
        self.Radius_of_Apoapsis_frame_lbl.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.Radius_of_Apoapsis_frame_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.Radius_of_Apoapsis_frame_lbl)


        self.Radius_of_Apoapsis_frame_layout.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.Radius_of_Apoapsis_spinbox = QDoubleSpinBox(self.Radius_of_Apoapsis_frame)
        self.Radius_of_Apoapsis_spinbox.setObjectName(u"Radius_of_Apoapsis_spinbox")
        self.Radius_of_Apoapsis_spinbox.setMinimumSize(QSize(80, 0))
        self.Radius_of_Apoapsis_spinbox.setMaximumSize(QSize(80, 16777215))
        self.Radius_of_Apoapsis_spinbox.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;  	\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-but"
                        "ton:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"QDoubleSpinBox{\n"
"border: 2px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.Radius_of_Apoapsis_spinbox.setAlignment(Qt.AlignCenter)
        self.Radius_of_Apoapsis_spinbox.setMinimum(-999999996.000000000000000)
        self.Radius_of_Apoapsis_spinbox.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_39.addWidget(self.Radius_of_Apoapsis_spinbox)


        self.Radius_of_Apoapsis_frame_layout.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.Radius_of_Apoapsis_dial = QDial(self.Radius_of_Apoapsis_frame)
        self.Radius_of_Apoapsis_dial.setObjectName(u"Radius_of_Apoapsis_dial")
        self.Radius_of_Apoapsis_dial.setMinimumSize(QSize(75, 75))
        self.Radius_of_Apoapsis_dial.setMaximumSize(QSize(75, 75))
        self.Radius_of_Apoapsis_dial.setMouseTracking(False)
        self.Radius_of_Apoapsis_dial.setStyleSheet(u"QDial::handle { background-color: black }")
        self.Radius_of_Apoapsis_dial.setMinimum(0)
        self.Radius_of_Apoapsis_dial.setMaximum(10)
        self.Radius_of_Apoapsis_dial.setWrapping(True)
        self.Radius_of_Apoapsis_dial.setNotchesVisible(True)

        self.horizontalLayout_40.addWidget(self.Radius_of_Apoapsis_dial)


        self.Radius_of_Apoapsis_frame_layout.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.Radius_of_Apoapsis_single_step = QDoubleSpinBox(self.Radius_of_Apoapsis_frame)
        self.Radius_of_Apoapsis_single_step.setObjectName(u"Radius_of_Apoapsis_single_step")
        self.Radius_of_Apoapsis_single_step.setMinimumSize(QSize(80, 0))
        self.Radius_of_Apoapsis_single_step.setMaximumSize(QSize(80, 16777215))
        self.Radius_of_Apoapsis_single_step.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow_white.svg);\n"
"        width: 12px;\n"
"        height: 20px;  	\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow_white.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinB"
                        "ox::down-button:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"QDoubleSpinBox{\n"
"border: 2px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.Radius_of_Apoapsis_single_step.setAlignment(Qt.AlignCenter)
        self.Radius_of_Apoapsis_single_step.setMinimum(10.000000000000000)
        self.Radius_of_Apoapsis_single_step.setMaximum(100000.000000000000000)

        self.horizontalLayout_45.addWidget(self.Radius_of_Apoapsis_single_step)


        self.Radius_of_Apoapsis_frame_layout.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.Radius_of_Apoapsis_slider = QSlider(self.Radius_of_Apoapsis_frame)
        self.Radius_of_Apoapsis_slider.setObjectName(u"Radius_of_Apoapsis_slider")
        self.Radius_of_Apoapsis_slider.setStyleSheet(u"")
        self.Radius_of_Apoapsis_slider.setMaximum(5)
        self.Radius_of_Apoapsis_slider.setPageStep(10)
        self.Radius_of_Apoapsis_slider.setValue(0)
        self.Radius_of_Apoapsis_slider.setSliderPosition(0)
        self.Radius_of_Apoapsis_slider.setOrientation(Qt.Horizontal)
        self.Radius_of_Apoapsis_slider.setTickPosition(QSlider.TicksAbove)
        self.Radius_of_Apoapsis_slider.setTickInterval(1)

        self.horizontalLayout_41.addWidget(self.Radius_of_Apoapsis_slider)


        self.Radius_of_Apoapsis_frame_layout.addLayout(self.horizontalLayout_41)


        self.horizontalLayout_37.addLayout(self.Radius_of_Apoapsis_frame_layout)


        self.verticalLayout_27.addWidget(self.Radius_of_Apoapsis_frame)

        self.Radius_of_Periapsis_frame = QFrame(self.Radius_of_apoapsis_and_periapsis_page)
        self.Radius_of_Periapsis_frame.setObjectName(u"Radius_of_Periapsis_frame")
        self.Radius_of_Periapsis_frame.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}")
        self.Radius_of_Periapsis_frame.setFrameShape(QFrame.StyledPanel)
        self.Radius_of_Periapsis_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.Radius_of_Periapsis_frame)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(8, 8, 8, 8)
        self.Radius_of_Periapsis_frame_layout = QVBoxLayout()
        self.Radius_of_Periapsis_frame_layout.setSpacing(0)
        self.Radius_of_Periapsis_frame_layout.setObjectName(u"Radius_of_Periapsis_frame_layout")
        self.Radius_of_Periapsis_frame_layout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.Radius_of_Periapsis_frame_lbl = QLabel(self.Radius_of_Periapsis_frame)
        self.Radius_of_Periapsis_frame_lbl.setObjectName(u"Radius_of_Periapsis_frame_lbl")
        self.Radius_of_Periapsis_frame_lbl.setMinimumSize(QSize(0, 20))
        self.Radius_of_Periapsis_frame_lbl.setMaximumSize(QSize(16777215, 20))
        self.Radius_of_Periapsis_frame_lbl.setFont(font12)
        self.Radius_of_Periapsis_frame_lbl.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.Radius_of_Periapsis_frame_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.Radius_of_Periapsis_frame_lbl)


        self.Radius_of_Periapsis_frame_layout.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.Radius_of_Periapsis_spinbox = QDoubleSpinBox(self.Radius_of_Periapsis_frame)
        self.Radius_of_Periapsis_spinbox.setObjectName(u"Radius_of_Periapsis_spinbox")
        self.Radius_of_Periapsis_spinbox.setMinimumSize(QSize(80, 0))
        self.Radius_of_Periapsis_spinbox.setMaximumSize(QSize(80, 16777215))
        self.Radius_of_Periapsis_spinbox.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;  	\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-but"
                        "ton:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"QDoubleSpinBox{\n"
"border: 2px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.Radius_of_Periapsis_spinbox.setAlignment(Qt.AlignCenter)
        self.Radius_of_Periapsis_spinbox.setMinimum(-999999996.000000000000000)
        self.Radius_of_Periapsis_spinbox.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_48.addWidget(self.Radius_of_Periapsis_spinbox)


        self.Radius_of_Periapsis_frame_layout.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.Radius_of_Periapsis_dial = QDial(self.Radius_of_Periapsis_frame)
        self.Radius_of_Periapsis_dial.setObjectName(u"Radius_of_Periapsis_dial")
        self.Radius_of_Periapsis_dial.setMinimumSize(QSize(75, 75))
        self.Radius_of_Periapsis_dial.setMaximumSize(QSize(75, 75))
        self.Radius_of_Periapsis_dial.setMouseTracking(False)
        self.Radius_of_Periapsis_dial.setStyleSheet(u"QDial::handle { background-color: black }")
        self.Radius_of_Periapsis_dial.setMinimum(0)
        self.Radius_of_Periapsis_dial.setMaximum(10)
        self.Radius_of_Periapsis_dial.setWrapping(True)
        self.Radius_of_Periapsis_dial.setNotchesVisible(True)

        self.horizontalLayout_49.addWidget(self.Radius_of_Periapsis_dial)


        self.Radius_of_Periapsis_frame_layout.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.Radius_of_Periapsis_single_step = QDoubleSpinBox(self.Radius_of_Periapsis_frame)
        self.Radius_of_Periapsis_single_step.setObjectName(u"Radius_of_Periapsis_single_step")
        self.Radius_of_Periapsis_single_step.setMinimumSize(QSize(80, 0))
        self.Radius_of_Periapsis_single_step.setMaximumSize(QSize(80, 16777215))
        self.Radius_of_Periapsis_single_step.setStyleSheet(u"    /*spinbox lift style*/\n"
"    QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(UI_Functions/Resources/right_arrow_white.svg);\n"
"        width: 12px;\n"
"        height: 20px;  	\n"
"    }\n"
"\n"
" \n"
"    QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {subcontrol-origin:border;\n"
"        subcontrol-position:left;\n"
"        image: url(UI_Functions/Resources/left_arrow_white.svg);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"     /*Button press style*/\n"
"    QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"        subcontrol-position:right;\n"
"        image: url(:/ico/pushed_right.png);\n"
"        width: 12px;\n"
"        height: 20px;       \n"
"    }\n"
"      \n"
"	QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinB"
                        "ox::down-button:pressed{\n"
"        subcontrol-position:left;\n"
"        image: url(:/ico/pushed_left.png);\n"
"        width: 12px;\n"
"        height: 20px;\n"
"    }\n"
"\n"
"QDoubleSpinBox{\n"
"border: 2px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.Radius_of_Periapsis_single_step.setAlignment(Qt.AlignCenter)
        self.Radius_of_Periapsis_single_step.setMinimum(10.000000000000000)
        self.Radius_of_Periapsis_single_step.setMaximum(100000.000000000000000)

        self.horizontalLayout_50.addWidget(self.Radius_of_Periapsis_single_step)


        self.Radius_of_Periapsis_frame_layout.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.Radius_of_Periapsis_slider = QSlider(self.Radius_of_Periapsis_frame)
        self.Radius_of_Periapsis_slider.setObjectName(u"Radius_of_Periapsis_slider")
        self.Radius_of_Periapsis_slider.setStyleSheet(u"")
        self.Radius_of_Periapsis_slider.setMaximum(5)
        self.Radius_of_Periapsis_slider.setPageStep(10)
        self.Radius_of_Periapsis_slider.setValue(0)
        self.Radius_of_Periapsis_slider.setSliderPosition(0)
        self.Radius_of_Periapsis_slider.setOrientation(Qt.Horizontal)
        self.Radius_of_Periapsis_slider.setTickPosition(QSlider.TicksAbove)
        self.Radius_of_Periapsis_slider.setTickInterval(1)

        self.horizontalLayout_51.addWidget(self.Radius_of_Periapsis_slider)


        self.Radius_of_Periapsis_frame_layout.addLayout(self.horizontalLayout_51)


        self.horizontalLayout_46.addLayout(self.Radius_of_Periapsis_frame_layout)


        self.verticalLayout_27.addWidget(self.Radius_of_Periapsis_frame)

        self.stackedWidget_2.addWidget(self.Radius_of_apoapsis_and_periapsis_page)
        self.r1v1gamma1_page = QWidget()
        self.r1v1gamma1_page.setObjectName(u"r1v1gamma1_page")
        self.verticalLayout_28 = QVBoxLayout(self.r1v1gamma1_page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_27 = QFrame(self.r1v1gamma1_page)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 160))
        self.frame_27.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_27)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.frame_41 = QFrame(self.frame_27)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"border:none")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 5, 0, 0)
        self.label_56 = QLabel(self.frame_41)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font4)
        self.label_56.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.label_56)


        self.verticalLayout_29.addWidget(self.frame_41)

        self.frame1 = QFrame(self.frame_27)
        self.frame1.setObjectName(u"frame1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy2)
        self.frame1.setStyleSheet(u"border:none")
        self.horizontalLayout_74 = QHBoxLayout(self.frame1)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.dial_2 = QDial(self.frame1)
        self.dial_2.setObjectName(u"dial_2")
        self.dial_2.setMinimumSize(QSize(75, 75))
        self.dial_2.setMaximumSize(QSize(85, 85))
        self.dial_2.setStyleSheet(u"border:none")
        self.dial_2.setWrapping(True)
        self.dial_2.setNotchesVisible(True)

        self.horizontalLayout_74.addWidget(self.dial_2)


        self.verticalLayout_29.addWidget(self.frame1)

        self.frame_42 = QFrame(self.frame_27)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"border:none")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.lineEdit_9 = QLineEdit(self.frame_42)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(50, 25))
        self.lineEdit_9.setMaximumSize(QSize(80, 25))
        self.lineEdit_9.setStyleSheet(u"QLineEdit{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 10px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid white;\n"
"}")
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.lineEdit_9)

        self.label_63 = QLabel(self.frame_42)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(50, 0))
        self.label_63.setMaximumSize(QSize(30, 16777215))
        self.label_63.setFont(font12)
        self.label_63.setStyleSheet(u"border:none")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.label_63)


        self.verticalLayout_29.addWidget(self.frame_42)


        self.verticalLayout_28.addWidget(self.frame_27)

        self.stackedWidget_2.addWidget(self.r1v1gamma1_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_30 = QVBoxLayout(self.page)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.Radius_of_Apoapsis_frame_2 = QFrame(self.page)
        self.Radius_of_Apoapsis_frame_2.setObjectName(u"Radius_of_Apoapsis_frame_2")
        self.Radius_of_Apoapsis_frame_2.setMinimumSize(QSize(0, 160))
        self.Radius_of_Apoapsis_frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.Radius_of_Apoapsis_frame_2.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}")
        self.Radius_of_Apoapsis_frame_2.setFrameShape(QFrame.StyledPanel)
        self.Radius_of_Apoapsis_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.Radius_of_Apoapsis_frame_2)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.Radius_of_Apoapsis_frame_layout_2 = QVBoxLayout()
        self.Radius_of_Apoapsis_frame_layout_2.setSpacing(0)
        self.Radius_of_Apoapsis_frame_layout_2.setObjectName(u"Radius_of_Apoapsis_frame_layout_2")
        self.Radius_of_Apoapsis_frame_layout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(-1, 5, -1, -1)
        self.Radius_of_Apoapsis_frame_lbl_2 = QLabel(self.Radius_of_Apoapsis_frame_2)
        self.Radius_of_Apoapsis_frame_lbl_2.setObjectName(u"Radius_of_Apoapsis_frame_lbl_2")
        self.Radius_of_Apoapsis_frame_lbl_2.setMinimumSize(QSize(0, 20))
        self.Radius_of_Apoapsis_frame_lbl_2.setMaximumSize(QSize(16777215, 20))
        self.Radius_of_Apoapsis_frame_lbl_2.setFont(font12)
        self.Radius_of_Apoapsis_frame_lbl_2.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.Radius_of_Apoapsis_frame_lbl_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.Radius_of_Apoapsis_frame_lbl_2)


        self.Radius_of_Apoapsis_frame_layout_2.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_54.addItem(self.verticalSpacer_8)


        self.Radius_of_Apoapsis_frame_layout_2.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_29 = QLabel(self.Radius_of_Apoapsis_frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(30, 0))
        self.label_29.setMaximumSize(QSize(30, 16777215))
        self.label_29.setStyleSheet(u"border:none")

        self.horizontalLayout_56.addWidget(self.label_29)

        self.lineEdit_4 = QLineEdit(self.Radius_of_Apoapsis_frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(80, 25))
        self.lineEdit_4.setMaximumSize(QSize(25, 25))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 10px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid white;\n"
"}")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.lineEdit_4)

        self.label_23 = QLabel(self.Radius_of_Apoapsis_frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(30, 0))
        self.label_23.setMaximumSize(QSize(30, 16777215))
        self.label_23.setFont(font12)
        self.label_23.setStyleSheet(u"border:none")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.label_23)


        self.Radius_of_Apoapsis_frame_layout_2.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_10 = QLabel(self.Radius_of_Apoapsis_frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 0))
        self.label_10.setMaximumSize(QSize(30, 16777215))
        font13 = QFont()
        font13.setBold(True)
        font13.setWeight(75)
        self.label_10.setFont(font13)
        self.label_10.setStyleSheet(u"border:none")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.label_10)


        self.Radius_of_Apoapsis_frame_layout_2.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_33 = QLabel(self.Radius_of_Apoapsis_frame_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(30, 0))
        self.label_33.setMaximumSize(QSize(30, 16777215))
        self.label_33.setStyleSheet(u"border:none")

        self.horizontalLayout_57.addWidget(self.label_33)

        self.lineEdit = QLineEdit(self.Radius_of_Apoapsis_frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(80, 25))
        self.lineEdit.setMaximumSize(QSize(80, 25))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 10px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid white;\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.lineEdit)

        self.label_24 = QLabel(self.Radius_of_Apoapsis_frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(30, 0))
        self.label_24.setMaximumSize(QSize(30, 16777215))
        self.label_24.setFont(font12)
        self.label_24.setStyleSheet(u"border:none")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.label_24)


        self.Radius_of_Apoapsis_frame_layout_2.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_18 = QLabel(self.Radius_of_Apoapsis_frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(30, 0))
        self.label_18.setMaximumSize(QSize(30, 16777215))
        self.label_18.setFont(font13)
        self.label_18.setStyleSheet(u"border:none")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_18)


        self.Radius_of_Apoapsis_frame_layout_2.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_37 = QLabel(self.Radius_of_Apoapsis_frame_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(30, 0))
        self.label_37.setMaximumSize(QSize(30, 16777215))
        self.label_37.setStyleSheet(u"border:none")

        self.horizontalLayout_59.addWidget(self.label_37)

        self.lineEdit_3 = QLineEdit(self.Radius_of_Apoapsis_frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(80, 25))
        self.lineEdit_3.setMaximumSize(QSize(80, 25))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 10px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid white;\n"
"}")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.lineEdit_3)

        self.label_28 = QLabel(self.Radius_of_Apoapsis_frame_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(30, 0))
        self.label_28.setMaximumSize(QSize(30, 16777215))
        self.label_28.setFont(font12)
        self.label_28.setStyleSheet(u"border:none")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.label_28)


        self.Radius_of_Apoapsis_frame_layout_2.addLayout(self.horizontalLayout_59)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Radius_of_Apoapsis_frame_layout_2.addItem(self.verticalSpacer_9)


        self.horizontalLayout_52.addLayout(self.Radius_of_Apoapsis_frame_layout_2)


        self.verticalLayout_30.addWidget(self.Radius_of_Apoapsis_frame_2)

        self.Radius_of_Apoapsis_frame_3 = QFrame(self.page)
        self.Radius_of_Apoapsis_frame_3.setObjectName(u"Radius_of_Apoapsis_frame_3")
        self.Radius_of_Apoapsis_frame_3.setMinimumSize(QSize(0, 160))
        self.Radius_of_Apoapsis_frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.Radius_of_Apoapsis_frame_3.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}")
        self.Radius_of_Apoapsis_frame_3.setFrameShape(QFrame.StyledPanel)
        self.Radius_of_Apoapsis_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.Radius_of_Apoapsis_frame_3)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.Radius_of_Apoapsis_frame_layout_3 = QVBoxLayout()
        self.Radius_of_Apoapsis_frame_layout_3.setSpacing(0)
        self.Radius_of_Apoapsis_frame_layout_3.setObjectName(u"Radius_of_Apoapsis_frame_layout_3")
        self.Radius_of_Apoapsis_frame_layout_3.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(-1, 5, -1, -1)
        self.Radius_of_Apoapsis_frame_lbl_3 = QLabel(self.Radius_of_Apoapsis_frame_3)
        self.Radius_of_Apoapsis_frame_lbl_3.setObjectName(u"Radius_of_Apoapsis_frame_lbl_3")
        self.Radius_of_Apoapsis_frame_lbl_3.setMinimumSize(QSize(0, 20))
        self.Radius_of_Apoapsis_frame_lbl_3.setMaximumSize(QSize(16777215, 20))
        self.Radius_of_Apoapsis_frame_lbl_3.setFont(font12)
        self.Radius_of_Apoapsis_frame_lbl_3.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.Radius_of_Apoapsis_frame_lbl_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.Radius_of_Apoapsis_frame_lbl_3)


        self.Radius_of_Apoapsis_frame_layout_3.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_62.addItem(self.verticalSpacer_10)


        self.Radius_of_Apoapsis_frame_layout_3.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_38 = QLabel(self.Radius_of_Apoapsis_frame_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(30, 0))
        self.label_38.setMaximumSize(QSize(30, 16777215))
        self.label_38.setStyleSheet(u"border:none")

        self.horizontalLayout_63.addWidget(self.label_38)

        self.lineEdit_5 = QLineEdit(self.Radius_of_Apoapsis_frame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(80, 25))
        self.lineEdit_5.setMaximumSize(QSize(25, 25))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 10px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid white;\n"
"}")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.lineEdit_5)

        self.label_40 = QLabel(self.Radius_of_Apoapsis_frame_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(30, 0))
        self.label_40.setMaximumSize(QSize(30, 16777215))
        self.label_40.setFont(font12)
        self.label_40.setStyleSheet(u"border:none")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_40)


        self.Radius_of_Apoapsis_frame_layout_3.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_43 = QLabel(self.Radius_of_Apoapsis_frame_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(30, 0))
        self.label_43.setMaximumSize(QSize(30, 16777215))
        self.label_43.setFont(font13)
        self.label_43.setStyleSheet(u"border:none")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label_43)


        self.Radius_of_Apoapsis_frame_layout_3.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_48 = QLabel(self.Radius_of_Apoapsis_frame_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(30, 0))
        self.label_48.setMaximumSize(QSize(30, 16777215))
        self.label_48.setStyleSheet(u"border:none")

        self.horizontalLayout_65.addWidget(self.label_48)

        self.lineEdit_2 = QLineEdit(self.Radius_of_Apoapsis_frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(80, 25))
        self.lineEdit_2.setMaximumSize(QSize(80, 25))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 10px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid white;\n"
"}")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.lineEdit_2)

        self.label_52 = QLabel(self.Radius_of_Apoapsis_frame_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(30, 0))
        self.label_52.setMaximumSize(QSize(30, 16777215))
        self.label_52.setFont(font12)
        self.label_52.setStyleSheet(u"border:none")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_52)


        self.Radius_of_Apoapsis_frame_layout_3.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_53 = QLabel(self.Radius_of_Apoapsis_frame_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(30, 0))
        self.label_53.setMaximumSize(QSize(30, 16777215))
        self.label_53.setFont(font13)
        self.label_53.setStyleSheet(u"border:none")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.label_53)


        self.Radius_of_Apoapsis_frame_layout_3.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_54 = QLabel(self.Radius_of_Apoapsis_frame_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(30, 0))
        self.label_54.setMaximumSize(QSize(30, 16777215))
        self.label_54.setStyleSheet(u"border:none")

        self.horizontalLayout_67.addWidget(self.label_54)

        self.lineEdit_6 = QLineEdit(self.Radius_of_Apoapsis_frame_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(80, 25))
        self.lineEdit_6.setMaximumSize(QSize(80, 25))
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 10px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid white;\n"
"}")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.lineEdit_6)

        self.label_55 = QLabel(self.Radius_of_Apoapsis_frame_3)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(30, 0))
        self.label_55.setMaximumSize(QSize(30, 16777215))
        self.label_55.setFont(font12)
        self.label_55.setStyleSheet(u"border:none")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.label_55)


        self.Radius_of_Apoapsis_frame_layout_3.addLayout(self.horizontalLayout_67)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Radius_of_Apoapsis_frame_layout_3.addItem(self.verticalSpacer_11)


        self.horizontalLayout_60.addLayout(self.Radius_of_Apoapsis_frame_layout_3)


        self.verticalLayout_30.addWidget(self.Radius_of_Apoapsis_frame_3)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_31 = QVBoxLayout(self.page_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.Radius_of_Apoapsis_frame_4 = QFrame(self.page_2)
        self.Radius_of_Apoapsis_frame_4.setObjectName(u"Radius_of_Apoapsis_frame_4")
        sizePolicy2.setHeightForWidth(self.Radius_of_Apoapsis_frame_4.sizePolicy().hasHeightForWidth())
        self.Radius_of_Apoapsis_frame_4.setSizePolicy(sizePolicy2)
        self.Radius_of_Apoapsis_frame_4.setMinimumSize(QSize(0, 160))
        self.Radius_of_Apoapsis_frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.Radius_of_Apoapsis_frame_4.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}")
        self.Radius_of_Apoapsis_frame_4.setFrameShape(QFrame.StyledPanel)
        self.Radius_of_Apoapsis_frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.Radius_of_Apoapsis_frame_4)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.Radius_of_Apoapsis_frame_layout_4 = QVBoxLayout()
        self.Radius_of_Apoapsis_frame_layout_4.setSpacing(0)
        self.Radius_of_Apoapsis_frame_layout_4.setObjectName(u"Radius_of_Apoapsis_frame_layout_4")
        self.Radius_of_Apoapsis_frame_layout_4.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(-1, 5, -1, -1)
        self.Radius_of_Apoapsis_frame_lbl_4 = QLabel(self.Radius_of_Apoapsis_frame_4)
        self.Radius_of_Apoapsis_frame_lbl_4.setObjectName(u"Radius_of_Apoapsis_frame_lbl_4")
        self.Radius_of_Apoapsis_frame_lbl_4.setMinimumSize(QSize(0, 20))
        self.Radius_of_Apoapsis_frame_lbl_4.setMaximumSize(QSize(16777215, 20))
        self.Radius_of_Apoapsis_frame_lbl_4.setFont(font12)
        self.Radius_of_Apoapsis_frame_lbl_4.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.Radius_of_Apoapsis_frame_lbl_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.Radius_of_Apoapsis_frame_lbl_4)


        self.Radius_of_Apoapsis_frame_layout_4.addLayout(self.horizontalLayout_69)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.Radius_of_Apoapsis_frame_4)
        self.widget.setObjectName(u"widget")

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.Radius_of_Apoapsis_frame_layout_4.addLayout(self.gridLayout_2)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.lineEdit_7 = QLineEdit(self.Radius_of_Apoapsis_frame_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(80, 25))
        self.lineEdit_7.setMaximumSize(QSize(25, 25))
        self.lineEdit_7.setStyleSheet(u"QLineEdit{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 10px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid white;\n"
"}")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.lineEdit_7)


        self.Radius_of_Apoapsis_frame_layout_4.addLayout(self.horizontalLayout_71)


        self.horizontalLayout_68.addLayout(self.Radius_of_Apoapsis_frame_layout_4)


        self.verticalLayout_31.addWidget(self.Radius_of_Apoapsis_frame_4)

        self.stackedWidget_2.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget_2)


        self.horizontalLayout_21.addWidget(self.VPCO_menu_toggle_frame)

        self.VPCO_output_frame = QFrame(self.VPCO_output)
        self.VPCO_output_frame.setObjectName(u"VPCO_output_frame")
        self.VPCO_output_frame.setMaximumSize(QSize(1030, 16777215))
        self.VPCO_output_frame.setStyleSheet(u"QFrame{\n"
"\n"
"border: 3px solid rgb(34, 14, 36);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"")
        self.VPCO_output_frame.setFrameShape(QFrame.StyledPanel)
        self.VPCO_output_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.VPCO_output_frame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.VPCO_output_frame)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 25))
        self.frame_40.setMaximumSize(QSize(16777215, 25))
        self.frame_40.setStyleSheet(u"border:none;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 30, 0)
        self.label_title_5 = QLabel(self.frame_40)
        self.label_title_5.setObjectName(u"label_title_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_title_5.sizePolicy().hasHeightForWidth())
        self.label_title_5.setSizePolicy(sizePolicy3)
        self.label_title_5.setMinimumSize(QSize(0, 0))
        self.label_title_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_title_5.setFont(font1)
        self.label_title_5.setStyleSheet(u"color:rgb(60, 235, 250);\n"
"border:none;")

        self.horizontalLayout_22.addWidget(self.label_title_5)

        self.vpco_feature_back_btn = QPushButton(self.frame_40)
        self.vpco_feature_back_btn.setObjectName(u"vpco_feature_back_btn")
        self.vpco_feature_back_btn.setMinimumSize(QSize(25, 25))
        self.vpco_feature_back_btn.setMaximumSize(QSize(30, 25))
        self.vpco_feature_back_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	image:url(UI_Functions/Resources/backk.svg);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 0.2em 0.2em 0.2em 0.2em;\n"
"	\n"
"}")

        self.horizontalLayout_22.addWidget(self.vpco_feature_back_btn)


        self.verticalLayout_23.addWidget(self.frame_40)

        self.VPCO_output_stack = QStackedWidget(self.VPCO_output_frame)
        self.VPCO_output_stack.setObjectName(u"VPCO_output_stack")
        self.VPCO_output_stack.setStyleSheet(u"border:none;")
        self.a_e_result_screen = QWidget()
        self.a_e_result_screen.setObjectName(u"a_e_result_screen")
        self.verticalLayout_26 = QVBoxLayout(self.a_e_result_screen)
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_132 = QLabel(self.a_e_result_screen)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(0, 30))
        self.label_132.setMaximumSize(QSize(16777215, 30))
        self.label_132.setFont(font9)
        self.label_132.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_132.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.label_132)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 13, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.label_51 = QLabel(self.a_e_result_screen)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 40))
        self.label_51.setMaximumSize(QSize(16777215, 40))
        self.label_51.setFont(font4)
        self.label_51.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_51, 6, 0, 1, 1)

        self.label_86 = QLabel(self.a_e_result_screen)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(0, 40))
        self.label_86.setMaximumSize(QSize(16777215, 40))
        self.label_86.setFont(font4)
        self.label_86.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_86, 10, 3, 1, 1)

        self.label_118 = QLabel(self.a_e_result_screen)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(40, 40))
        self.label_118.setMaximumSize(QSize(40, 40))
        self.label_118.setFont(font4)
        self.label_118.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_118.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_118, 0, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.label_123 = QLabel(self.a_e_result_screen)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(40, 40))
        self.label_123.setMaximumSize(QSize(40, 40))
        self.label_123.setFont(font4)
        self.label_123.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_123.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_123, 12, 2, 1, 1)

        self.label_125 = QLabel(self.a_e_result_screen)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(40, 40))
        self.label_125.setMaximumSize(QSize(40, 40))
        self.label_125.setFont(font4)
        self.label_125.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_125.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_125, 12, 5, 1, 1)

        self.label_122 = QLabel(self.a_e_result_screen)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(40, 40))
        self.label_122.setMaximumSize(QSize(40, 40))
        self.label_122.setFont(font4)
        self.label_122.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_122.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_122, 8, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 9, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.label_120 = QLabel(self.a_e_result_screen)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(40, 40))
        self.label_120.setMaximumSize(QSize(40, 40))
        self.label_120.setFont(font4)
        self.label_120.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_120.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_120, 4, 2, 1, 1)

        self.rp_ae = QLabel(self.a_e_result_screen)
        self.rp_ae.setObjectName(u"rp_ae")
        self.rp_ae.setMinimumSize(QSize(150, 30))
        self.rp_ae.setMaximumSize(QSize(150, 30))
        self.rp_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.rp_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.rp_ae, 0, 1, 1, 1)

        self.p_ae = QLabel(self.a_e_result_screen)
        self.p_ae.setObjectName(u"p_ae")
        self.p_ae.setMinimumSize(QSize(150, 30))
        self.p_ae.setMaximumSize(QSize(150, 30))
        self.p_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.p_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.p_ae, 6, 4, 1, 1)

        self.ra_ae = QLabel(self.a_e_result_screen)
        self.ra_ae.setObjectName(u"ra_ae")
        self.ra_ae.setMinimumSize(QSize(150, 30))
        self.ra_ae.setMaximumSize(QSize(150, 30))
        self.ra_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.ra_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ra_ae, 2, 1, 1, 1)

        self.label_81 = QLabel(self.a_e_result_screen)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(0, 40))
        self.label_81.setMaximumSize(QSize(16777215, 40))
        self.label_81.setFont(font4)
        self.label_81.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_81.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_81, 0, 3, 1, 1)

        self.label_128 = QLabel(self.a_e_result_screen)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(40, 40))
        self.label_128.setMaximumSize(QSize(40, 40))
        self.label_128.setFont(font4)
        self.label_128.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_128.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_128, 8, 5, 1, 1)

        self.label_49 = QLabel(self.a_e_result_screen)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 40))
        self.label_49.setMaximumSize(QSize(16777215, 40))
        self.label_49.setFont(font4)
        self.label_49.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_49, 2, 0, 1, 1)

        self.h_ae = QLabel(self.a_e_result_screen)
        self.h_ae.setObjectName(u"h_ae")
        self.h_ae.setMinimumSize(QSize(150, 30))
        self.h_ae.setMaximumSize(QSize(150, 30))
        self.h_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.h_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.h_ae, 6, 1, 1, 1)

        self.label_114 = QLabel(self.a_e_result_screen)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(0, 40))
        self.label_114.setMaximumSize(QSize(16777215, 40))
        self.label_114.setFont(font4)
        self.label_114.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_114.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_114, 12, 0, 1, 1)

        self.label_113 = QLabel(self.a_e_result_screen)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(0, 40))
        self.label_113.setMaximumSize(QSize(16777215, 40))
        self.label_113.setFont(font4)
        self.label_113.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_113.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_113, 10, 0, 1, 1)

        self.label_131 = QLabel(self.a_e_result_screen)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(40, 40))
        self.label_131.setMaximumSize(QSize(40, 40))
        self.label_131.setFont(font4)
        self.label_131.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_131.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_131, 4, 5, 1, 1)

        self.gfa_ae = QLabel(self.a_e_result_screen)
        self.gfa_ae.setObjectName(u"gfa_ae")
        self.gfa_ae.setMinimumSize(QSize(150, 30))
        self.gfa_ae.setMaximumSize(QSize(150, 30))
        self.gfa_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.gfa_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.gfa_ae, 4, 4, 1, 1)

        self.label_117 = QLabel(self.a_e_result_screen)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(0, 40))
        self.label_117.setMaximumSize(QSize(16777215, 40))
        self.label_117.setFont(font4)
        self.label_117.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_117.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_117, 8, 0, 1, 1)

        self.label_84 = QLabel(self.a_e_result_screen)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(0, 40))
        self.label_84.setMaximumSize(QSize(16777215, 40))
        self.label_84.setFont(font4)
        self.label_84.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_84.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_84, 6, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.label_82 = QLabel(self.a_e_result_screen)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(0, 40))
        self.label_82.setMaximumSize(QSize(16777215, 40))
        self.label_82.setFont(font4)
        self.label_82.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_82.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_82, 2, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 11, 0, 1, 1)

        self.label_50 = QLabel(self.a_e_result_screen)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(0, 40))
        self.label_50.setMaximumSize(QSize(16777215, 40))
        self.label_50.setFont(font4)
        self.label_50.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_50, 4, 0, 1, 1)

        self.gfp_ae = QLabel(self.a_e_result_screen)
        self.gfp_ae.setObjectName(u"gfp_ae")
        self.gfp_ae.setMinimumSize(QSize(150, 30))
        self.gfp_ae.setMaximumSize(QSize(150, 30))
        self.gfp_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.gfp_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.gfp_ae, 2, 4, 1, 1)

        self.label_87 = QLabel(self.a_e_result_screen)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(0, 40))
        self.label_87.setMaximumSize(QSize(16777215, 40))
        self.label_87.setFont(font4)
        self.label_87.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_87.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_87, 12, 3, 1, 1)

        self.vp_ae = QLabel(self.a_e_result_screen)
        self.vp_ae.setObjectName(u"vp_ae")
        self.vp_ae.setMinimumSize(QSize(150, 30))
        self.vp_ae.setMaximumSize(QSize(150, 30))
        self.vp_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.vp_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.vp_ae, 12, 1, 1, 1)

        self.mu_ae = QLabel(self.a_e_result_screen)
        self.mu_ae.setObjectName(u"mu_ae")
        self.mu_ae.setMinimumSize(QSize(150, 30))
        self.mu_ae.setMaximumSize(QSize(150, 30))
        self.mu_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.mu_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mu_ae, 4, 1, 1, 1)

        self.label_129 = QLabel(self.a_e_result_screen)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(40, 40))
        self.label_129.setMaximumSize(QSize(40, 40))
        self.label_129.setFont(font4)
        self.label_129.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_129, 10, 5, 1, 1)

        self.label_119 = QLabel(self.a_e_result_screen)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(40, 40))
        self.label_119.setMaximumSize(QSize(40, 40))
        self.label_119.setFont(font4)
        self.label_119.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_119.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_119, 2, 2, 1, 1)

        self.T_ae = QLabel(self.a_e_result_screen)
        self.T_ae.setObjectName(u"T_ae")
        self.T_ae.setMinimumSize(QSize(150, 30))
        self.T_ae.setMaximumSize(QSize(150, 30))
        self.T_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.T_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_ae, 8, 1, 1, 1)

        self.escvp_ae = QLabel(self.a_e_result_screen)
        self.escvp_ae.setObjectName(u"escvp_ae")
        self.escvp_ae.setMinimumSize(QSize(150, 30))
        self.escvp_ae.setMaximumSize(QSize(150, 30))
        self.escvp_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.escvp_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.escvp_ae, 10, 4, 1, 1)

        self.label_121 = QLabel(self.a_e_result_screen)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(40, 40))
        self.label_121.setMaximumSize(QSize(40, 40))
        self.label_121.setFont(font4)
        self.label_121.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_121.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_121, 6, 2, 1, 1)

        self.vlatus_ae = QLabel(self.a_e_result_screen)
        self.vlatus_ae.setObjectName(u"vlatus_ae")
        self.vlatus_ae.setMinimumSize(QSize(150, 30))
        self.vlatus_ae.setMaximumSize(QSize(150, 30))
        self.vlatus_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.vlatus_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.vlatus_ae, 8, 4, 1, 1)

        self.n_ae = QLabel(self.a_e_result_screen)
        self.n_ae.setObjectName(u"n_ae")
        self.n_ae.setMinimumSize(QSize(150, 30))
        self.n_ae.setMaximumSize(QSize(150, 30))
        self.n_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.n_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.n_ae, 10, 1, 1, 1)

        self.label_130 = QLabel(self.a_e_result_screen)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(40, 40))
        self.label_130.setMaximumSize(QSize(40, 40))
        self.label_130.setFont(font4)
        self.label_130.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_130, 2, 5, 1, 1)

        self.label_83 = QLabel(self.a_e_result_screen)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(0, 40))
        self.label_83.setMaximumSize(QSize(16777215, 40))
        self.label_83.setFont(font4)
        self.label_83.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_83, 4, 3, 1, 1)

        self.label_127 = QLabel(self.a_e_result_screen)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(40, 40))
        self.label_127.setMaximumSize(QSize(40, 40))
        self.label_127.setFont(font4)
        self.label_127.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_127, 6, 5, 1, 1)

        self.label_22 = QLabel(self.a_e_result_screen)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 40))
        self.label_22.setMaximumSize(QSize(16777215, 40))
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1)

        self.va_ae = QLabel(self.a_e_result_screen)
        self.va_ae.setObjectName(u"va_ae")
        self.va_ae.setMinimumSize(QSize(150, 30))
        self.va_ae.setMaximumSize(QSize(150, 30))
        self.va_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.va_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.va_ae, 0, 4, 1, 1)

        self.escva_ae = QLabel(self.a_e_result_screen)
        self.escva_ae.setObjectName(u"escva_ae")
        self.escva_ae.setMinimumSize(QSize(150, 30))
        self.escva_ae.setMaximumSize(QSize(150, 30))
        self.escva_ae.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 4px solid rgb(84, 84, 197);\n"
"	font: 10pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.escva_ae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.escva_ae, 12, 4, 1, 1)

        self.label_85 = QLabel(self.a_e_result_screen)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(0, 40))
        self.label_85.setMaximumSize(QSize(16777215, 40))
        self.label_85.setFont(font4)
        self.label_85.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_85, 8, 3, 1, 1)

        self.label_126 = QLabel(self.a_e_result_screen)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(40, 40))
        self.label_126.setMaximumSize(QSize(40, 40))
        self.label_126.setFont(font4)
        self.label_126.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_126, 0, 5, 1, 1)

        self.label_124 = QLabel(self.a_e_result_screen)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(40, 40))
        self.label_124.setMaximumSize(QSize(40, 40))
        self.label_124.setFont(font4)
        self.label_124.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_124.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_124, 10, 2, 1, 1)


        self.verticalLayout_26.addLayout(self.gridLayout)

        self.VPCO_output_stack.addWidget(self.a_e_result_screen)
        self.ra_rp_result_screen = QWidget()
        self.ra_rp_result_screen.setObjectName(u"ra_rp_result_screen")
        self.label_241 = QLabel(self.ra_rp_result_screen)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setGeometry(QRect(500, 300, 321, 41))
        self.label_241.setFont(font9)
        self.label_241.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_241.setAlignment(Qt.AlignCenter)
        self.label_242 = QLabel(self.ra_rp_result_screen)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setGeometry(QRect(980, 230, 47, 41))
        self.label_242.setFont(font9)
        self.label_242.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_242.setAlignment(Qt.AlignCenter)
        self.label_243 = QLabel(self.ra_rp_result_screen)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setGeometry(QRect(500, 90, 321, 41))
        self.label_243.setFont(font9)
        self.label_243.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_243.setAlignment(Qt.AlignCenter)
        self.label_244 = QLabel(self.ra_rp_result_screen)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setGeometry(QRect(500, 230, 321, 41))
        self.label_244.setFont(font9)
        self.label_244.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_244.setAlignment(Qt.AlignCenter)
        self.escvp_rarp = QLabel(self.ra_rp_result_screen)
        self.escvp_rarp.setObjectName(u"escvp_rarp")
        self.escvp_rarp.setGeometry(QRect(860, 370, 121, 41))
        self.escvp_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_246 = QLabel(self.ra_rp_result_screen)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setGeometry(QRect(440, 370, 47, 41))
        self.label_246.setFont(font9)
        self.label_246.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_246.setAlignment(Qt.AlignCenter)
        self.gfp_rarp = QLabel(self.ra_rp_result_screen)
        self.gfp_rarp.setObjectName(u"gfp_rarp")
        self.gfp_rarp.setGeometry(QRect(860, 92, 121, 41))
        self.gfp_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_248 = QLabel(self.ra_rp_result_screen)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setGeometry(QRect(450, 230, 47, 41))
        self.label_248.setFont(font9)
        self.label_248.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_248.setAlignment(Qt.AlignCenter)
        self.label_249 = QLabel(self.ra_rp_result_screen)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setGeometry(QRect(980, 370, 47, 41))
        self.label_249.setFont(font9)
        self.label_249.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_249.setAlignment(Qt.AlignCenter)
        self.label_250 = QLabel(self.ra_rp_result_screen)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setGeometry(QRect(-30, 450, 321, 21))
        self.label_250.setFont(font9)
        self.label_250.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_250.setAlignment(Qt.AlignCenter)
        self.label_251 = QLabel(self.ra_rp_result_screen)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setGeometry(QRect(-30, 240, 321, 21))
        self.label_251.setFont(font9)
        self.label_251.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_251.setAlignment(Qt.AlignCenter)
        self.vlatus_rarp = QLabel(self.ra_rp_result_screen)
        self.vlatus_rarp.setObjectName(u"vlatus_rarp")
        self.vlatus_rarp.setGeometry(QRect(860, 300, 121, 41))
        self.vlatus_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.escva_rarp = QLabel(self.ra_rp_result_screen)
        self.escva_rarp.setObjectName(u"escva_rarp")
        self.escva_rarp.setGeometry(QRect(860, 440, 121, 41))
        self.escva_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_254 = QLabel(self.ra_rp_result_screen)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setGeometry(QRect(-30, 310, 321, 21))
        self.label_254.setFont(font9)
        self.label_254.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_254.setAlignment(Qt.AlignCenter)
        self.e_rarp = QLabel(self.ra_rp_result_screen)
        self.e_rarp.setObjectName(u"e_rarp")
        self.e_rarp.setGeometry(QRect(310, 90, 121, 41))
        self.e_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.h_rarp = QLabel(self.ra_rp_result_screen)
        self.h_rarp.setObjectName(u"h_rarp")
        self.h_rarp.setGeometry(QRect(310, 228, 121, 41))
        self.h_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_257 = QLabel(self.ra_rp_result_screen)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setGeometry(QRect(980, 160, 47, 41))
        self.label_257.setFont(font9)
        self.label_257.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_257.setAlignment(Qt.AlignCenter)
        self.vp_rarp = QLabel(self.ra_rp_result_screen)
        self.vp_rarp.setObjectName(u"vp_rarp")
        self.vp_rarp.setGeometry(QRect(310, 438, 121, 41))
        self.vp_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_259 = QLabel(self.ra_rp_result_screen)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setGeometry(QRect(-30, 30, 321, 21))
        self.label_259.setFont(font9)
        self.label_259.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_259.setAlignment(Qt.AlignCenter)
        self.T_rarp = QLabel(self.ra_rp_result_screen)
        self.T_rarp.setObjectName(u"T_rarp")
        self.T_rarp.setGeometry(QRect(310, 300, 121, 41))
        self.T_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.p_rarp = QLabel(self.ra_rp_result_screen)
        self.p_rarp.setObjectName(u"p_rarp")
        self.p_rarp.setGeometry(QRect(860, 230, 121, 41))
        self.p_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.gfa_rarp = QLabel(self.ra_rp_result_screen)
        self.gfa_rarp.setObjectName(u"gfa_rarp")
        self.gfa_rarp.setGeometry(QRect(860, 162, 121, 41))
        self.gfa_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_263 = QLabel(self.ra_rp_result_screen)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setGeometry(QRect(980, 90, 47, 41))
        self.label_263.setFont(font9)
        self.label_263.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_263.setAlignment(Qt.AlignCenter)
        self.va_rarp = QLabel(self.ra_rp_result_screen)
        self.va_rarp.setObjectName(u"va_rarp")
        self.va_rarp.setGeometry(QRect(860, 24, 121, 41))
        self.va_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_265 = QLabel(self.ra_rp_result_screen)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setGeometry(QRect(0, 0, 1051, 21))
        self.label_265.setFont(font9)
        self.label_265.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_265.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_266 = QLabel(self.ra_rp_result_screen)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setGeometry(QRect(980, 300, 47, 41))
        self.label_266.setFont(font9)
        self.label_266.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_266.setAlignment(Qt.AlignCenter)
        self.a_rarp = QLabel(self.ra_rp_result_screen)
        self.a_rarp.setObjectName(u"a_rarp")
        self.a_rarp.setGeometry(QRect(310, 22, 121, 41))
        self.a_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"	\n"
"	\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_268 = QLabel(self.ra_rp_result_screen)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setGeometry(QRect(440, 20, 47, 41))
        self.label_268.setFont(font9)
        self.label_268.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_268.setAlignment(Qt.AlignCenter)
        self.label_269 = QLabel(self.ra_rp_result_screen)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setGeometry(QRect(440, 440, 47, 41))
        self.label_269.setFont(font9)
        self.label_269.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_269.setAlignment(Qt.AlignCenter)
        self.mu_rarp = QLabel(self.ra_rp_result_screen)
        self.mu_rarp.setObjectName(u"mu_rarp")
        self.mu_rarp.setGeometry(QRect(310, 160, 121, 41))
        self.mu_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_271 = QLabel(self.ra_rp_result_screen)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setGeometry(QRect(440, 300, 47, 41))
        self.label_271.setFont(font9)
        self.label_271.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_271.setAlignment(Qt.AlignCenter)
        self.label_272 = QLabel(self.ra_rp_result_screen)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setGeometry(QRect(-30, 380, 321, 21))
        self.label_272.setFont(font9)
        self.label_272.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_272.setAlignment(Qt.AlignCenter)
        self.label_274 = QLabel(self.ra_rp_result_screen)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setGeometry(QRect(500, 160, 321, 41))
        self.label_274.setFont(font9)
        self.label_274.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_274.setAlignment(Qt.AlignCenter)
        self.label_275 = QLabel(self.ra_rp_result_screen)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setGeometry(QRect(980, 440, 47, 41))
        self.label_275.setFont(font9)
        self.label_275.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_275.setAlignment(Qt.AlignCenter)
        self.label_276 = QLabel(self.ra_rp_result_screen)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setGeometry(QRect(-30, 170, 321, 21))
        self.label_276.setFont(font9)
        self.label_276.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_276.setAlignment(Qt.AlignCenter)
        self.label_277 = QLabel(self.ra_rp_result_screen)
        self.label_277.setObjectName(u"label_277")
        self.label_277.setGeometry(QRect(980, 20, 47, 41))
        self.label_277.setFont(font9)
        self.label_277.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_277.setAlignment(Qt.AlignCenter)
        self.n_rarp = QLabel(self.ra_rp_result_screen)
        self.n_rarp.setObjectName(u"n_rarp")
        self.n_rarp.setGeometry(QRect(310, 370, 121, 41))
        self.n_rarp.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_279 = QLabel(self.ra_rp_result_screen)
        self.label_279.setObjectName(u"label_279")
        self.label_279.setGeometry(QRect(500, 440, 321, 41))
        self.label_279.setFont(font9)
        self.label_279.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_279.setAlignment(Qt.AlignCenter)
        self.label_280 = QLabel(self.ra_rp_result_screen)
        self.label_280.setObjectName(u"label_280")
        self.label_280.setGeometry(QRect(500, 20, 321, 41))
        self.label_280.setFont(font9)
        self.label_280.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_280.setAlignment(Qt.AlignCenter)
        self.label_281 = QLabel(self.ra_rp_result_screen)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setGeometry(QRect(440, 160, 47, 41))
        self.label_281.setFont(font9)
        self.label_281.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_281.setAlignment(Qt.AlignCenter)
        self.label_282 = QLabel(self.ra_rp_result_screen)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setGeometry(QRect(500, 370, 321, 41))
        self.label_282.setFont(font9)
        self.label_282.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_282.setAlignment(Qt.AlignCenter)
        self.label_283 = QLabel(self.ra_rp_result_screen)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setGeometry(QRect(-30, 100, 331, 21))
        self.label_283.setFont(font9)
        self.label_283.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_283.setAlignment(Qt.AlignCenter)
        self.type_of_input_toggle_2 = QComboBox(self.ra_rp_result_screen)
        self.type_of_input_toggle_2.addItem("")
        self.type_of_input_toggle_2.addItem("")
        self.type_of_input_toggle_2.addItem("")
        self.type_of_input_toggle_2.addItem("")
        self.type_of_input_toggle_2.setObjectName(u"type_of_input_toggle_2")
        self.type_of_input_toggle_2.setGeometry(QRect(170, 370, 77, 26))
        self.type_of_input_toggle_2.setMinimumSize(QSize(0, 20))
        self.type_of_input_toggle_2.setMaximumSize(QSize(100, 30))
        self.type_of_input_toggle_2.setLayoutDirection(Qt.LeftToRight)
        self.type_of_input_toggle_2.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	\n"
"	border: 3px solid rgb(34, 14, 36);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 10px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::drop-down{\n"
"	border-width:2px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(UI_Functions/Resources/down_chavron.jpg);\n"
"	\n"
"}")
        self.type_of_input_toggle_2.setEditable(False)
        self.frame_43 = QFrame(self.ra_rp_result_screen)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(100, 110, 100, 100))
        self.frame_43.setMinimumSize(QSize(100, 100))
        self.frame_43.setMaximumSize(QSize(100, 100))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.VPCO_output_stack.addWidget(self.ra_rp_result_screen)
        self.r_v_gamma_result_screen = QWidget()
        self.r_v_gamma_result_screen.setObjectName(u"r_v_gamma_result_screen")
        self.label_273 = QLabel(self.r_v_gamma_result_screen)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setGeometry(QRect(500, 322, 321, 41))
        self.label_273.setFont(font9)
        self.label_273.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_273.setAlignment(Qt.AlignCenter)
        self.label_284 = QLabel(self.r_v_gamma_result_screen)
        self.label_284.setObjectName(u"label_284")
        self.label_284.setGeometry(QRect(980, 262, 47, 41))
        self.label_284.setFont(font9)
        self.label_284.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_284.setAlignment(Qt.AlignCenter)
        self.label_285 = QLabel(self.r_v_gamma_result_screen)
        self.label_285.setObjectName(u"label_285")
        self.label_285.setGeometry(QRect(500, 142, 321, 41))
        self.label_285.setFont(font9)
        self.label_285.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_285.setAlignment(Qt.AlignCenter)
        self.label_286 = QLabel(self.r_v_gamma_result_screen)
        self.label_286.setObjectName(u"label_286")
        self.label_286.setGeometry(QRect(500, 262, 321, 41))
        self.label_286.setFont(font9)
        self.label_286.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_286.setAlignment(Qt.AlignCenter)
        self.vlatus_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.vlatus_rvgamma.setObjectName(u"vlatus_rvgamma")
        self.vlatus_rvgamma.setGeometry(QRect(840, 322, 121, 41))
        self.vlatus_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_288 = QLabel(self.r_v_gamma_result_screen)
        self.label_288.setObjectName(u"label_288")
        self.label_288.setGeometry(QRect(440, 382, 47, 41))
        self.label_288.setFont(font9)
        self.label_288.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_288.setAlignment(Qt.AlignCenter)
        self.va_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.va_rvgamma.setObjectName(u"va_rvgamma")
        self.va_rvgamma.setGeometry(QRect(840, 84, 121, 41))
        self.va_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_290 = QLabel(self.r_v_gamma_result_screen)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setGeometry(QRect(440, 262, 47, 41))
        self.label_290.setFont(font9)
        self.label_290.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_290.setAlignment(Qt.AlignCenter)
        self.label_291 = QLabel(self.r_v_gamma_result_screen)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setGeometry(QRect(980, 382, 47, 41))
        self.label_291.setFont(font9)
        self.label_291.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_291.setAlignment(Qt.AlignCenter)
        self.label_292 = QLabel(self.r_v_gamma_result_screen)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setGeometry(QRect(-30, 452, 321, 21))
        self.label_292.setFont(font9)
        self.label_292.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_292.setAlignment(Qt.AlignCenter)
        self.label_293 = QLabel(self.r_v_gamma_result_screen)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setGeometry(QRect(-30, 272, 321, 21))
        self.label_293.setFont(font9)
        self.label_293.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_293.setAlignment(Qt.AlignCenter)
        self.p_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.p_rvgamma.setObjectName(u"p_rvgamma")
        self.p_rvgamma.setGeometry(QRect(840, 262, 121, 41))
        self.p_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.escvp_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.escvp_rvgamma.setObjectName(u"escvp_rvgamma")
        self.escvp_rvgamma.setGeometry(QRect(840, 382, 121, 41))
        self.escvp_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_296 = QLabel(self.r_v_gamma_result_screen)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setGeometry(QRect(-30, 332, 321, 21))
        self.label_296.setFont(font9)
        self.label_296.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_296.setAlignment(Qt.AlignCenter)
        self.rp_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.rp_rvgamma.setObjectName(u"rp_rvgamma")
        self.rp_rvgamma.setGeometry(QRect(310, 82, 121, 41))
        self.rp_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.mu_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.mu_rvgamma.setObjectName(u"mu_rvgamma")
        self.mu_rvgamma.setGeometry(QRect(310, 200, 121, 41))
        self.mu_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_299 = QLabel(self.r_v_gamma_result_screen)
        self.label_299.setObjectName(u"label_299")
        self.label_299.setGeometry(QRect(980, 202, 47, 41))
        self.label_299.setFont(font9)
        self.label_299.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_299.setAlignment(Qt.AlignCenter)
        self.n_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.n_rvgamma.setObjectName(u"n_rvgamma")
        self.n_rvgamma.setGeometry(QRect(310, 380, 121, 41))
        self.n_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_301 = QLabel(self.r_v_gamma_result_screen)
        self.label_301.setObjectName(u"label_301")
        self.label_301.setGeometry(QRect(-30, 92, 321, 21))
        self.label_301.setFont(font9)
        self.label_301.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_301.setAlignment(Qt.AlignCenter)
        self.h_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.h_rvgamma.setObjectName(u"h_rvgamma")
        self.h_rvgamma.setGeometry(QRect(310, 262, 121, 41))
        self.h_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.gfa_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.gfa_rvgamma.setObjectName(u"gfa_rvgamma")
        self.gfa_rvgamma.setGeometry(QRect(840, 202, 121, 41))
        self.gfa_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.gfp_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.gfp_rvgamma.setObjectName(u"gfp_rvgamma")
        self.gfp_rvgamma.setGeometry(QRect(840, 144, 121, 41))
        self.gfp_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_305 = QLabel(self.r_v_gamma_result_screen)
        self.label_305.setObjectName(u"label_305")
        self.label_305.setGeometry(QRect(980, 142, 47, 41))
        self.label_305.setFont(font9)
        self.label_305.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_305.setAlignment(Qt.AlignCenter)
        self.e_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.e_rvgamma.setObjectName(u"e_rvgamma")
        self.e_rvgamma.setGeometry(QRect(840, 26, 121, 41))
        self.e_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_307 = QLabel(self.r_v_gamma_result_screen)
        self.label_307.setObjectName(u"label_307")
        self.label_307.setGeometry(QRect(0, 0, 1051, 21))
        self.label_307.setFont(font9)
        self.label_307.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_307.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_308 = QLabel(self.r_v_gamma_result_screen)
        self.label_308.setObjectName(u"label_308")
        self.label_308.setGeometry(QRect(980, 322, 47, 41))
        self.label_308.setFont(font9)
        self.label_308.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_308.setAlignment(Qt.AlignCenter)
        self.a_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.a_rvgamma.setObjectName(u"a_rvgamma")
        self.a_rvgamma.setGeometry(QRect(310, 24, 121, 41))
        self.a_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_310 = QLabel(self.r_v_gamma_result_screen)
        self.label_310.setObjectName(u"label_310")
        self.label_310.setGeometry(QRect(440, 82, 47, 41))
        self.label_310.setFont(font9)
        self.label_310.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_310.setAlignment(Qt.AlignCenter)
        self.label_311 = QLabel(self.r_v_gamma_result_screen)
        self.label_311.setObjectName(u"label_311")
        self.label_311.setGeometry(QRect(440, 442, 47, 41))
        self.label_311.setFont(font9)
        self.label_311.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_311.setAlignment(Qt.AlignCenter)
        self.ra_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.ra_rvgamma.setObjectName(u"ra_rvgamma")
        self.ra_rvgamma.setGeometry(QRect(310, 142, 121, 41))
        self.ra_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_313 = QLabel(self.r_v_gamma_result_screen)
        self.label_313.setObjectName(u"label_313")
        self.label_313.setGeometry(QRect(440, 322, 47, 41))
        self.label_313.setFont(font9)
        self.label_313.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_313.setAlignment(Qt.AlignCenter)
        self.label_314 = QLabel(self.r_v_gamma_result_screen)
        self.label_314.setObjectName(u"label_314")
        self.label_314.setGeometry(QRect(-30, 392, 321, 21))
        self.label_314.setFont(font9)
        self.label_314.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_314.setAlignment(Qt.AlignCenter)
        self.label_315 = QLabel(self.r_v_gamma_result_screen)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setGeometry(QRect(440, 142, 47, 41))
        self.label_315.setFont(font9)
        self.label_315.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_315.setAlignment(Qt.AlignCenter)
        self.label_316 = QLabel(self.r_v_gamma_result_screen)
        self.label_316.setObjectName(u"label_316")
        self.label_316.setGeometry(QRect(500, 202, 321, 41))
        self.label_316.setFont(font9)
        self.label_316.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_316.setAlignment(Qt.AlignCenter)
        self.label_317 = QLabel(self.r_v_gamma_result_screen)
        self.label_317.setObjectName(u"label_317")
        self.label_317.setGeometry(QRect(980, 442, 47, 41))
        self.label_317.setFont(font9)
        self.label_317.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_317.setAlignment(Qt.AlignCenter)
        self.label_318 = QLabel(self.r_v_gamma_result_screen)
        self.label_318.setObjectName(u"label_318")
        self.label_318.setGeometry(QRect(-30, 212, 321, 21))
        self.label_318.setFont(font9)
        self.label_318.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_318.setAlignment(Qt.AlignCenter)
        self.label_319 = QLabel(self.r_v_gamma_result_screen)
        self.label_319.setObjectName(u"label_319")
        self.label_319.setGeometry(QRect(980, 82, 47, 41))
        self.label_319.setFont(font9)
        self.label_319.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_319.setAlignment(Qt.AlignCenter)
        self.T_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.T_rvgamma.setObjectName(u"T_rvgamma")
        self.T_rvgamma.setGeometry(QRect(310, 322, 121, 41))
        self.T_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_321 = QLabel(self.r_v_gamma_result_screen)
        self.label_321.setObjectName(u"label_321")
        self.label_321.setGeometry(QRect(500, 442, 321, 41))
        self.label_321.setFont(font9)
        self.label_321.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_321.setAlignment(Qt.AlignCenter)
        self.label_322 = QLabel(self.r_v_gamma_result_screen)
        self.label_322.setObjectName(u"label_322")
        self.label_322.setGeometry(QRect(500, 82, 321, 41))
        self.label_322.setFont(font9)
        self.label_322.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_322.setAlignment(Qt.AlignCenter)
        self.label_323 = QLabel(self.r_v_gamma_result_screen)
        self.label_323.setObjectName(u"label_323")
        self.label_323.setGeometry(QRect(440, 202, 47, 41))
        self.label_323.setFont(font9)
        self.label_323.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_323.setAlignment(Qt.AlignCenter)
        self.label_324 = QLabel(self.r_v_gamma_result_screen)
        self.label_324.setObjectName(u"label_324")
        self.label_324.setGeometry(QRect(500, 382, 321, 41))
        self.label_324.setFont(font9)
        self.label_324.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_324.setAlignment(Qt.AlignCenter)
        self.label_325 = QLabel(self.r_v_gamma_result_screen)
        self.label_325.setObjectName(u"label_325")
        self.label_325.setGeometry(QRect(-30, 152, 321, 21))
        self.label_325.setFont(font9)
        self.label_325.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_325.setAlignment(Qt.AlignCenter)
        self.escva_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.escva_rvgamma.setObjectName(u"escva_rvgamma")
        self.escva_rvgamma.setGeometry(QRect(840, 442, 121, 41))
        self.escva_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.vp_rvgamma = QLabel(self.r_v_gamma_result_screen)
        self.vp_rvgamma.setObjectName(u"vp_rvgamma")
        self.vp_rvgamma.setGeometry(QRect(310, 440, 121, 41))
        self.vp_rvgamma.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_330 = QLabel(self.r_v_gamma_result_screen)
        self.label_330.setObjectName(u"label_330")
        self.label_330.setGeometry(QRect(-30, 32, 321, 21))
        self.label_330.setFont(font9)
        self.label_330.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_330.setAlignment(Qt.AlignCenter)
        self.label_331 = QLabel(self.r_v_gamma_result_screen)
        self.label_331.setObjectName(u"label_331")
        self.label_331.setGeometry(QRect(500, 22, 321, 41))
        self.label_331.setFont(font9)
        self.label_331.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_331.setAlignment(Qt.AlignCenter)
        self.label_462 = QLabel(self.r_v_gamma_result_screen)
        self.label_462.setObjectName(u"label_462")
        self.label_462.setGeometry(QRect(440, 22, 47, 41))
        self.label_462.setFont(font9)
        self.label_462.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_462.setAlignment(Qt.AlignCenter)
        self.VPCO_output_stack.addWidget(self.r_v_gamma_result_screen)
        self.OrbitalElements_result_screen = QWidget()
        self.OrbitalElements_result_screen.setObjectName(u"OrbitalElements_result_screen")
        self.label_463 = QLabel(self.OrbitalElements_result_screen)
        self.label_463.setObjectName(u"label_463")
        self.label_463.setGeometry(QRect(500, 298, 321, 41))
        self.label_463.setFont(font9)
        self.label_463.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_463.setAlignment(Qt.AlignCenter)
        self.label_464 = QLabel(self.OrbitalElements_result_screen)
        self.label_464.setObjectName(u"label_464")
        self.label_464.setGeometry(QRect(980, 228, 47, 41))
        self.label_464.setFont(font9)
        self.label_464.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_464.setAlignment(Qt.AlignCenter)
        self.label_465 = QLabel(self.OrbitalElements_result_screen)
        self.label_465.setObjectName(u"label_465")
        self.label_465.setGeometry(QRect(500, 88, 321, 41))
        self.label_465.setFont(font9)
        self.label_465.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_465.setAlignment(Qt.AlignCenter)
        self.label_466 = QLabel(self.OrbitalElements_result_screen)
        self.label_466.setObjectName(u"label_466")
        self.label_466.setGeometry(QRect(500, 228, 321, 41))
        self.label_466.setFont(font9)
        self.label_466.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_466.setAlignment(Qt.AlignCenter)
        self.escvp_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.escvp_orbitalElements.setObjectName(u"escvp_orbitalElements")
        self.escvp_orbitalElements.setGeometry(QRect(840, 368, 121, 41))
        self.escvp_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_468 = QLabel(self.OrbitalElements_result_screen)
        self.label_468.setObjectName(u"label_468")
        self.label_468.setGeometry(QRect(440, 368, 47, 41))
        self.label_468.setFont(font9)
        self.label_468.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_468.setAlignment(Qt.AlignCenter)
        self.gfp_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.gfp_orbitalElements.setObjectName(u"gfp_orbitalElements")
        self.gfp_orbitalElements.setGeometry(QRect(840, 90, 121, 41))
        self.gfp_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_470 = QLabel(self.OrbitalElements_result_screen)
        self.label_470.setObjectName(u"label_470")
        self.label_470.setGeometry(QRect(440, 228, 47, 41))
        self.label_470.setFont(font9)
        self.label_470.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_470.setAlignment(Qt.AlignCenter)
        self.label_471 = QLabel(self.OrbitalElements_result_screen)
        self.label_471.setObjectName(u"label_471")
        self.label_471.setGeometry(QRect(980, 368, 47, 41))
        self.label_471.setFont(font9)
        self.label_471.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_471.setAlignment(Qt.AlignCenter)
        self.label_472 = QLabel(self.OrbitalElements_result_screen)
        self.label_472.setObjectName(u"label_472")
        self.label_472.setGeometry(QRect(-30, 448, 321, 21))
        self.label_472.setFont(font9)
        self.label_472.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_472.setAlignment(Qt.AlignCenter)
        self.label_473 = QLabel(self.OrbitalElements_result_screen)
        self.label_473.setObjectName(u"label_473")
        self.label_473.setGeometry(QRect(-30, 238, 321, 21))
        self.label_473.setFont(font9)
        self.label_473.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_473.setAlignment(Qt.AlignCenter)
        self.vlatus_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.vlatus_orbitalElements.setObjectName(u"vlatus_orbitalElements")
        self.vlatus_orbitalElements.setGeometry(QRect(840, 298, 121, 41))
        self.vlatus_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.escva_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.escva_orbitalElements.setObjectName(u"escva_orbitalElements")
        self.escva_orbitalElements.setGeometry(QRect(840, 438, 121, 41))
        self.escva_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_476 = QLabel(self.OrbitalElements_result_screen)
        self.label_476.setObjectName(u"label_476")
        self.label_476.setGeometry(QRect(-30, 308, 321, 21))
        self.label_476.setFont(font9)
        self.label_476.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_476.setAlignment(Qt.AlignCenter)
        self.ra_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.ra_orbitalElements.setObjectName(u"ra_orbitalElements")
        self.ra_orbitalElements.setGeometry(QRect(310, 88, 121, 41))
        self.ra_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.h_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.h_orbitalElements.setObjectName(u"h_orbitalElements")
        self.h_orbitalElements.setGeometry(QRect(310, 226, 121, 41))
        self.h_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_479 = QLabel(self.OrbitalElements_result_screen)
        self.label_479.setObjectName(u"label_479")
        self.label_479.setGeometry(QRect(980, 158, 47, 41))
        self.label_479.setFont(font9)
        self.label_479.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_479.setAlignment(Qt.AlignCenter)
        self.vp_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.vp_orbitalElements.setObjectName(u"vp_orbitalElements")
        self.vp_orbitalElements.setGeometry(QRect(310, 436, 121, 41))
        self.vp_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_481 = QLabel(self.OrbitalElements_result_screen)
        self.label_481.setObjectName(u"label_481")
        self.label_481.setGeometry(QRect(-30, 28, 321, 21))
        self.label_481.setFont(font9)
        self.label_481.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_481.setAlignment(Qt.AlignCenter)
        self.T_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.T_orbitalElements.setObjectName(u"T_orbitalElements")
        self.T_orbitalElements.setGeometry(QRect(310, 298, 121, 41))
        self.T_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.p_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.p_orbitalElements.setObjectName(u"p_orbitalElements")
        self.p_orbitalElements.setGeometry(QRect(840, 228, 121, 41))
        self.p_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.gfa_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.gfa_orbitalElements.setObjectName(u"gfa_orbitalElements")
        self.gfa_orbitalElements.setGeometry(QRect(840, 160, 121, 41))
        self.gfa_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_485 = QLabel(self.OrbitalElements_result_screen)
        self.label_485.setObjectName(u"label_485")
        self.label_485.setGeometry(QRect(980, 88, 47, 41))
        self.label_485.setFont(font9)
        self.label_485.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_485.setAlignment(Qt.AlignCenter)
        self.va_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.va_orbitalElements.setObjectName(u"va_orbitalElements")
        self.va_orbitalElements.setGeometry(QRect(840, 22, 121, 41))
        self.va_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_487 = QLabel(self.OrbitalElements_result_screen)
        self.label_487.setObjectName(u"label_487")
        self.label_487.setGeometry(QRect(0, 0, 1051, 21))
        self.label_487.setFont(font9)
        self.label_487.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_487.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_488 = QLabel(self.OrbitalElements_result_screen)
        self.label_488.setObjectName(u"label_488")
        self.label_488.setGeometry(QRect(980, 298, 47, 41))
        self.label_488.setFont(font9)
        self.label_488.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_488.setAlignment(Qt.AlignCenter)
        self.rp_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.rp_orbitalElements.setObjectName(u"rp_orbitalElements")
        self.rp_orbitalElements.setGeometry(QRect(310, 20, 121, 41))
        self.rp_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_490 = QLabel(self.OrbitalElements_result_screen)
        self.label_490.setObjectName(u"label_490")
        self.label_490.setGeometry(QRect(440, 438, 47, 41))
        self.label_490.setFont(font9)
        self.label_490.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_490.setAlignment(Qt.AlignCenter)
        self.mu_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.mu_orbitalElements.setObjectName(u"mu_orbitalElements")
        self.mu_orbitalElements.setGeometry(QRect(310, 158, 121, 41))
        self.mu_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_492 = QLabel(self.OrbitalElements_result_screen)
        self.label_492.setObjectName(u"label_492")
        self.label_492.setGeometry(QRect(440, 298, 47, 41))
        self.label_492.setFont(font9)
        self.label_492.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_492.setAlignment(Qt.AlignCenter)
        self.label_493 = QLabel(self.OrbitalElements_result_screen)
        self.label_493.setObjectName(u"label_493")
        self.label_493.setGeometry(QRect(-30, 378, 321, 21))
        self.label_493.setFont(font9)
        self.label_493.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_493.setAlignment(Qt.AlignCenter)
        self.label_494 = QLabel(self.OrbitalElements_result_screen)
        self.label_494.setObjectName(u"label_494")
        self.label_494.setGeometry(QRect(440, 88, 47, 41))
        self.label_494.setFont(font9)
        self.label_494.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_494.setAlignment(Qt.AlignCenter)
        self.label_495 = QLabel(self.OrbitalElements_result_screen)
        self.label_495.setObjectName(u"label_495")
        self.label_495.setGeometry(QRect(500, 158, 321, 41))
        self.label_495.setFont(font9)
        self.label_495.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_495.setAlignment(Qt.AlignCenter)
        self.label_496 = QLabel(self.OrbitalElements_result_screen)
        self.label_496.setObjectName(u"label_496")
        self.label_496.setGeometry(QRect(-30, 168, 321, 21))
        self.label_496.setFont(font9)
        self.label_496.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_496.setAlignment(Qt.AlignCenter)
        self.label_497 = QLabel(self.OrbitalElements_result_screen)
        self.label_497.setObjectName(u"label_497")
        self.label_497.setGeometry(QRect(980, 438, 47, 41))
        self.label_497.setFont(font9)
        self.label_497.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_497.setAlignment(Qt.AlignCenter)
        self.label_498 = QLabel(self.OrbitalElements_result_screen)
        self.label_498.setObjectName(u"label_498")
        self.label_498.setGeometry(QRect(980, 18, 47, 41))
        self.label_498.setFont(font9)
        self.label_498.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_498.setAlignment(Qt.AlignCenter)
        self.n_orbitalElements = QLabel(self.OrbitalElements_result_screen)
        self.n_orbitalElements.setObjectName(u"n_orbitalElements")
        self.n_orbitalElements.setGeometry(QRect(310, 368, 121, 41))
        self.n_orbitalElements.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_500 = QLabel(self.OrbitalElements_result_screen)
        self.label_500.setObjectName(u"label_500")
        self.label_500.setGeometry(QRect(500, 438, 321, 41))
        self.label_500.setFont(font9)
        self.label_500.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_500.setAlignment(Qt.AlignCenter)
        self.label_501 = QLabel(self.OrbitalElements_result_screen)
        self.label_501.setObjectName(u"label_501")
        self.label_501.setGeometry(QRect(500, 18, 321, 41))
        self.label_501.setFont(font9)
        self.label_501.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_501.setAlignment(Qt.AlignCenter)
        self.label_502 = QLabel(self.OrbitalElements_result_screen)
        self.label_502.setObjectName(u"label_502")
        self.label_502.setGeometry(QRect(440, 158, 47, 41))
        self.label_502.setFont(font9)
        self.label_502.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_502.setAlignment(Qt.AlignCenter)
        self.label_503 = QLabel(self.OrbitalElements_result_screen)
        self.label_503.setObjectName(u"label_503")
        self.label_503.setGeometry(QRect(-30, 98, 331, 21))
        self.label_503.setFont(font9)
        self.label_503.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_503.setAlignment(Qt.AlignCenter)
        self.label_504 = QLabel(self.OrbitalElements_result_screen)
        self.label_504.setObjectName(u"label_504")
        self.label_504.setGeometry(QRect(500, 368, 321, 41))
        self.label_504.setFont(font9)
        self.label_504.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_504.setAlignment(Qt.AlignCenter)
        self.label_499 = QLabel(self.OrbitalElements_result_screen)
        self.label_499.setObjectName(u"label_499")
        self.label_499.setGeometry(QRect(440, 18, 47, 41))
        self.label_499.setFont(font9)
        self.label_499.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_499.setAlignment(Qt.AlignCenter)
        self.VPCO_output_stack.addWidget(self.OrbitalElements_result_screen)
        self.StateVector_result_screen = QWidget()
        self.StateVector_result_screen.setObjectName(u"StateVector_result_screen")
        self.label_505 = QLabel(self.StateVector_result_screen)
        self.label_505.setObjectName(u"label_505")
        self.label_505.setGeometry(QRect(-30, 330, 321, 21))
        self.label_505.setFont(font9)
        self.label_505.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_505.setAlignment(Qt.AlignCenter)
        self.rp_stateVector = QLabel(self.StateVector_result_screen)
        self.rp_stateVector.setObjectName(u"rp_stateVector")
        self.rp_stateVector.setGeometry(QRect(310, 80, 121, 41))
        self.rp_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.gfa_stateVector = QLabel(self.StateVector_result_screen)
        self.gfa_stateVector.setObjectName(u"gfa_stateVector")
        self.gfa_stateVector.setGeometry(QRect(840, 200, 121, 41))
        self.gfa_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.escva_stateVector = QLabel(self.StateVector_result_screen)
        self.escva_stateVector.setObjectName(u"escva_stateVector")
        self.escva_stateVector.setGeometry(QRect(840, 440, 121, 41))
        self.escva_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_509 = QLabel(self.StateVector_result_screen)
        self.label_509.setObjectName(u"label_509")
        self.label_509.setGeometry(QRect(-30, 30, 321, 21))
        self.label_509.setFont(font9)
        self.label_509.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_509.setAlignment(Qt.AlignCenter)
        self.label_510 = QLabel(self.StateVector_result_screen)
        self.label_510.setObjectName(u"label_510")
        self.label_510.setGeometry(QRect(440, 380, 47, 41))
        self.label_510.setFont(font9)
        self.label_510.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_510.setAlignment(Qt.AlignCenter)
        self.label_511 = QLabel(self.StateVector_result_screen)
        self.label_511.setObjectName(u"label_511")
        self.label_511.setGeometry(QRect(-30, 90, 321, 21))
        self.label_511.setFont(font9)
        self.label_511.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_511.setAlignment(Qt.AlignCenter)
        self.mu_stateVector = QLabel(self.StateVector_result_screen)
        self.mu_stateVector.setObjectName(u"mu_stateVector")
        self.mu_stateVector.setGeometry(QRect(310, 198, 121, 41))
        self.mu_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.escvp_stateVector = QLabel(self.StateVector_result_screen)
        self.escvp_stateVector.setObjectName(u"escvp_stateVector")
        self.escvp_stateVector.setGeometry(QRect(840, 380, 121, 41))
        self.escvp_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.ra_stateVector = QLabel(self.StateVector_result_screen)
        self.ra_stateVector.setObjectName(u"ra_stateVector")
        self.ra_stateVector.setGeometry(QRect(310, 140, 121, 41))
        self.ra_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_515 = QLabel(self.StateVector_result_screen)
        self.label_515.setObjectName(u"label_515")
        self.label_515.setGeometry(QRect(980, 200, 47, 41))
        self.label_515.setFont(font9)
        self.label_515.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_515.setAlignment(Qt.AlignCenter)
        self.label_516 = QLabel(self.StateVector_result_screen)
        self.label_516.setObjectName(u"label_516")
        self.label_516.setGeometry(QRect(-30, 450, 321, 21))
        self.label_516.setFont(font9)
        self.label_516.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_516.setAlignment(Qt.AlignCenter)
        self.label_517 = QLabel(self.StateVector_result_screen)
        self.label_517.setObjectName(u"label_517")
        self.label_517.setGeometry(QRect(440, 80, 47, 41))
        self.label_517.setFont(font9)
        self.label_517.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_517.setAlignment(Qt.AlignCenter)
        self.label_518 = QLabel(self.StateVector_result_screen)
        self.label_518.setObjectName(u"label_518")
        self.label_518.setGeometry(QRect(-30, 150, 321, 21))
        self.label_518.setFont(font9)
        self.label_518.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_518.setAlignment(Qt.AlignCenter)
        self.n_stateVector = QLabel(self.StateVector_result_screen)
        self.n_stateVector.setObjectName(u"n_stateVector")
        self.n_stateVector.setGeometry(QRect(310, 378, 121, 41))
        self.n_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.e_stateVector = QLabel(self.StateVector_result_screen)
        self.e_stateVector.setObjectName(u"e_stateVector")
        self.e_stateVector.setGeometry(QRect(840, 24, 121, 41))
        self.e_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.h_stateVector = QLabel(self.StateVector_result_screen)
        self.h_stateVector.setObjectName(u"h_stateVector")
        self.h_stateVector.setGeometry(QRect(310, 260, 121, 41))
        self.h_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.vp_stateVector = QLabel(self.StateVector_result_screen)
        self.vp_stateVector.setObjectName(u"vp_stateVector")
        self.vp_stateVector.setGeometry(QRect(310, 438, 121, 41))
        self.vp_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_523 = QLabel(self.StateVector_result_screen)
        self.label_523.setObjectName(u"label_523")
        self.label_523.setGeometry(QRect(980, 380, 47, 41))
        self.label_523.setFont(font9)
        self.label_523.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_523.setAlignment(Qt.AlignCenter)
        self.p_stateVector_lbl = QLabel(self.StateVector_result_screen)
        self.p_stateVector_lbl.setObjectName(u"p_stateVector_lbl")
        self.p_stateVector_lbl.setGeometry(QRect(500, 260, 321, 41))
        self.p_stateVector_lbl.setFont(font9)
        self.p_stateVector_lbl.setStyleSheet(u"border:none;\n"
"color:white;")
        self.p_stateVector_lbl.setAlignment(Qt.AlignCenter)
        self.gfa_stateVector_lbl = QLabel(self.StateVector_result_screen)
        self.gfa_stateVector_lbl.setObjectName(u"gfa_stateVector_lbl")
        self.gfa_stateVector_lbl.setGeometry(QRect(500, 200, 321, 41))
        self.gfa_stateVector_lbl.setFont(font9)
        self.gfa_stateVector_lbl.setStyleSheet(u"border:none;\n"
"color:white;")
        self.gfa_stateVector_lbl.setAlignment(Qt.AlignCenter)
        self.escva_stateVector_lbl = QLabel(self.StateVector_result_screen)
        self.escva_stateVector_lbl.setObjectName(u"escva_stateVector_lbl")
        self.escva_stateVector_lbl.setGeometry(QRect(500, 440, 321, 41))
        self.escva_stateVector_lbl.setFont(font9)
        self.escva_stateVector_lbl.setStyleSheet(u"border:none;\n"
"color:white;")
        self.escva_stateVector_lbl.setAlignment(Qt.AlignCenter)
        self.label_527 = QLabel(self.StateVector_result_screen)
        self.label_527.setObjectName(u"label_527")
        self.label_527.setGeometry(QRect(980, 320, 47, 41))
        self.label_527.setFont(font9)
        self.label_527.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_527.setAlignment(Qt.AlignCenter)
        self.p_stateVector = QLabel(self.StateVector_result_screen)
        self.p_stateVector.setObjectName(u"p_stateVector")
        self.p_stateVector.setGeometry(QRect(840, 260, 121, 41))
        self.p_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_529 = QLabel(self.StateVector_result_screen)
        self.label_529.setObjectName(u"label_529")
        self.label_529.setGeometry(QRect(500, 20, 321, 41))
        self.label_529.setFont(font9)
        self.label_529.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_529.setAlignment(Qt.AlignCenter)
        self.label_530 = QLabel(self.StateVector_result_screen)
        self.label_530.setObjectName(u"label_530")
        self.label_530.setGeometry(QRect(980, 140, 47, 41))
        self.label_530.setFont(font9)
        self.label_530.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_530.setAlignment(Qt.AlignCenter)
        self.escvp_stateVector_lbl = QLabel(self.StateVector_result_screen)
        self.escvp_stateVector_lbl.setObjectName(u"escvp_stateVector_lbl")
        self.escvp_stateVector_lbl.setGeometry(QRect(500, 380, 321, 41))
        self.escvp_stateVector_lbl.setFont(font9)
        self.escvp_stateVector_lbl.setStyleSheet(u"border:none;\n"
"color:white;")
        self.escvp_stateVector_lbl.setAlignment(Qt.AlignCenter)
        self.vlatus_stateVector = QLabel(self.StateVector_result_screen)
        self.vlatus_stateVector.setObjectName(u"vlatus_stateVector")
        self.vlatus_stateVector.setGeometry(QRect(840, 320, 121, 41))
        self.vlatus_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_533 = QLabel(self.StateVector_result_screen)
        self.label_533.setObjectName(u"label_533")
        self.label_533.setGeometry(QRect(980, 260, 47, 41))
        self.label_533.setFont(font9)
        self.label_533.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_533.setAlignment(Qt.AlignCenter)
        self.va_stateVector_lbl = QLabel(self.StateVector_result_screen)
        self.va_stateVector_lbl.setObjectName(u"va_stateVector_lbl")
        self.va_stateVector_lbl.setGeometry(QRect(500, 80, 321, 41))
        self.va_stateVector_lbl.setFont(font9)
        self.va_stateVector_lbl.setStyleSheet(u"border:none;\n"
"color:white;")
        self.va_stateVector_lbl.setAlignment(Qt.AlignCenter)
        self.label_535 = QLabel(self.StateVector_result_screen)
        self.label_535.setObjectName(u"label_535")
        self.label_535.setGeometry(QRect(440, 140, 47, 41))
        self.label_535.setFont(font9)
        self.label_535.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_535.setAlignment(Qt.AlignCenter)
        self.gfp_stateVector = QLabel(self.StateVector_result_screen)
        self.gfp_stateVector.setObjectName(u"gfp_stateVector")
        self.gfp_stateVector.setGeometry(QRect(840, 142, 121, 41))
        self.gfp_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_537 = QLabel(self.StateVector_result_screen)
        self.label_537.setObjectName(u"label_537")
        self.label_537.setGeometry(QRect(440, 200, 47, 41))
        self.label_537.setFont(font9)
        self.label_537.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_537.setAlignment(Qt.AlignCenter)
        self.label_538 = QLabel(self.StateVector_result_screen)
        self.label_538.setObjectName(u"label_538")
        self.label_538.setGeometry(QRect(440, 320, 47, 41))
        self.label_538.setFont(font9)
        self.label_538.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_538.setAlignment(Qt.AlignCenter)
        self.T_stateVector = QLabel(self.StateVector_result_screen)
        self.T_stateVector.setObjectName(u"T_stateVector")
        self.T_stateVector.setGeometry(QRect(310, 320, 121, 41))
        self.T_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.label_540 = QLabel(self.StateVector_result_screen)
        self.label_540.setObjectName(u"label_540")
        self.label_540.setGeometry(QRect(440, 20, 47, 41))
        self.label_540.setFont(font9)
        self.label_540.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_540.setAlignment(Qt.AlignCenter)
        self.label_541 = QLabel(self.StateVector_result_screen)
        self.label_541.setObjectName(u"label_541")
        self.label_541.setGeometry(QRect(980, 440, 47, 41))
        self.label_541.setFont(font9)
        self.label_541.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_541.setAlignment(Qt.AlignCenter)
        self.label_542 = QLabel(self.StateVector_result_screen)
        self.label_542.setObjectName(u"label_542")
        self.label_542.setGeometry(QRect(440, 260, 47, 41))
        self.label_542.setFont(font9)
        self.label_542.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_542.setAlignment(Qt.AlignCenter)
        self.label_543 = QLabel(self.StateVector_result_screen)
        self.label_543.setObjectName(u"label_543")
        self.label_543.setGeometry(QRect(-30, 210, 321, 21))
        self.label_543.setFont(font9)
        self.label_543.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_543.setAlignment(Qt.AlignCenter)
        self.label_544 = QLabel(self.StateVector_result_screen)
        self.label_544.setObjectName(u"label_544")
        self.label_544.setGeometry(QRect(-30, 390, 321, 21))
        self.label_544.setFont(font9)
        self.label_544.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_544.setAlignment(Qt.AlignCenter)
        self.va_stateVector = QLabel(self.StateVector_result_screen)
        self.va_stateVector.setObjectName(u"va_stateVector")
        self.va_stateVector.setGeometry(QRect(840, 82, 121, 41))
        self.va_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.a_stateVector = QLabel(self.StateVector_result_screen)
        self.a_stateVector.setObjectName(u"a_stateVector")
        self.a_stateVector.setGeometry(QRect(310, 22, 121, 41))
        self.a_stateVector.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"\n"
"\n"
"}")
        self.gfp_stateVector_lbl = QLabel(self.StateVector_result_screen)
        self.gfp_stateVector_lbl.setObjectName(u"gfp_stateVector_lbl")
        self.gfp_stateVector_lbl.setGeometry(QRect(500, 140, 321, 41))
        self.gfp_stateVector_lbl.setFont(font9)
        self.gfp_stateVector_lbl.setStyleSheet(u"border:none;\n"
"color:white;")
        self.gfp_stateVector_lbl.setAlignment(Qt.AlignCenter)
        self.label_548 = QLabel(self.StateVector_result_screen)
        self.label_548.setObjectName(u"label_548")
        self.label_548.setGeometry(QRect(440, 440, 47, 41))
        self.label_548.setFont(font9)
        self.label_548.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_548.setAlignment(Qt.AlignCenter)
        self.vlatus_stateVector_lbl = QLabel(self.StateVector_result_screen)
        self.vlatus_stateVector_lbl.setObjectName(u"vlatus_stateVector_lbl")
        self.vlatus_stateVector_lbl.setGeometry(QRect(500, 320, 321, 41))
        self.vlatus_stateVector_lbl.setFont(font9)
        self.vlatus_stateVector_lbl.setStyleSheet(u"border:none;\n"
"color:white;")
        self.vlatus_stateVector_lbl.setAlignment(Qt.AlignCenter)
        self.label_550 = QLabel(self.StateVector_result_screen)
        self.label_550.setObjectName(u"label_550")
        self.label_550.setGeometry(QRect(0, 0, 1051, 21))
        self.label_550.setFont(font9)
        self.label_550.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_550.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_551 = QLabel(self.StateVector_result_screen)
        self.label_551.setObjectName(u"label_551")
        self.label_551.setGeometry(QRect(980, 80, 47, 41))
        self.label_551.setFont(font9)
        self.label_551.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_551.setAlignment(Qt.AlignCenter)
        self.label_552 = QLabel(self.StateVector_result_screen)
        self.label_552.setObjectName(u"label_552")
        self.label_552.setGeometry(QRect(-30, 270, 321, 21))
        self.label_552.setFont(font9)
        self.label_552.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_552.setAlignment(Qt.AlignCenter)
        self.VPCO_output_stack.addWidget(self.StateVector_result_screen)

        self.verticalLayout_23.addWidget(self.VPCO_output_stack)


        self.horizontalLayout_21.addWidget(self.VPCO_output_frame)

        self.stackedWidget.addWidget(self.VPCO_output)
        self.COEnAOE = QWidget()
        self.COEnAOE.setObjectName(u"COEnAOE")
        self.horizontalLayout_43 = QHBoxLayout(self.COEnAOE)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.COEnAOE_frame = QFrame(self.COEnAOE)
        self.COEnAOE_frame.setObjectName(u"COEnAOE_frame")
        self.COEnAOE_frame.setFrameShape(QFrame.StyledPanel)
        self.COEnAOE_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.COEnAOE_frame)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(-1, -1, -1, 0)
        self.PosNVelVector_inpt_frame = QFrame(self.COEnAOE_frame)
        self.PosNVelVector_inpt_frame.setObjectName(u"PosNVelVector_inpt_frame")
        self.PosNVelVector_inpt_frame.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197,88%);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189,88%);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"border: 5px solid rgb(143, 55, 143,88%);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid  rgb(255, 248, 166,88%);\n"
"	\n"
"}\n"
"")
        self.PosNVelVector_inpt_frame.setFrameShape(QFrame.StyledPanel)
        self.PosNVelVector_inpt_frame.setFrameShadow(QFrame.Raised)
        self.label_25 = QLabel(self.PosNVelVector_inpt_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(130, 50, 181, 41))
        self.label_25.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_26 = QLabel(self.PosNVelVector_inpt_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(420, 50, 41, 41))
        self.label_26.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_27 = QLabel(self.PosNVelVector_inpt_frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(580, 50, 41, 41))
        self.label_27.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_36 = QLabel(self.PosNVelVector_inpt_frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(740, 50, 41, 41))
        self.label_36.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_36.setAlignment(Qt.AlignCenter)
        self.R_unit_coe_n_aoe = QComboBox(self.PosNVelVector_inpt_frame)
        self.R_unit_coe_n_aoe.addItem("")
        self.R_unit_coe_n_aoe.addItem("")
        self.R_unit_coe_n_aoe.addItem("")
        self.R_unit_coe_n_aoe.addItem("")
        self.R_unit_coe_n_aoe.setObjectName(u"R_unit_coe_n_aoe")
        self.R_unit_coe_n_aoe.setGeometry(QRect(790, 50, 100, 40))
        self.R_unit_coe_n_aoe.setMinimumSize(QSize(100, 40))
        self.R_unit_coe_n_aoe.setMaximumSize(QSize(100, 40))
        self.R_unit_coe_n_aoe.setLayoutDirection(Qt.LeftToRight)
        self.R_unit_coe_n_aoe.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.R_unit_coe_n_aoe.setEditable(False)
        self.Ri_coe_n_aoe = QLineEdit(self.PosNVelVector_inpt_frame)
        self.Ri_coe_n_aoe.setObjectName(u"Ri_coe_n_aoe")
        self.Ri_coe_n_aoe.setGeometry(QRect(310, 50, 101, 41))
        self.Ri_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.Ri_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.Rj_coe_n_aoe = QLineEdit(self.PosNVelVector_inpt_frame)
        self.Rj_coe_n_aoe.setObjectName(u"Rj_coe_n_aoe")
        self.Rj_coe_n_aoe.setGeometry(QRect(470, 50, 101, 41))
        self.Rj_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.Rj_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.Rk_coe_n_aoe = QLineEdit(self.PosNVelVector_inpt_frame)
        self.Rk_coe_n_aoe.setObjectName(u"Rk_coe_n_aoe")
        self.Rk_coe_n_aoe.setGeometry(QRect(630, 50, 101, 41))
        self.Rk_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.Rk_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.V_unit_coe_n_aoe = QComboBox(self.PosNVelVector_inpt_frame)
        self.V_unit_coe_n_aoe.addItem("")
        self.V_unit_coe_n_aoe.addItem("")
        self.V_unit_coe_n_aoe.addItem("")
        self.V_unit_coe_n_aoe.addItem("")
        self.V_unit_coe_n_aoe.setObjectName(u"V_unit_coe_n_aoe")
        self.V_unit_coe_n_aoe.setGeometry(QRect(790, 120, 100, 40))
        self.V_unit_coe_n_aoe.setMinimumSize(QSize(100, 40))
        self.V_unit_coe_n_aoe.setMaximumSize(QSize(100, 40))
        self.V_unit_coe_n_aoe.setLayoutDirection(Qt.LeftToRight)
        self.V_unit_coe_n_aoe.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.V_unit_coe_n_aoe.setEditable(False)
        self.label_44 = QLabel(self.PosNVelVector_inpt_frame)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(130, 120, 181, 41))
        self.label_44.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_44.setAlignment(Qt.AlignCenter)
        self.label_45 = QLabel(self.PosNVelVector_inpt_frame)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(420, 120, 41, 41))
        self.label_45.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.Vj_coe_n_aoe = QLineEdit(self.PosNVelVector_inpt_frame)
        self.Vj_coe_n_aoe.setObjectName(u"Vj_coe_n_aoe")
        self.Vj_coe_n_aoe.setGeometry(QRect(470, 120, 101, 41))
        self.Vj_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.Vj_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.Vi_coe_n_aoe = QLineEdit(self.PosNVelVector_inpt_frame)
        self.Vi_coe_n_aoe.setObjectName(u"Vi_coe_n_aoe")
        self.Vi_coe_n_aoe.setGeometry(QRect(310, 120, 101, 41))
        self.Vi_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.Vi_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.label_46 = QLabel(self.PosNVelVector_inpt_frame)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(580, 120, 41, 41))
        self.label_46.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_46.setAlignment(Qt.AlignCenter)
        self.label_47 = QLabel(self.PosNVelVector_inpt_frame)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(740, 120, 41, 41))
        self.label_47.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_47.setAlignment(Qt.AlignCenter)
        self.Vk_coe_n_aoe = QLineEdit(self.PosNVelVector_inpt_frame)
        self.Vk_coe_n_aoe.setObjectName(u"Vk_coe_n_aoe")
        self.Vk_coe_n_aoe.setGeometry(QRect(630, 120, 101, 41))
        self.Vk_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.Vk_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.maj_body_CoOE = QComboBox(self.PosNVelVector_inpt_frame)
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.addItem("")
        self.maj_body_CoOE.setObjectName(u"maj_body_CoOE")
        self.maj_body_CoOE.setGeometry(QRect(410, 190, 251, 41))
        self.maj_body_CoOE.setStyleSheet(u"QComboBox{\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.otherbody_stack = QStackedWidget(self.PosNVelVector_inpt_frame)
        self.otherbody_stack.setObjectName(u"otherbody_stack")
        self.otherbody_stack.setGeometry(QRect(690, 160, 331, 91))
        self.otherbody_stack.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.blanck = QWidget()
        self.blanck.setObjectName(u"blanck")
        self.otherbody_stack.addWidget(self.blanck)
        self.show_page = QWidget()
        self.show_page.setObjectName(u"show_page")
        self.other_body_mass_coe_n_aoe = QLineEdit(self.show_page)
        self.other_body_mass_coe_n_aoe.setObjectName(u"other_body_mass_coe_n_aoe")
        self.other_body_mass_coe_n_aoe.setGeometry(QRect(40, 10, 111, 41))
        self.other_body_mass_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color: black;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.other_body_mass_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.other_body_radius_coe_n_aoe = QLineEdit(self.show_page)
        self.other_body_radius_coe_n_aoe.setObjectName(u"other_body_radius_coe_n_aoe")
        self.other_body_radius_coe_n_aoe.setGeometry(QRect(180, 10, 111, 41))
        self.other_body_radius_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color: black;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.other_body_radius_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.cal_btn_coe_n_aoe = QPushButton(self.show_page)
        self.cal_btn_coe_n_aoe.setObjectName(u"cal_btn_coe_n_aoe")
        self.cal_btn_coe_n_aoe.setGeometry(QRect(130, 60, 71, 21))
        self.cal_btn_coe_n_aoe.setFont(font4)
        self.cal_btn_coe_n_aoe.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0,60%);\n"
"}")
        self.otherbody_stack.addWidget(self.show_page)
        self.label_264 = QLabel(self.PosNVelVector_inpt_frame)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setGeometry(QRect(20, 10, 221, 21))
        self.label_264.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_264.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_49.addWidget(self.PosNVelVector_inpt_frame)

        self.CoOE_output_frame = QFrame(self.COEnAOE_frame)
        self.CoOE_output_frame.setObjectName(u"CoOE_output_frame")
        self.CoOE_output_frame.setMinimumSize(QSize(0, 0))
        self.CoOE_output_frame.setMaximumSize(QSize(30000, 256))
        self.CoOE_output_frame.setStyleSheet(u"QLabel{\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197,88%);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189,88%);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"border: 5px solid rgb(143, 55, 143,88%);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid  rgb(255, 248, 166,88%);\n"
"	\n"
"}\n"
"")
        self.CoOE_output_frame.setFrameShape(QFrame.StyledPanel)
        self.CoOE_output_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.CoOE_output_frame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.CoOE_output_stack = QStackedWidget(self.CoOE_output_frame)
        self.CoOE_output_stack.setObjectName(u"CoOE_output_stack")
        self.CoOE_output_stack.setStyleSheet(u"border:none;")
        self.CoOE_output_lbl_error_screen = QWidget()
        self.CoOE_output_lbl_error_screen.setObjectName(u"CoOE_output_lbl_error_screen")
        self.verticalLayout_25 = QVBoxLayout(self.CoOE_output_lbl_error_screen)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.CoOE_output_lbl_error = QLineEdit(self.CoOE_output_lbl_error_screen)
        self.CoOE_output_lbl_error.setObjectName(u"CoOE_output_lbl_error")
        self.CoOE_output_lbl_error.setFont(font9)
        self.CoOE_output_lbl_error.setStyleSheet(u"background-color:transparent;\n"
"color: black;\n"
"")
        self.CoOE_output_lbl_error.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.CoOE_output_lbl_error)

        self.CoOE_output_stack.addWidget(self.CoOE_output_lbl_error_screen)
        self.CoOE_output_parameters_screen = QWidget()
        self.CoOE_output_parameters_screen.setObjectName(u"CoOE_output_parameters_screen")
        self.arg_of_per_unit_coe_n_aoe = QComboBox(self.CoOE_output_parameters_screen)
        self.arg_of_per_unit_coe_n_aoe.addItem("")
        self.arg_of_per_unit_coe_n_aoe.addItem("")
        self.arg_of_per_unit_coe_n_aoe.setObjectName(u"arg_of_per_unit_coe_n_aoe")
        self.arg_of_per_unit_coe_n_aoe.setGeometry(QRect(880, 130, 100, 40))
        self.arg_of_per_unit_coe_n_aoe.setMinimumSize(QSize(100, 40))
        self.arg_of_per_unit_coe_n_aoe.setMaximumSize(QSize(100, 40))
        self.arg_of_per_unit_coe_n_aoe.setLayoutDirection(Qt.LeftToRight)
        self.arg_of_per_unit_coe_n_aoe.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.arg_of_per_unit_coe_n_aoe.setEditable(False)
        self.RAAN_CoOE_lbl = QLabel(self.CoOE_output_parameters_screen)
        self.RAAN_CoOE_lbl.setObjectName(u"RAAN_CoOE_lbl")
        self.RAAN_CoOE_lbl.setGeometry(QRect(490, 60, 231, 41))
        self.RAAN_CoOE_lbl.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.RAAN_CoOE_lbl.setAlignment(Qt.AlignCenter)
        self.sma_CoOE_lbl = QLabel(self.CoOE_output_parameters_screen)
        self.sma_CoOE_lbl.setObjectName(u"sma_CoOE_lbl")
        self.sma_CoOE_lbl.setGeometry(QRect(0, 60, 221, 41))
        self.sma_CoOE_lbl.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.sma_CoOE_lbl.setAlignment(Qt.AlignCenter)
        self.arg_of_per_coe_n_aoe = QLabel(self.CoOE_output_parameters_screen)
        self.arg_of_per_coe_n_aoe.setObjectName(u"arg_of_per_coe_n_aoe")
        self.arg_of_per_coe_n_aoe.setGeometry(QRect(730, 130, 141, 41))
        self.arg_of_per_coe_n_aoe.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:black;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.arg_of_per_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.inclination_coe_n_aoe = QLabel(self.CoOE_output_parameters_screen)
        self.inclination_coe_n_aoe.setObjectName(u"inclination_coe_n_aoe")
        self.inclination_coe_n_aoe.setGeometry(QRect(230, 200, 141, 41))
        self.inclination_coe_n_aoe.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:black;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.inclination_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.tru_ano_CoOE_lbl = QLabel(self.CoOE_output_parameters_screen)
        self.tru_ano_CoOE_lbl.setObjectName(u"tru_ano_CoOE_lbl")
        self.tru_ano_CoOE_lbl.setGeometry(QRect(490, 200, 231, 41))
        self.tru_ano_CoOE_lbl.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.tru_ano_CoOE_lbl.setAlignment(Qt.AlignCenter)
        self.semimajor_axis_coe_n_aoe = QLabel(self.CoOE_output_parameters_screen)
        self.semimajor_axis_coe_n_aoe.setObjectName(u"semimajor_axis_coe_n_aoe")
        self.semimajor_axis_coe_n_aoe.setGeometry(QRect(230, 60, 141, 41))
        self.semimajor_axis_coe_n_aoe.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:black;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.semimajor_axis_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.tru_ana_coe_n_aoe = QLabel(self.CoOE_output_parameters_screen)
        self.tru_ana_coe_n_aoe.setObjectName(u"tru_ana_coe_n_aoe")
        self.tru_ana_coe_n_aoe.setGeometry(QRect(730, 200, 141, 41))
        self.tru_ana_coe_n_aoe.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:black;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.tru_ana_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.semimajor_axis_unit_coe_n_aoe = QComboBox(self.CoOE_output_parameters_screen)
        self.semimajor_axis_unit_coe_n_aoe.addItem("")
        self.semimajor_axis_unit_coe_n_aoe.addItem("")
        self.semimajor_axis_unit_coe_n_aoe.addItem("")
        self.semimajor_axis_unit_coe_n_aoe.addItem("")
        self.semimajor_axis_unit_coe_n_aoe.setObjectName(u"semimajor_axis_unit_coe_n_aoe")
        self.semimajor_axis_unit_coe_n_aoe.setGeometry(QRect(380, 60, 100, 40))
        self.semimajor_axis_unit_coe_n_aoe.setMinimumSize(QSize(100, 40))
        self.semimajor_axis_unit_coe_n_aoe.setMaximumSize(QSize(100, 40))
        self.semimajor_axis_unit_coe_n_aoe.setLayoutDirection(Qt.LeftToRight)
        self.semimajor_axis_unit_coe_n_aoe.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.semimajor_axis_unit_coe_n_aoe.setEditable(False)
        self.arg_of_per_CoOE_lbl = QLabel(self.CoOE_output_parameters_screen)
        self.arg_of_per_CoOE_lbl.setObjectName(u"arg_of_per_CoOE_lbl")
        self.arg_of_per_CoOE_lbl.setGeometry(QRect(490, 130, 231, 41))
        self.arg_of_per_CoOE_lbl.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.arg_of_per_CoOE_lbl.setAlignment(Qt.AlignCenter)
        self.inclination_unit_coe_n_aoe = QComboBox(self.CoOE_output_parameters_screen)
        self.inclination_unit_coe_n_aoe.addItem("")
        self.inclination_unit_coe_n_aoe.addItem("")
        self.inclination_unit_coe_n_aoe.setObjectName(u"inclination_unit_coe_n_aoe")
        self.inclination_unit_coe_n_aoe.setGeometry(QRect(380, 200, 100, 40))
        self.inclination_unit_coe_n_aoe.setMinimumSize(QSize(100, 40))
        self.inclination_unit_coe_n_aoe.setMaximumSize(QSize(100, 40))
        self.inclination_unit_coe_n_aoe.setLayoutDirection(Qt.LeftToRight)
        self.inclination_unit_coe_n_aoe.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.inclination_unit_coe_n_aoe.setEditable(False)
        self.RAAN_unit_coe_n_aoe = QComboBox(self.CoOE_output_parameters_screen)
        self.RAAN_unit_coe_n_aoe.addItem("")
        self.RAAN_unit_coe_n_aoe.addItem("")
        self.RAAN_unit_coe_n_aoe.setObjectName(u"RAAN_unit_coe_n_aoe")
        self.RAAN_unit_coe_n_aoe.setGeometry(QRect(880, 60, 100, 40))
        self.RAAN_unit_coe_n_aoe.setMinimumSize(QSize(100, 40))
        self.RAAN_unit_coe_n_aoe.setMaximumSize(QSize(100, 40))
        self.RAAN_unit_coe_n_aoe.setLayoutDirection(Qt.LeftToRight)
        self.RAAN_unit_coe_n_aoe.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.RAAN_unit_coe_n_aoe.setEditable(False)
        self.tru_ana_unit_coe_n_aoe = QComboBox(self.CoOE_output_parameters_screen)
        self.tru_ana_unit_coe_n_aoe.addItem("")
        self.tru_ana_unit_coe_n_aoe.addItem("")
        self.tru_ana_unit_coe_n_aoe.setObjectName(u"tru_ana_unit_coe_n_aoe")
        self.tru_ana_unit_coe_n_aoe.setGeometry(QRect(880, 200, 100, 40))
        self.tru_ana_unit_coe_n_aoe.setMinimumSize(QSize(100, 40))
        self.tru_ana_unit_coe_n_aoe.setMaximumSize(QSize(100, 40))
        self.tru_ana_unit_coe_n_aoe.setLayoutDirection(Qt.LeftToRight)
        self.tru_ana_unit_coe_n_aoe.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.tru_ana_unit_coe_n_aoe.setEditable(False)
        self.inc_CoOE_lbl = QLabel(self.CoOE_output_parameters_screen)
        self.inc_CoOE_lbl.setObjectName(u"inc_CoOE_lbl")
        self.inc_CoOE_lbl.setGeometry(QRect(0, 200, 221, 41))
        self.inc_CoOE_lbl.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.inc_CoOE_lbl.setAlignment(Qt.AlignCenter)
        self.ecce_CoOE_lbl = QLabel(self.CoOE_output_parameters_screen)
        self.ecce_CoOE_lbl.setObjectName(u"ecce_CoOE_lbl")
        self.ecce_CoOE_lbl.setGeometry(QRect(0, 130, 221, 41))
        self.ecce_CoOE_lbl.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.ecce_CoOE_lbl.setAlignment(Qt.AlignCenter)
        self.label_262 = QLabel(self.CoOE_output_parameters_screen)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setGeometry(QRect(20, 30, 221, 21))
        self.label_262.setStyleSheet(u"border:none;\n"
"color:white;\n"
"")
        self.label_262.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.eccentricity_coe_n_aoe = QLabel(self.CoOE_output_parameters_screen)
        self.eccentricity_coe_n_aoe.setObjectName(u"eccentricity_coe_n_aoe")
        self.eccentricity_coe_n_aoe.setGeometry(QRect(230, 130, 141, 41))
        self.eccentricity_coe_n_aoe.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:black;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.eccentricity_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.RAAN_coe_n_aoe = QLabel(self.CoOE_output_parameters_screen)
        self.RAAN_coe_n_aoe.setObjectName(u"RAAN_coe_n_aoe")
        self.RAAN_coe_n_aoe.setGeometry(QRect(730, 60, 141, 41))
        self.RAAN_coe_n_aoe.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(131, 200, 168, 255), stop:1 rgba(224, 255, 190, 255));\n"
"	border: 5px solid rgb(84, 84, 197);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:black;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")
        self.RAAN_coe_n_aoe.setAlignment(Qt.AlignCenter)
        self.CoOE_output_para_lbl = QLineEdit(self.CoOE_output_parameters_screen)
        self.CoOE_output_para_lbl.setObjectName(u"CoOE_output_para_lbl")
        self.CoOE_output_para_lbl.setGeometry(QRect(90, 10, 901, 31))
        self.CoOE_output_para_lbl.setFont(font9)
        self.CoOE_output_para_lbl.setStyleSheet(u"background-color:transparent;\n"
"\n"
"color:white;\n"
"border-radius:10px;")
        self.CoOE_output_para_lbl.setAlignment(Qt.AlignCenter)
        self.CoOE_output_stack.addWidget(self.CoOE_output_parameters_screen)

        self.horizontalLayout_24.addWidget(self.CoOE_output_stack)


        self.verticalLayout_49.addWidget(self.CoOE_output_frame)


        self.horizontalLayout_43.addWidget(self.COEnAOE_frame)

        self.stackedWidget.addWidget(self.COEnAOE)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(0, 15))
        self.credits_bar.setMaximumSize(QSize(16777215, 20))
        self.credits_bar.setStyleSheet(u"background-color: None")
        self.credits_bar.setFrameShape(QFrame.StyledPanel)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setMinimumSize(QSize(20, 0))
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_label_credits)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 5)
        self.frame_31 = QFrame(self.frame_label_credits)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(1000, 0))
        self.frame_31.setMaximumSize(QSize(1000, 16777215))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_31)

        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setMinimumSize(QSize(50, 0))
        self.label_credits.setMaximumSize(QSize(50, 16777215))
        font14 = QFont()
        font14.setFamily(u"Arial")
        font14.setPointSize(6)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        self.label_credits.setFont(font14)
        self.label_credits.setStyleSheet(u"image:url(UI_Functions/Resources/MOPy Cover_transparent.png);")
        self.label_credits.setPixmap(QPixmap(u"Users/manjunath neelmath/.designer/backup/GUI-test/Resources/MOPy Cover_transparent.png"))
        self.label_credits.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_credits)

        self.frame_30 = QFrame(self.frame_label_credits)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_30)


        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding:5px")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.Orbit_type_stack.setCurrentIndex(5)
        self.stackedWidget_2.setCurrentIndex(4)
        self.VPCO_output_stack.setCurrentIndex(1)
        self.otherbody_stack.setCurrentIndex(0)
        self.CoOE_output_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MOPy", None))
#if QT_CONFIG(tooltip)
        self.Home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Home</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Home_btn.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"    MOPy", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_title_2.setText(QCoreApplication.translate("MainWindow", u"            JulianDay Calculation:", None))
        self.type_of_calendar.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Type Of Calendar", None))
        self.type_of_calendar.setItemText(1, QCoreApplication.translate("MainWindow", u"  Julian Calendar", None))
        self.type_of_calendar.setItemText(2, QCoreApplication.translate("MainWindow", u"  Gregorian Calendar", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"         Inputs:", None))
        self.Error_state.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Time:", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"UT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Digits of Accuracy:", None))
        self.calculate_btn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"       Output:", None))
        self.JulianDay_Result.setText("")
        self.label_title_3.setText(QCoreApplication.translate("MainWindow", u"    SOI of Planet", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"                      Inputs:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sphere of Influence of:", None))
        self.lbl_mass.setText(QCoreApplication.translate("MainWindow", u"Mass of ", None))
        self.SOI_planet_name.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Body", None))
        self.SOI_planet_name.setItemText(1, QCoreApplication.translate("MainWindow", u"  Moon", None))
        self.SOI_planet_name.setItemText(2, QCoreApplication.translate("MainWindow", u"  Earth", None))
        self.SOI_planet_name.setItemText(3, QCoreApplication.translate("MainWindow", u"  Jupiter", None))
        self.SOI_planet_name.setItemText(4, QCoreApplication.translate("MainWindow", u"  Mercury", None))
        self.SOI_planet_name.setItemText(5, QCoreApplication.translate("MainWindow", u"  Venus", None))
        self.SOI_planet_name.setItemText(6, QCoreApplication.translate("MainWindow", u"  Mars", None))
        self.SOI_planet_name.setItemText(7, QCoreApplication.translate("MainWindow", u"  Saturn", None))
        self.SOI_planet_name.setItemText(8, QCoreApplication.translate("MainWindow", u"  Uranus", None))
        self.SOI_planet_name.setItemText(9, QCoreApplication.translate("MainWindow", u"  Neptune", None))
        self.SOI_planet_name.setItemText(10, QCoreApplication.translate("MainWindow", u"  Pluto", None))

        self.lbl_dist_frm_sun.setText(QCoreApplication.translate("MainWindow", u"Distance From Sun:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Kg", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.soi_mass.setText("")
        self.dist_frm_sun.setText("")
        self.soi_cal.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"                      Outputs:", None))
        self.get_3D_soi.setText(QCoreApplication.translate("MainWindow", u"Get 3D Visualization", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.rSOI_of_planet_lbl.setText("")
        self.soi_rad.setText("")
        self.label_title_4.setText(QCoreApplication.translate("MainWindow", u"                    Various Parameters of an Orbit", None))
#if QT_CONFIG(tooltip)
        self.Home_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"VPCO Home", None))
#endif // QT_CONFIG(tooltip)
        self.Home_btn_2.setText("")
        self.vpco_input_type.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Type of Inputs", None))
        self.vpco_input_type.setItemText(1, QCoreApplication.translate("MainWindow", u"  a , e", None))
        self.vpco_input_type.setItemText(2, QCoreApplication.translate("MainWindow", u"  ra , rp ", None))
        self.vpco_input_type.setItemText(3, QCoreApplication.translate("MainWindow", u"  r , v , gamma", None))
        self.vpco_input_type.setItemText(4, QCoreApplication.translate("MainWindow", u"  Orbital Elements", None))
        self.vpco_input_type.setItemText(5, QCoreApplication.translate("MainWindow", u"  State Vectors", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Select any of the inputs listed in the dropdown box, about your Orbit", None))
        self.vpco_major_body.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Major Body", None))
        self.vpco_major_body.setItemText(1, QCoreApplication.translate("MainWindow", u"  Moon", None))
        self.vpco_major_body.setItemText(2, QCoreApplication.translate("MainWindow", u"  Earth", None))
        self.vpco_major_body.setItemText(3, QCoreApplication.translate("MainWindow", u"  Jupiter", None))
        self.vpco_major_body.setItemText(4, QCoreApplication.translate("MainWindow", u"  Mercury", None))
        self.vpco_major_body.setItemText(5, QCoreApplication.translate("MainWindow", u"  Venus", None))
        self.vpco_major_body.setItemText(6, QCoreApplication.translate("MainWindow", u"  Mars", None))
        self.vpco_major_body.setItemText(7, QCoreApplication.translate("MainWindow", u"  Saturn", None))
        self.vpco_major_body.setItemText(8, QCoreApplication.translate("MainWindow", u"  Uranus", None))
        self.vpco_major_body.setItemText(9, QCoreApplication.translate("MainWindow", u"  Neptune", None))
        self.vpco_major_body.setItemText(10, QCoreApplication.translate("MainWindow", u"  Pluto", None))
        self.vpco_major_body.setItemText(11, QCoreApplication.translate("MainWindow", u"  Sun", None))

        self.input_type_go_btn_vpco.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.error_selct_body.setText("")
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Semi-Major Axis:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Eccentricity:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.orbit_type_ae.setText("")
        self.orbit_type_btn_inpt_ae.setText(QCoreApplication.translate("MainWindow", u"Orbit Type", None))
        self.go_btn_inpt_ae.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.ra_inpt_rarp.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Apoapsis Radius (ra):", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Periapsis Radius (rp):", None))
        self.rp_inpt_rarp.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.orbit_type_rarp.setText("")
        self.distance_frm_cntr_of_body_inpt_rvgamma.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"At any point on Orbit", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Distance from center of major body (r)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Velocity at that point (v)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.v_at_point_inpt_rvgamma.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.flt_path_angle_inpt_rvgamma.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Flight Path Angle (gamma)", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"degree", None))
        self.orbit_type_rvgamma.setText("")
        self.semi_major_axis_inpt_orbitalElements.setText("")
        self.eccentricity_inpt_orbitalElements.setText("")
        self.inclination_inpt_orbitalElements.setText("")
        self.raan_inpt_orbitalElements.setText("")
        self.argment_of_peri__inpt_orbitalElements.setText("")
        self.tru_anmly_inpt_orbitalElements.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Semi-Major Axis (a)", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"   Eccentricity (e)", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Inclination (i)", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"True Anamoly (Theta)", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"RAAN (Ohm)", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Arguement of Periapsis (Omega)", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"degree", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"degree", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"degree", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"degree", None))
        self.orbit_type_orbitalElements.setText("")
        self.position_vector_inpt_stateVector.setText("")
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Position Vector", None))
        self.velocity_vector_inpt_stateVector.setText("")
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Velocity Vector", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.orbit_type_stateVector.setText("")
        self.Error_parabola.setText("")
        self.toggle_menu_btn.setText("")
        self.type_of_input_toggle.setItemText(0, QCoreApplication.translate("MainWindow", u"  a and e", None))
        self.type_of_input_toggle.setItemText(1, QCoreApplication.translate("MainWindow", u"  ra and rp", None))
        self.type_of_input_toggle.setItemText(2, QCoreApplication.translate("MainWindow", u"  r1, v1, \u03b31", None))
        self.type_of_input_toggle.setItemText(3, QCoreApplication.translate("MainWindow", u"  State Vectors", None))
        self.type_of_input_toggle.setItemText(4, QCoreApplication.translate("MainWindow", u"  page", None))
        self.type_of_input_toggle.setItemText(5, QCoreApplication.translate("MainWindow", u"  page_2", None))

        self.semi_major_axis_toggle_menu_lbl_2.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.eccentricity_toggle_menu_lbl_2.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.inclination_toggle_menu_lbl_2.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.RAAN_toggle_menu_lbl_2.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.arg_of_per_toggle_menu_lbl_2.setText(QCoreApplication.translate("MainWindow", u"\u03c9", None))
        self.tru_ano_toggle_menu_lbl_2.setText(QCoreApplication.translate("MainWindow", u"\u03b3", None))
        self.semi_major_axis_toggle_menu_lbl.setText(QCoreApplication.translate("MainWindow", u"Semi-Major Axis", None))
#if QT_CONFIG(tooltip)
        self.semi_major_axis_toggle_menu_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"Semi-Major Axis", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Semi_dial.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate to alter the Semi-Major axis value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.semi_major_axis_toggle_menu_single_step.setToolTip(QCoreApplication.translate("MainWindow", u"Current Single Step", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.semi_major_axis_toggle_menu_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Slide to Change the single step to be altered", None))
#endif // QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_lbl.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
#if QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ecce_dial.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate to alter the Eccentricity value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_single_step.setToolTip(QCoreApplication.translate("MainWindow", u"Current Single Step", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Slide to change the single step to be altered ", None))
#endif // QT_CONFIG(tooltip)
        self.Radius_of_Apoapsis_frame_lbl.setText(QCoreApplication.translate("MainWindow", u"Radius of Apoapsis", None))
#if QT_CONFIG(tooltip)
        self.Radius_of_Apoapsis_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"Semi-Major Axis", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Radius_of_Apoapsis_dial.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate to alter the Semi-Major axis value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Radius_of_Apoapsis_single_step.setToolTip(QCoreApplication.translate("MainWindow", u"Current Single Step", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Radius_of_Apoapsis_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Slide to Change the single step to be altered", None))
#endif // QT_CONFIG(tooltip)
        self.Radius_of_Periapsis_frame_lbl.setText(QCoreApplication.translate("MainWindow", u"Radius of Periapsis", None))
#if QT_CONFIG(tooltip)
        self.Radius_of_Periapsis_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"Semi-Major Axis", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Radius_of_Periapsis_dial.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate to alter the Semi-Major axis value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Radius_of_Periapsis_single_step.setToolTip(QCoreApplication.translate("MainWindow", u"Current Single Step", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Radius_of_Periapsis_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Slide to Change the single step to be altered", None))
#endif // QT_CONFIG(tooltip)
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Gamma", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"degree", None))
        self.Radius_of_Apoapsis_frame_lbl_2.setText(QCoreApplication.translate("MainWindow", u"Position Vector", None))
        self.label_29.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_33.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"j", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_37.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.Radius_of_Apoapsis_frame_lbl_3.setText(QCoreApplication.translate("MainWindow", u"Velocity Vector", None))
        self.label_38.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_48.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"j", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_54.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.Radius_of_Apoapsis_frame_lbl_4.setText(QCoreApplication.translate("MainWindow", u"Distnce frm MainBody", None))
        self.label_title_5.setText(QCoreApplication.translate("MainWindow", u"                    Various Parameters of an Orbit", None))
#if QT_CONFIG(tooltip)
        self.vpco_feature_back_btn.setToolTip(QCoreApplication.translate("MainWindow", u"VPCO Home", None))
#endif // QT_CONFIG(tooltip)
        self.vpco_feature_back_btn.setText("")
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"     Output:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Specific Angular Momentum", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Periapsis", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"J/kg", None))
        self.rp_ae.setText("")
        self.p_ae.setText("")
        self.ra_ae.setText("")
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Velocity at Apoapsis", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Radius of Apoapsis", None))
        self.h_ae.setText("")
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Velocity at Periapsis", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Mean Motion", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.gfa_ae.setText("")
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Semi-latus Rectum", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Periapsis", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Specific Mechanical Energy", None))
        self.gfp_ae.setText("")
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Apoapsis", None))
        self.vp_ae.setText("")
        self.mu_ae.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.T_ae.setText("")
        self.escvp_ae.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"m^2/s", None))
        self.vlatus_ae.setText("")
        self.n_ae.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Apoapsis", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Radius of Periapsis", None))
        self.va_ae.setText("")
        self.escva_ae.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Velocity at Semi-latus Rectum", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"rad/s", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Velocity at Semi-latus Rectum", None))
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Periapsis", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"Semi-latus Rectum", None))
        self.escvp_rarp.setText("")
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"rad/s", None))
        self.gfp_rarp.setText("")
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"m^2/s", None))
        self.label_249.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"Velocity at Periapsis", None))
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"Specific Angular Momentum", None))
        self.vlatus_rarp.setText("")
        self.escva_rarp.setText("")
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.e_rarp.setText("")
        self.h_rarp.setText("")
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.vp_rarp.setText("")
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"Semi-major Axis", None))
        self.T_rarp.setText("")
        self.p_rarp.setText("")
        self.gfa_rarp.setText("")
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.va_rarp.setText("")
        self.label_265.setText(QCoreApplication.translate("MainWindow", u"         Output:", None))
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.a_rarp.setText("")
        self.label_268.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.mu_rarp.setText("")
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_272.setText(QCoreApplication.translate("MainWindow", u"Mean Motion", None))
        self.label_274.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Apoapsis", None))
        self.label_275.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_276.setText(QCoreApplication.translate("MainWindow", u"Specific Mechanical Energy", None))
        self.label_277.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.n_rarp.setText("")
        self.label_279.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Apoapsis", None))
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"Velocity at Apoapsis", None))
        self.label_281.setText(QCoreApplication.translate("MainWindow", u"J/kg", None))
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Periapsis", None))
        self.label_283.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
        self.type_of_input_toggle_2.setItemText(0, QCoreApplication.translate("MainWindow", u"  a and e", None))
        self.type_of_input_toggle_2.setItemText(1, QCoreApplication.translate("MainWindow", u"  ra and rp", None))
        self.type_of_input_toggle_2.setItemText(2, QCoreApplication.translate("MainWindow", u"  r1, v1, \u03b31", None))
        self.type_of_input_toggle_2.setItemText(3, QCoreApplication.translate("MainWindow", u"  State Vectors", None))

        self.label_273.setText(QCoreApplication.translate("MainWindow", u"Velocity at Semi-latus Rectum", None))
        self.label_284.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_285.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Periapsis", None))
        self.label_286.setText(QCoreApplication.translate("MainWindow", u"Semi-latus Rectum", None))
        self.vlatus_rvgamma.setText("")
        self.label_288.setText(QCoreApplication.translate("MainWindow", u"rad/s", None))
        self.va_rvgamma.setText("")
        self.label_290.setText(QCoreApplication.translate("MainWindow", u"m^2/s", None))
        self.label_291.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_292.setText(QCoreApplication.translate("MainWindow", u"Velocity at Periapsis", None))
        self.label_293.setText(QCoreApplication.translate("MainWindow", u"Specific Angular Momentum", None))
        self.p_rvgamma.setText("")
        self.escvp_rvgamma.setText("")
        self.label_296.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.rp_rvgamma.setText("")
        self.mu_rvgamma.setText("")
        self.label_299.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.n_rvgamma.setText("")
        self.label_301.setText(QCoreApplication.translate("MainWindow", u"Radius of Periapsis", None))
        self.h_rvgamma.setText("")
        self.gfa_rvgamma.setText("")
        self.gfp_rvgamma.setText("")
        self.label_305.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.e_rvgamma.setText("")
        self.label_307.setText(QCoreApplication.translate("MainWindow", u"         Output:", None))
        self.label_308.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.a_rvgamma.setText("")
        self.label_310.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_311.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.ra_rvgamma.setText("")
        self.label_313.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"Mean Motion", None))
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_316.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Apoapsis", None))
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_318.setText(QCoreApplication.translate("MainWindow", u"Specific Mechanical Energy", None))
        self.label_319.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.T_rvgamma.setText("")
        self.label_321.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Apoapsis", None))
        self.label_322.setText(QCoreApplication.translate("MainWindow", u"Velocity at Apoapsis", None))
        self.label_323.setText(QCoreApplication.translate("MainWindow", u"J/kg", None))
        self.label_324.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Periapsis", None))
        self.label_325.setText(QCoreApplication.translate("MainWindow", u"Radius of Apoapsis", None))
        self.escva_rvgamma.setText("")
        self.vp_rvgamma.setText("")
        self.label_330.setText(QCoreApplication.translate("MainWindow", u"Semi-major Axis", None))
        self.label_331.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
        self.label_462.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_463.setText(QCoreApplication.translate("MainWindow", u"Velocity at Semi-latus Rectum", None))
        self.label_464.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_465.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Periapsis", None))
        self.label_466.setText(QCoreApplication.translate("MainWindow", u"Semi-latus Rectum", None))
        self.escvp_orbitalElements.setText("")
        self.label_468.setText(QCoreApplication.translate("MainWindow", u"rad/s", None))
        self.gfp_orbitalElements.setText("")
        self.label_470.setText(QCoreApplication.translate("MainWindow", u"m^2/s", None))
        self.label_471.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_472.setText(QCoreApplication.translate("MainWindow", u"Velocity at Periapsis", None))
        self.label_473.setText(QCoreApplication.translate("MainWindow", u"Specific Angular Momentum", None))
        self.vlatus_orbitalElements.setText("")
        self.escva_orbitalElements.setText("")
        self.label_476.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.ra_orbitalElements.setText("")
        self.h_orbitalElements.setText("")
        self.label_479.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.vp_orbitalElements.setText("")
        self.label_481.setText(QCoreApplication.translate("MainWindow", u"Radius of Periapsis", None))
        self.T_orbitalElements.setText("")
        self.p_orbitalElements.setText("")
        self.gfa_orbitalElements.setText("")
        self.label_485.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.va_orbitalElements.setText("")
        self.label_487.setText(QCoreApplication.translate("MainWindow", u"         Output:", None))
        self.label_488.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.rp_orbitalElements.setText("")
        self.label_490.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.mu_orbitalElements.setText("")
        self.label_492.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_493.setText(QCoreApplication.translate("MainWindow", u"Mean Motion", None))
        self.label_494.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_495.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Apoapsis", None))
        self.label_496.setText(QCoreApplication.translate("MainWindow", u"Specific Mechanical Energy", None))
        self.label_497.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_498.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.n_orbitalElements.setText("")
        self.label_500.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Apoapsis", None))
        self.label_501.setText(QCoreApplication.translate("MainWindow", u"Velocity at Apoapsis", None))
        self.label_502.setText(QCoreApplication.translate("MainWindow", u"J/kg", None))
        self.label_503.setText(QCoreApplication.translate("MainWindow", u"Radius of Apoapsis", None))
        self.label_504.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Periapsis", None))
        self.label_499.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_505.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.rp_stateVector.setText("")
        self.gfa_stateVector.setText("")
        self.escva_stateVector.setText("")
        self.label_509.setText(QCoreApplication.translate("MainWindow", u"Semi-major Axis", None))
        self.label_510.setText(QCoreApplication.translate("MainWindow", u"rad/s", None))
        self.label_511.setText(QCoreApplication.translate("MainWindow", u"Radius of Periapsis", None))
        self.mu_stateVector.setText("")
        self.escvp_stateVector.setText("")
        self.ra_stateVector.setText("")
        self.label_515.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_516.setText(QCoreApplication.translate("MainWindow", u"Velocity at Periapsis", None))
        self.label_517.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_518.setText(QCoreApplication.translate("MainWindow", u"Radius of Apoapsis", None))
        self.n_stateVector.setText("")
        self.e_stateVector.setText("")
        self.h_stateVector.setText("")
        self.vp_stateVector.setText("")
        self.label_523.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.p_stateVector_lbl.setText(QCoreApplication.translate("MainWindow", u"Semi-latus Rectum", None))
        self.gfa_stateVector_lbl.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Apoapsis", None))
        self.escva_stateVector_lbl.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Apoapsis", None))
        self.label_527.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.p_stateVector.setText("")
        self.label_529.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
        self.label_530.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.escvp_stateVector_lbl.setText(QCoreApplication.translate("MainWindow", u"Escape Velocity at Periapsis", None))
        self.vlatus_stateVector.setText("")
        self.label_533.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.va_stateVector_lbl.setText(QCoreApplication.translate("MainWindow", u"Velocity at Apoapsis", None))
        self.label_535.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.gfp_stateVector.setText("")
        self.label_537.setText(QCoreApplication.translate("MainWindow", u"J/kg", None))
        self.label_538.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.T_stateVector.setText("")
        self.label_540.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_541.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_542.setText(QCoreApplication.translate("MainWindow", u"m^2/s", None))
        self.label_543.setText(QCoreApplication.translate("MainWindow", u"Specific Mechanical Energy", None))
        self.label_544.setText(QCoreApplication.translate("MainWindow", u"Mean Motion", None))
        self.va_stateVector.setText("")
        self.a_stateVector.setText("")
        self.gfp_stateVector_lbl.setText(QCoreApplication.translate("MainWindow", u"Gravitational Force at Periapsis", None))
        self.label_548.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.vlatus_stateVector_lbl.setText(QCoreApplication.translate("MainWindow", u"Velocity at Semi-latus Rectum", None))
        self.label_550.setText(QCoreApplication.translate("MainWindow", u"         Output:", None))
        self.label_551.setText(QCoreApplication.translate("MainWindow", u"km/s", None))
        self.label_552.setText(QCoreApplication.translate("MainWindow", u"Specific Angular Momentum", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Position Vector", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"i       +", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"j       +", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"k       ", None))
        self.R_unit_coe_n_aoe.setItemText(0, QCoreApplication.translate("MainWindow", u"  km", None))
        self.R_unit_coe_n_aoe.setItemText(1, QCoreApplication.translate("MainWindow", u"  miles", None))
        self.R_unit_coe_n_aoe.setItemText(2, QCoreApplication.translate("MainWindow", u"  AU", None))
        self.R_unit_coe_n_aoe.setItemText(3, QCoreApplication.translate("MainWindow", u"  DU", None))

        self.Ri_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"8250", None))
        self.Rj_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"390", None))
        self.Rk_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"6900", None))
        self.V_unit_coe_n_aoe.setItemText(0, QCoreApplication.translate("MainWindow", u"  km/s", None))
        self.V_unit_coe_n_aoe.setItemText(1, QCoreApplication.translate("MainWindow", u"  miles/s", None))
        self.V_unit_coe_n_aoe.setItemText(2, QCoreApplication.translate("MainWindow", u"  AU/s", None))
        self.V_unit_coe_n_aoe.setItemText(3, QCoreApplication.translate("MainWindow", u"  DU/TU", None))

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Velocity Vector", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"i       +", None))
        self.Vj_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"6.6", None))
        self.Vi_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"-0.7", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"j       +", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"k       ", None))
        self.Vk_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"-0.6", None))
        self.maj_body_CoOE.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Major Body", None))
        self.maj_body_CoOE.setItemText(1, QCoreApplication.translate("MainWindow", u"  Moon", None))
        self.maj_body_CoOE.setItemText(2, QCoreApplication.translate("MainWindow", u"  Earth", None))
        self.maj_body_CoOE.setItemText(3, QCoreApplication.translate("MainWindow", u"  Jupiter", None))
        self.maj_body_CoOE.setItemText(4, QCoreApplication.translate("MainWindow", u"  Mercury", None))
        self.maj_body_CoOE.setItemText(5, QCoreApplication.translate("MainWindow", u"  Venus", None))
        self.maj_body_CoOE.setItemText(6, QCoreApplication.translate("MainWindow", u"  Mars", None))
        self.maj_body_CoOE.setItemText(7, QCoreApplication.translate("MainWindow", u"  Saturn", None))
        self.maj_body_CoOE.setItemText(8, QCoreApplication.translate("MainWindow", u"  Uranus", None))
        self.maj_body_CoOE.setItemText(9, QCoreApplication.translate("MainWindow", u"  Neptune", None))
        self.maj_body_CoOE.setItemText(10, QCoreApplication.translate("MainWindow", u"  Pluto", None))
        self.maj_body_CoOE.setItemText(11, QCoreApplication.translate("MainWindow", u"  Other", None))

        self.other_body_mass_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"8e24", None))
        self.other_body_radius_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"6378", None))
        self.cal_btn_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_264.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.arg_of_per_unit_coe_n_aoe.setItemText(0, QCoreApplication.translate("MainWindow", u"  Degree", None))
        self.arg_of_per_unit_coe_n_aoe.setItemText(1, QCoreApplication.translate("MainWindow", u"  Radians", None))

        self.RAAN_CoOE_lbl.setText("")
        self.sma_CoOE_lbl.setText(QCoreApplication.translate("MainWindow", u"Semi-major Axis", None))
        self.arg_of_per_coe_n_aoe.setText("")
        self.inclination_coe_n_aoe.setText("")
        self.tru_ano_CoOE_lbl.setText(QCoreApplication.translate("MainWindow", u"True Anamoly", None))
        self.semimajor_axis_coe_n_aoe.setText("")
        self.tru_ana_coe_n_aoe.setText("")
        self.semimajor_axis_unit_coe_n_aoe.setItemText(0, QCoreApplication.translate("MainWindow", u"  km", None))
        self.semimajor_axis_unit_coe_n_aoe.setItemText(1, QCoreApplication.translate("MainWindow", u"  miles", None))
        self.semimajor_axis_unit_coe_n_aoe.setItemText(2, QCoreApplication.translate("MainWindow", u"  AU", None))
        self.semimajor_axis_unit_coe_n_aoe.setItemText(3, QCoreApplication.translate("MainWindow", u"  DU", None))

        self.arg_of_per_CoOE_lbl.setText("")
        self.inclination_unit_coe_n_aoe.setItemText(0, QCoreApplication.translate("MainWindow", u"  Degree", None))
        self.inclination_unit_coe_n_aoe.setItemText(1, QCoreApplication.translate("MainWindow", u"  Radians", None))

        self.RAAN_unit_coe_n_aoe.setItemText(0, QCoreApplication.translate("MainWindow", u"  Degree", None))
        self.RAAN_unit_coe_n_aoe.setItemText(1, QCoreApplication.translate("MainWindow", u"  Radians", None))

        self.tru_ana_unit_coe_n_aoe.setItemText(0, QCoreApplication.translate("MainWindow", u"  Degree", None))
        self.tru_ana_unit_coe_n_aoe.setItemText(1, QCoreApplication.translate("MainWindow", u"  Radians", None))

        self.inc_CoOE_lbl.setText(QCoreApplication.translate("MainWindow", u"Inclination", None))
        self.ecce_CoOE_lbl.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.eccentricity_coe_n_aoe.setText("")
        self.RAAN_coe_n_aoe.setText("")
        self.label_credits.setText("")
    # retranslateUi

