# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home_PagejfCklA.ui'
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
        MainWindow.resize(1077, 674)
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
"border-radius: 15px;\n"
"	\n"
"border-color:rgb(8, 255, 173);\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 4, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 45))
        self.title_bar.setMaximumSize(QSize(16777215, 45))
        self.title_bar.setStyleSheet(u"background-color: None")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
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
        self.horizontalLayout_14.setContentsMargins(10, 0, 0, 0)
        self.Home_btn = QPushButton(self.frame_title)
        self.Home_btn.setObjectName(u"Home_btn")
        self.Home_btn.setMinimumSize(QSize(30, 30))
        self.Home_btn.setMaximumSize(QSize(30, 30))
        self.Home_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px;\n"
"	image:url(UI_Functions/Resources/MOPy Cover_transparent.png);\n"
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

        self.horizontalLayout_14.addWidget(self.Home_btn)

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

        self.btn_go_back_2 = QPushButton(self.frame_title)
        self.btn_go_back_2.setObjectName(u"btn_go_back_2")
        self.btn_go_back_2.setMinimumSize(QSize(35, 35))
        self.btn_go_back_2.setMaximumSize(QSize(35, 35))
        self.btn_go_back_2.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:8px;\n"
"	image:url(UI_Functions/Resources/backk.drawio.png);\n"
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

        self.horizontalLayout_14.addWidget(self.btn_go_back_2)

        self.pushButton_5 = QPushButton(self.frame_title)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(35, 35))
        self.pushButton_5.setMaximumSize(QSize(35, 35))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:8px;\n"
"	image:url(UI_Functions/Resources/Question_Mark.png);\n"
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

        self.horizontalLayout_14.addWidget(self.pushButton_5)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(100, 40))
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
        self.horizontalLayout_70.setContentsMargins(-1, -1, 9, -1)
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(20, 20))
        self.btn_minimize.setMaximumSize(QSize(20, 20))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:8px;\n"
"	image:url(UI_Functions/Resources/Minimize_2.drawio.png);\n"
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
"	image:url(UI_Functions/Resources/Close_2.drawio.png);\n"
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
"border-radius:8px;\n"
"\n"
"}\n"
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
"}\n"
"\n"
"\n"
"\n"
"/*Horizontal Scrollbar*/\n"
"QScrollBar:horizontal{\n"
"border:none;\n"
"background-color:rgb(59, 59, 90);\n"
"width:8px;\n"
"margin: 15px 0 15px 0;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"/* Handle Bar Horizontal *"
                        "/\n"
"QScrollBar::handle:horizontal{\n"
"background-color: rgb(80, 80, 122);\n"
"min-height: 30px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background-color: rgb(108, 87, 134);\n"
"	\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - Scrollbar*/\n"
"QScrollBar::sub-line:horizontal{\n"
"border:none;\n"
"background-color: rgb(59, 59, 90);\n"
"height:15px;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover{\n"
"background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - Scrollbar*/\n"
"QScrollBar::add-line:horizontal{\n"
"border:none;\n"
"background-color: rgb(59, 59, 90);\n"
"height:15px;\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"subcontrol-po"
                        "sition: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover{\n"
"background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed{\n"
"background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW*/\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"border:none;\n"
"background: rgb(78, 79, 132);\n"
"}\n"
"\n"
"")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1039, 630))
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
        self.Home_VPCO = QWidget(self.frame_2)
        self.Home_VPCO.setObjectName(u"Home_VPCO")
        self.Home_VPCO.setMinimumSize(QSize(150, 150))
        self.Home_VPCO.setMaximumSize(QSize(230, 200))
        self.Home_VPCO.setStyleSheet(u"QWidget{\n"
"background-color:#000005;\n"
"image:url(UI_Functions/Resources/Orbits.jpg);\n"
"}	")
        self.verticalLayout_13 = QVBoxLayout(self.Home_VPCO)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Home_VPCO_Filler = QFrame(self.Home_VPCO)
        self.Home_VPCO_Filler.setObjectName(u"Home_VPCO_Filler")
        self.Home_VPCO_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;")
        self.Home_VPCO_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_VPCO_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.Home_VPCO_Filler)

        self.Home_VPCO_Slider = QFrame(self.Home_VPCO)
        self.Home_VPCO_Slider.setObjectName(u"Home_VPCO_Slider")
        self.Home_VPCO_Slider.setMinimumSize(QSize(150, 80))
        self.Home_VPCO_Slider.setMaximumSize(QSize(230, 200))
        self.Home_VPCO_Slider.setStyleSheet(u"background-color: rgba(67, 67, 67, 60%);\n"
"image:none;")
        self.Home_VPCO_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_VPCO_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.Home_VPCO_Slider)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(6, 6, 6, 6)
        self.Home_VPCO_Label = QLabel(self.Home_VPCO_Slider)
        self.Home_VPCO_Label.setObjectName(u"Home_VPCO_Label")
        self.Home_VPCO_Label.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"background-color: rgba(0, 0, 0, 40%);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"text:\"Hu bhai change ho gaya\";\n"
"}")
        self.Home_VPCO_Label.setAlignment(Qt.AlignCenter)
        self.Home_VPCO_Label.setWordWrap(True)

        self.verticalLayout_41.addWidget(self.Home_VPCO_Label)


        self.verticalLayout_13.addWidget(self.Home_VPCO_Slider)


        self.horizontalLayout_4.addWidget(self.Home_VPCO)

        self.Home_Julian_Day = QWidget(self.frame_2)
        self.Home_Julian_Day.setObjectName(u"Home_Julian_Day")
        self.Home_Julian_Day.setMinimumSize(QSize(150, 150))
        self.Home_Julian_Day.setMaximumSize(QSize(230, 200))
        self.Home_Julian_Day.setStyleSheet(u"background-color:#e1a2b4;\n"
"image:url(UI_Functions/Resources/Julian_Day.png);")
        self.verticalLayout_32 = QVBoxLayout(self.Home_Julian_Day)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.Home_Julian_Day_Filler = QFrame(self.Home_Julian_Day)
        self.Home_Julian_Day_Filler.setObjectName(u"Home_Julian_Day_Filler")
        self.Home_Julian_Day_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.Home_Julian_Day_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Julian_Day_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_32.addWidget(self.Home_Julian_Day_Filler)

        self.Home_Julian_Day_Slider = QFrame(self.Home_Julian_Day)
        self.Home_Julian_Day_Slider.setObjectName(u"Home_Julian_Day_Slider")
        self.Home_Julian_Day_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Julian_Day_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Julian_Day_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.Home_Julian_Day_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_Julian_Day_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.Home_Julian_Day_Slider)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(6, 6, 6, 6)
        self.Home_Julian_Day_Label = QLabel(self.Home_Julian_Day_Slider)
        self.Home_Julian_Day_Label.setObjectName(u"Home_Julian_Day_Label")
        self.Home_Julian_Day_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 40%);\n"
"")
        self.Home_Julian_Day_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.Home_Julian_Day_Label)


        self.verticalLayout_32.addWidget(self.Home_Julian_Day_Slider)


        self.horizontalLayout_4.addWidget(self.Home_Julian_Day)

        self.Home_Orbital_Elements = QWidget(self.frame_2)
        self.Home_Orbital_Elements.setObjectName(u"Home_Orbital_Elements")
        self.Home_Orbital_Elements.setMinimumSize(QSize(150, 150))
        self.Home_Orbital_Elements.setMaximumSize(QSize(230, 200))
        self.Home_Orbital_Elements.setStyleSheet(u"background-color:#081026;\n"
"image:url(UI_Functions/Resources/Orbital_Elements.png);")
        self.verticalLayout_36 = QVBoxLayout(self.Home_Orbital_Elements)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.Home_Orbital_Elements_Filler = QFrame(self.Home_Orbital_Elements)
        self.Home_Orbital_Elements_Filler.setObjectName(u"Home_Orbital_Elements_Filler")
        self.Home_Orbital_Elements_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;")
        self.Home_Orbital_Elements_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Orbital_Elements_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_36.addWidget(self.Home_Orbital_Elements_Filler)

        self.Home_Orbital_Elements_Slider = QFrame(self.Home_Orbital_Elements)
        self.Home_Orbital_Elements_Slider.setObjectName(u"Home_Orbital_Elements_Slider")
        self.Home_Orbital_Elements_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Orbital_Elements_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Orbital_Elements_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,30%);\n"
"image:none;")
        self.Home_Orbital_Elements_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_Orbital_Elements_Slider.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Home_Orbital_Elements_Slider)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.Home_Orbital_Elements_Label = QLabel(self.Home_Orbital_Elements_Slider)
        self.Home_Orbital_Elements_Label.setObjectName(u"Home_Orbital_Elements_Label")
        self.Home_Orbital_Elements_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 40%);")
        self.Home_Orbital_Elements_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.Home_Orbital_Elements_Label)


        self.verticalLayout_36.addWidget(self.Home_Orbital_Elements_Slider)


        self.horizontalLayout_4.addWidget(self.Home_Orbital_Elements)

        self.Home_SOI = QWidget(self.frame_2)
        self.Home_SOI.setObjectName(u"Home_SOI")
        self.Home_SOI.setMinimumSize(QSize(150, 150))
        self.Home_SOI.setMaximumSize(QSize(230, 200))
        self.Home_SOI.setStyleSheet(u"background-color:#010008;\n"
"image:url(UI_Functions/Resources/SOI.jpg);")
        self.verticalLayout_37 = QVBoxLayout(self.Home_SOI)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.Home_SOI_Filler = QFrame(self.Home_SOI)
        self.Home_SOI_Filler.setObjectName(u"Home_SOI_Filler")
        self.Home_SOI_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;")
        self.Home_SOI_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_SOI_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_37.addWidget(self.Home_SOI_Filler)

        self.Home_SOI_Slider = QFrame(self.Home_SOI)
        self.Home_SOI_Slider.setObjectName(u"Home_SOI_Slider")
        self.Home_SOI_Slider.setMinimumSize(QSize(150, 80))
        self.Home_SOI_Slider.setMaximumSize(QSize(230, 200))
        self.Home_SOI_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.Home_SOI_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_SOI_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.Home_SOI_Slider)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(6, 6, 6, 6)
        self.Home_SOI_Label = QLabel(self.Home_SOI_Slider)
        self.Home_SOI_Label.setObjectName(u"Home_SOI_Label")
        self.Home_SOI_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 60%);")
        self.Home_SOI_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.Home_SOI_Label)


        self.verticalLayout_37.addWidget(self.Home_SOI_Slider)


        self.horizontalLayout_4.addWidget(self.Home_SOI)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 200))
        self.frame_8.setMaximumSize(QSize(16777215, 250))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Home_Orbit_Visualization = QWidget(self.frame_8)
        self.Home_Orbit_Visualization.setObjectName(u"Home_Orbit_Visualization")
        self.Home_Orbit_Visualization.setMinimumSize(QSize(150, 150))
        self.Home_Orbit_Visualization.setMaximumSize(QSize(230, 200))
        self.Home_Orbit_Visualization.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(44, 61, 146, 255), stop:1 rgba(35, 51, 126, 255));\n"
"image:url(UI_Functions/Resources/Orbit_Visualization.png);")
        self.verticalLayout_33 = QVBoxLayout(self.Home_Orbit_Visualization)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Home_Orbit_Visualization_Filler = QFrame(self.Home_Orbit_Visualization)
        self.Home_Orbit_Visualization_Filler.setObjectName(u"Home_Orbit_Visualization_Filler")
        self.Home_Orbit_Visualization_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.Home_Orbit_Visualization_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Orbit_Visualization_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.Home_Orbit_Visualization_Filler)

        self.Home_Orbit_Visualization_Slider = QFrame(self.Home_Orbit_Visualization)
        self.Home_Orbit_Visualization_Slider.setObjectName(u"Home_Orbit_Visualization_Slider")
        self.Home_Orbit_Visualization_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Orbit_Visualization_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Orbit_Visualization_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.Home_Orbit_Visualization_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_Orbit_Visualization_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.Home_Orbit_Visualization_Slider)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(6, 6, 6, 6)
        self.Home_Orbit_Visualization_Label = QLabel(self.Home_Orbit_Visualization_Slider)
        self.Home_Orbit_Visualization_Label.setObjectName(u"Home_Orbit_Visualization_Label")
        self.Home_Orbit_Visualization_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 40%);\n"
"")
        self.Home_Orbit_Visualization_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.Home_Orbit_Visualization_Label)


        self.verticalLayout_33.addWidget(self.Home_Orbit_Visualization_Slider)


        self.horizontalLayout_8.addWidget(self.Home_Orbit_Visualization)

        self.Home_Ground_Track = QWidget(self.frame_8)
        self.Home_Ground_Track.setObjectName(u"Home_Ground_Track")
        self.Home_Ground_Track.setMinimumSize(QSize(150, 150))
        self.Home_Ground_Track.setMaximumSize(QSize(230, 200))
        self.Home_Ground_Track.setStyleSheet(u"background-color:#eef3f9;\n"
"image:url(UI_Functions/Resources/Ground_track.png);")
        self.verticalLayout_34 = QVBoxLayout(self.Home_Ground_Track)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Home_Ground_Track_Filler = QFrame(self.Home_Ground_Track)
        self.Home_Ground_Track_Filler.setObjectName(u"Home_Ground_Track_Filler")
        self.Home_Ground_Track_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.Home_Ground_Track_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Ground_Track_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_34.addWidget(self.Home_Ground_Track_Filler)

        self.Home_Ground_Track_Slider = QFrame(self.Home_Ground_Track)
        self.Home_Ground_Track_Slider.setObjectName(u"Home_Ground_Track_Slider")
        self.Home_Ground_Track_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Ground_Track_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Ground_Track_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.Home_Ground_Track_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_Ground_Track_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.Home_Ground_Track_Slider)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(6, 6, 6, 6)
        self.Home_Ground_Track_Label = QLabel(self.Home_Ground_Track_Slider)
        self.Home_Ground_Track_Label.setObjectName(u"Home_Ground_Track_Label")
        self.Home_Ground_Track_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 40%);\n"
"")
        self.Home_Ground_Track_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.Home_Ground_Track_Label)


        self.verticalLayout_34.addWidget(self.Home_Ground_Track_Slider)


        self.horizontalLayout_8.addWidget(self.Home_Ground_Track)

        self.Home_Planet_in_Shadow = QWidget(self.frame_8)
        self.Home_Planet_in_Shadow.setObjectName(u"Home_Planet_in_Shadow")
        self.Home_Planet_in_Shadow.setMinimumSize(QSize(150, 150))
        self.Home_Planet_in_Shadow.setMaximumSize(QSize(230, 200))
        self.Home_Planet_in_Shadow.setStyleSheet(u"background-color:#000002;\n"
"image:url(UI_Functions/Resources/DSPS.png);")
        self.verticalLayout_35 = QVBoxLayout(self.Home_Planet_in_Shadow)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Home_Planet_in_Shadow_Filler = QFrame(self.Home_Planet_in_Shadow)
        self.Home_Planet_in_Shadow_Filler.setObjectName(u"Home_Planet_in_Shadow_Filler")
        self.Home_Planet_in_Shadow_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.Home_Planet_in_Shadow_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Planet_in_Shadow_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_35.addWidget(self.Home_Planet_in_Shadow_Filler)

        self.Home_Planet_in_Shadow_Slider = QFrame(self.Home_Planet_in_Shadow)
        self.Home_Planet_in_Shadow_Slider.setObjectName(u"Home_Planet_in_Shadow_Slider")
        self.Home_Planet_in_Shadow_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Planet_in_Shadow_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Planet_in_Shadow_Slider.setStyleSheet(u"background-color: rgba(47, 47, 48, 50%);\n"
"image:none;")
        self.Home_Planet_in_Shadow_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_Planet_in_Shadow_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.Home_Planet_in_Shadow_Slider)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(6, 6, 6, 6)
        self.Home_Planet_in_Shadow_Label = QLabel(self.Home_Planet_in_Shadow_Slider)
        self.Home_Planet_in_Shadow_Label.setObjectName(u"Home_Planet_in_Shadow_Label")
        self.Home_Planet_in_Shadow_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 40%);\n"
"")
        self.Home_Planet_in_Shadow_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.Home_Planet_in_Shadow_Label)


        self.verticalLayout_35.addWidget(self.Home_Planet_in_Shadow_Slider)


        self.horizontalLayout_8.addWidget(self.Home_Planet_in_Shadow)

        self.Home_Planetary_Ephimeris = QWidget(self.frame_8)
        self.Home_Planetary_Ephimeris.setObjectName(u"Home_Planetary_Ephimeris")
        self.Home_Planetary_Ephimeris.setMinimumSize(QSize(150, 150))
        self.Home_Planetary_Ephimeris.setMaximumSize(QSize(230, 200))
        self.Home_Planetary_Ephimeris.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.597, x2:1, y2:0.08, stop:0 rgba(17, 24, 66, 255), stop:1 rgba(11, 11, 11, 255));\n"
"image:url(UI_Functions/Resources/Planetary_Ephemeris.jpg);")
        self.verticalLayout_40 = QVBoxLayout(self.Home_Planetary_Ephimeris)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Home_Planetary_Ephimeris_Filler = QFrame(self.Home_Planetary_Ephimeris)
        self.Home_Planetary_Ephimeris_Filler.setObjectName(u"Home_Planetary_Ephimeris_Filler")
        self.Home_Planetary_Ephimeris_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;")
        self.Home_Planetary_Ephimeris_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Planetary_Ephimeris_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_40.addWidget(self.Home_Planetary_Ephimeris_Filler)

        self.Home_Planetary_Ephimeris_Slider = QFrame(self.Home_Planetary_Ephimeris)
        self.Home_Planetary_Ephimeris_Slider.setObjectName(u"Home_Planetary_Ephimeris_Slider")
        self.Home_Planetary_Ephimeris_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Planetary_Ephimeris_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Planetary_Ephimeris_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.Home_Planetary_Ephimeris_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_Planetary_Ephimeris_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.Home_Planetary_Ephimeris_Slider)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(6, 6, 6, 6)
        self.Home_Planetary_Ephimeris_Label = QLabel(self.Home_Planetary_Ephimeris_Slider)
        self.Home_Planetary_Ephimeris_Label.setObjectName(u"Home_Planetary_Ephimeris_Label")
        self.Home_Planetary_Ephimeris_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 60%);\n"
"")
        self.Home_Planetary_Ephimeris_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.Home_Planetary_Ephimeris_Label)


        self.verticalLayout_40.addWidget(self.Home_Planetary_Ephimeris_Slider)


        self.horizontalLayout_8.addWidget(self.Home_Planetary_Ephimeris)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 200))
        self.frame_15.setMaximumSize(QSize(16777215, 250))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.Home_Numerical_integ = QWidget(self.frame_15)
        self.Home_Numerical_integ.setObjectName(u"Home_Numerical_integ")
        self.Home_Numerical_integ.setMinimumSize(QSize(150, 150))
        self.Home_Numerical_integ.setMaximumSize(QSize(230, 200))
        self.Home_Numerical_integ.setStyleSheet(u"background-color:#000001;\n"
"image:url(UI_Functions/Resources/Numerical_Integration.jpg);")
        self.verticalLayout_38 = QVBoxLayout(self.Home_Numerical_integ)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Home_Numerical_integ_Filler = QFrame(self.Home_Numerical_integ)
        self.Home_Numerical_integ_Filler.setObjectName(u"Home_Numerical_integ_Filler")
        self.Home_Numerical_integ_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.Home_Numerical_integ_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Numerical_integ_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.Home_Numerical_integ_Filler)

        self.Home_Numerical_integ_Slider = QFrame(self.Home_Numerical_integ)
        self.Home_Numerical_integ_Slider.setObjectName(u"Home_Numerical_integ_Slider")
        self.Home_Numerical_integ_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Numerical_integ_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Numerical_integ_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.Home_Numerical_integ_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_Numerical_integ_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.Home_Numerical_integ_Slider)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(6, 6, 6, 6)
        self.Home_Numerical_integ_Label = QLabel(self.Home_Numerical_integ_Slider)
        self.Home_Numerical_integ_Label.setObjectName(u"Home_Numerical_integ_Label")
        self.Home_Numerical_integ_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 40%);\n"
"")
        self.Home_Numerical_integ_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.Home_Numerical_integ_Label)


        self.verticalLayout_38.addWidget(self.Home_Numerical_integ_Slider)


        self.horizontalLayout_72.addWidget(self.Home_Numerical_integ)

        self.Home_Eulers_Angle = QWidget(self.frame_15)
        self.Home_Eulers_Angle.setObjectName(u"Home_Eulers_Angle")
        self.Home_Eulers_Angle.setMinimumSize(QSize(475, 0))
        self.Home_Eulers_Angle.setMaximumSize(QSize(475, 16777215))
        self.Home_Eulers_Angle.setStyleSheet(u"background-color:#000001;\n"
"image:url(UI_Functions/Resources/Eulers Angle.png);")
        self.horizontalLayout_75 = QHBoxLayout(self.Home_Eulers_Angle)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.Home_Eulers_Angle_Filler = QFrame(self.Home_Eulers_Angle)
        self.Home_Eulers_Angle_Filler.setObjectName(u"Home_Eulers_Angle_Filler")
        self.Home_Eulers_Angle_Filler.setAutoFillBackground(False)
        self.Home_Eulers_Angle_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.Home_Eulers_Angle_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Eulers_Angle_Filler.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_75.addWidget(self.Home_Eulers_Angle_Filler)

        self.Home_Eulers_Angle_Slider = QFrame(self.Home_Eulers_Angle)
        self.Home_Eulers_Angle_Slider.setObjectName(u"Home_Eulers_Angle_Slider")
        self.Home_Eulers_Angle_Slider.setStyleSheet(u"background-color: rgba(47, 47, 48, 60%);\n"
"image:none;")
        self.Home_Eulers_Angle_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_Eulers_Angle_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.Home_Eulers_Angle_Slider)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(6, 6, 6, 6)
        self.Home_Eulers_Angle_Label = QLabel(self.Home_Eulers_Angle_Slider)
        self.Home_Eulers_Angle_Label.setObjectName(u"Home_Eulers_Angle_Label")
        self.Home_Eulers_Angle_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 40%);\n"
"")
        self.Home_Eulers_Angle_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.Home_Eulers_Angle_Label)


        self.horizontalLayout_75.addWidget(self.Home_Eulers_Angle_Slider)


        self.horizontalLayout_72.addWidget(self.Home_Eulers_Angle)

        self.Home_Orbital_transfer = QWidget(self.frame_15)
        self.Home_Orbital_transfer.setObjectName(u"Home_Orbital_transfer")
        self.Home_Orbital_transfer.setMinimumSize(QSize(150, 150))
        self.Home_Orbital_transfer.setMaximumSize(QSize(230, 200))
        self.Home_Orbital_transfer.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(77, 169, 244, 255), stop:1 rgba(49, 96, 218, 255));\n"
"image:url(UI_Functions/Resources/Orbital Transfer.png);")
        self.verticalLayout_39 = QVBoxLayout(self.Home_Orbital_transfer)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.Home_Orbital_transfer_Filler = QFrame(self.Home_Orbital_transfer)
        self.Home_Orbital_transfer_Filler.setObjectName(u"Home_Orbital_transfer_Filler")
        self.Home_Orbital_transfer_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.Home_Orbital_transfer_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Orbital_transfer_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_39.addWidget(self.Home_Orbital_transfer_Filler)

        self.Home_Orbital_transfer_Slider = QFrame(self.Home_Orbital_transfer)
        self.Home_Orbital_transfer_Slider.setObjectName(u"Home_Orbital_transfer_Slider")
        self.Home_Orbital_transfer_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Orbital_transfer_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Orbital_transfer_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.Home_Orbital_transfer_Slider.setFrameShape(QFrame.StyledPanel)
        self.Home_Orbital_transfer_Slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.Home_Orbital_transfer_Slider)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(6, 6, 6, 6)
        self.Home_Orbital_transfer_Label = QLabel(self.Home_Orbital_transfer_Slider)
        self.Home_Orbital_transfer_Label.setObjectName(u"Home_Orbital_transfer_Label")
        self.Home_Orbital_transfer_Label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(0, 0, 0, 40%);\n"
"")
        self.Home_Orbital_transfer_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.Home_Orbital_transfer_Label)


        self.verticalLayout_39.addWidget(self.Home_Orbital_transfer_Slider)


        self.horizontalLayout_72.addWidget(self.Home_Orbital_transfer)


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
        self.verticalLayout_5.setContentsMargins(7, 0, 7, 0)
        self.frame_content_Julian_calculation = QFrame(self.Julian_Day_Screen)
        self.frame_content_Julian_calculation.setObjectName(u"frame_content_Julian_calculation")
        self.frame_content_Julian_calculation.setStyleSheet(u"QFrame{background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));}\n"
"")
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
        self.frame_14.setStyleSheet(u"background:none;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.frame_14)

        self.frame_9 = QFrame(self.frame_content_Julian_calculation)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setStyleSheet(u"background:none;")
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
"	\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	background-color:#c98cff;\n"
"	border: 8px solid transparent;\n"
"	\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 2px solid rgba(168, 128, 243, 60%);\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.type_of_calendar, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame_18 = QFrame(self.frame_content_Julian_calculation)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 20))
        self.frame_18.setMaximumSize(QSize(16777215, 20))
        self.frame_18.setStyleSheet(u"background:none;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_24 = QFrame(self.frame_18)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(0, 0, 16, 20))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
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
        font3 = QFont()
        font3.setPointSize(10)
        self.Error_state.setFont(font3)
        self.Error_state.setStyleSheet(u"color:rgb(255, 0, 0);")

        self.verticalLayout_17.addWidget(self.Error_state)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.frame = QFrame(self.frame_content_Julian_calculation)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 280))
        self.frame.setStyleSheet(u"background:none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background:none;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_84.setSpacing(40)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(40, 40, 40, 40)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(320, 250))
        self.frame_7.setMaximumSize(QSize(360, 250))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"\n"
"border: transparent;\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(168, 128, 243, 255), stop:1 rgba(108, 121, 240, 255));\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 4px solid rgba(168, 128, 243, 60%);\n"
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
"	background-color: green;\n"
"	border: 2px solid black;\n"
"	border-radius:4px;\n"
"\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView\n"
"{\n"
"background-color: rgb(192,192,192); \n"
"selection-background-color: rgb(0, 170, 0, 60%);\n"
"selection-border: 1px solid black;\n"
"selection-border-radius:2px;\n"
"selection-color: black; \n"
"border:2px solid black;\n"
"border-radius:4px;\n"
"}")

        self.horizontalLayout_13.addWidget(self.calendarWidget)


        self.horizontalLayout_84.addWidget(self.frame_7)

        self.Date_time_frame = QFrame(self.frame_5)
        self.Date_time_frame.setObjectName(u"Date_time_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Date_time_frame.sizePolicy().hasHeightForWidth())
        self.Date_time_frame.setSizePolicy(sizePolicy1)
        self.Date_time_frame.setMinimumSize(QSize(320, 250))
        self.Date_time_frame.setMaximumSize(QSize(340, 250))
        font4 = QFont()
        font4.setPointSize(15)
        self.Date_time_frame.setFont(font4)
        self.Date_time_frame.setStyleSheet(u"QFrame{\n"
"\n"
"border: transparent;\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(168, 128, 243, 255), stop:1 rgba(108, 121, 240, 255));\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 4px solid rgba(168, 128, 243, 60%);\n"
"}")
        self.Date_time_frame.setFrameShape(QFrame.NoFrame)
        self.Date_time_frame.setFrameShadow(QFrame.Raised)
        self.digits_accuracy = QSpinBox(self.Date_time_frame)
        self.digits_accuracy.setObjectName(u"digits_accuracy")
        self.digits_accuracy.setGeometry(QRect(230, 120, 61, 31))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setWeight(50)
        self.digits_accuracy.setFont(font5)
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
"	QSpinBox{\n"
"	\n"
"	background-color: rgb(201, 140, 255);\n"
"}")
        self.digits_accuracy.setAlignment(Qt.AlignCenter)
        self.digits_accuracy.setMaximum(8)
        self.label = QLabel(self.Date_time_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 111, 16))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setWeight(75)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.timeEdit = QTimeEdit(self.Date_time_frame)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(130, 30, 141, 31))
        self.timeEdit.setFont(font4)
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
"    }\n"
"	QTimeEdit{\n"
"	\n"
"	background-color: rgb(201, 140, 255);\n"
"}")
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.label_2 = QLabel(self.Date_time_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 35, 31, 21))
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.Date_time_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 70, 101, 16))
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.label_4 = QLabel(self.Date_time_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 171, 31))
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.calculate_btn = QPushButton(self.Date_time_frame)
        self.calculate_btn.setObjectName(u"calculate_btn")
        self.calculate_btn.setGeometry(QRect(100, 192, 151, 31))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.calculate_btn.setFont(font7)
        self.calculate_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 14px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0,60%);\n"
"}")

        self.horizontalLayout_84.addWidget(self.Date_time_frame)


        self.horizontalLayout_6.addWidget(self.frame_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_content_Julian_calculation)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 170))
        self.frame_4.setStyleSheet(u"background:none;")
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
        self.frame_20.setStyleSheet(u"background:none;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(0, 0, 10, 20))
        self.frame_25.setMinimumSize(QSize(10, 0))
        self.frame_25.setMaximumSize(QSize(10, 16777215))
        self.frame_25.setStyleSheet(u"background:none;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background:none;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background:none;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_22)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(350, 0))
        self.frame_21.setMaximumSize(QSize(350, 16777215))
        self.frame_21.setStyleSheet(u"background:none;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_34 = QWidget(self.frame_21)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMinimumSize(QSize(280, 35))
        self.widget_34.setMaximumSize(QSize(250, 35))
        self.widget_34.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_190 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_190.setSpacing(3)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(0, 0, 0, 0)
        self.frame_124 = QFrame(self.widget_34)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMinimumSize(QSize(130, 35))
        self.frame_124.setMaximumSize(QSize(250, 16777215))
        self.frame_124.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_191 = QHBoxLayout(self.frame_124)
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.horizontalLayout_191.setContentsMargins(6, 6, 6, 6)
        self.label_174 = QLabel(self.frame_124)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setMinimumSize(QSize(100, 20))
        self.label_174.setMaximumSize(QSize(125, 20))
        self.label_174.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_174.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_191.addWidget(self.label_174)


        self.horizontalLayout_190.addWidget(self.frame_124, 0, Qt.AlignVCenter)

        self.frame_125 = QFrame(self.widget_34)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_192 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.horizontalLayout_192.setContentsMargins(6, 6, 6, 6)
        self.JulianDay_Result = QLabel(self.frame_125)
        self.JulianDay_Result.setObjectName(u"JulianDay_Result")
        self.JulianDay_Result.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.JulianDay_Result.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_192.addWidget(self.JulianDay_Result)

        self.label_176 = QLabel(self.frame_125)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setMinimumSize(QSize(30, 0))
        self.label_176.setMaximumSize(QSize(45, 16777215))
        self.label_176.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_192.addWidget(self.label_176)


        self.horizontalLayout_190.addWidget(self.frame_125)


        self.horizontalLayout_12.addWidget(self.widget_34)


        self.horizontalLayout_11.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_23)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(304, 102, 31, 31))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:8px;\n"
"	image:url(UI_Functions/Resources/Question_Mark.png);\n"
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
"	background-color:rgba(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0,60%);\n"
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
        self.frame_36 = QFrame(self.frame_28)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(270, 0, 534, 213))
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
"	background-color:rgba(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0,60%);\n"
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
        self.pushButton_2 = QPushButton(self.frame_28)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1030, 180, 31, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:8px;\n"
"	image:url(UI_Functions/Resources/Question_Mark.png);\n"
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

        self.verticalLayout_16.addWidget(self.frame_28)


        self.horizontalLayout_17.addWidget(self.SOI_frame_content)

        self.stackedWidget.addWidget(self.SOI_Screen)
        self.VPCO_input = QWidget()
        self.VPCO_input.setObjectName(u"VPCO_input")
        self.verticalLayout_20 = QVBoxLayout(self.VPCO_input)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.VPCO_Outer_Frame = QFrame(self.VPCO_input)
        self.VPCO_Outer_Frame.setObjectName(u"VPCO_Outer_Frame")
        self.VPCO_Outer_Frame.setStyleSheet(u"QTabWidget{\n"
"	\n"
"	background-color: rgb(115, 118, 199);\n"
"	/*border: 2px solid #ff99ff;*/\n"
"	\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(78, 79, 132);\n"
"}")
        self.VPCO_Outer_Frame.setFrameShape(QFrame.StyledPanel)
        self.VPCO_Outer_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.VPCO_Outer_Frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.VPCO_tabs = QTabWidget(self.VPCO_Outer_Frame)
        self.VPCO_tabs.setObjectName(u"VPCO_tabs")
        font10 = QFont()
        font10.setFamily(u"Calibri")
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setWeight(75)
        self.VPCO_tabs.setFont(font10)
        self.VPCO_tabs.setStyleSheet(u"")
        self.VPCO_tabs.setTabPosition(QTabWidget.North)
        self.VPCO_tabs.setTabShape(QTabWidget.Rounded)
        self.VPCO_tabs.setElideMode(Qt.ElideLeft)
        self.VPCO_tabs.setDocumentMode(True)
        self.VPCO_tabs.setMovable(True)
        self.a_and_e_tab = QWidget()
        self.a_and_e_tab.setObjectName(u"a_and_e_tab")
        self.a_and_e_tab.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.a_and_e_tab)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.a_and_e_tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_3)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, -1, 0, -1)
        self.tab_container_frame_for_a_and_e = QFrame(self.frame_3)
        self.tab_container_frame_for_a_and_e.setObjectName(u"tab_container_frame_for_a_and_e")
        self.tab_container_frame_for_a_and_e.setStyleSheet(u"background-color:transparent;")
        self.tab_container_frame_for_a_and_e.setFrameShape(QFrame.StyledPanel)
        self.tab_container_frame_for_a_and_e.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.tab_container_frame_for_a_and_e)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.a_and_e_VPCO = QFrame(self.tab_container_frame_for_a_and_e)
        self.a_and_e_VPCO.setObjectName(u"a_and_e_VPCO")
        self.a_and_e_VPCO.setMinimumSize(QSize(526, 0))
        self.a_and_e_VPCO.setMaximumSize(QSize(526, 16777215))
        self.a_and_e_VPCO.setStyleSheet(u"background-color:transparent;")
        self.a_and_e_VPCO.setFrameShape(QFrame.StyledPanel)
        self.a_and_e_VPCO.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.a_and_e_VPCO)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.VPCO_Input_Stack = QStackedWidget(self.a_and_e_VPCO)
        self.VPCO_Input_Stack.setObjectName(u"VPCO_Input_Stack")
        self.VPCO_Input_Stack.setStyleSheet(u"border:none;")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_109 = QHBoxLayout(self.page_3)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.frame_29 = QFrame(self.page_3)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(528, 16777215))
        self.frame_29.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_29)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(9, -1, -1, -1)
        self.verticalSpacer_15 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_15)

        self.frame_56 = QFrame(self.frame_29)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_56)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.widget_2 = QWidget(self.frame_56)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(410, 50))
        self.widget_2.setMaximumSize(QSize(410, 60))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.widget_2)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(225, 0))
        self.frame_30.setMaximumSize(QSize(250, 16777215))
        self.frame_30.setStyleSheet(u"background:none;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_9 = QLabel(self.frame_30)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 30))
        self.label_9.setMaximumSize(QSize(200, 16777215))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_9)


        self.horizontalLayout_10.addWidget(self.frame_30)

        self.frame_38 = QFrame(self.widget_2)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background:none;")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 9, 9, 9)
        self.VPCO_Input_a_lineedit = QLineEdit(self.frame_38)
        self.VPCO_Input_a_lineedit.setObjectName(u"VPCO_Input_a_lineedit")
        self.VPCO_Input_a_lineedit.setMinimumSize(QSize(130, 40))
        self.VPCO_Input_a_lineedit.setMaximumSize(QSize(200, 50))
        self.VPCO_Input_a_lineedit.setLayoutDirection(Qt.RightToLeft)
        self.VPCO_Input_a_lineedit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:10px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.VPCO_Input_a_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.VPCO_Input_a_lineedit)

        self.label_109 = QLabel(self.frame_38)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(30, 0))
        self.label_109.setMaximumSize(QSize(45, 16777215))
        font11 = QFont()
        font11.setBold(True)
        font11.setWeight(75)
        self.label_109.setFont(font11)
        self.label_109.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_23.addWidget(self.label_109)


        self.horizontalLayout_10.addWidget(self.frame_38)


        self.verticalLayout_75.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.frame_56)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(410, 50))
        self.widget_3.setMaximumSize(QSize(410, 60))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"}")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.widget_3)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(225, 0))
        self.frame_39.setMaximumSize(QSize(250, 16777215))
        self.frame_39.setStyleSheet(u"background:none;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_12 = QLabel(self.frame_39)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 30))
        self.label_12.setMaximumSize(QSize(200, 16777215))
        self.label_12.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.label_12)


        self.horizontalLayout_78.addWidget(self.frame_39)

        self.frame_44 = QFrame(self.widget_3)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"background:none;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(-1, -1, 45, -1)
        self.VPCO_Input_e_lineedit = QLineEdit(self.frame_44)
        self.VPCO_Input_e_lineedit.setObjectName(u"VPCO_Input_e_lineedit")
        self.VPCO_Input_e_lineedit.setMinimumSize(QSize(130, 40))
        self.VPCO_Input_e_lineedit.setMaximumSize(QSize(200, 50))
        self.VPCO_Input_e_lineedit.setLayoutDirection(Qt.RightToLeft)
        self.VPCO_Input_e_lineedit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:10px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.VPCO_Input_e_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_80.addWidget(self.VPCO_Input_e_lineedit)


        self.horizontalLayout_78.addWidget(self.frame_44)


        self.verticalLayout_75.addWidget(self.widget_3, 0, Qt.AlignHCenter)


        self.verticalLayout_53.addWidget(self.frame_56)

        self.verticalSpacer_13 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_13)

        self.frame_47 = QFrame(self.frame_29)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 40))
        self.frame_47.setMaximumSize(QSize(16777215, 40))
        self.frame_47.setStyleSheet(u"border:none;\n"
"background:none;")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.maj_body_CoOE_2 = QComboBox(self.frame_47)
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.addItem("")
        self.maj_body_CoOE_2.setObjectName(u"maj_body_CoOE_2")
        self.maj_body_CoOE_2.setMinimumSize(QSize(300, 40))
        self.maj_body_CoOE_2.setMaximumSize(QSize(350, 40))
        self.maj_body_CoOE_2.setStyleSheet(u"QComboBox{\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:12px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"\n"
"QComboBoxt:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")

        self.horizontalLayout_82.addWidget(self.maj_body_CoOE_2)


        self.verticalLayout_53.addWidget(self.frame_47)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_24)

        self.VPCO_Submit_button = QPushButton(self.frame_29)
        self.VPCO_Submit_button.setObjectName(u"VPCO_Submit_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.VPCO_Submit_button.sizePolicy().hasHeightForWidth())
        self.VPCO_Submit_button.setSizePolicy(sizePolicy2)
        self.VPCO_Submit_button.setMinimumSize(QSize(125, 40))
        self.VPCO_Submit_button.setMaximumSize(QSize(150, 80))
        self.VPCO_Submit_button.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:10px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:rgb(175, 101, 174);\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"")

        self.verticalLayout_53.addWidget(self.VPCO_Submit_button, 0, Qt.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_14)


        self.horizontalLayout_109.addWidget(self.frame_29)

        self.VPCO_Input_Stack.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_60 = QVBoxLayout(self.page_4)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.frame_88 = QFrame(self.page_4)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMaximumSize(QSize(528, 16777215))
        self.frame_88.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 255), stop:1 rgba(161, 161, 161, 255));\n"
"	\n"
"\n"
"}")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_88)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.frame_89 = QFrame(self.frame_88)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_158 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_158.setSpacing(6)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.frame_90 = QFrame(self.frame_89)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(125, 0))
        self.frame_90.setMaximumSize(QSize(125, 16777215))
        self.frame_90.setStyleSheet(u"background:transparent;\n"
"border:1px solid  rgb(136, 136, 136);\n"
"")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_90)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.semi_major_axis_toggle_menu_lbl_4 = QLabel(self.frame_90)
        self.semi_major_axis_toggle_menu_lbl_4.setObjectName(u"semi_major_axis_toggle_menu_lbl_4")
        self.semi_major_axis_toggle_menu_lbl_4.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_4.setMaximumSize(QSize(16777215, 20))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setWeight(75)
        self.semi_major_axis_toggle_menu_lbl_4.setFont(font12)
        self.semi_major_axis_toggle_menu_lbl_4.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.semi_major_axis_toggle_menu_lbl_4)

        self.eccentricity_toggle_menu_spinbox_3 = QDoubleSpinBox(self.frame_90)
        self.eccentricity_toggle_menu_spinbox_3.setObjectName(u"eccentricity_toggle_menu_spinbox_3")
        self.eccentricity_toggle_menu_spinbox_3.setMinimumSize(QSize(80, 0))
        self.eccentricity_toggle_menu_spinbox_3.setMaximumSize(QSize(80, 16777215))
        self.eccentricity_toggle_menu_spinbox_3.setStyleSheet(u"    /*spinbox lift style*/\n"
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
        self.eccentricity_toggle_menu_spinbox_3.setAlignment(Qt.AlignCenter)
        self.eccentricity_toggle_menu_spinbox_3.setMinimum(0.000000000000000)
        self.eccentricity_toggle_menu_spinbox_3.setMaximum(50000000.000000000000000)

        self.verticalLayout_61.addWidget(self.eccentricity_toggle_menu_spinbox_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_158.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.frame_89)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"background:transparent;\n"
"border:1px solid  rgb(136, 136, 136);\n"
"")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.ecce_dial_3 = QDial(self.frame_91)
        self.ecce_dial_3.setObjectName(u"ecce_dial_3")
        self.ecce_dial_3.setMinimumSize(QSize(75, 75))
        self.ecce_dial_3.setMaximumSize(QSize(75, 75))
        self.ecce_dial_3.setMaximum(10)
        self.ecce_dial_3.setNotchesVisible(True)

        self.horizontalLayout_147.addWidget(self.ecce_dial_3)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(-1, 10, -1, 0)
        self.label_103 = QLabel(self.frame_91)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(100, 20))
        self.label_103.setMaximumSize(QSize(125, 20))
        self.label_103.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_103.setAlignment(Qt.AlignCenter)

        self.verticalLayout_59.addWidget(self.label_103, 0, Qt.AlignHCenter)

        self.eccentricity_toggle_menu_slider_3 = QSlider(self.frame_91)
        self.eccentricity_toggle_menu_slider_3.setObjectName(u"eccentricity_toggle_menu_slider_3")
        self.eccentricity_toggle_menu_slider_3.setStyleSheet(u"\n"
"border:none;")
        self.eccentricity_toggle_menu_slider_3.setMaximum(7)
        self.eccentricity_toggle_menu_slider_3.setValue(0)
        self.eccentricity_toggle_menu_slider_3.setSliderPosition(0)
        self.eccentricity_toggle_menu_slider_3.setOrientation(Qt.Horizontal)
        self.eccentricity_toggle_menu_slider_3.setTickPosition(QSlider.TicksAbove)
        self.eccentricity_toggle_menu_slider_3.setTickInterval(1)

        self.verticalLayout_59.addWidget(self.eccentricity_toggle_menu_slider_3)

        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setSpacing(0)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.label_106 = QLabel(self.frame_91)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(70, 20))
        self.label_106.setMaximumSize(QSize(80, 20))
        self.label_106.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_106.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_149.addWidget(self.label_106)

        self.eccentricity_toggle_menu_spinbox_6 = QDoubleSpinBox(self.frame_91)
        self.eccentricity_toggle_menu_spinbox_6.setObjectName(u"eccentricity_toggle_menu_spinbox_6")
        self.eccentricity_toggle_menu_spinbox_6.setMinimumSize(QSize(80, 0))
        self.eccentricity_toggle_menu_spinbox_6.setMaximumSize(QSize(80, 16777215))
        self.eccentricity_toggle_menu_spinbox_6.setStyleSheet(u"    /*spinbox lift style*/\n"
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
        self.eccentricity_toggle_menu_spinbox_6.setAlignment(Qt.AlignCenter)
        self.eccentricity_toggle_menu_spinbox_6.setMinimum(0.000000000000000)
        self.eccentricity_toggle_menu_spinbox_6.setMaximum(1000000.000000000000000)

        self.horizontalLayout_149.addWidget(self.eccentricity_toggle_menu_spinbox_6)


        self.verticalLayout_59.addLayout(self.horizontalLayout_149)


        self.horizontalLayout_147.addLayout(self.verticalLayout_59)


        self.horizontalLayout_158.addWidget(self.frame_91)


        self.verticalLayout_64.addWidget(self.frame_89)

        self.frame_92 = QFrame(self.frame_88)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(125, 0))
        self.frame_93.setMaximumSize(QSize(125, 16777215))
        self.frame_93.setStyleSheet(u"background:transparent;\n"
"border:1px solid  rgb(136, 136, 136);\n"
"")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_93)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.eccentricity_toggle_menu_lbl_4 = QLabel(self.frame_93)
        self.eccentricity_toggle_menu_lbl_4.setObjectName(u"eccentricity_toggle_menu_lbl_4")
        self.eccentricity_toggle_menu_lbl_4.setMinimumSize(QSize(0, 20))
        self.eccentricity_toggle_menu_lbl_4.setMaximumSize(QSize(16777215, 20))
        self.eccentricity_toggle_menu_lbl_4.setFont(font12)
        self.eccentricity_toggle_menu_lbl_4.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.eccentricity_toggle_menu_lbl_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.eccentricity_toggle_menu_lbl_4)

        self.semi_major_axis_toggle_menu_spinbox_3 = QDoubleSpinBox(self.frame_93)
        self.semi_major_axis_toggle_menu_spinbox_3.setObjectName(u"semi_major_axis_toggle_menu_spinbox_3")
        self.semi_major_axis_toggle_menu_spinbox_3.setMinimumSize(QSize(80, 0))
        self.semi_major_axis_toggle_menu_spinbox_3.setMaximumSize(QSize(80, 16777215))
        self.semi_major_axis_toggle_menu_spinbox_3.setStyleSheet(u"    /*spinbox lift style*/\n"
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
        self.semi_major_axis_toggle_menu_spinbox_3.setAlignment(Qt.AlignCenter)
        self.semi_major_axis_toggle_menu_spinbox_3.setMinimum(-50.000000000000000)
        self.semi_major_axis_toggle_menu_spinbox_3.setMaximum(50.000000000000000)

        self.verticalLayout_62.addWidget(self.semi_major_axis_toggle_menu_spinbox_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_159.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.frame_92)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setStyleSheet(u"background:transparent;\n"
"border:1px solid  rgb(136, 136, 136);\n"
"")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_146 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_146.setSpacing(0)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.Semi_dial_3 = QDial(self.frame_94)
        self.Semi_dial_3.setObjectName(u"Semi_dial_3")
        self.Semi_dial_3.setMinimumSize(QSize(80, 80))
        self.Semi_dial_3.setMaximumSize(QSize(80, 80))
        self.Semi_dial_3.setMouseTracking(False)
        self.Semi_dial_3.setStyleSheet(u"QDial::handle { background-color: black }")
        self.Semi_dial_3.setMinimum(0)
        self.Semi_dial_3.setMaximum(10)
        self.Semi_dial_3.setNotchesVisible(True)

        self.horizontalLayout_146.addWidget(self.Semi_dial_3)

        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(-1, 10, -1, 0)
        self.label_104 = QLabel(self.frame_94)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(100, 20))
        self.label_104.setMaximumSize(QSize(125, 20))
        self.label_104.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_104.setAlignment(Qt.AlignCenter)

        self.verticalLayout_63.addWidget(self.label_104, 0, Qt.AlignHCenter)

        self.eccentricity_toggle_menu_slider_4 = QSlider(self.frame_94)
        self.eccentricity_toggle_menu_slider_4.setObjectName(u"eccentricity_toggle_menu_slider_4")
        self.eccentricity_toggle_menu_slider_4.setStyleSheet(u"\n"
"border:none;")
        self.eccentricity_toggle_menu_slider_4.setMaximum(7)
        self.eccentricity_toggle_menu_slider_4.setValue(0)
        self.eccentricity_toggle_menu_slider_4.setSliderPosition(0)
        self.eccentricity_toggle_menu_slider_4.setOrientation(Qt.Horizontal)
        self.eccentricity_toggle_menu_slider_4.setTickPosition(QSlider.TicksAbove)
        self.eccentricity_toggle_menu_slider_4.setTickInterval(1)

        self.verticalLayout_63.addWidget(self.eccentricity_toggle_menu_slider_4)

        self.horizontalLayout_148 = QHBoxLayout()
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.label_105 = QLabel(self.frame_94)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(70, 20))
        self.label_105.setMaximumSize(QSize(80, 20))
        self.label_105.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_105.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_148.addWidget(self.label_105)

        self.eccentricity_toggle_menu_spinbox_5 = QDoubleSpinBox(self.frame_94)
        self.eccentricity_toggle_menu_spinbox_5.setObjectName(u"eccentricity_toggle_menu_spinbox_5")
        self.eccentricity_toggle_menu_spinbox_5.setMinimumSize(QSize(80, 0))
        self.eccentricity_toggle_menu_spinbox_5.setMaximumSize(QSize(80, 16777215))
        self.eccentricity_toggle_menu_spinbox_5.setStyleSheet(u"    /*spinbox lift style*/\n"
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
        self.eccentricity_toggle_menu_spinbox_5.setAlignment(Qt.AlignCenter)
        self.eccentricity_toggle_menu_spinbox_5.setMinimum(-50.000000000000000)
        self.eccentricity_toggle_menu_spinbox_5.setMaximum(50.000000000000000)

        self.horizontalLayout_148.addWidget(self.eccentricity_toggle_menu_spinbox_5)


        self.verticalLayout_63.addLayout(self.horizontalLayout_148)


        self.horizontalLayout_146.addLayout(self.verticalLayout_63)


        self.horizontalLayout_159.addWidget(self.frame_94)


        self.verticalLayout_64.addWidget(self.frame_92)


        self.verticalLayout_60.addWidget(self.frame_88)

        self.VPCO_Input_Stack.addWidget(self.page_4)

        self.verticalLayout_52.addWidget(self.VPCO_Input_Stack)


        self.horizontalLayout_7.addWidget(self.a_and_e_VPCO)

        self.a_and_e_graph_VPCO = QFrame(self.tab_container_frame_for_a_and_e)
        self.a_and_e_graph_VPCO.setObjectName(u"a_and_e_graph_VPCO")
        self.a_and_e_graph_VPCO.setStyleSheet(u"background-color:transparent;")
        self.a_and_e_graph_VPCO.setFrameShape(QFrame.StyledPanel)
        self.a_and_e_graph_VPCO.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.a_and_e_graph_VPCO)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, -1, 9, -1)
        self.graph_widget = QWidget(self.a_and_e_graph_VPCO)
        self.graph_widget.setObjectName(u"graph_widget")
        self.graph_widget.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"")

        self.horizontalLayout_81.addWidget(self.graph_widget)


        self.horizontalLayout_7.addWidget(self.a_and_e_graph_VPCO)


        self.verticalLayout_57.addWidget(self.tab_container_frame_for_a_and_e)

        self.Bottom_slider_VPCO_Output = QFrame(self.frame_3)
        self.Bottom_slider_VPCO_Output.setObjectName(u"Bottom_slider_VPCO_Output")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Bottom_slider_VPCO_Output.sizePolicy().hasHeightForWidth())
        self.Bottom_slider_VPCO_Output.setSizePolicy(sizePolicy3)
        self.Bottom_slider_VPCO_Output.setMinimumSize(QSize(0, 0))
        self.Bottom_slider_VPCO_Output.setMaximumSize(QSize(16878, 0))
        self.Bottom_slider_VPCO_Output.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 255), stop:1 rgba(161, 161, 161, 255));\n"
"	\n"
"\n"
"}")
        self.Bottom_slider_VPCO_Output.setFrameShape(QFrame.StyledPanel)
        self.Bottom_slider_VPCO_Output.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.Bottom_slider_VPCO_Output)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(30, -1, 30, -1)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_11 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(280, 35))
        self.widget_11.setMaximumSize(QSize(280, 35))
        self.widget_11.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_119 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_119.setSpacing(3)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.widget_11)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(130, 35))
        self.frame_70.setMaximumSize(QSize(250, 16777215))
        self.frame_70.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(6, 6, 6, 6)
        self.label_41 = QLabel(self.frame_70)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(100, 20))
        self.label_41.setMaximumSize(QSize(125, 20))
        self.label_41.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_120.addWidget(self.label_41, 0, Qt.AlignVCenter)


        self.horizontalLayout_119.addWidget(self.frame_70, 0, Qt.AlignVCenter)

        self.frame_71 = QFrame(self.widget_11)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(6, 6, 6, 6)
        self.label_42 = QLabel(self.frame_71)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_121.addWidget(self.label_42)

        self.label_92 = QLabel(self.frame_71)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(45, 0))
        self.label_92.setMaximumSize(QSize(30, 16777215))
        self.label_92.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_121.addWidget(self.label_92)


        self.horizontalLayout_119.addWidget(self.frame_71)


        self.gridLayout_3.addWidget(self.widget_11, 1, 0, 1, 1)

        self.widget_18 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(280, 35))
        self.widget_18.setMaximumSize(QSize(280, 35))
        self.widget_18.setStyleSheet(u"background:none;")
        self.horizontalLayout_140 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_140.setSpacing(3)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.widget_18)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(130, 35))
        self.frame_84.setMaximumSize(QSize(250, 16777215))
        self.frame_84.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(6, 6, 6, 6)
        self.label_80 = QLabel(self.frame_84)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(100, 20))
        self.label_80.setMaximumSize(QSize(125, 20))
        self.label_80.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_80.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_141.addWidget(self.label_80, 0, Qt.AlignVCenter)


        self.horizontalLayout_140.addWidget(self.frame_84, 0, Qt.AlignVCenter)

        self.frame_85 = QFrame(self.widget_18)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(6, 6, 6, 6)
        self.label_88 = QLabel(self.frame_85)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_88.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_142.addWidget(self.label_88)

        self.label_98 = QLabel(self.frame_85)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(30, 0))
        self.label_98.setMaximumSize(QSize(45, 16777215))
        self.label_98.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_142.addWidget(self.label_98)


        self.horizontalLayout_140.addWidget(self.frame_85)


        self.gridLayout_3.addWidget(self.widget_18, 3, 2, 1, 1)

        self.widget_16 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(280, 35))
        self.widget_16.setMaximumSize(QSize(280, 35))
        self.widget_16.setStyleSheet(u"background:none;")
        self.horizontalLayout_134 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_134.setSpacing(3)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.frame_80 = QFrame(self.widget_16)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(130, 35))
        self.frame_80.setMaximumSize(QSize(250, 16777215))
        self.frame_80.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(6, 6, 6, 6)
        self.label_76 = QLabel(self.frame_80)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(100, 20))
        self.label_76.setMaximumSize(QSize(125, 20))
        self.label_76.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_76.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_135.addWidget(self.label_76, 0, Qt.AlignVCenter)


        self.horizontalLayout_134.addWidget(self.frame_80, 0, Qt.AlignVCenter)

        self.frame_81 = QFrame(self.widget_16)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(6, 6, 6, 6)
        self.label_77 = QLabel(self.frame_81)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_77.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_136.addWidget(self.label_77)

        self.label_96 = QLabel(self.frame_81)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(30, 0))
        self.label_96.setMaximumSize(QSize(45, 16777215))
        self.label_96.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_136.addWidget(self.label_96)


        self.horizontalLayout_134.addWidget(self.frame_81)


        self.gridLayout_3.addWidget(self.widget_16, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.widget_13 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(280, 35))
        self.widget_13.setMaximumSize(QSize(280, 35))
        self.widget_13.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}\n"
"")
        self.horizontalLayout_125 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_125.setSpacing(3)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.frame_74 = QFrame(self.widget_13)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(130, 35))
        self.frame_74.setMaximumSize(QSize(250, 16777215))
        self.frame_74.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(6, 6, 6, 6)
        self.label_70 = QLabel(self.frame_74)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(100, 20))
        self.label_70.setMaximumSize(QSize(125, 20))
        self.label_70.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_70.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_126.addWidget(self.label_70, 0, Qt.AlignVCenter)


        self.horizontalLayout_125.addWidget(self.frame_74, 0, Qt.AlignVCenter)

        self.frame_75 = QFrame(self.widget_13)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(6, 6, 6, 6)
        self.label_71 = QLabel(self.frame_75)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_127.addWidget(self.label_71)

        self.label_93 = QLabel(self.frame_75)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(45, 0))
        self.label_93.setMaximumSize(QSize(30, 16777215))
        self.label_93.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_127.addWidget(self.label_93)


        self.horizontalLayout_125.addWidget(self.frame_75)


        self.gridLayout_3.addWidget(self.widget_13, 2, 0, 1, 1)

        self.widget_15 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(280, 35))
        self.widget_15.setMaximumSize(QSize(280, 35))
        self.widget_15.setStyleSheet(u"background:none;")
        self.horizontalLayout_131 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_131.setSpacing(3)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.frame_78 = QFrame(self.widget_15)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(130, 35))
        self.frame_78.setMaximumSize(QSize(280, 16777215))
        self.frame_78.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(6, 6, 6, 6)
        self.label_74 = QLabel(self.frame_78)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(100, 20))
        self.label_74.setMaximumSize(QSize(125, 20))
        self.label_74.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_74.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_132.addWidget(self.label_74, 0, Qt.AlignVCenter)


        self.horizontalLayout_131.addWidget(self.frame_78, 0, Qt.AlignVCenter)

        self.frame_79 = QFrame(self.widget_15)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(6, 6, 6, 6)
        self.label_75 = QLabel(self.frame_79)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_133.addWidget(self.label_75)

        self.label_102 = QLabel(self.frame_79)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(30, 0))
        self.label_102.setMaximumSize(QSize(45, 16777215))
        self.label_102.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_133.addWidget(self.label_102)


        self.horizontalLayout_131.addWidget(self.frame_79)


        self.gridLayout_3.addWidget(self.widget_15, 2, 4, 1, 1)

        self.widget_19 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(280, 35))
        self.widget_19.setMaximumSize(QSize(280, 60))
        self.widget_19.setStyleSheet(u"background:none;")
        self.horizontalLayout_143 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_143.setSpacing(3)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.widget_19)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(130, 35))
        self.frame_86.setMaximumSize(QSize(250, 16777215))
        self.frame_86.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(6, 6, 6, 6)
        self.label_89 = QLabel(self.frame_86)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(100, 20))
        self.label_89.setMaximumSize(QSize(125, 20))
        self.label_89.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_89.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_144.addWidget(self.label_89, 0, Qt.AlignVCenter)


        self.horizontalLayout_143.addWidget(self.frame_86, 0, Qt.AlignVCenter)

        self.frame_87 = QFrame(self.widget_19)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(6, 6, 6, 6)
        self.label_90 = QLabel(self.frame_87)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_90.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_145.addWidget(self.label_90)

        self.label_95 = QLabel(self.frame_87)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(30, 0))
        self.label_95.setMaximumSize(QSize(45, 16777215))
        self.label_95.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_145.addWidget(self.label_95)


        self.horizontalLayout_143.addWidget(self.frame_87)


        self.gridLayout_3.addWidget(self.widget_19, 0, 2, 1, 1)

        self.widget_12 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(280, 35))
        self.widget_12.setMaximumSize(QSize(280, 60))
        self.widget_12.setStyleSheet(u"background:none;")
        self.horizontalLayout_122 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_122.setSpacing(3)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.frame_72 = QFrame(self.widget_12)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(130, 35))
        self.frame_72.setMaximumSize(QSize(250, 16777215))
        self.frame_72.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(6, 6, 6, 6)
        self.label_57 = QLabel(self.frame_72)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(100, 20))
        self.label_57.setMaximumSize(QSize(125, 20))
        self.label_57.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_123.addWidget(self.label_57, 0, Qt.AlignVCenter)


        self.horizontalLayout_122.addWidget(self.frame_72, 0, Qt.AlignVCenter)

        self.frame_73 = QFrame(self.widget_12)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(6, 6, 6, 6)
        self.label_69 = QLabel(self.frame_73)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_124.addWidget(self.label_69)

        self.label_101 = QLabel(self.frame_73)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(30, 0))
        self.label_101.setMaximumSize(QSize(45, 16777215))
        self.label_101.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_124.addWidget(self.label_101)


        self.horizontalLayout_122.addWidget(self.frame_73)


        self.gridLayout_3.addWidget(self.widget_12, 3, 4, 1, 1)

        self.widget_14 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(280, 35))
        self.widget_14.setMaximumSize(QSize(280, 35))
        self.widget_14.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_128 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_128.setSpacing(3)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.frame_76 = QFrame(self.widget_14)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(130, 35))
        self.frame_76.setMaximumSize(QSize(250, 16777215))
        self.frame_76.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(6, 6, 6, 6)
        self.label_72 = QLabel(self.frame_76)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(100, 20))
        self.label_72.setMaximumSize(QSize(125, 20))
        self.label_72.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_129.addWidget(self.label_72, 0, Qt.AlignVCenter)


        self.horizontalLayout_128.addWidget(self.frame_76, 0, Qt.AlignVCenter)

        self.frame_77 = QFrame(self.widget_14)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(6, 6, 6, 6)
        self.label_73 = QLabel(self.frame_77)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_73.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_130.addWidget(self.label_73)

        self.label_94 = QLabel(self.frame_77)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(45, 0))
        self.label_94.setMaximumSize(QSize(45, 16777215))
        self.label_94.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_130.addWidget(self.label_94)


        self.horizontalLayout_128.addWidget(self.frame_77)


        self.gridLayout_3.addWidget(self.widget_14, 3, 0, 1, 1)

        self.widget_17 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(280, 35))
        self.widget_17.setMaximumSize(QSize(280, 35))
        self.widget_17.setStyleSheet(u"background:none;")
        self.horizontalLayout_137 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_137.setSpacing(3)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.frame_82 = QFrame(self.widget_17)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(130, 35))
        self.frame_82.setMaximumSize(QSize(250, 16777215))
        self.frame_82.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(6, 6, 6, 6)
        self.label_78 = QLabel(self.frame_82)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(100, 20))
        self.label_78.setMaximumSize(QSize(125, 20))
        self.label_78.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_78.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_138.addWidget(self.label_78, 0, Qt.AlignVCenter)


        self.horizontalLayout_137.addWidget(self.frame_82, 0, Qt.AlignVCenter)

        self.frame_83 = QFrame(self.widget_17)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(6, 6, 6, 6)
        self.label_79 = QLabel(self.frame_83)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_139.addWidget(self.label_79)

        self.label_99 = QLabel(self.frame_83)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMinimumSize(QSize(30, 0))
        self.label_99.setMaximumSize(QSize(45, 16777215))
        self.label_99.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_139.addWidget(self.label_99)


        self.horizontalLayout_137.addWidget(self.frame_83)


        self.gridLayout_3.addWidget(self.widget_17, 0, 4, 1, 1)

        self.widget_10 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(280, 35))
        self.widget_10.setMaximumSize(QSize(280, 35))
        self.widget_10.setStyleSheet(u"background:none;")
        self.horizontalLayout_116 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_116.setSpacing(3)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.frame_68 = QFrame(self.widget_10)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(130, 35))
        self.frame_68.setMaximumSize(QSize(250, 16777215))
        self.frame_68.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(6, 6, 6, 6)
        self.label_35 = QLabel(self.frame_68)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(104, 20))
        self.label_35.setMaximumSize(QSize(130, 20))
        self.label_35.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_117.addWidget(self.label_35, 0, Qt.AlignVCenter)


        self.horizontalLayout_116.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.widget_10)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(6, 6, 6, 6)
        self.label_39 = QLabel(self.frame_69)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_118.addWidget(self.label_39)

        self.label_100 = QLabel(self.frame_69)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMinimumSize(QSize(30, 0))
        self.label_100.setMaximumSize(QSize(45, 16777215))
        self.label_100.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_118.addWidget(self.label_100)


        self.horizontalLayout_116.addWidget(self.frame_69)


        self.gridLayout_3.addWidget(self.widget_10, 1, 4, 1, 1)

        self.widget_8 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(280, 35))
        self.widget_8.setMaximumSize(QSize(250, 35))
        self.widget_8.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_110 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_110.setSpacing(3)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.frame_64 = QFrame(self.widget_8)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(130, 35))
        self.frame_64.setMaximumSize(QSize(250, 16777215))
        self.frame_64.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(6, 6, 6, 6)
        self.label_30 = QLabel(self.frame_64)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(100, 20))
        self.label_30.setMaximumSize(QSize(125, 20))
        self.label_30.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_111.addWidget(self.label_30)


        self.horizontalLayout_110.addWidget(self.frame_64, 0, Qt.AlignVCenter)

        self.frame_65 = QFrame(self.widget_8)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(6, 6, 6, 6)
        self.label_31 = QLabel(self.frame_65)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_112.addWidget(self.label_31)

        self.label_91 = QLabel(self.frame_65)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(30, 0))
        self.label_91.setMaximumSize(QSize(45, 16777215))
        self.label_91.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_112.addWidget(self.label_91)


        self.horizontalLayout_110.addWidget(self.frame_65)


        self.gridLayout_3.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.Bottom_slider_VPCO_Output)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(280, 35))
        self.widget_9.setMaximumSize(QSize(280, 60))
        self.widget_9.setStyleSheet(u"background:none;")
        self.horizontalLayout_113 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_113.setSpacing(3)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.widget_9)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(130, 35))
        self.frame_66.setMaximumSize(QSize(250, 16777215))
        self.frame_66.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(6, 6, 6, 6)
        self.label_32 = QLabel(self.frame_66)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 20))
        self.label_32.setMaximumSize(QSize(125, 20))
        self.label_32.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_114.addWidget(self.label_32, 0, Qt.AlignVCenter)


        self.horizontalLayout_113.addWidget(self.frame_66, 0, Qt.AlignVCenter)

        self.frame_67 = QFrame(self.widget_9)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(6, 6, 6, 6)
        self.label_34 = QLabel(self.frame_67)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_115.addWidget(self.label_34)

        self.label_97 = QLabel(self.frame_67)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(30, 0))
        self.label_97.setMaximumSize(QSize(45, 16777215))
        self.label_97.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_115.addWidget(self.label_97)


        self.horizontalLayout_113.addWidget(self.frame_67)


        self.gridLayout_3.addWidget(self.widget_9, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.verticalLayout_58.addLayout(self.gridLayout_3)


        self.verticalLayout_57.addWidget(self.Bottom_slider_VPCO_Output)


        self.verticalLayout_22.addWidget(self.frame_3)

        self.VPCO_tabs.addTab(self.a_and_e_tab, "")
        self.ra_and_rp = QWidget()
        self.ra_and_rp.setObjectName(u"ra_and_rp")
        self.horizontalLayout_108 = QHBoxLayout(self.ra_and_rp)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(9, -1, 9, -1)
        self.tab_container_frame_for_a_and_e_2 = QFrame(self.ra_and_rp)
        self.tab_container_frame_for_a_and_e_2.setObjectName(u"tab_container_frame_for_a_and_e_2")
        self.tab_container_frame_for_a_and_e_2.setStyleSheet(u"background-color:transparent;")
        self.tab_container_frame_for_a_and_e_2.setFrameShape(QFrame.StyledPanel)
        self.tab_container_frame_for_a_and_e_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.tab_container_frame_for_a_and_e_2)
        self.horizontalLayout_97.setSpacing(9)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.a_and_e_VPCO_2 = QFrame(self.tab_container_frame_for_a_and_e_2)
        self.a_and_e_VPCO_2.setObjectName(u"a_and_e_VPCO_2")
        self.a_and_e_VPCO_2.setMinimumSize(QSize(526, 0))
        self.a_and_e_VPCO_2.setMaximumSize(QSize(526, 16777215))
        self.a_and_e_VPCO_2.setStyleSheet(u"background-color:transparent;")
        self.a_and_e_VPCO_2.setFrameShape(QFrame.StyledPanel)
        self.a_and_e_VPCO_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.a_and_e_VPCO_2)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 9, 0, 9)
        self.frame_17 = QFrame(self.a_and_e_VPCO_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(528, 16777215))
        self.frame_17.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 255), stop:1 rgba(161, 161, 161, 255));\n"
"	\n"
"\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_17)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalSpacer_20 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_20)

        self.frame_57 = QFrame(self.frame_17)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(0, 60))
        self.frame_57.setMaximumSize(QSize(16777215, 60))
        self.frame_57.setStyleSheet(u"border:none;\n"
"background:none;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.frame_57)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(400, 50))
        self.widget_6.setMaximumSize(QSize(450, 60))
        self.widget_6.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color:rgb(175, 101, 174);\n"
"}")
        self.horizontalLayout_99 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.widget_6)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(225, 0))
        self.frame_58.setMaximumSize(QSize(250, 16777215))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.label_20 = QLabel(self.frame_58)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(150, 30))
        self.label_20.setMaximumSize(QSize(200, 16777215))
        self.label_20.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_100.addWidget(self.label_20)


        self.horizontalLayout_99.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.widget_6)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(9, 9, 9, 9)
        self.VPCO_Input_a_lineedit_4 = QLineEdit(self.frame_59)
        self.VPCO_Input_a_lineedit_4.setObjectName(u"VPCO_Input_a_lineedit_4")
        self.VPCO_Input_a_lineedit_4.setMinimumSize(QSize(130, 40))
        self.VPCO_Input_a_lineedit_4.setMaximumSize(QSize(200, 50))
        self.VPCO_Input_a_lineedit_4.setLayoutDirection(Qt.RightToLeft)
        self.VPCO_Input_a_lineedit_4.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:10px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.VPCO_Input_a_lineedit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_101.addWidget(self.VPCO_Input_a_lineedit_4)


        self.horizontalLayout_99.addWidget(self.frame_59)


        self.horizontalLayout_98.addWidget(self.widget_6)


        self.verticalLayout_56.addWidget(self.frame_57)

        self.verticalSpacer_21 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_21)

        self.frame_60 = QFrame(self.frame_17)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 60))
        self.frame_60.setMaximumSize(QSize(16777215, 60))
        self.frame_60.setStyleSheet(u"border:none;\n"
"background:none;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.frame_60)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(400, 50))
        self.widget_7.setMaximumSize(QSize(450, 60))
        self.widget_7.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color:rgb(175, 101, 174);\n"
"}")
        self.horizontalLayout_103 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_103.setSpacing(0)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.widget_7)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(225, 0))
        self.frame_61.setMaximumSize(QSize(250, 16777215))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.label_21 = QLabel(self.frame_61)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(150, 30))
        self.label_21.setMaximumSize(QSize(200, 16777215))
        self.label_21.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_104.addWidget(self.label_21)


        self.horizontalLayout_103.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.widget_7)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.VPCO_Input_e_lineedit_3 = QLineEdit(self.frame_62)
        self.VPCO_Input_e_lineedit_3.setObjectName(u"VPCO_Input_e_lineedit_3")
        self.VPCO_Input_e_lineedit_3.setMinimumSize(QSize(130, 40))
        self.VPCO_Input_e_lineedit_3.setMaximumSize(QSize(200, 50))
        self.VPCO_Input_e_lineedit_3.setLayoutDirection(Qt.RightToLeft)
        self.VPCO_Input_e_lineedit_3.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:10px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.VPCO_Input_e_lineedit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_105.addWidget(self.VPCO_Input_e_lineedit_3)


        self.horizontalLayout_103.addWidget(self.frame_62)


        self.horizontalLayout_102.addWidget(self.widget_7)


        self.verticalLayout_56.addWidget(self.frame_60)

        self.verticalSpacer_22 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_22)

        self.frame_63 = QFrame(self.frame_17)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 60))
        self.frame_63.setMaximumSize(QSize(16777215, 60))
        self.frame_63.setStyleSheet(u"border:none;\n"
"background:none;")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.maj_body_CoOE_4 = QComboBox(self.frame_63)
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.addItem("")
        self.maj_body_CoOE_4.setObjectName(u"maj_body_CoOE_4")
        self.maj_body_CoOE_4.setMinimumSize(QSize(300, 60))
        self.maj_body_CoOE_4.setMaximumSize(QSize(350, 60))
        self.maj_body_CoOE_4.setStyleSheet(u"QComboBox{\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:12px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"\n"
"QComboBoxt:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")

        self.horizontalLayout_106.addWidget(self.maj_body_CoOE_4)


        self.verticalLayout_56.addWidget(self.frame_63)

        self.verticalSpacer_23 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_23)

        self.VPCO_Submit_button_2 = QPushButton(self.frame_17)
        self.VPCO_Submit_button_2.setObjectName(u"VPCO_Submit_button_2")
        sizePolicy2.setHeightForWidth(self.VPCO_Submit_button_2.sizePolicy().hasHeightForWidth())
        self.VPCO_Submit_button_2.setSizePolicy(sizePolicy2)
        self.VPCO_Submit_button_2.setMinimumSize(QSize(125, 40))
        self.VPCO_Submit_button_2.setMaximumSize(QSize(150, 80))
        self.VPCO_Submit_button_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:10px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:rgb(175, 101, 174);\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"")

        self.verticalLayout_56.addWidget(self.VPCO_Submit_button_2, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.frame_17)


        self.horizontalLayout_97.addWidget(self.a_and_e_VPCO_2)

        self.a_and_e_graph_VPCO_2 = QFrame(self.tab_container_frame_for_a_and_e_2)
        self.a_and_e_graph_VPCO_2.setObjectName(u"a_and_e_graph_VPCO_2")
        self.a_and_e_graph_VPCO_2.setStyleSheet(u"background-color:transparent;")
        self.a_and_e_graph_VPCO_2.setFrameShape(QFrame.StyledPanel)
        self.a_and_e_graph_VPCO_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.a_and_e_graph_VPCO_2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, 0, -1)
        self.graph_widget_2 = QWidget(self.a_and_e_graph_VPCO_2)
        self.graph_widget_2.setObjectName(u"graph_widget_2")
        self.graph_widget_2.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 255), stop:1 rgba(161, 161, 161, 255));")

        self.horizontalLayout_15.addWidget(self.graph_widget_2)

        self.frame_12 = QFrame(self.a_and_e_graph_VPCO_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(35, 0))
        self.frame_12.setMaximumSize(QSize(35, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_15.addWidget(self.frame_12)


        self.horizontalLayout_97.addWidget(self.a_and_e_graph_VPCO_2)


        self.horizontalLayout_108.addWidget(self.tab_container_frame_for_a_and_e_2)

        self.VPCO_tabs.addTab(self.ra_and_rp, "")

        self.verticalLayout_21.addWidget(self.VPCO_tabs)


        self.verticalLayout_20.addWidget(self.VPCO_Outer_Frame)

        self.stackedWidget.addWidget(self.VPCO_input)
        self.VPCO_output = QWidget()
        self.VPCO_output.setObjectName(u"VPCO_output")
        self.horizontalLayout_21 = QHBoxLayout(self.VPCO_output)
        self.horizontalLayout_21.setSpacing(3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(6, 0, 6, 0)
        self.VPCO_menu_toggle_frame = QFrame(self.VPCO_output)
        self.VPCO_menu_toggle_frame.setObjectName(u"VPCO_menu_toggle_frame")
        self.VPCO_menu_toggle_frame.setMaximumSize(QSize(200, 16777215))
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
        self.label_56.setFont(font3)
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
        self.label_10.setFont(font11)
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
        self.label_18.setFont(font11)
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
        self.label_43.setFont(font11)
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
        self.label_53.setFont(font11)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_title_5.sizePolicy().hasHeightForWidth())
        self.label_title_5.setSizePolicy(sizePolicy4)
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
        self.label_51.setFont(font3)
        self.label_51.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_51, 6, 0, 1, 1)

        self.label_86 = QLabel(self.a_e_result_screen)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(0, 40))
        self.label_86.setMaximumSize(QSize(16777215, 40))
        self.label_86.setFont(font3)
        self.label_86.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_86, 10, 3, 1, 1)

        self.label_118 = QLabel(self.a_e_result_screen)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(40, 40))
        self.label_118.setMaximumSize(QSize(40, 40))
        self.label_118.setFont(font3)
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
        self.label_123.setFont(font3)
        self.label_123.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_123.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_123, 12, 2, 1, 1)

        self.label_125 = QLabel(self.a_e_result_screen)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(40, 40))
        self.label_125.setMaximumSize(QSize(40, 40))
        self.label_125.setFont(font3)
        self.label_125.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_125.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_125, 12, 5, 1, 1)

        self.label_122 = QLabel(self.a_e_result_screen)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(40, 40))
        self.label_122.setMaximumSize(QSize(40, 40))
        self.label_122.setFont(font3)
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
        self.label_120.setFont(font3)
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
        self.label_81.setFont(font3)
        self.label_81.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_81.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_81, 0, 3, 1, 1)

        self.label_128 = QLabel(self.a_e_result_screen)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(40, 40))
        self.label_128.setMaximumSize(QSize(40, 40))
        self.label_128.setFont(font3)
        self.label_128.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_128.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_128, 8, 5, 1, 1)

        self.label_49 = QLabel(self.a_e_result_screen)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 40))
        self.label_49.setMaximumSize(QSize(16777215, 40))
        self.label_49.setFont(font3)
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
        self.label_114.setFont(font3)
        self.label_114.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_114.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_114, 12, 0, 1, 1)

        self.label_113 = QLabel(self.a_e_result_screen)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(0, 40))
        self.label_113.setMaximumSize(QSize(16777215, 40))
        self.label_113.setFont(font3)
        self.label_113.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_113.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_113, 10, 0, 1, 1)

        self.label_131 = QLabel(self.a_e_result_screen)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(40, 40))
        self.label_131.setMaximumSize(QSize(40, 40))
        self.label_131.setFont(font3)
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
        self.label_117.setFont(font3)
        self.label_117.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_117.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_117, 8, 0, 1, 1)

        self.label_84 = QLabel(self.a_e_result_screen)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(0, 40))
        self.label_84.setMaximumSize(QSize(16777215, 40))
        self.label_84.setFont(font3)
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
        self.label_82.setFont(font3)
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
        self.label_50.setFont(font3)
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
        self.label_87.setFont(font3)
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
        self.label_129.setFont(font3)
        self.label_129.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_129, 10, 5, 1, 1)

        self.label_119 = QLabel(self.a_e_result_screen)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(40, 40))
        self.label_119.setMaximumSize(QSize(40, 40))
        self.label_119.setFont(font3)
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
        self.label_121.setFont(font3)
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
        self.label_130.setFont(font3)
        self.label_130.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_130, 2, 5, 1, 1)

        self.label_83 = QLabel(self.a_e_result_screen)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(0, 40))
        self.label_83.setMaximumSize(QSize(16777215, 40))
        self.label_83.setFont(font3)
        self.label_83.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_83, 4, 3, 1, 1)

        self.label_127 = QLabel(self.a_e_result_screen)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(40, 40))
        self.label_127.setMaximumSize(QSize(40, 40))
        self.label_127.setFont(font3)
        self.label_127.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_127, 6, 5, 1, 1)

        self.label_22 = QLabel(self.a_e_result_screen)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 40))
        self.label_22.setMaximumSize(QSize(16777215, 40))
        self.label_22.setFont(font3)
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
        self.label_85.setFont(font3)
        self.label_85.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_85, 8, 3, 1, 1)

        self.label_126 = QLabel(self.a_e_result_screen)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(40, 40))
        self.label_126.setMaximumSize(QSize(40, 40))
        self.label_126.setFont(font3)
        self.label_126.setStyleSheet(u"border:none;\n"
"color:white;")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_126, 0, 5, 1, 1)

        self.label_124 = QLabel(self.a_e_result_screen)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(40, 40))
        self.label_124.setMaximumSize(QSize(40, 40))
        self.label_124.setFont(font3)
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
"	border: 5px solid rgba(84, 84, 197,88%);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgba(2, 119, 189,88%);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"border: 5px solid rgba(143, 55, 143,88%);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid  rgba(255, 248, 166,88%);\n"
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
        self.cal_btn_coe_n_aoe.setFont(font3)
        self.cal_btn_coe_n_aoe.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0,60%);\n"
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
"	border: 5px solid rgba(84, 84, 197,88%);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	color:white;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	border: 4px solid rgba(2, 119, 189,88%);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"border: 5px solid rgba(143, 55, 143,88%);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid  rgba(255, 248, 166,88%);\n"
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
        self.Orbital_Transfer = QWidget()
        self.Orbital_Transfer.setObjectName(u"Orbital_Transfer")
        self.Orbital_Transfer.setStyleSheet(u"background:transparent;")
        self.horizontalLayout_85 = QHBoxLayout(self.Orbital_Transfer)
        self.horizontalLayout_85.setSpacing(6)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(-1, -1, 3, -1)
        self.Container_for_Type_of_Orbital_Transfer = QFrame(self.Orbital_Transfer)
        self.Container_for_Type_of_Orbital_Transfer.setObjectName(u"Container_for_Type_of_Orbital_Transfer")
        self.Container_for_Type_of_Orbital_Transfer.setMinimumSize(QSize(450, 0))
        self.Container_for_Type_of_Orbital_Transfer.setMaximumSize(QSize(16777215, 16777215))
        self.Container_for_Type_of_Orbital_Transfer.setStyleSheet(u"\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.Container_for_Type_of_Orbital_Transfer.setFrameShape(QFrame.StyledPanel)
        self.Container_for_Type_of_Orbital_Transfer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.Container_for_Type_of_Orbital_Transfer)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.Container_for_Type_of_Orbital_Transfer)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(450, 0))
        self.frame_45.setMaximumSize(QSize(16777215, 16777215))
        self.frame_45.setStyleSheet(u"background:transparent;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.Stacked_widg_Types_of_Orbital_Transfer = QStackedWidget(self.frame_45)
        self.Stacked_widg_Types_of_Orbital_Transfer.setObjectName(u"Stacked_widg_Types_of_Orbital_Transfer")
        self.Stacked_widg_Types_of_Orbital_Transfer.setMinimumSize(QSize(450, 0))
        self.Stacked_widg_Types_of_Orbital_Transfer.setMaximumSize(QSize(16777215, 16777215))
        self.Stacked_widg_Types_of_Orbital_Transfer.setStyleSheet(u"border:none;\n"
"background:transparent;")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_68 = QVBoxLayout(self.page_7)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_46 = QFrame(self.page_7)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"background:none;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.Orbit_Visualization_3 = QWidget(self.frame_46)
        self.Orbit_Visualization_3.setObjectName(u"Orbit_Visualization_3")
        self.Orbit_Visualization_3.setMinimumSize(QSize(450, 250))
        self.Orbit_Visualization_3.setMaximumSize(QSize(450, 250))
        self.Orbit_Visualization_3.setStyleSheet(u"background-color: #1b1b1b;\n"
"image:url(UI_Functions/Resources/Hohmann Transfer.png);")
        self.verticalLayout_66 = QVBoxLayout(self.Orbit_Visualization_3)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.filler_13 = QFrame(self.Orbit_Visualization_3)
        self.filler_13.setObjectName(u"filler_13")
        self.filler_13.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.filler_13.setFrameShape(QFrame.StyledPanel)
        self.filler_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout_66.addWidget(self.filler_13)

        self.slider_13 = QFrame(self.Orbit_Visualization_3)
        self.slider_13.setObjectName(u"slider_13")
        self.slider_13.setMinimumSize(QSize(450, 80))
        self.slider_13.setMaximumSize(QSize(450, 200))
        self.slider_13.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.slider_13.setFrameShape(QFrame.StyledPanel)
        self.slider_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.slider_13)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(5, 5, 5, 5)
        self.Hohmn_transf_label = QLabel(self.slider_13)
        self.Hohmn_transf_label.setObjectName(u"Hohmn_transf_label")
        self.Hohmn_transf_label.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(44, 44, 44, 80%);\n"
"")
        self.Hohmn_transf_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.Hohmn_transf_label)


        self.verticalLayout_66.addWidget(self.slider_13)


        self.horizontalLayout_88.addWidget(self.Orbit_Visualization_3)

        self.Orbit_Visualization_2 = QWidget(self.frame_46)
        self.Orbit_Visualization_2.setObjectName(u"Orbit_Visualization_2")
        self.Orbit_Visualization_2.setMinimumSize(QSize(450, 250))
        self.Orbit_Visualization_2.setMaximumSize(QSize(450, 250))
        self.Orbit_Visualization_2.setStyleSheet(u"background-color: #1b1b1b;\n"
"image:url(UI_Functions/Resources/Bi-Elliptical Hohmann Transfer.png);")
        self.verticalLayout_54 = QVBoxLayout(self.Orbit_Visualization_2)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.filler_12 = QFrame(self.Orbit_Visualization_2)
        self.filler_12.setObjectName(u"filler_12")
        self.filler_12.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.filler_12.setFrameShape(QFrame.StyledPanel)
        self.filler_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_54.addWidget(self.filler_12)

        self.slider_12 = QFrame(self.Orbit_Visualization_2)
        self.slider_12.setObjectName(u"slider_12")
        self.slider_12.setMinimumSize(QSize(450, 80))
        self.slider_12.setMaximumSize(QSize(230, 200))
        self.slider_12.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.slider_12.setFrameShape(QFrame.StyledPanel)
        self.slider_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.slider_12)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(5, 5, 5, 5)
        self.label_107 = QLabel(self.slider_12)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(44, 44, 44, 80%);\n"
"")
        self.label_107.setAlignment(Qt.AlignCenter)
        self.label_107.setWordWrap(True)

        self.verticalLayout_65.addWidget(self.label_107)


        self.verticalLayout_54.addWidget(self.slider_12)


        self.horizontalLayout_88.addWidget(self.Orbit_Visualization_2)


        self.verticalLayout_68.addWidget(self.frame_46)

        self.frame_53 = QFrame(self.page_7)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"background:none;")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.Orbit_Visualization_5 = QWidget(self.frame_53)
        self.Orbit_Visualization_5.setObjectName(u"Orbit_Visualization_5")
        self.Orbit_Visualization_5.setMinimumSize(QSize(450, 250))
        self.Orbit_Visualization_5.setMaximumSize(QSize(450, 250))
        self.Orbit_Visualization_5.setStyleSheet(u"background-color: #1b1b1b;\n"
"image:url(UI_Functions/Resources/Phasing Maneuver.png);")
        self.verticalLayout_72 = QVBoxLayout(self.Orbit_Visualization_5)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.filler_16 = QFrame(self.Orbit_Visualization_5)
        self.filler_16.setObjectName(u"filler_16")
        self.filler_16.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"")
        self.filler_16.setFrameShape(QFrame.StyledPanel)
        self.filler_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_72.addWidget(self.filler_16)

        self.slider_16 = QFrame(self.Orbit_Visualization_5)
        self.slider_16.setObjectName(u"slider_16")
        self.slider_16.setMinimumSize(QSize(450, 80))
        self.slider_16.setMaximumSize(QSize(230, 200))
        self.slider_16.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;")
        self.slider_16.setFrameShape(QFrame.StyledPanel)
        self.slider_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.slider_16)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(5, 5, 5, 5)
        self.label_111 = QLabel(self.slider_16)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setStyleSheet(u"color:white;\n"
"\n"
"font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: rgba(44, 44, 44, 80%);\n"
"")
        self.label_111.setAlignment(Qt.AlignCenter)

        self.verticalLayout_73.addWidget(self.label_111)


        self.verticalLayout_72.addWidget(self.slider_16)


        self.horizontalLayout_90.addWidget(self.Orbit_Visualization_5)


        self.verticalLayout_68.addWidget(self.frame_53)

        self.Stacked_widg_Types_of_Orbital_Transfer.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_77 = QVBoxLayout(self.page_8)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.frame_54 = QFrame(self.page_8)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(27, 27, 27);\n"
"	image:url(UI_Functions/Resources/Hohmann Transfer.png);\n"
"}")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)

        self.verticalLayout_77.addWidget(self.frame_54)

        self.frame_97 = QFrame(self.page_8)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setStyleSheet(u"background-color: #1b1b1b;")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_97)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(250, 25))
        self.frame_98.setMaximumSize(QSize(300, 30))
        self.frame_98.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_98)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_9 = QLabel(self.frame_98)
        self.semi_major_axis_toggle_menu_lbl_9.setObjectName(u"semi_major_axis_toggle_menu_lbl_9")
        self.semi_major_axis_toggle_menu_lbl_9.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_9.setMaximumSize(QSize(16777215, 20))
        font13 = QFont()
        font13.setPointSize(11)
        font13.setBold(True)
        font13.setWeight(75)
        self.semi_major_axis_toggle_menu_lbl_9.setFont(font13)
        self.semi_major_axis_toggle_menu_lbl_9.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_79.addWidget(self.semi_major_axis_toggle_menu_lbl_9)


        self.verticalLayout_80.addWidget(self.frame_98, 0, Qt.AlignHCenter)

        self.frame_99 = QFrame(self.frame_97)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 30))
        self.frame_99.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	\n"
"	background:transparent;\n"
"	\n"
"\n"
"}")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_99)
        self.label_5.setObjectName(u"label_5")
        font14 = QFont()
        font14.setPointSize(13)
        self.label_5.setFont(font14)
        self.label_5.setFocusPolicy(Qt.NoFocus)
        self.label_5.setStyleSheet(u"color:grey;")
        self.label_5.setWordWrap(True)

        self.horizontalLayout_91.addWidget(self.label_5)


        self.verticalLayout_80.addWidget(self.frame_99)


        self.verticalLayout_77.addWidget(self.frame_97)

        self.Stacked_widg_Types_of_Orbital_Transfer.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_83 = QVBoxLayout(self.page_9)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.frame_112 = QFrame(self.page_9)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(27, 27, 27);\n"
"	image:url(UI_Functions/Resources/Phasing Maneuver.png);\n"
"}")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)

        self.verticalLayout_83.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.page_9)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setStyleSheet(u"background-color: #1b1b1b;")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_113)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.frame_116 = QFrame(self.frame_113)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(250, 25))
        self.frame_116.setMaximumSize(QSize(300, 30))
        self.frame_116.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_116)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_10 = QLabel(self.frame_116)
        self.semi_major_axis_toggle_menu_lbl_10.setObjectName(u"semi_major_axis_toggle_menu_lbl_10")
        self.semi_major_axis_toggle_menu_lbl_10.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_10.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_10.setFont(font13)
        self.semi_major_axis_toggle_menu_lbl_10.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_82.addWidget(self.semi_major_axis_toggle_menu_lbl_10)


        self.verticalLayout_81.addWidget(self.frame_116, 0, Qt.AlignHCenter)

        self.frame_117 = QFrame(self.frame_113)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setMinimumSize(QSize(0, 30))
        self.frame_117.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	\n"
"	background:transparent;\n"
"	\n"
"\n"
"}")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_117)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font14)
        self.label_6.setFocusPolicy(Qt.NoFocus)
        self.label_6.setStyleSheet(u"color:grey;")
        self.label_6.setWordWrap(True)

        self.horizontalLayout_92.addWidget(self.label_6)


        self.verticalLayout_81.addWidget(self.frame_117)


        self.verticalLayout_83.addWidget(self.frame_113)

        self.Stacked_widg_Types_of_Orbital_Transfer.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_86 = QVBoxLayout(self.page_10)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.frame_143 = QFrame(self.page_10)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(27, 27, 27);\n"
"	image:url(UI_Functions/Resources/Bi-Elliptical Transfer.png);\n"
"}")
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)

        self.verticalLayout_86.addWidget(self.frame_143)

        self.frame_118 = QFrame(self.page_10)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setStyleSheet(u"background-color: #1b1b1b;")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_118)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.frame_119 = QFrame(self.frame_118)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMinimumSize(QSize(250, 25))
        self.frame_119.setMaximumSize(QSize(300, 30))
        self.frame_119.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_119)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_11 = QLabel(self.frame_119)
        self.semi_major_axis_toggle_menu_lbl_11.setObjectName(u"semi_major_axis_toggle_menu_lbl_11")
        self.semi_major_axis_toggle_menu_lbl_11.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_11.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_11.setFont(font13)
        self.semi_major_axis_toggle_menu_lbl_11.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.semi_major_axis_toggle_menu_lbl_11)


        self.verticalLayout_84.addWidget(self.frame_119, 0, Qt.AlignHCenter)

        self.frame_142 = QFrame(self.frame_118)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setMinimumSize(QSize(0, 30))
        self.frame_142.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	\n"
"	background:transparent;\n"
"	\n"
"\n"
"}")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_142)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_142)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font14)
        self.label_13.setFocusPolicy(Qt.NoFocus)
        self.label_13.setStyleSheet(u"color:grey;")
        self.label_13.setWordWrap(True)

        self.horizontalLayout_93.addWidget(self.label_13)


        self.verticalLayout_84.addWidget(self.frame_142)


        self.verticalLayout_86.addWidget(self.frame_118)

        self.Stacked_widg_Types_of_Orbital_Transfer.addWidget(self.page_10)

        self.horizontalLayout_83.addWidget(self.Stacked_widg_Types_of_Orbital_Transfer)


        self.horizontalLayout_89.addWidget(self.frame_45)


        self.horizontalLayout_85.addWidget(self.Container_for_Type_of_Orbital_Transfer)

        self.Orbtl_tranf_Inp_n_Out_frames_container = QFrame(self.Orbital_Transfer)
        self.Orbtl_tranf_Inp_n_Out_frames_container.setObjectName(u"Orbtl_tranf_Inp_n_Out_frames_container")
        sizePolicy1.setHeightForWidth(self.Orbtl_tranf_Inp_n_Out_frames_container.sizePolicy().hasHeightForWidth())
        self.Orbtl_tranf_Inp_n_Out_frames_container.setSizePolicy(sizePolicy1)
        self.Orbtl_tranf_Inp_n_Out_frames_container.setMinimumSize(QSize(0, 0))
        self.Orbtl_tranf_Inp_n_Out_frames_container.setMaximumSize(QSize(0, 16777215))
        self.Orbtl_tranf_Inp_n_Out_frames_container.setFrameShape(QFrame.StyledPanel)
        self.Orbtl_tranf_Inp_n_Out_frames_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.Orbtl_tranf_Inp_n_Out_frames_container)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.Orbtl_tranf_Inp_frame = QFrame(self.Orbtl_tranf_Inp_n_Out_frames_container)
        self.Orbtl_tranf_Inp_frame.setObjectName(u"Orbtl_tranf_Inp_frame")
        sizePolicy1.setHeightForWidth(self.Orbtl_tranf_Inp_frame.sizePolicy().hasHeightForWidth())
        self.Orbtl_tranf_Inp_frame.setSizePolicy(sizePolicy1)
        self.Orbtl_tranf_Inp_frame.setMinimumSize(QSize(560, 350))
        self.Orbtl_tranf_Inp_frame.setMaximumSize(QSize(560, 16777215))
        self.Orbtl_tranf_Inp_frame.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.Orbtl_tranf_Inp_frame.setFrameShape(QFrame.StyledPanel)
        self.Orbtl_tranf_Inp_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.Orbtl_tranf_Inp_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(4)
        self.gridLayout_6.setContentsMargins(-1, 9, -1, 6)
        self.frame_49 = QFrame(self.Orbtl_tranf_Inp_frame)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 320))
        self.frame_49.setStyleSheet(u"background:none;")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_49)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setVerticalSpacing(5)
        self.gridLayout_12.setContentsMargins(-1, 5, -1, 5)
        self.frame_55 = QFrame(self.frame_49)
        self.frame_55.setObjectName(u"frame_55")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy5)
        self.frame_55.setStyleSheet(u"background-color: #1b1b1b;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_55)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.widget_36 = QWidget(self.frame_55)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setMinimumSize(QSize(300, 30))
        self.widget_36.setMaximumSize(QSize(300, 35))
        self.widget_36.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_196 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_196.setSpacing(3)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.frame_128 = QFrame(self.widget_36)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMinimumSize(QSize(130, 30))
        self.frame_128.setMaximumSize(QSize(250, 16777215))
        self.frame_128.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_197 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_197.setSpacing(0)
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.horizontalLayout_197.setContentsMargins(0, 0, 0, 0)
        self.label_179 = QLabel(self.frame_128)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setMinimumSize(QSize(100, 20))
        self.label_179.setMaximumSize(QSize(125, 20))
        self.label_179.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_179.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_197.addWidget(self.label_179)


        self.horizontalLayout_196.addWidget(self.frame_128, 0, Qt.AlignVCenter)

        self.frame_129 = QFrame(self.widget_36)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_198 = QHBoxLayout(self.frame_129)
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.horizontalLayout_198.setContentsMargins(6, 6, 6, 6)
        self.label_180 = QLabel(self.frame_129)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_180.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_198.addWidget(self.label_180)

        self.label_181 = QLabel(self.frame_129)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setMinimumSize(QSize(52, 0))
        self.label_181.setMaximumSize(QSize(52, 16777215))
        self.label_181.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_198.addWidget(self.label_181)


        self.horizontalLayout_196.addWidget(self.frame_129)


        self.gridLayout_5.addWidget(self.widget_36, 2, 0, 1, 1)

        self.widget_35 = QWidget(self.frame_55)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMinimumSize(QSize(300, 30))
        self.widget_35.setMaximumSize(QSize(300, 35))
        self.widget_35.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_193 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_193.setSpacing(3)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(0, 0, 0, 0)
        self.frame_126 = QFrame(self.widget_35)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMinimumSize(QSize(130, 30))
        self.frame_126.setMaximumSize(QSize(250, 16777215))
        self.frame_126.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_194 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.label_175 = QLabel(self.frame_126)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMinimumSize(QSize(100, 20))
        self.label_175.setMaximumSize(QSize(125, 20))
        self.label_175.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_175.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_194.addWidget(self.label_175)


        self.horizontalLayout_193.addWidget(self.frame_126, 0, Qt.AlignVCenter)

        self.frame_127 = QFrame(self.widget_35)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_195 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(6, 6, 6, 6)
        self.label_177 = QLabel(self.frame_127)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_177.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_195.addWidget(self.label_177)

        self.label_178 = QLabel(self.frame_127)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setMinimumSize(QSize(52, 0))
        self.label_178.setMaximumSize(QSize(52, 16777215))
        self.label_178.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_195.addWidget(self.label_178)


        self.horizontalLayout_193.addWidget(self.frame_127)


        self.gridLayout_5.addWidget(self.widget_35, 1, 0, 1, 1, Qt.AlignHCenter)

        self.frame_50 = QFrame(self.frame_55)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 30))
        self.frame_50.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_50)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_5 = QLabel(self.frame_50)
        self.semi_major_axis_toggle_menu_lbl_5.setObjectName(u"semi_major_axis_toggle_menu_lbl_5")
        self.semi_major_axis_toggle_menu_lbl_5.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_5.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_5.setFont(font12)
        self.semi_major_axis_toggle_menu_lbl_5.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.semi_major_axis_toggle_menu_lbl_5)


        self.gridLayout_5.addWidget(self.frame_50, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_55, 0, 0, 1, 1)

        self.frame_95 = QFrame(self.frame_49)
        self.frame_95.setObjectName(u"frame_95")
        sizePolicy5.setHeightForWidth(self.frame_95.sizePolicy().hasHeightForWidth())
        self.frame_95.setSizePolicy(sizePolicy5)
        self.frame_95.setStyleSheet(u"background-color: #1b1b1b;")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_95)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.widget_37 = QWidget(self.frame_95)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMinimumSize(QSize(300, 30))
        self.widget_37.setMaximumSize(QSize(300, 35))
        self.widget_37.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_199 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_199.setSpacing(3)
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.horizontalLayout_199.setContentsMargins(0, 0, 0, 0)
        self.frame_130 = QFrame(self.widget_37)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMinimumSize(QSize(130, 30))
        self.frame_130.setMaximumSize(QSize(250, 16777215))
        self.frame_130.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_200 = QHBoxLayout(self.frame_130)
        self.horizontalLayout_200.setSpacing(0)
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.label_182 = QLabel(self.frame_130)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMinimumSize(QSize(100, 20))
        self.label_182.setMaximumSize(QSize(125, 20))
        self.label_182.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_182.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_200.addWidget(self.label_182)


        self.horizontalLayout_199.addWidget(self.frame_130, 0, Qt.AlignVCenter)

        self.frame_131 = QFrame(self.widget_37)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_201 = QHBoxLayout(self.frame_131)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(6, 6, 6, 6)
        self.label_183 = QLabel(self.frame_131)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_183.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_201.addWidget(self.label_183)

        self.label_184 = QLabel(self.frame_131)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setMinimumSize(QSize(52, 0))
        self.label_184.setMaximumSize(QSize(52, 16777215))
        self.label_184.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_201.addWidget(self.label_184)


        self.horizontalLayout_199.addWidget(self.frame_131)


        self.gridLayout_7.addWidget(self.widget_37, 2, 0, 1, 1)

        self.widget_38 = QWidget(self.frame_95)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setMinimumSize(QSize(300, 30))
        self.widget_38.setMaximumSize(QSize(300, 35))
        self.widget_38.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_202 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_202.setSpacing(3)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.frame_132 = QFrame(self.widget_38)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(130, 30))
        self.frame_132.setMaximumSize(QSize(250, 16777215))
        self.frame_132.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_203 = QHBoxLayout(self.frame_132)
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.horizontalLayout_203.setContentsMargins(0, 0, 0, 0)
        self.label_185 = QLabel(self.frame_132)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setMinimumSize(QSize(100, 20))
        self.label_185.setMaximumSize(QSize(125, 20))
        self.label_185.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_185.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_203.addWidget(self.label_185)


        self.horizontalLayout_202.addWidget(self.frame_132, 0, Qt.AlignVCenter)

        self.frame_133 = QFrame(self.widget_38)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_204 = QHBoxLayout(self.frame_133)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.horizontalLayout_204.setContentsMargins(6, 6, 6, 6)
        self.label_186 = QLabel(self.frame_133)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_186.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_204.addWidget(self.label_186)

        self.label_187 = QLabel(self.frame_133)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setMinimumSize(QSize(52, 0))
        self.label_187.setMaximumSize(QSize(52, 16777215))
        self.label_187.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_204.addWidget(self.label_187)


        self.horizontalLayout_202.addWidget(self.frame_133)


        self.gridLayout_7.addWidget(self.widget_38, 1, 0, 1, 1, Qt.AlignHCenter)

        self.frame_51 = QFrame(self.frame_95)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 30))
        self.frame_51.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_51)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_6 = QLabel(self.frame_51)
        self.semi_major_axis_toggle_menu_lbl_6.setObjectName(u"semi_major_axis_toggle_menu_lbl_6")
        self.semi_major_axis_toggle_menu_lbl_6.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_6.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_6.setFont(font12)
        self.semi_major_axis_toggle_menu_lbl_6.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_74.addWidget(self.semi_major_axis_toggle_menu_lbl_6)


        self.gridLayout_7.addWidget(self.frame_51, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_95, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_49, 3, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_17, 6, 0, 1, 1)

        self.semi_major_axis_toggle_menu_lbl_7 = QLabel(self.Orbtl_tranf_Inp_frame)
        self.semi_major_axis_toggle_menu_lbl_7.setObjectName(u"semi_major_axis_toggle_menu_lbl_7")
        self.semi_major_axis_toggle_menu_lbl_7.setMinimumSize(QSize(425, 25))
        self.semi_major_axis_toggle_menu_lbl_7.setMaximumSize(QSize(425, 20))
        font15 = QFont()
        font15.setPointSize(14)
        font15.setBold(True)
        font15.setWeight(75)
        self.semi_major_axis_toggle_menu_lbl_7.setFont(font15)
        self.semi_major_axis_toggle_menu_lbl_7.setStyleSheet(u"QLabel{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.semi_major_axis_toggle_menu_lbl_7, 0, 0, 1, 1)

        self.Orbital_Transfer_plot_button = QPushButton(self.Orbtl_tranf_Inp_frame)
        self.Orbital_Transfer_plot_button.setObjectName(u"Orbital_Transfer_plot_button")
        sizePolicy2.setHeightForWidth(self.Orbital_Transfer_plot_button.sizePolicy().hasHeightForWidth())
        self.Orbital_Transfer_plot_button.setSizePolicy(sizePolicy2)
        self.Orbital_Transfer_plot_button.setMinimumSize(QSize(130, 30))
        self.Orbital_Transfer_plot_button.setMaximumSize(QSize(150, 40))
        self.Orbital_Transfer_plot_button.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:10px;\n"
"	color:#fff;\n"
"	background-color: rgb(175, 101, 174);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:rgb(175, 101, 194);\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.Orbital_Transfer_plot_button, 5, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_12, 2, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_16, 4, 0, 1, 1)


        self.verticalLayout_69.addWidget(self.Orbtl_tranf_Inp_frame)

        self.Orbtl_tranf_Out_frame = QFrame(self.Orbtl_tranf_Inp_n_Out_frames_container)
        self.Orbtl_tranf_Out_frame.setObjectName(u"Orbtl_tranf_Out_frame")
        self.Orbtl_tranf_Out_frame.setMinimumSize(QSize(0, 130))
        self.Orbtl_tranf_Out_frame.setMaximumSize(QSize(16777215, 1500))
        self.Orbtl_tranf_Out_frame.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.Orbtl_tranf_Out_frame.setFrameShape(QFrame.StyledPanel)
        self.Orbtl_tranf_Out_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_173 = QHBoxLayout(self.Orbtl_tranf_Out_frame)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.frame_96 = QFrame(self.Orbtl_tranf_Out_frame)
        self.frame_96.setObjectName(u"frame_96")
        sizePolicy5.setHeightForWidth(self.frame_96.sizePolicy().hasHeightForWidth())
        self.frame_96.setSizePolicy(sizePolicy5)
        self.frame_96.setMinimumSize(QSize(0, 120))
        self.frame_96.setMaximumSize(QSize(16777215, 120))
        self.frame_96.setStyleSheet(u"background-color: #1b1b1b;")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_96)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.frame_52 = QFrame(self.frame_96)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 25))
        self.frame_52.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	border-radius:10px;\n"
"	\n"
"\n"
"}")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_52)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_8 = QLabel(self.frame_52)
        self.semi_major_axis_toggle_menu_lbl_8.setObjectName(u"semi_major_axis_toggle_menu_lbl_8")
        self.semi_major_axis_toggle_menu_lbl_8.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_8.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_8.setFont(font12)
        self.semi_major_axis_toggle_menu_lbl_8.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.semi_major_axis_toggle_menu_lbl_8)


        self.verticalLayout_90.addWidget(self.frame_52)

        self.widget_40 = QWidget(self.frame_96)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMinimumSize(QSize(250, 30))
        self.widget_40.setMaximumSize(QSize(250, 30))
        self.widget_40.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_214 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_214.setSpacing(3)
        self.horizontalLayout_214.setObjectName(u"horizontalLayout_214")
        self.horizontalLayout_214.setContentsMargins(0, 0, 0, 0)
        self.frame_140 = QFrame(self.widget_40)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setMinimumSize(QSize(130, 30))
        self.frame_140.setMaximumSize(QSize(250, 16777215))
        self.frame_140.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_140)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 12)
        self.label_197 = QLabel(self.frame_140)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setMinimumSize(QSize(100, 30))
        self.label_197.setMaximumSize(QSize(125, 20))
        self.label_197.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_197.setAlignment(Qt.AlignCenter)
        self.label_197.setWordWrap(True)

        self.horizontalLayout_87.addWidget(self.label_197)


        self.horizontalLayout_214.addWidget(self.frame_140, 0, Qt.AlignVCenter)

        self.frame_141 = QFrame(self.widget_40)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_216 = QHBoxLayout(self.frame_141)
        self.horizontalLayout_216.setObjectName(u"horizontalLayout_216")
        self.horizontalLayout_216.setContentsMargins(6, 6, 6, 6)
        self.label_198 = QLabel(self.frame_141)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setMinimumSize(QSize(0, 18))
        self.label_198.setMaximumSize(QSize(16777215, 18))
        self.label_198.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_198.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_216.addWidget(self.label_198)

        self.label_199 = QLabel(self.frame_141)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setMinimumSize(QSize(35, 0))
        self.label_199.setMaximumSize(QSize(35, 16777215))
        self.label_199.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_216.addWidget(self.label_199)


        self.horizontalLayout_214.addWidget(self.frame_141)


        self.verticalLayout_90.addWidget(self.widget_40)

        self.widget_42 = QWidget(self.frame_96)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMinimumSize(QSize(250, 30))
        self.widget_42.setMaximumSize(QSize(250, 30))
        self.widget_42.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_218 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_218.setSpacing(3)
        self.horizontalLayout_218.setObjectName(u"horizontalLayout_218")
        self.horizontalLayout_218.setContentsMargins(0, 0, 0, 0)
        self.frame_146 = QFrame(self.widget_42)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMinimumSize(QSize(130, 30))
        self.frame_146.setMaximumSize(QSize(250, 16777215))
        self.frame_146.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 12)
        self.label_203 = QLabel(self.frame_146)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setMinimumSize(QSize(100, 30))
        self.label_203.setMaximumSize(QSize(125, 20))
        self.label_203.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_203.setAlignment(Qt.AlignCenter)
        self.label_203.setWordWrap(True)

        self.horizontalLayout_96.addWidget(self.label_203)


        self.horizontalLayout_218.addWidget(self.frame_146, 0, Qt.AlignVCenter)

        self.frame_147 = QFrame(self.widget_42)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_219 = QHBoxLayout(self.frame_147)
        self.horizontalLayout_219.setObjectName(u"horizontalLayout_219")
        self.horizontalLayout_219.setContentsMargins(6, 6, 6, 6)
        self.label_204 = QLabel(self.frame_147)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setMinimumSize(QSize(0, 18))
        self.label_204.setMaximumSize(QSize(16777215, 18))
        self.label_204.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_204.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_219.addWidget(self.label_204)

        self.label_205 = QLabel(self.frame_147)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setMinimumSize(QSize(35, 0))
        self.label_205.setMaximumSize(QSize(35, 16777215))
        self.label_205.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_219.addWidget(self.label_205)


        self.horizontalLayout_218.addWidget(self.frame_147)


        self.verticalLayout_90.addWidget(self.widget_42)


        self.horizontalLayout_173.addWidget(self.frame_96)

        self.frame_138 = QFrame(self.Orbtl_tranf_Out_frame)
        self.frame_138.setObjectName(u"frame_138")
        sizePolicy5.setHeightForWidth(self.frame_138.sizePolicy().hasHeightForWidth())
        self.frame_138.setSizePolicy(sizePolicy5)
        self.frame_138.setMinimumSize(QSize(0, 120))
        self.frame_138.setMaximumSize(QSize(16777215, 120))
        self.frame_138.setStyleSheet(u"background-color: #1b1b1b;")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_138)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.frame_139 = QFrame(self.frame_138)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setMinimumSize(QSize(0, 25))
        self.frame_139.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	border-radius:10px;\n"
"	\n"
"\n"
"}")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_139)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_12 = QLabel(self.frame_139)
        self.semi_major_axis_toggle_menu_lbl_12.setObjectName(u"semi_major_axis_toggle_menu_lbl_12")
        self.semi_major_axis_toggle_menu_lbl_12.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_12.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_12.setFont(font12)
        self.semi_major_axis_toggle_menu_lbl_12.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_87.addWidget(self.semi_major_axis_toggle_menu_lbl_12)


        self.verticalLayout_91.addWidget(self.frame_139)

        self.widget_41 = QWidget(self.frame_138)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setMinimumSize(QSize(250, 30))
        self.widget_41.setMaximumSize(QSize(250, 30))
        self.widget_41.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_215 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_215.setSpacing(3)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.horizontalLayout_215.setContentsMargins(0, 0, 0, 0)
        self.frame_144 = QFrame(self.widget_41)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setMinimumSize(QSize(130, 30))
        self.frame_144.setMaximumSize(QSize(250, 16777215))
        self.frame_144.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_144)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 12)
        self.label_200 = QLabel(self.frame_144)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setMinimumSize(QSize(100, 30))
        self.label_200.setMaximumSize(QSize(125, 20))
        self.label_200.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_200.setAlignment(Qt.AlignCenter)
        self.label_200.setWordWrap(True)

        self.horizontalLayout_94.addWidget(self.label_200)


        self.horizontalLayout_215.addWidget(self.frame_144, 0, Qt.AlignVCenter)

        self.frame_145 = QFrame(self.widget_41)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_217 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_217.setObjectName(u"horizontalLayout_217")
        self.horizontalLayout_217.setContentsMargins(6, 6, 6, 6)
        self.label_201 = QLabel(self.frame_145)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setMinimumSize(QSize(0, 18))
        self.label_201.setMaximumSize(QSize(16777215, 18))
        self.label_201.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_201.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_217.addWidget(self.label_201)

        self.label_202 = QLabel(self.frame_145)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setMinimumSize(QSize(35, 0))
        self.label_202.setMaximumSize(QSize(35, 16777215))
        self.label_202.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_217.addWidget(self.label_202)


        self.horizontalLayout_215.addWidget(self.frame_145)


        self.verticalLayout_91.addWidget(self.widget_41)

        self.widget_43 = QWidget(self.frame_138)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMinimumSize(QSize(250, 30))
        self.widget_43.setMaximumSize(QSize(250, 30))
        self.widget_43.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_220 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_220.setSpacing(3)
        self.horizontalLayout_220.setObjectName(u"horizontalLayout_220")
        self.horizontalLayout_220.setContentsMargins(0, 0, 0, 0)
        self.frame_148 = QFrame(self.widget_43)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setMinimumSize(QSize(130, 30))
        self.frame_148.setMaximumSize(QSize(250, 16777215))
        self.frame_148.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_151 = QHBoxLayout(self.frame_148)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_151.setContentsMargins(0, 0, 0, 12)
        self.label_206 = QLabel(self.frame_148)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setMinimumSize(QSize(100, 30))
        self.label_206.setMaximumSize(QSize(125, 20))
        self.label_206.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_206.setAlignment(Qt.AlignCenter)
        self.label_206.setWordWrap(True)

        self.horizontalLayout_151.addWidget(self.label_206)


        self.horizontalLayout_220.addWidget(self.frame_148, 0, Qt.AlignVCenter)

        self.frame_149 = QFrame(self.widget_43)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_221 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_221.setObjectName(u"horizontalLayout_221")
        self.horizontalLayout_221.setContentsMargins(6, 6, 6, 6)
        self.label_207 = QLabel(self.frame_149)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setMinimumSize(QSize(0, 18))
        self.label_207.setMaximumSize(QSize(16777215, 18))
        self.label_207.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_207.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_221.addWidget(self.label_207)

        self.label_208 = QLabel(self.frame_149)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setMinimumSize(QSize(35, 0))
        self.label_208.setMaximumSize(QSize(35, 16777215))
        self.label_208.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_221.addWidget(self.label_208)


        self.horizontalLayout_220.addWidget(self.frame_149)


        self.verticalLayout_91.addWidget(self.widget_43)


        self.horizontalLayout_173.addWidget(self.frame_138)


        self.verticalLayout_69.addWidget(self.Orbtl_tranf_Out_frame)


        self.horizontalLayout_85.addWidget(self.Orbtl_tranf_Inp_n_Out_frames_container)

        self.Plot_frame_for_Orbital_transfer = QFrame(self.Orbital_Transfer)
        self.Plot_frame_for_Orbital_transfer.setObjectName(u"Plot_frame_for_Orbital_transfer")
        self.Plot_frame_for_Orbital_transfer.setMinimumSize(QSize(0, 0))
        self.Plot_frame_for_Orbital_transfer.setMaximumSize(QSize(0, 16777215))
        self.Plot_frame_for_Orbital_transfer.setSizeIncrement(QSize(0, 0))
        self.Plot_frame_for_Orbital_transfer.setStyleSheet(u"background:transparent;")
        self.Plot_frame_for_Orbital_transfer.setFrameShape(QFrame.StyledPanel)
        self.Plot_frame_for_Orbital_transfer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.Plot_frame_for_Orbital_transfer)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_150 = QFrame(self.Plot_frame_for_Orbital_transfer)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setMinimumSize(QSize(450, 0))
        self.frame_150.setMaximumSize(QSize(450, 16777215))
        self.frame_150.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_150)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.Plot_Widget_for_Orbital_Transfer = QWidget(self.frame_150)
        self.Plot_Widget_for_Orbital_Transfer.setObjectName(u"Plot_Widget_for_Orbital_Transfer")

        self.verticalLayout_88.addWidget(self.Plot_Widget_for_Orbital_Transfer)


        self.verticalLayout_78.addWidget(self.frame_150)

        self.Total_Delta_V_container = QFrame(self.Plot_frame_for_Orbital_transfer)
        self.Total_Delta_V_container.setObjectName(u"Total_Delta_V_container")
        self.Total_Delta_V_container.setMinimumSize(QSize(0, 150))
        self.Total_Delta_V_container.setMaximumSize(QSize(16777215, 150))
        self.Total_Delta_V_container.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.Total_Delta_V_container.setFrameShape(QFrame.StyledPanel)
        self.Total_Delta_V_container.setFrameShadow(QFrame.Raised)
        self.frame_152 = QFrame(self.Total_Delta_V_container)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setGeometry(QRect(95, 40, 260, 70))
        sizePolicy5.setHeightForWidth(self.frame_152.sizePolicy().hasHeightForWidth())
        self.frame_152.setSizePolicy(sizePolicy5)
        self.frame_152.setMinimumSize(QSize(0, 70))
        self.frame_152.setMaximumSize(QSize(16777215, 70))
        self.frame_152.setStyleSheet(u"background-color: #1b1b1b;")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_152)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(5)
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.frame_155 = QFrame(self.frame_152)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setMinimumSize(QSize(0, 25))
        self.frame_155.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	border-radius:10px;\n"
"	\n"
"\n"
"}")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_155)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_13 = QLabel(self.frame_155)
        self.semi_major_axis_toggle_menu_lbl_13.setObjectName(u"semi_major_axis_toggle_menu_lbl_13")
        self.semi_major_axis_toggle_menu_lbl_13.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_13.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_13.setFont(font12)
        self.semi_major_axis_toggle_menu_lbl_13.setStyleSheet(u"QLabel{\n"
"color: rgb(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_89.addWidget(self.semi_major_axis_toggle_menu_lbl_13)


        self.gridLayout_11.addWidget(self.frame_155, 0, 0, 1, 1)

        self.widget_44 = QWidget(self.frame_152)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setMinimumSize(QSize(250, 30))
        self.widget_44.setMaximumSize(QSize(250, 30))
        self.widget_44.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_224 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_224.setSpacing(3)
        self.horizontalLayout_224.setObjectName(u"horizontalLayout_224")
        self.horizontalLayout_224.setContentsMargins(0, 0, 0, 0)
        self.frame_153 = QFrame(self.widget_44)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMinimumSize(QSize(130, 30))
        self.frame_153.setMaximumSize(QSize(250, 16777215))
        self.frame_153.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 6)
        self.label_209 = QLabel(self.frame_153)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setMinimumSize(QSize(100, 30))
        self.label_209.setMaximumSize(QSize(125, 20))
        self.label_209.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_209.setAlignment(Qt.AlignCenter)
        self.label_209.setWordWrap(True)

        self.horizontalLayout_95.addWidget(self.label_209)


        self.horizontalLayout_224.addWidget(self.frame_153, 0, Qt.AlignVCenter)

        self.frame_154 = QFrame(self.widget_44)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_225 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_225.setObjectName(u"horizontalLayout_225")
        self.horizontalLayout_225.setContentsMargins(6, 6, 6, 6)
        self.label_210 = QLabel(self.frame_154)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setMinimumSize(QSize(0, 18))
        self.label_210.setMaximumSize(QSize(16777215, 18))
        self.label_210.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_210.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_225.addWidget(self.label_210)

        self.label_211 = QLabel(self.frame_154)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setMinimumSize(QSize(35, 0))
        self.label_211.setMaximumSize(QSize(35, 16777215))
        self.label_211.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_225.addWidget(self.label_211)


        self.horizontalLayout_224.addWidget(self.frame_154)


        self.gridLayout_11.addWidget(self.widget_44, 1, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_78.addWidget(self.Total_Delta_V_container)


        self.horizontalLayout_85.addWidget(self.Plot_frame_for_Orbital_transfer)

        self.stackedWidget.addWidget(self.Orbital_Transfer)
        self.Planetary_Ephemeris = QWidget()
        self.Planetary_Ephemeris.setObjectName(u"Planetary_Ephemeris")
        self.horizontalLayout_73 = QHBoxLayout(self.Planetary_Ephemeris)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(5, 0, 5, 0)
        self.frame_6 = QFrame(self.Planetary_Ephemeris)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_48 = QFrame(self.frame_6)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 50))
        self.frame_48.setMaximumSize(QSize(16777215, 50))
        self.frame_48.setStyleSheet(u"background:none;")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_172 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.SOI_planet_name_2 = QComboBox(self.frame_48)
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.addItem("")
        self.SOI_planet_name_2.setObjectName(u"SOI_planet_name_2")
        self.SOI_planet_name_2.setMinimumSize(QSize(200, 40))
        self.SOI_planet_name_2.setMaximumSize(QSize(200, 40))
        self.SOI_planet_name_2.setLayoutDirection(Qt.LeftToRight)
        self.SOI_planet_name_2.setStyleSheet(u"QComboBox{\n"
"	\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 20px;\n"
"	background-color:#c98cff;\n"
"	border: 8px solid transparent;\n"
"	\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 2px solid rgba(168, 128, 243, 60%);\n"
"}\n"
"")

        self.horizontalLayout_172.addWidget(self.SOI_planet_name_2)


        self.verticalLayout_12.addWidget(self.frame_48)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 300))
        self.frame_10.setMaximumSize(QSize(16777215, 300))
        self.frame_10.setStyleSheet(u"background:none;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_5)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background:none;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_107.setSpacing(40)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(9, 9, 9, 9)
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(320, 250))
        self.frame_16.setMaximumSize(QSize(360, 250))
        self.frame_16.setStyleSheet(u"QFrame{\n"
"\n"
"border: transparent;\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(168, 128, 243, 255), stop:1 rgba(108, 121, 240, 255));\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 4px solid rgba(168, 128, 243, 60%);\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_10 = QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_137 = QLabel(self.frame_16)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setStyleSheet(u"QLabel{background-color:#c98cff;\n"
"border-radius:8px;}\n"
"\n"
"QLabel:hover{\n"
"border:none;\n"
"}\n"
"")
        self.label_137.setMargin(3)

        self.verticalLayout_10.addWidget(self.label_137, 0, Qt.AlignHCenter)

        self.calendarWidget_2 = QCalendarWidget(self.frame_16)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")
        self.calendarWidget_2.setMinimumSize(QSize(320, 200))
        self.calendarWidget_2.setMaximumSize(QSize(320, 205))
        self.calendarWidget_2.setStyleSheet(u"\n"
"QCalendarWidget QToolButton{\n"
"\n"
"	\n"
"	height: 20px;\n"
"	width: 150px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	icon-size: 30px,30px;\n"
"	background-color: green;\n"
"	border: 2px solid black;\n"
"	border-radius:4px;\n"
"\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView\n"
"{\n"
"	background-color: rgb(192,192,192); \n"
"	selection-background-color: rgb(0, 170, 0, 60%);\n"
"	selection-border: 1px solid black;\n"
"	selection-border-radius:2px;\n"
"	selection-color: black; \n"
"	border:2px solid black;\n"
"	border-radius:4px;\n"
"}")

        self.verticalLayout_10.addWidget(self.calendarWidget_2)


        self.horizontalLayout_107.addWidget(self.frame_16, 0, Qt.AlignVCenter)

        self.Date_time_frame_2 = QFrame(self.frame_13)
        self.Date_time_frame_2.setObjectName(u"Date_time_frame_2")
        sizePolicy1.setHeightForWidth(self.Date_time_frame_2.sizePolicy().hasHeightForWidth())
        self.Date_time_frame_2.setSizePolicy(sizePolicy1)
        self.Date_time_frame_2.setMinimumSize(QSize(320, 250))
        self.Date_time_frame_2.setMaximumSize(QSize(340, 250))
        self.Date_time_frame_2.setFont(font4)
        self.Date_time_frame_2.setStyleSheet(u"QFrame{\n"
"\n"
"border: transparent;\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(168, 128, 243, 255), stop:1 rgba(108, 121, 240, 255));\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 4px solid rgba(168, 128, 243, 60%);\n"
"}")
        self.Date_time_frame_2.setFrameShape(QFrame.StyledPanel)
        self.Date_time_frame_2.setFrameShadow(QFrame.Sunken)
        self.label_110 = QLabel(self.Date_time_frame_2)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(20, 90, 111, 16))
        self.label_110.setFont(font6)
        self.label_110.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.timeEdit_2 = QTimeEdit(self.Date_time_frame_2)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setGeometry(QRect(130, 80, 141, 31))
        self.timeEdit_2.setFont(font4)
        self.timeEdit_2.setStyleSheet(u"    /*spinbox lift style*/\n"
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
"    }\n"
"	QTimeEdit{\n"
"	\n"
"	background-color: rgb(201, 140, 255);\n"
"}")
        self.timeEdit_2.setAlignment(Qt.AlignCenter)
        self.timeEdit_2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.timeEdit_2.setCurrentSection(QDateTimeEdit.HourSection)
        self.label_135 = QLabel(self.Date_time_frame_2)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(280, 90, 31, 21))
        self.label_135.setFont(font6)
        self.label_135.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.label_135.setAlignment(Qt.AlignCenter)
        self.label_136 = QLabel(self.Date_time_frame_2)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(160, 120, 101, 16))
        self.label_136.setFont(font6)
        self.label_136.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.PE_Cal_Btn = QPushButton(self.Date_time_frame_2)
        self.PE_Cal_Btn.setObjectName(u"PE_Cal_Btn")
        self.PE_Cal_Btn.setGeometry(QRect(90, 192, 151, 31))
        self.PE_Cal_Btn.setFont(font7)
        self.PE_Cal_Btn.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(2, 119, 189,60%);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 14px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0,60%);\n"
"}")

        self.horizontalLayout_107.addWidget(self.Date_time_frame_2)


        self.horizontalLayout_86.addWidget(self.frame_13)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_6)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.Bottom_slider_PE_Output = QFrame(self.frame_6)
        self.Bottom_slider_PE_Output.setObjectName(u"Bottom_slider_PE_Output")
        sizePolicy3.setHeightForWidth(self.Bottom_slider_PE_Output.sizePolicy().hasHeightForWidth())
        self.Bottom_slider_PE_Output.setSizePolicy(sizePolicy3)
        self.Bottom_slider_PE_Output.setMinimumSize(QSize(0, 0))
        self.Bottom_slider_PE_Output.setMaximumSize(QSize(16878, 0))
        self.Bottom_slider_PE_Output.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 255), stop:1 rgba(161, 161, 161, 255));\n"
"	\n"
"\n"
"}")
        self.Bottom_slider_PE_Output.setFrameShape(QFrame.StyledPanel)
        self.Bottom_slider_PE_Output.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.Bottom_slider_PE_Output)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(30, -1, 30, -1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(20)
        self.widget_27 = QWidget(self.Bottom_slider_PE_Output)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(300, 35))
        self.widget_27.setMaximumSize(QSize(300, 60))
        self.widget_27.setStyleSheet(u"background:none;")
        self.horizontalLayout_169 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_169.setSpacing(3)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.horizontalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.frame_110 = QFrame(self.widget_27)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(130, 35))
        self.frame_110.setMaximumSize(QSize(250, 16777215))
        self.frame_110.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_170 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_170.setContentsMargins(6, 6, 6, 6)
        self.label_153 = QLabel(self.frame_110)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMinimumSize(QSize(100, 20))
        self.label_153.setMaximumSize(QSize(125, 20))
        self.label_153.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_153.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_170.addWidget(self.label_153, 0, Qt.AlignVCenter)


        self.horizontalLayout_169.addWidget(self.frame_110, 0, Qt.AlignVCenter)

        self.frame_111 = QFrame(self.widget_27)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_171 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.horizontalLayout_171.setContentsMargins(6, 6, 6, 6)
        self.label_154 = QLabel(self.frame_111)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_154.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_171.addWidget(self.label_154)

        self.label_155 = QLabel(self.frame_111)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMinimumSize(QSize(52, 0))
        self.label_155.setMaximumSize(QSize(52, 16777215))
        self.label_155.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_171.addWidget(self.label_155)


        self.horizontalLayout_169.addWidget(self.frame_111)


        self.gridLayout_4.addWidget(self.widget_27, 0, 2, 1, 1)

        self.widget_32 = QWidget(self.Bottom_slider_PE_Output)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMinimumSize(QSize(300, 35))
        self.widget_32.setMaximumSize(QSize(300, 35))
        self.widget_32.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_184 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_184.setSpacing(3)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.frame_120 = QFrame(self.widget_32)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMinimumSize(QSize(130, 35))
        self.frame_120.setMaximumSize(QSize(250, 16777215))
        self.frame_120.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_185 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.horizontalLayout_185.setContentsMargins(6, 6, 6, 6)
        self.label_168 = QLabel(self.frame_120)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setMinimumSize(QSize(100, 20))
        self.label_168.setMaximumSize(QSize(125, 20))
        self.label_168.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_168.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_185.addWidget(self.label_168)


        self.horizontalLayout_184.addWidget(self.frame_120, 0, Qt.AlignVCenter)

        self.frame_121 = QFrame(self.widget_32)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_186 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(6, 6, 6, 6)
        self.label_169 = QLabel(self.frame_121)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_169.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_186.addWidget(self.label_169)

        self.label_170 = QLabel(self.frame_121)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMinimumSize(QSize(52, 0))
        self.label_170.setMaximumSize(QSize(52, 16777215))
        self.label_170.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_186.addWidget(self.label_170)


        self.horizontalLayout_184.addWidget(self.frame_121)


        self.gridLayout_4.addWidget(self.widget_32, 0, 0, 1, 1)

        self.widget_25 = QWidget(self.Bottom_slider_PE_Output)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(300, 35))
        self.widget_25.setMaximumSize(QSize(300, 35))
        self.widget_25.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}\n"
"")
        self.horizontalLayout_163 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_163.setSpacing(3)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.frame_106 = QFrame(self.widget_25)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(130, 35))
        self.frame_106.setMaximumSize(QSize(250, 16777215))
        self.frame_106.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_164 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.horizontalLayout_164.setContentsMargins(6, 6, 6, 6)
        self.label_147 = QLabel(self.frame_106)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMinimumSize(QSize(100, 20))
        self.label_147.setMaximumSize(QSize(125, 20))
        self.label_147.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_147.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_164.addWidget(self.label_147, 0, Qt.AlignVCenter)


        self.horizontalLayout_163.addWidget(self.frame_106, 0, Qt.AlignVCenter)

        self.frame_107 = QFrame(self.widget_25)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_165 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_165.setSpacing(6)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalLayout_165.setContentsMargins(6, 6, 6, 6)
        self.label_148 = QLabel(self.frame_107)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_148.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_165.addWidget(self.label_148)

        self.label_149 = QLabel(self.frame_107)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMinimumSize(QSize(52, 0))
        self.label_149.setMaximumSize(QSize(52, 16777215))
        self.label_149.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_149.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_165.addWidget(self.label_149)


        self.horizontalLayout_163.addWidget(self.frame_107)


        self.gridLayout_4.addWidget(self.widget_25, 2, 0, 1, 1)

        self.widget_22 = QWidget(self.Bottom_slider_PE_Output)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(300, 35))
        self.widget_22.setMaximumSize(QSize(300, 35))
        self.widget_22.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_152 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_152.setSpacing(3)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalLayout_152.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.widget_22)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(130, 35))
        self.frame_100.setMaximumSize(QSize(250, 16777215))
        self.frame_100.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_153 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_153.setContentsMargins(6, 6, 6, 6)
        self.label_138 = QLabel(self.frame_100)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMinimumSize(QSize(100, 20))
        self.label_138.setMaximumSize(QSize(125, 20))
        self.label_138.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_138.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_153.addWidget(self.label_138, 0, Qt.AlignVCenter)


        self.horizontalLayout_152.addWidget(self.frame_100, 0, Qt.AlignVCenter)

        self.frame_101 = QFrame(self.widget_22)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(6, 6, 6, 6)
        self.label_139 = QLabel(self.frame_101)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_154.addWidget(self.label_139)

        self.label_140 = QLabel(self.frame_101)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(52, 0))
        self.label_140.setMaximumSize(QSize(52, 16777215))
        self.label_140.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_140.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_154.addWidget(self.label_140)


        self.horizontalLayout_152.addWidget(self.frame_101)


        self.gridLayout_4.addWidget(self.widget_22, 1, 0, 1, 1)

        self.widget_33 = QWidget(self.Bottom_slider_PE_Output)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(300, 35))
        self.widget_33.setMaximumSize(QSize(300, 60))
        self.widget_33.setStyleSheet(u"background:none;")
        self.horizontalLayout_187 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_187.setSpacing(3)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.frame_122 = QFrame(self.widget_33)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMinimumSize(QSize(130, 35))
        self.frame_122.setMaximumSize(QSize(250, 16777215))
        self.frame_122.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_188 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_188.setContentsMargins(6, 6, 6, 6)
        self.label_171 = QLabel(self.frame_122)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMinimumSize(QSize(100, 20))
        self.label_171.setMaximumSize(QSize(125, 20))
        self.label_171.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_171.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_188.addWidget(self.label_171, 0, Qt.AlignVCenter)


        self.horizontalLayout_187.addWidget(self.frame_122, 0, Qt.AlignVCenter)

        self.frame_123 = QFrame(self.widget_33)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_189 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_189.setContentsMargins(6, 6, 6, 6)
        self.label_172 = QLabel(self.frame_123)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_172.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_189.addWidget(self.label_172)

        self.label_173 = QLabel(self.frame_123)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setMinimumSize(QSize(52, 0))
        self.label_173.setMaximumSize(QSize(52, 16777215))
        self.label_173.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_189.addWidget(self.label_173)


        self.horizontalLayout_187.addWidget(self.frame_123)


        self.gridLayout_4.addWidget(self.widget_33, 2, 2, 1, 1)

        self.widget_24 = QWidget(self.Bottom_slider_PE_Output)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(300, 35))
        self.widget_24.setMaximumSize(QSize(300, 35))
        self.widget_24.setStyleSheet(u"background:none;")
        self.horizontalLayout_160 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_160.setSpacing(3)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_160.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.widget_24)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(130, 35))
        self.frame_104.setMaximumSize(QSize(250, 16777215))
        self.frame_104.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_161 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.horizontalLayout_161.setContentsMargins(6, 6, 6, 6)
        self.label_144 = QLabel(self.frame_104)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(100, 20))
        self.label_144.setMaximumSize(QSize(125, 20))
        self.label_144.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_144.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_161.addWidget(self.label_144, 0, Qt.AlignVCenter)


        self.horizontalLayout_160.addWidget(self.frame_104, 0, Qt.AlignVCenter)

        self.frame_105 = QFrame(self.widget_24)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_162 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalLayout_162.setContentsMargins(6, 6, 6, 6)
        self.label_145 = QLabel(self.frame_105)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_145.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_162.addWidget(self.label_145)

        self.label_146 = QLabel(self.frame_105)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(52, 0))
        self.label_146.setMaximumSize(QSize(52, 16777215))
        self.label_146.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_162.addWidget(self.label_146)


        self.horizontalLayout_160.addWidget(self.frame_105)


        self.gridLayout_4.addWidget(self.widget_24, 1, 2, 1, 1)

        self.widget_29 = QWidget(self.Bottom_slider_PE_Output)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMinimumSize(QSize(300, 35))
        self.widget_29.setMaximumSize(QSize(300, 35))
        self.widget_29.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background:none;\n"
"}")
        self.horizontalLayout_175 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_175.setSpacing(3)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(0, 0, 0, 0)
        self.frame_114 = QFrame(self.widget_29)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(130, 35))
        self.frame_114.setMaximumSize(QSize(250, 16777215))
        self.frame_114.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_176 = QHBoxLayout(self.frame_114)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(6, 6, 6, 6)
        self.label_159 = QLabel(self.frame_114)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMinimumSize(QSize(100, 20))
        self.label_159.setMaximumSize(QSize(125, 20))
        self.label_159.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_159.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_176.addWidget(self.label_159, 0, Qt.AlignVCenter)


        self.horizontalLayout_175.addWidget(self.frame_114, 0, Qt.AlignVCenter)

        self.frame_115 = QFrame(self.widget_29)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_177 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(6, 6, 6, 6)
        self.label_160 = QLabel(self.frame_115)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_160.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_177.addWidget(self.label_160)

        self.label_161 = QLabel(self.frame_115)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setMinimumSize(QSize(52, 0))
        self.label_161.setMaximumSize(QSize(52, 16777215))
        self.label_161.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_177.addWidget(self.label_161)


        self.horizontalLayout_175.addWidget(self.frame_115)


        self.gridLayout_4.addWidget(self.widget_29, 2, 1, 1, 1)

        self.widget_23 = QWidget(self.Bottom_slider_PE_Output)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(300, 35))
        self.widget_23.setMaximumSize(QSize(300, 35))
        self.widget_23.setStyleSheet(u"background:none;")
        self.horizontalLayout_155 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_155.setSpacing(3)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.frame_102 = QFrame(self.widget_23)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(130, 35))
        self.frame_102.setMaximumSize(QSize(250, 16777215))
        self.frame_102.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_156 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(6, 6, 6, 6)
        self.label_141 = QLabel(self.frame_102)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(100, 20))
        self.label_141.setMaximumSize(QSize(125, 20))
        self.label_141.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_141.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.label_141, 0, Qt.AlignVCenter)


        self.horizontalLayout_155.addWidget(self.frame_102, 0, Qt.AlignVCenter)

        self.frame_103 = QFrame(self.widget_23)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_157 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(6, 6, 6, 6)
        self.label_142 = QLabel(self.frame_103)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_142.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_157.addWidget(self.label_142)

        self.label_143 = QLabel(self.frame_103)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(52, 0))
        self.label_143.setMaximumSize(QSize(52, 16777215))
        self.label_143.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_157.addWidget(self.label_143)


        self.horizontalLayout_155.addWidget(self.frame_103)


        self.gridLayout_4.addWidget(self.widget_23, 0, 1, 1, 1)

        self.widget_26 = QWidget(self.Bottom_slider_PE_Output)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(300, 35))
        self.widget_26.setMaximumSize(QSize(300, 35))
        self.widget_26.setStyleSheet(u"background:none;")
        self.horizontalLayout_166 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_166.setSpacing(3)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.horizontalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.frame_108 = QFrame(self.widget_26)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(130, 35))
        self.frame_108.setMaximumSize(QSize(250, 16777215))
        self.frame_108.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_167 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalLayout_167.setContentsMargins(6, 6, 6, 6)
        self.label_150 = QLabel(self.frame_108)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMinimumSize(QSize(100, 20))
        self.label_150.setMaximumSize(QSize(125, 20))
        self.label_150.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:11px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_150.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_167.addWidget(self.label_150, 0, Qt.AlignVCenter)


        self.horizontalLayout_166.addWidget(self.frame_108, 0, Qt.AlignVCenter)

        self.frame_109 = QFrame(self.widget_26)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_168 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(6, 6, 6, 6)
        self.label_151 = QLabel(self.frame_109)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setStyleSheet(u"QLabel{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	border-radius:5px;\n"
"	color:#fff;\n"
"	background-color: rgb(94, 96, 159);\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLabel:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.label_151.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_168.addWidget(self.label_151)

        self.label_152 = QLabel(self.frame_109)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMinimumSize(QSize(52, 0))
        self.label_152.setMaximumSize(QSize(52, 16777215))
        self.label_152.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_152.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_168.addWidget(self.label_152)


        self.horizontalLayout_166.addWidget(self.frame_109)


        self.gridLayout_4.addWidget(self.widget_26, 1, 1, 1, 1)


        self.verticalLayout_71.addLayout(self.gridLayout_4)


        self.verticalLayout_12.addWidget(self.Bottom_slider_PE_Output)


        self.horizontalLayout_73.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.Planetary_Ephemeris)

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
        font16 = QFont()
        font16.setFamily(u"Arial")
        font16.setPointSize(6)
        font16.setBold(False)
        font16.setItalic(False)
        font16.setWeight(50)
        self.label_credits.setFont(font16)
        self.label_credits.setStyleSheet(u"")
        self.label_credits.setPixmap(QPixmap(u"Users/manjunath neelmath/.designer/backup/GUI-test/Resources/MOPy Cover_transparent.png"))
        self.label_credits.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_credits)


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
        self.VPCO_tabs.setCurrentIndex(0)
        self.VPCO_Input_Stack.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.VPCO_output_stack.setCurrentIndex(1)
        self.otherbody_stack.setCurrentIndex(1)
        self.CoOE_output_stack.setCurrentIndex(1)
        self.Stacked_widg_Types_of_Orbital_Transfer.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MOPy", None))
#if QT_CONFIG(tooltip)
        self.Home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Home</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Home_btn.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"    MOPy - Orbital Transfer | Phasing Maneuver", None))
#if QT_CONFIG(tooltip)
        self.btn_go_back_2.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_go_back_2.setText("")
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.Home_VPCO_Label.setText(QCoreApplication.translate("MainWindow", u"Various Parameters at any given point and Constants in orbit", None))
        self.Home_Julian_Day_Label.setText(QCoreApplication.translate("MainWindow", u"Calculation of Julian Day", None))
        self.Home_Orbital_Elements_Label.setText(QCoreApplication.translate("MainWindow", u"Orbital Elements", None))
        self.Home_SOI_Label.setText(QCoreApplication.translate("MainWindow", u"Sphere of Influence", None))
        self.Home_Orbit_Visualization_Label.setText(QCoreApplication.translate("MainWindow", u"Orbit Visualization", None))
        self.Home_Ground_Track_Label.setText(QCoreApplication.translate("MainWindow", u"Ground Track", None))
        self.Home_Planet_in_Shadow_Label.setText(QCoreApplication.translate("MainWindow", u"Planet in Shadow", None))
        self.Home_Planetary_Ephimeris_Label.setText(QCoreApplication.translate("MainWindow", u"Planetary Ephimeris", None))
        self.Home_Numerical_integ_Label.setText(QCoreApplication.translate("MainWindow", u"Numerical Methods", None))
        self.Home_Eulers_Angle_Label.setText(QCoreApplication.translate("MainWindow", u"Eulers Angle", None))
        self.Home_Orbital_transfer_Label.setText(QCoreApplication.translate("MainWindow", u"Orbital Transfer", None))
        self.type_of_calendar.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Type Of Calendar", None))
        self.type_of_calendar.setItemText(1, QCoreApplication.translate("MainWindow", u"  Julian Calendar", None))
        self.type_of_calendar.setItemText(2, QCoreApplication.translate("MainWindow", u"  Gregorian Calendar", None))

        self.Error_state.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Time:", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"UT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Digits of Accuracy:", None))
        self.calculate_btn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Julian Days", None))
        self.JulianDay_Result.setText(QCoreApplication.translate("MainWindow", u"12500.00", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.pushButton.setText("")
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
        self.pushButton_2.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Semi-major axis", None))
        self.VPCO_Input_a_lineedit.setText("")
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
        self.VPCO_Input_e_lineedit.setText("")
        self.maj_body_CoOE_2.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Major Body", None))
        self.maj_body_CoOE_2.setItemText(1, QCoreApplication.translate("MainWindow", u"  Moon", None))
        self.maj_body_CoOE_2.setItemText(2, QCoreApplication.translate("MainWindow", u"  Earth", None))
        self.maj_body_CoOE_2.setItemText(3, QCoreApplication.translate("MainWindow", u"  Jupiter", None))
        self.maj_body_CoOE_2.setItemText(4, QCoreApplication.translate("MainWindow", u"  Mercury", None))
        self.maj_body_CoOE_2.setItemText(5, QCoreApplication.translate("MainWindow", u"  Venus", None))
        self.maj_body_CoOE_2.setItemText(6, QCoreApplication.translate("MainWindow", u"  Mars", None))
        self.maj_body_CoOE_2.setItemText(7, QCoreApplication.translate("MainWindow", u"  Saturn", None))
        self.maj_body_CoOE_2.setItemText(8, QCoreApplication.translate("MainWindow", u"  Uranus", None))
        self.maj_body_CoOE_2.setItemText(9, QCoreApplication.translate("MainWindow", u"  Neptune", None))
        self.maj_body_CoOE_2.setItemText(10, QCoreApplication.translate("MainWindow", u"  Pluto", None))
        self.maj_body_CoOE_2.setItemText(11, QCoreApplication.translate("MainWindow", u"  Other", None))

        self.VPCO_Submit_button.setText(QCoreApplication.translate("MainWindow", u"Plot Orbital Transfer", None))
        self.semi_major_axis_toggle_menu_lbl_4.setText(QCoreApplication.translate("MainWindow", u"Semi-Major Axis", None))
#if QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_spinbox_3.setToolTip(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ecce_dial_3.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate to alter the Eccentricity value", None))
#endif // QT_CONFIG(tooltip)
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Dial Sensitivity", None))
#if QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_slider_3.setToolTip(QCoreApplication.translate("MainWindow", u"Slide to change the single step to be altered ", None))
#endif // QT_CONFIG(tooltip)
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Step Size:", None))
#if QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_spinbox_6.setToolTip(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
#endif // QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_lbl_4.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
#if QT_CONFIG(tooltip)
        self.semi_major_axis_toggle_menu_spinbox_3.setToolTip(QCoreApplication.translate("MainWindow", u"Semi-Major Axis", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Semi_dial_3.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate to alter the Semi-Major axis value", None))
#endif // QT_CONFIG(tooltip)
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Dial Sensitivity", None))
#if QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_slider_4.setToolTip(QCoreApplication.translate("MainWindow", u"Slide to change the single step to be altered ", None))
#endif // QT_CONFIG(tooltip)
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Step Size:", None))
#if QT_CONFIG(tooltip)
        self.eccentricity_toggle_menu_spinbox_5.setToolTip(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
#endif // QT_CONFIG(tooltip)
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Radius of Apoapsis", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"37500.00", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Velocity at Apoapsis", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"2.30", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Mean Motion", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"6264.12", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"rad/s", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Sp. Mechanical Energy", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"-7.96", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"J/Kg", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Esc. Velocity at Periapsis", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"7.98", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"39358.61", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Esc. Velocity at Periapsis", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"4.61", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Sp. Angular Momentum", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"136043.01", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"m^2/s", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Semi-latus Rectum", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"18750.00", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Vel. at Semi-latus Rectum", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"5.15", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Radius of Periapsis", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"12500.00", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Velocity at Periapsis", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"6.91", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.VPCO_tabs.setTabText(self.VPCO_tabs.indexOf(self.a_and_e_tab), QCoreApplication.translate("MainWindow", u"Semi-major axis and Eccentricity", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Radius of Perigee", None))
        self.VPCO_Input_a_lineedit_4.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Radius of Apogee", None))
        self.VPCO_Input_e_lineedit_3.setText("")
        self.maj_body_CoOE_4.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Major Body", None))
        self.maj_body_CoOE_4.setItemText(1, QCoreApplication.translate("MainWindow", u"  Moon", None))
        self.maj_body_CoOE_4.setItemText(2, QCoreApplication.translate("MainWindow", u"  Earth", None))
        self.maj_body_CoOE_4.setItemText(3, QCoreApplication.translate("MainWindow", u"  Jupiter", None))
        self.maj_body_CoOE_4.setItemText(4, QCoreApplication.translate("MainWindow", u"  Mercury", None))
        self.maj_body_CoOE_4.setItemText(5, QCoreApplication.translate("MainWindow", u"  Venus", None))
        self.maj_body_CoOE_4.setItemText(6, QCoreApplication.translate("MainWindow", u"  Mars", None))
        self.maj_body_CoOE_4.setItemText(7, QCoreApplication.translate("MainWindow", u"  Saturn", None))
        self.maj_body_CoOE_4.setItemText(8, QCoreApplication.translate("MainWindow", u"  Uranus", None))
        self.maj_body_CoOE_4.setItemText(9, QCoreApplication.translate("MainWindow", u"  Neptune", None))
        self.maj_body_CoOE_4.setItemText(10, QCoreApplication.translate("MainWindow", u"  Pluto", None))
        self.maj_body_CoOE_4.setItemText(11, QCoreApplication.translate("MainWindow", u"  Other", None))

        self.VPCO_Submit_button_2.setText(QCoreApplication.translate("MainWindow", u"Plot Orbital Transfer", None))
        self.VPCO_tabs.setTabText(self.VPCO_tabs.indexOf(self.ra_and_rp), QCoreApplication.translate("MainWindow", u"Radius of Perigee and Radius of Apogee", None))
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
        self.Hohmn_transf_label.setText(QCoreApplication.translate("MainWindow", u"Hohmann Transfer", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Bi-elliptical Hohmann Transfer", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Phasing Maneuver", None))
        self.semi_major_axis_toggle_menu_lbl_9.setText(QCoreApplication.translate("MainWindow", u"Hohmann Transfer", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"The Hohmann transfer is the most energy efficient transfer for transferring between two coplanar orbits sharing a common focus. The Hohmann transfer orbit is an elliptical orbit tangent to both orbits on its apse line. During the maneuver only one half of the transfer orbit is flown. This can be in either direction, i.e., inner to outer, or vice versa. ", None))
        self.semi_major_axis_toggle_menu_lbl_10.setText(QCoreApplication.translate("MainWindow", u"Phasing Maneuver", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"A phasing maneuver is a two-impulse Hohmann transfer from and back to the same orbit. The Hohmann transfer ellipse is the phasing orbit with a period selected to return the spacecraft to the main orbit within a specified time. Phasing maneuvers are used to change the position of a spacecraft in its orbit.", None))
        self.semi_major_axis_toggle_menu_lbl_11.setText(QCoreApplication.translate("MainWindow", u"Bi-elliptical Transfer", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"The Bi-Elliptical Hohmann Transfer(BEHT) uses two coaxial semi ellipses which extend beyond the outer target orbit. Each of the two ellipses is tangent to the one of the orbits (initial and final) and are tangent to each other too. This is usually done so that the point B is placed sufficiently far from the focus that the DeltaV will be very small. This is suitable when the deltaV_(BEHT) < deltaV_(HT). ", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"Radius of Periapsis", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"6800", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Radius of Apoapsis", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"13600", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.semi_major_axis_toggle_menu_lbl_5.setText(QCoreApplication.translate("MainWindow", u"Initial Orbit", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Theta- 2 (Sat-B)", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"90", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Theta-1 (Sat-A)", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.semi_major_axis_toggle_menu_lbl_6.setText(QCoreApplication.translate("MainWindow", u"Satellites' Angle from Periapsis", None))
        self.semi_major_axis_toggle_menu_lbl_7.setText(QCoreApplication.translate("MainWindow", u"Phasing Maneuver", None))
        self.Orbital_Transfer_plot_button.setText(QCoreApplication.translate("MainWindow", u"Plot Orbital Transfer", None))
        self.semi_major_axis_toggle_menu_lbl_8.setText(QCoreApplication.translate("MainWindow", u"Initial Orbit", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Change in Velocity at Periapsis", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"-0.24851", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"10252", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"  s", None))
        self.semi_major_axis_toggle_menu_lbl_12.setText(QCoreApplication.translate("MainWindow", u"Phasing Orbit", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Change in Velocity at Periapsis", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"0.24851", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"8756.3", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"  s", None))
        self.semi_major_axis_toggle_menu_lbl_13.setText(QCoreApplication.translate("MainWindow", u"Total Change in Velocity", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"\u2207V1 + \u2207V2", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"0.4970", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.SOI_planet_name_2.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select a Celestial Body", None))
        self.SOI_planet_name_2.setItemText(1, QCoreApplication.translate("MainWindow", u"                Moon", None))
        self.SOI_planet_name_2.setItemText(2, QCoreApplication.translate("MainWindow", u"                 Earth", None))
        self.SOI_planet_name_2.setItemText(3, QCoreApplication.translate("MainWindow", u"                Jupiter", None))
        self.SOI_planet_name_2.setItemText(4, QCoreApplication.translate("MainWindow", u"               Mercury", None))
        self.SOI_planet_name_2.setItemText(5, QCoreApplication.translate("MainWindow", u"                 Venus", None))
        self.SOI_planet_name_2.setItemText(6, QCoreApplication.translate("MainWindow", u"                  Mars", None))
        self.SOI_planet_name_2.setItemText(7, QCoreApplication.translate("MainWindow", u"                 Saturn", None))
        self.SOI_planet_name_2.setItemText(8, QCoreApplication.translate("MainWindow", u"                 Uranus", None))
        self.SOI_planet_name_2.setItemText(9, QCoreApplication.translate("MainWindow", u"               Neptune", None))
        self.SOI_planet_name_2.setItemText(10, QCoreApplication.translate("MainWindow", u"                 Pluto", None))

        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Select the date", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Select Time:", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"UT", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.PE_Cal_Btn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"RAAN", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Semi-Major Axis", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"1.4960e8", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Inclination", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"-0.0005", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"0.0167", None))
        self.label_140.setText("")
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Arguement of Periheilion", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"102.9500", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"True Anomaly", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"230.8200", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Sp. Angular Momentum", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"4.4451e9", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"km^2/s", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"29.4767", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Mean Anomaly", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"232.3200", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_credits.setText("")
    # retranslateUi

