# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home_PageUYhXIG.ui'
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
        MainWindow.resize(1033, 697)
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
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font = QFont()
        font.setFamily(u"Rockwell Condensed")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setStyleSheet(u"background-color: rgb(78, 79, 132);\n"
"border:2px solid white;\n"
"")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 0, 4, 0)
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
        self.btn_go_back_2.setMinimumSize(QSize(30, 30))
        self.btn_go_back_2.setMaximumSize(QSize(30, 30))
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
        self.pushButton_5.setMinimumSize(QSize(30, 30))
        self.pushButton_5.setMaximumSize(QSize(30, 30))
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
        self.frame_btns.setMinimumSize(QSize(95, 35))
        self.frame_btns.setMaximumSize(QSize(95, 16777215))
        font2 = QFont()
        font2.setFamily(u"MS Serif")
        self.frame_btns.setFont(font2)
        self.frame_btns.setStyleSheet(u"background-color: rgb(78, 79, 132);\n"
"border:2px solid white;\n"
"")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(20, 20))
        self.btn_minimize.setMaximumSize(QSize(20, 20))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:10px;\n"
"	image:url(UI_Functions/Resources/Minimize_2.drawio.png);\n"
"	padding: 0.2em 0.2em 0.2em 0.2em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 1px solid transparent;\n"
"	background-color:#60628b;\n"
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
"	border-radius:10px;\n"
"	image:url(UI_Functions/Resources/Close_2.drawio.png);\n"
"	padding: 0.1em 0.1em 0.2em 0.1em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 1px solid transparent;\n"
"	background-color:#60628b;\n"
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 995, 630))
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
"\n"
"}	")
        self.verticalLayout_13 = QVBoxLayout(self.Home_VPCO)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Home_VPCO_Filler = QFrame(self.Home_VPCO)
        self.Home_VPCO_Filler.setObjectName(u"Home_VPCO_Filler")
        self.Home_VPCO_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;")
        self.Home_VPCO_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_VPCO_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.Home_VPCO_Filler)

        self.Home_VPCO_Slider = QFrame(self.Home_VPCO)
        self.Home_VPCO_Slider.setObjectName(u"Home_VPCO_Slider")
        self.Home_VPCO_Slider.setMinimumSize(QSize(150, 80))
        self.Home_VPCO_Slider.setMaximumSize(QSize(230, 200))
        self.Home_VPCO_Slider.setStyleSheet(u"background-color: rgba(67, 67, 67, 60%);\n"
"image:none;\n"
"border:none;")
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
"border:none;\n"
"}\n"
"\n"
"")
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
"image:url(UI_Functions/Resources/Julian_Day.png);\n"
"")
        self.verticalLayout_32 = QVBoxLayout(self.Home_Julian_Day)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.Home_Julian_Day_Filler = QFrame(self.Home_Julian_Day)
        self.Home_Julian_Day_Filler.setObjectName(u"Home_Julian_Day_Filler")
        self.Home_Julian_Day_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;\n"
"")
        self.Home_Julian_Day_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Julian_Day_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_32.addWidget(self.Home_Julian_Day_Filler)

        self.Home_Julian_Day_Slider = QFrame(self.Home_Julian_Day)
        self.Home_Julian_Day_Slider.setObjectName(u"Home_Julian_Day_Slider")
        self.Home_Julian_Day_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Julian_Day_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Julian_Day_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"border:none;\n"
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
"image:url(UI_Functions/Resources/Orbital_Elements.png);\n"
"")
        self.verticalLayout_36 = QVBoxLayout(self.Home_Orbital_Elements)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.Home_Orbital_Elements_Filler = QFrame(self.Home_Orbital_Elements)
        self.Home_Orbital_Elements_Filler.setObjectName(u"Home_Orbital_Elements_Filler")
        self.Home_Orbital_Elements_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;")
        self.Home_Orbital_Elements_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Orbital_Elements_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_36.addWidget(self.Home_Orbital_Elements_Filler)

        self.Home_Orbital_Elements_Slider = QFrame(self.Home_Orbital_Elements)
        self.Home_Orbital_Elements_Slider.setObjectName(u"Home_Orbital_Elements_Slider")
        self.Home_Orbital_Elements_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Orbital_Elements_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Orbital_Elements_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,30%);\n"
"image:none;\n"
"border:none;")
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
"background-color: rgba(0, 0, 0, 40%);\n"
"\n"
"border:none;")
        self.Home_Orbital_Elements_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.Home_Orbital_Elements_Label)


        self.verticalLayout_36.addWidget(self.Home_Orbital_Elements_Slider)


        self.horizontalLayout_4.addWidget(self.Home_Orbital_Elements)

        self.Home_SOI = QWidget(self.frame_2)
        self.Home_SOI.setObjectName(u"Home_SOI")
        self.Home_SOI.setMinimumSize(QSize(150, 150))
        self.Home_SOI.setMaximumSize(QSize(230, 200))
        self.Home_SOI.setStyleSheet(u"background-color:#010008;\n"
"image:url(UI_Functions/Resources/SOI.jpg);\n"
"")
        self.verticalLayout_37 = QVBoxLayout(self.Home_SOI)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.Home_SOI_Filler = QFrame(self.Home_SOI)
        self.Home_SOI_Filler.setObjectName(u"Home_SOI_Filler")
        self.Home_SOI_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;")
        self.Home_SOI_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_SOI_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_37.addWidget(self.Home_SOI_Filler)

        self.Home_SOI_Slider = QFrame(self.Home_SOI)
        self.Home_SOI_Slider.setObjectName(u"Home_SOI_Slider")
        self.Home_SOI_Slider.setMinimumSize(QSize(150, 80))
        self.Home_SOI_Slider.setMaximumSize(QSize(230, 200))
        self.Home_SOI_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"background-color: rgba(0, 0, 0, 60%);\n"
"\n"
"border:none;")
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
"image:url(UI_Functions/Resources/Orbit_Visualization.png);\n"
"")
        self.verticalLayout_33 = QVBoxLayout(self.Home_Orbit_Visualization)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Home_Orbit_Visualization_Filler = QFrame(self.Home_Orbit_Visualization)
        self.Home_Orbit_Visualization_Filler.setObjectName(u"Home_Orbit_Visualization_Filler")
        self.Home_Orbit_Visualization_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;\n"
"")
        self.Home_Orbit_Visualization_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Orbit_Visualization_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.Home_Orbit_Visualization_Filler)

        self.Home_Orbit_Visualization_Slider = QFrame(self.Home_Orbit_Visualization)
        self.Home_Orbit_Visualization_Slider.setObjectName(u"Home_Orbit_Visualization_Slider")
        self.Home_Orbit_Visualization_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Orbit_Visualization_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Orbit_Visualization_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;\n"
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
"image:url(UI_Functions/Resources/Ground_track.png);\n"
"")
        self.verticalLayout_34 = QVBoxLayout(self.Home_Ground_Track)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Home_Ground_Track_Filler = QFrame(self.Home_Ground_Track)
        self.Home_Ground_Track_Filler.setObjectName(u"Home_Ground_Track_Filler")
        self.Home_Ground_Track_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;")
        self.Home_Ground_Track_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Ground_Track_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_34.addWidget(self.Home_Ground_Track_Filler)

        self.Home_Ground_Track_Slider = QFrame(self.Home_Ground_Track)
        self.Home_Ground_Track_Slider.setObjectName(u"Home_Ground_Track_Slider")
        self.Home_Ground_Track_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Ground_Track_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Ground_Track_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;\n"
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
"image:url(UI_Functions/Resources/DSPS.png);\n"
"")
        self.verticalLayout_35 = QVBoxLayout(self.Home_Planet_in_Shadow)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Home_Planet_in_Shadow_Filler = QFrame(self.Home_Planet_in_Shadow)
        self.Home_Planet_in_Shadow_Filler.setObjectName(u"Home_Planet_in_Shadow_Filler")
        self.Home_Planet_in_Shadow_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;")
        self.Home_Planet_in_Shadow_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Planet_in_Shadow_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_35.addWidget(self.Home_Planet_in_Shadow_Filler)

        self.Home_Planet_in_Shadow_Slider = QFrame(self.Home_Planet_in_Shadow)
        self.Home_Planet_in_Shadow_Slider.setObjectName(u"Home_Planet_in_Shadow_Slider")
        self.Home_Planet_in_Shadow_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Planet_in_Shadow_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Planet_in_Shadow_Slider.setStyleSheet(u"background-color: rgba(47, 47, 48, 50%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;\n"
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
"image:url(UI_Functions/Resources/Planetary_Ephemeris.jpg);\n"
"")
        self.verticalLayout_40 = QVBoxLayout(self.Home_Planetary_Ephimeris)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Home_Planetary_Ephimeris_Filler = QFrame(self.Home_Planetary_Ephimeris)
        self.Home_Planetary_Ephimeris_Filler.setObjectName(u"Home_Planetary_Ephimeris_Filler")
        self.Home_Planetary_Ephimeris_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;")
        self.Home_Planetary_Ephimeris_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Planetary_Ephimeris_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_40.addWidget(self.Home_Planetary_Ephimeris_Filler)

        self.Home_Planetary_Ephimeris_Slider = QFrame(self.Home_Planetary_Ephimeris)
        self.Home_Planetary_Ephimeris_Slider.setObjectName(u"Home_Planetary_Ephimeris_Slider")
        self.Home_Planetary_Ephimeris_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Planetary_Ephimeris_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Planetary_Ephimeris_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;")
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
"image:url(UI_Functions/Resources/Numerical_Integration.jpg);\n"
"")
        self.verticalLayout_38 = QVBoxLayout(self.Home_Numerical_integ)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Home_Numerical_integ_Filler = QFrame(self.Home_Numerical_integ)
        self.Home_Numerical_integ_Filler.setObjectName(u"Home_Numerical_integ_Filler")
        self.Home_Numerical_integ_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;")
        self.Home_Numerical_integ_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Numerical_integ_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.Home_Numerical_integ_Filler)

        self.Home_Numerical_integ_Slider = QFrame(self.Home_Numerical_integ)
        self.Home_Numerical_integ_Slider.setObjectName(u"Home_Numerical_integ_Slider")
        self.Home_Numerical_integ_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Numerical_integ_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Numerical_integ_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;\n"
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
"image:url(UI_Functions/Resources/Eulers Angle.png);\n"
"")
        self.horizontalLayout_75 = QHBoxLayout(self.Home_Eulers_Angle)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.Home_Eulers_Angle_Filler = QFrame(self.Home_Eulers_Angle)
        self.Home_Eulers_Angle_Filler.setObjectName(u"Home_Eulers_Angle_Filler")
        self.Home_Eulers_Angle_Filler.setAutoFillBackground(False)
        self.Home_Eulers_Angle_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;")
        self.Home_Eulers_Angle_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Eulers_Angle_Filler.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_75.addWidget(self.Home_Eulers_Angle_Filler)

        self.Home_Eulers_Angle_Slider = QFrame(self.Home_Eulers_Angle)
        self.Home_Eulers_Angle_Slider.setObjectName(u"Home_Eulers_Angle_Slider")
        self.Home_Eulers_Angle_Slider.setStyleSheet(u"background-color: rgba(47, 47, 48, 60%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;\n"
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
"image:url(UI_Functions/Resources/Orbital Transfer.png);\n"
"")
        self.verticalLayout_39 = QVBoxLayout(self.Home_Orbital_transfer)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.Home_Orbital_transfer_Filler = QFrame(self.Home_Orbital_transfer)
        self.Home_Orbital_transfer_Filler.setObjectName(u"Home_Orbital_transfer_Filler")
        self.Home_Orbital_transfer_Filler.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;")
        self.Home_Orbital_transfer_Filler.setFrameShape(QFrame.StyledPanel)
        self.Home_Orbital_transfer_Filler.setFrameShadow(QFrame.Raised)

        self.verticalLayout_39.addWidget(self.Home_Orbital_transfer_Filler)

        self.Home_Orbital_transfer_Slider = QFrame(self.Home_Orbital_transfer)
        self.Home_Orbital_transfer_Slider.setObjectName(u"Home_Orbital_transfer_Slider")
        self.Home_Orbital_transfer_Slider.setMinimumSize(QSize(150, 80))
        self.Home_Orbital_transfer_Slider.setMaximumSize(QSize(230, 200))
        self.Home_Orbital_transfer_Slider.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;")
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
        self.horizontalLayout_19 = QHBoxLayout(self.Julian_Day_Screen)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(6, 2, 6, 0)
        self.frame_content_Julian_calculation = QFrame(self.Julian_Day_Screen)
        self.frame_content_Julian_calculation.setObjectName(u"frame_content_Julian_calculation")
        self.frame_content_Julian_calculation.setMinimumSize(QSize(0, 0))
        self.frame_content_Julian_calculation.setMaximumSize(QSize(16777215, 16777215))
        self.frame_content_Julian_calculation.setStyleSheet(u"QFrame{background-color: rgb(78, 79, 132);\n"
"	border:2px solid white;}\n"
"")
        self.frame_content_Julian_calculation.setFrameShape(QFrame.StyledPanel)
        self.frame_content_Julian_calculation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_content_Julian_calculation)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, 15, 15, 15)
        self.frame_5 = QFrame(self.frame_content_Julian_calculation)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(400, 0))
        self.frame_5.setStyleSheet(u"border:none;\n"
"background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: #1b1b1b;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 12)
        self.type_of_calendar = QComboBox(self.frame_7)
        self.type_of_calendar.addItem("")
        self.type_of_calendar.addItem("")
        self.type_of_calendar.addItem("")
        self.type_of_calendar.setObjectName(u"type_of_calendar")
        self.type_of_calendar.setMinimumSize(QSize(305, 40))
        self.type_of_calendar.setMaximumSize(QSize(305, 40))
        self.type_of_calendar.setStyleSheet(u"QComboBox{\n"
"	\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 14px;\n"
"	background-color:#04ae92;\n"
"	border: 8px solid transparent;\n"
"	\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 1px solid rgba(168, 128, 243, 60%);\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.type_of_calendar, 0, Qt.AlignHCenter)

        self.scrollArea_3 = QScrollArea(self.frame_7)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"/*QSrollArea{\n"
"background-color:#4e4f84;}*/\n"
"\n"
"/*Vertical Scrollbar*/\n"
"QScrollBar:vertical{\n"
"border:none;\n"
"background-color:white;\n"
"width:8px;\n"
"margin: 15px 0 15px 0;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"/* Handle Bar Vertical */\n"
"QScrollBar::handle:vertical{\n"
"background-color: white;\n"
"min-height: 30px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vetical:hover{\n"
"background-color: white;\n"
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
"background-color: none;\n"
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
"background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - Scroll"
                        "bar*/\n"
"QScrollBar::add-line:vertical{\n"
"border:none;\n"
"background-color:none;\n"
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
"background: transparent;\n"
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
"/* Handle Bar Horizontal */\n"
"QScrollBar::handle:horizontal{\n"
"background-color: rg"
                        "b(80, 80, 122);\n"
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
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
""
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
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 364, 454))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_9 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 250))
        self.frame_9.setMaximumSize(QSize(360, 250))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"\n"
"border: transparent;\n"
"border-radius: 15px;\n"
"background-color:#04ae92;\n"
"\n"
"}\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(6, 6, 6, 6)
        self.calendarWidget = QCalendarWidget(self.frame_9)
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
"\n"
"\n"
"\n"
"\n"
"border:2px solid black;\n"
"border-radius:4px;\n"
"}")

        self.horizontalLayout_13.addWidget(self.calendarWidget)


        self.verticalLayout_15.addWidget(self.frame_9)

        self.Date_time_frame = QFrame(self.scrollAreaWidgetContents_5)
        self.Date_time_frame.setObjectName(u"Date_time_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Date_time_frame.sizePolicy().hasHeightForWidth())
        self.Date_time_frame.setSizePolicy(sizePolicy1)
        self.Date_time_frame.setMinimumSize(QSize(0, 180))
        self.Date_time_frame.setMaximumSize(QSize(360, 200))
        font3 = QFont()
        font3.setPointSize(15)
        self.Date_time_frame.setFont(font3)
        self.Date_time_frame.setStyleSheet(u"QFrame{\n"
"\n"
"border: transparent;\n"
"border-radius: 15px;\n"
"background-color: #04ae92;\n"
"\n"
"}\n"
"\n"
"")
        self.Date_time_frame.setFrameShape(QFrame.NoFrame)
        self.Date_time_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Date_time_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_11 = QFrame(self.Date_time_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(16987, 35))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, 0, 40, 0)
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")

        self.horizontalLayout_9.addWidget(self.label)

        self.timeEdit = QTimeEdit(self.frame_11)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(110, 30))
        self.timeEdit.setFont(font3)
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

        self.horizontalLayout_9.addWidget(self.timeEdit)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_2)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.frame_18 = QFrame(self.Date_time_frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 30))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_18)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(140, -1, -1, -1)
        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")

        self.verticalLayout_17.addWidget(self.label_3)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.frame_14 = QFrame(self.Date_time_frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(230, 0))
        self.frame_14.setMaximumSize(QSize(16777215, 35))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(40, 0, 45, 0)
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.digits_accuracy = QSpinBox(self.frame_14)
        self.digits_accuracy.setObjectName(u"digits_accuracy")
        self.digits_accuracy.setMinimumSize(QSize(20, 30))
        self.digits_accuracy.setMaximumSize(QSize(70, 16777215))
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

        self.horizontalLayout_11.addWidget(self.digits_accuracy)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.calculate_btn = QPushButton(self.Date_time_frame)
        self.calculate_btn.setObjectName(u"calculate_btn")
        self.calculate_btn.setMinimumSize(QSize(120, 0))
        self.calculate_btn.setMaximumSize(QSize(150, 35))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.calculate_btn.setFont(font6)
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

        self.verticalLayout_8.addWidget(self.calculate_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.Date_time_frame)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_5.addWidget(self.scrollArea_3)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.Julian_Day_Frame = QFrame(self.frame_5)
        self.Julian_Day_Frame.setObjectName(u"Julian_Day_Frame")
        self.Julian_Day_Frame.setMinimumSize(QSize(320, 0))
        self.Julian_Day_Frame.setMaximumSize(QSize(350, 16777215))
        self.Julian_Day_Frame.setStyleSheet(u"background-color:#1b1b1b;\n"
"border-radius:15px;")
        self.Julian_Day_Frame.setFrameShape(QFrame.StyledPanel)
        self.Julian_Day_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.Julian_Day_Frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_34 = QWidget(self.Julian_Day_Frame)
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
        self.frame_124.setStyleSheet(u"background-color: white;\n"
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
        font7 = QFont()
        self.label_174.setFont(font7)
        self.label_174.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_174.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_191.addWidget(self.label_174)


        self.horizontalLayout_190.addWidget(self.frame_124, 0, Qt.AlignVCenter)

        self.frame_125 = QFrame(self.widget_34)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setStyleSheet(u"background-color:transparent;\n"
"border-radius:8px;")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_192 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.horizontalLayout_192.setContentsMargins(6, 6, 6, 6)
        self.JulianDay_Result = QLabel(self.frame_125)
        self.JulianDay_Result.setObjectName(u"JulianDay_Result")
        self.JulianDay_Result.setMinimumSize(QSize(0, 0))
        self.JulianDay_Result.setMaximumSize(QSize(100, 16777215))
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


        self.horizontalLayout_190.addWidget(self.frame_125)


        self.horizontalLayout_12.addWidget(self.widget_34)


        self.verticalLayout_9.addWidget(self.Julian_Day_Frame, 0, Qt.AlignHCenter)

        self.Error_Frame = QFrame(self.frame_5)
        self.Error_Frame.setObjectName(u"Error_Frame")
        self.Error_Frame.setMinimumSize(QSize(320, 0))
        self.Error_Frame.setMaximumSize(QSize(350, 16777215))
        self.Error_Frame.setStyleSheet(u"background-color:#1b1b1b;\n"
"border-radius:15px;")
        self.Error_Frame.setFrameShape(QFrame.StyledPanel)
        self.Error_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_251 = QHBoxLayout(self.Error_Frame)
        self.horizontalLayout_251.setObjectName(u"horizontalLayout_251")
        self.frame_190 = QFrame(self.Error_Frame)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setMinimumSize(QSize(250, 25))
        self.frame_190.setMaximumSize(QSize(300, 25))
        self.frame_190.setStyleSheet(u"background-color: white;\n"
"border-radius:8px;")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_253 = QHBoxLayout(self.frame_190)
        self.horizontalLayout_253.setObjectName(u"horizontalLayout_253")
        self.horizontalLayout_253.setContentsMargins(0, 0, 0, 0)
        self.Error_state = QLabel(self.frame_190)
        self.Error_state.setObjectName(u"Error_state")
        self.Error_state.setMinimumSize(QSize(300, 20))
        self.Error_state.setMaximumSize(QSize(300, 20))
        self.Error_state.setFont(font7)
        self.Error_state.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:red;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.Error_state.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_253.addWidget(self.Error_state)


        self.horizontalLayout_251.addWidget(self.frame_190, 0, Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.Error_Frame, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_5)

        self.frame_37 = QFrame(self.frame_content_Julian_calculation)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"	border:none;\n"
"}")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_37)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.frame_151 = QFrame(self.frame_37)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	image:url(UI_Functions/Resources/SOI.png);\n"
"	border:2px solid white;\n"
"}")
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)

        self.verticalLayout_105.addWidget(self.frame_151)

        self.frame_181 = QFrame(self.frame_37)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	border:2px solid white;\n"
"}")
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_181)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.frame_182 = QFrame(self.frame_181)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setMinimumSize(QSize(200, 25))
        self.frame_182.setMaximumSize(QSize(200, 30))
        self.frame_182.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_182)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_17 = QLabel(self.frame_182)
        self.semi_major_axis_toggle_menu_lbl_17.setObjectName(u"semi_major_axis_toggle_menu_lbl_17")
        self.semi_major_axis_toggle_menu_lbl_17.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_17.setMaximumSize(QSize(16777215, 20))
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setWeight(75)
        self.semi_major_axis_toggle_menu_lbl_17.setFont(font8)
        self.semi_major_axis_toggle_menu_lbl_17.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_107.addWidget(self.semi_major_axis_toggle_menu_lbl_17, 0, Qt.AlignHCenter)


        self.verticalLayout_106.addWidget(self.frame_182, 0, Qt.AlignHCenter)

        self.label_36 = QLabel(self.frame_181)
        self.label_36.setObjectName(u"label_36")
        font9 = QFont()
        font9.setPointSize(13)
        self.label_36.setFont(font9)
        self.label_36.setFocusPolicy(Qt.NoFocus)
        self.label_36.setStyleSheet(u"color:grey;\n"
"border:none;")
        self.label_36.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_36.setWordWrap(True)

        self.verticalLayout_106.addWidget(self.label_36)


        self.verticalLayout_105.addWidget(self.frame_181)


        self.horizontalLayout_6.addWidget(self.frame_37)


        self.horizontalLayout_19.addWidget(self.frame_content_Julian_calculation)

        self.stackedWidget.addWidget(self.Julian_Day_Screen)
        self.SOI_Screen = QWidget()
        self.SOI_Screen.setObjectName(u"SOI_Screen")
        self.horizontalLayout_17 = QHBoxLayout(self.SOI_Screen)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 0, 5, 0)
        self.SOI_frame_content = QFrame(self.SOI_Screen)
        self.SOI_frame_content.setObjectName(u"SOI_frame_content")
        self.SOI_frame_content.setStyleSheet(u"background-color: rgb(78, 79, 132);\n"
"border:2px solid white;")
        self.SOI_frame_content.setFrameShape(QFrame.StyledPanel)
        self.SOI_frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.SOI_frame_content)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(4, 4, 4, 4)
        self.frame_35 = QFrame(self.SOI_frame_content)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: transparent;\n"
"	border:none;\n"
"	\n"
"\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_28 = QFrame(self.frame_35)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_28)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.frame_32 = QFrame(self.frame_28)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	image:url(UI_Functions/Resources/SOI.png);\n"
"	border:2px solid white;\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.verticalLayout_99.addWidget(self.frame_32)

        self.frame_166 = QFrame(self.frame_28)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	border:2px solid white;\n"
"}")
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_166)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(20, 20, 20, -1)
        self.frame_167 = QFrame(self.frame_166)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setMinimumSize(QSize(200, 30))
        self.frame_167.setMaximumSize(QSize(200, 30))
        self.frame_167.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_167)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_15 = QLabel(self.frame_167)
        self.semi_major_axis_toggle_menu_lbl_15.setObjectName(u"semi_major_axis_toggle_menu_lbl_15")
        self.semi_major_axis_toggle_menu_lbl_15.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_15.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_15.setFont(font8)
        self.semi_major_axis_toggle_menu_lbl_15.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_98.addWidget(self.semi_major_axis_toggle_menu_lbl_15, 0, Qt.AlignHCenter)


        self.verticalLayout_97.addWidget(self.frame_167, 0, Qt.AlignHCenter)

        self.label_31 = QLabel(self.frame_166)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font9)
        self.label_31.setFocusPolicy(Qt.NoFocus)
        self.label_31.setStyleSheet(u"color:grey;\n"
"border:none;")
        self.label_31.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_31.setWordWrap(True)

        self.verticalLayout_97.addWidget(self.label_31)


        self.verticalLayout_99.addWidget(self.frame_166)


        self.horizontalLayout_16.addWidget(self.frame_28)

        self.frame_26 = QFrame(self.frame_35)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(430, 0))
        self.frame_26.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_26)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(-1, 30, -1, 30)
        self.SOI_planet_name = QComboBox(self.frame_26)
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
        self.SOI_planet_name.setMinimumSize(QSize(300, 50))
        self.SOI_planet_name.setMaximumSize(QSize(350, 50))
        self.SOI_planet_name.setStyleSheet(u"QComboBox{\n"
"	border:3px solid #04ae92;\n"
"	border-radius:12px;\n"
"	color:#fff;\n"
"	background-color: #04ae92;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 2px solid #04ae92;\n"
"}\n"
"\n"
"\n"
"QComboBoxt:focus{\n"
"	border: 2px solid #04ae92;\n"
"}")

        self.verticalLayout_95.addWidget(self.SOI_planet_name, 0, Qt.AlignHCenter)

        self.frame_33 = QFrame(self.frame_26)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 200))
        self.frame_33.setMaximumSize(QSize(16777215, 200))
        self.frame_33.setStyleSheet(u"background:none;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(-1, 40, -1, -1)
        self.frame_76 = QFrame(self.frame_33)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMaximumSize(QSize(350, 150))
        self.frame_76.setStyleSheet(u"QFrame{\n"
"	background-color:#04ae92;\n"
"	\n"
"}\n"
"")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_76)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Planet_name_display = QLineEdit(self.frame_76)
        self.Planet_name_display.setObjectName(u"Planet_name_display")
        self.Planet_name_display.setMinimumSize(QSize(120, 30))
        self.Planet_name_display.setMaximumSize(QSize(120, 30))
        self.Planet_name_display.setStyleSheet(u"QLineEdit{\n"
"	font: 18px;\n"
"	color:#ef7464;\n"
"	background-color:white}")
        self.Planet_name_display.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.Planet_name_display, 0, Qt.AlignHCenter)

        self.widget_30 = QWidget(self.frame_76)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(330, 35))
        self.widget_30.setMaximumSize(QSize(330, 35))
        self.widget_30.setStyleSheet(u"background:none;\n"
"border:none;")
        self.horizontalLayout_208 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_208.setSpacing(3)
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.horizontalLayout_208.setContentsMargins(0, 0, 0, 0)
        self.frame_160 = QFrame(self.widget_30)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setMinimumSize(QSize(165, 35))
        self.frame_160.setMaximumSize(QSize(165, 16777215))
        self.frame_160.setStyleSheet(u"background-color: white;\n"
"border-radius:8px;")
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_209 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.horizontalLayout_209.setContentsMargins(0, 0, 0, 0)
        self.Mass_of_the_Body_SOI = QLabel(self.frame_160)
        self.Mass_of_the_Body_SOI.setObjectName(u"Mass_of_the_Body_SOI")
        self.Mass_of_the_Body_SOI.setMinimumSize(QSize(165, 35))
        self.Mass_of_the_Body_SOI.setMaximumSize(QSize(165, 35))
        self.Mass_of_the_Body_SOI.setFont(font7)
        self.Mass_of_the_Body_SOI.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.Mass_of_the_Body_SOI.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_209.addWidget(self.Mass_of_the_Body_SOI, 0, Qt.AlignVCenter)


        self.horizontalLayout_208.addWidget(self.frame_160, 0, Qt.AlignVCenter)

        self.frame_161 = QFrame(self.widget_30)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMinimumSize(QSize(150, 0))
        self.frame_161.setMaximumSize(QSize(150, 16777215))
        self.frame_161.setStyleSheet(u"background-color: white;\n"
"border-radius:8px;")
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_210 = QHBoxLayout(self.frame_161)
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.horizontalLayout_210.setContentsMargins(6, 6, 6, 6)
        self.Mass_of_other_planet_SOI = QLineEdit(self.frame_161)
        self.Mass_of_other_planet_SOI.setObjectName(u"Mass_of_other_planet_SOI")
        self.Mass_of_other_planet_SOI.setMinimumSize(QSize(87, 23))
        self.Mass_of_other_planet_SOI.setMaximumSize(QSize(87, 23))
        self.Mass_of_other_planet_SOI.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")

        self.horizontalLayout_210.addWidget(self.Mass_of_other_planet_SOI)

        self.Mass_of_planet_SOI = QLabel(self.frame_161)
        self.Mass_of_planet_SOI.setObjectName(u"Mass_of_planet_SOI")
        self.Mass_of_planet_SOI.setStyleSheet(u"QLabel{\n"
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
        self.Mass_of_planet_SOI.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_210.addWidget(self.Mass_of_planet_SOI)

        self.label_158 = QLabel(self.frame_161)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setMinimumSize(QSize(30, 0))
        self.label_158.setMaximumSize(QSize(45, 16777215))
        self.label_158.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_210.addWidget(self.label_158)


        self.horizontalLayout_208.addWidget(self.frame_161)


        self.verticalLayout_19.addWidget(self.widget_30, 0, Qt.AlignHCenter)

        self.widget_31 = QWidget(self.frame_76)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMinimumSize(QSize(330, 35))
        self.widget_31.setMaximumSize(QSize(330, 35))
        self.widget_31.setStyleSheet(u"background:none;\n"
"border:none;")
        self.horizontalLayout_211 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_211.setSpacing(3)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.horizontalLayout_211.setContentsMargins(0, 0, 0, 0)
        self.frame_162 = QFrame(self.widget_31)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setMinimumSize(QSize(165, 35))
        self.frame_162.setMaximumSize(QSize(165, 16777215))
        self.frame_162.setStyleSheet(u"background-color: white;\n"
"border-radius:8px;")
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_212 = QHBoxLayout(self.frame_162)
        self.horizontalLayout_212.setSpacing(0)
        self.horizontalLayout_212.setObjectName(u"horizontalLayout_212")
        self.horizontalLayout_212.setContentsMargins(0, 0, 0, 0)
        self.Dist_from_the_sun_SOI = QLabel(self.frame_162)
        self.Dist_from_the_sun_SOI.setObjectName(u"Dist_from_the_sun_SOI")
        self.Dist_from_the_sun_SOI.setMinimumSize(QSize(165, 35))
        self.Dist_from_the_sun_SOI.setMaximumSize(QSize(165, 35))
        self.Dist_from_the_sun_SOI.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.Dist_from_the_sun_SOI.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_212.addWidget(self.Dist_from_the_sun_SOI, 0, Qt.AlignVCenter)


        self.horizontalLayout_211.addWidget(self.frame_162, 0, Qt.AlignVCenter)

        self.frame_163 = QFrame(self.widget_31)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setMinimumSize(QSize(150, 0))
        self.frame_163.setMaximumSize(QSize(150, 16777215))
        self.frame_163.setStyleSheet(u"background-color:white;\n"
"border-radius:8px;")
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_213 = QHBoxLayout(self.frame_163)
        self.horizontalLayout_213.setObjectName(u"horizontalLayout_213")
        self.horizontalLayout_213.setContentsMargins(6, 6, 6, 6)
        self.dist_from_sun_of_other_planet_SOI = QLineEdit(self.frame_163)
        self.dist_from_sun_of_other_planet_SOI.setObjectName(u"dist_from_sun_of_other_planet_SOI")
        self.dist_from_sun_of_other_planet_SOI.setMinimumSize(QSize(87, 23))
        self.dist_from_sun_of_other_planet_SOI.setMaximumSize(QSize(87, 23))
        self.dist_from_sun_of_other_planet_SOI.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")

        self.horizontalLayout_213.addWidget(self.dist_from_sun_of_other_planet_SOI)

        self.dist_from_sun_SOI = QLabel(self.frame_163)
        self.dist_from_sun_SOI.setObjectName(u"dist_from_sun_SOI")
        self.dist_from_sun_SOI.setStyleSheet(u"QLabel{\n"
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
        self.dist_from_sun_SOI.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_213.addWidget(self.dist_from_sun_SOI)

        self.dist_from_sun_unit_SOI = QLabel(self.frame_163)
        self.dist_from_sun_unit_SOI.setObjectName(u"dist_from_sun_unit_SOI")
        self.dist_from_sun_unit_SOI.setMinimumSize(QSize(30, 0))
        self.dist_from_sun_unit_SOI.setMaximumSize(QSize(45, 16777215))
        self.dist_from_sun_unit_SOI.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_213.addWidget(self.dist_from_sun_unit_SOI)


        self.horizontalLayout_211.addWidget(self.frame_163)


        self.verticalLayout_19.addWidget(self.widget_31, 0, Qt.AlignHCenter)


        self.horizontalLayout_128.addWidget(self.frame_76)


        self.verticalLayout_95.addWidget(self.frame_33)

        self.soi_cal = QPushButton(self.frame_26)
        self.soi_cal.setObjectName(u"soi_cal")
        self.soi_cal.setMinimumSize(QSize(120, 40))
        self.soi_cal.setMaximumSize(QSize(150, 40))
        font10 = QFont()
        font10.setPointSize(12)
        self.soi_cal.setFont(font10)
        self.soi_cal.setStyleSheet(u"QPushButton{\n"
"	background-color:#917899;\n"
"	color:white;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:orange;\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_95.addWidget(self.soi_cal, 0, Qt.AlignHCenter)

        self.frame_36 = QFrame(self.frame_26)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(360, 0))
        self.frame_36.setMaximumSize(QSize(360, 150))
        self.frame_36.setStyleSheet(u"\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color:#ef7464;\n"
"	border:2px solid white;\n"
"	\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_36)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.widget_39 = QWidget(self.frame_36)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMinimumSize(QSize(320, 35))
        self.widget_39.setMaximumSize(QSize(320, 35))
        self.widget_39.setStyleSheet(u"border:none;\n"
"background:none;")
        self.horizontalLayout_222 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_222.setSpacing(3)
        self.horizontalLayout_222.setObjectName(u"horizontalLayout_222")
        self.horizontalLayout_222.setContentsMargins(0, 0, 0, 0)
        self.frame_164 = QFrame(self.widget_39)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setMinimumSize(QSize(160, 35))
        self.frame_164.setMaximumSize(QSize(160, 16777215))
        self.frame_164.setStyleSheet(u"background-color:white;\n"
"border-radius:8px;")
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_223 = QHBoxLayout(self.frame_164)
        self.horizontalLayout_223.setSpacing(0)
        self.horizontalLayout_223.setObjectName(u"horizontalLayout_223")
        self.horizontalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.label_164 = QLabel(self.frame_164)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setMinimumSize(QSize(150, 35))
        self.label_164.setMaximumSize(QSize(150, 20))
        self.label_164.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_164.setAlignment(Qt.AlignCenter)
        self.label_164.setWordWrap(True)

        self.horizontalLayout_223.addWidget(self.label_164, 0, Qt.AlignVCenter)


        self.horizontalLayout_222.addWidget(self.frame_164, 0, Qt.AlignVCenter)

        self.frame_165 = QFrame(self.widget_39)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setMinimumSize(QSize(150, 0))
        self.frame_165.setMaximumSize(QSize(150, 16777215))
        self.frame_165.setStyleSheet(u"background-color: white;\n"
"border-radius:8px;")
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_226 = QHBoxLayout(self.frame_165)
        self.horizontalLayout_226.setObjectName(u"horizontalLayout_226")
        self.horizontalLayout_226.setContentsMargins(6, 6, 6, 6)
        self.rSOI_of_planet_lbl = QLabel(self.frame_165)
        self.rSOI_of_planet_lbl.setObjectName(u"rSOI_of_planet_lbl")
        self.rSOI_of_planet_lbl.setStyleSheet(u"QLabel{\n"
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
        self.rSOI_of_planet_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_226.addWidget(self.rSOI_of_planet_lbl)

        self.SOI_unit = QLabel(self.frame_165)
        self.SOI_unit.setObjectName(u"SOI_unit")
        self.SOI_unit.setMinimumSize(QSize(30, 0))
        self.SOI_unit.setMaximumSize(QSize(45, 16777215))
        self.SOI_unit.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_226.addWidget(self.SOI_unit)


        self.horizontalLayout_222.addWidget(self.frame_165)


        self.verticalLayout_96.addWidget(self.widget_39, 0, Qt.AlignHCenter)

        self.get_3D_soi = QPushButton(self.frame_36)
        self.get_3D_soi.setObjectName(u"get_3D_soi")
        self.get_3D_soi.setMinimumSize(QSize(250, 40))
        self.get_3D_soi.setMaximumSize(QSize(250, 40))
        self.get_3D_soi.setFont(font10)
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

        self.verticalLayout_96.addWidget(self.get_3D_soi, 0, Qt.AlignHCenter)


        self.verticalLayout_95.addWidget(self.frame_36, 0, Qt.AlignHCenter)


        self.horizontalLayout_16.addWidget(self.frame_26)


        self.verticalLayout_16.addWidget(self.frame_35)


        self.horizontalLayout_17.addWidget(self.SOI_frame_content)

        self.stackedWidget.addWidget(self.SOI_Screen)
        self.VPCO_input = QWidget()
        self.VPCO_input.setObjectName(u"VPCO_input")
        self.verticalLayout_20 = QVBoxLayout(self.VPCO_input)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 0, 5, 0)
        self.VPCO_Outer_Frame = QFrame(self.VPCO_input)
        self.VPCO_Outer_Frame.setObjectName(u"VPCO_Outer_Frame")
        self.VPCO_Outer_Frame.setStyleSheet(u"QTabWidget{\n"
"	\n"
"	background-color: rgb(115, 118, 199);\n"
"	\n"
"	\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(78, 79, 132);\n"
"	border: 2px solid white;\n"
"}")
        self.VPCO_Outer_Frame.setFrameShape(QFrame.StyledPanel)
        self.VPCO_Outer_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.VPCO_Outer_Frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.VPCO_tabs = QTabWidget(self.VPCO_Outer_Frame)
        self.VPCO_tabs.setObjectName(u"VPCO_tabs")
        font11 = QFont()
        font11.setFamily(u"Calibri")
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setWeight(75)
        self.VPCO_tabs.setFont(font11)
        self.VPCO_tabs.setStyleSheet(u"border:none;")
        self.VPCO_tabs.setTabPosition(QTabWidget.North)
        self.VPCO_tabs.setTabShape(QTabWidget.Rounded)
        self.VPCO_tabs.setElideMode(Qt.ElideLeft)
        self.VPCO_tabs.setDocumentMode(True)
        self.VPCO_tabs.setMovable(True)
        self.a_and_e_tab = QWidget()
        self.a_and_e_tab.setObjectName(u"a_and_e_tab")
        self.a_and_e_tab.setStyleSheet(u"QTab{\n"
"	border:2px solid white;\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.a_and_e_tab)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 9)
        self.frame_3 = QFrame(self.a_and_e_tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_3)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 5, 0, 0)
        self.tab_container_frame_for_a_and_e = QFrame(self.frame_3)
        self.tab_container_frame_for_a_and_e.setObjectName(u"tab_container_frame_for_a_and_e")
        self.tab_container_frame_for_a_and_e.setMinimumSize(QSize(0, 0))
        self.tab_container_frame_for_a_and_e.setMaximumSize(QSize(16777215, 16777215))
        self.tab_container_frame_for_a_and_e.setStyleSheet(u"QFrame{\n"
"background-color:transparent;\n"
"border:none;\n"
"}")
        self.tab_container_frame_for_a_and_e.setFrameShape(QFrame.StyledPanel)
        self.tab_container_frame_for_a_and_e.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.tab_container_frame_for_a_and_e)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 5)
        self.a_and_e_VPCO = QFrame(self.tab_container_frame_for_a_and_e)
        self.a_and_e_VPCO.setObjectName(u"a_and_e_VPCO")
        self.a_and_e_VPCO.setMinimumSize(QSize(510, 0))
        self.a_and_e_VPCO.setMaximumSize(QSize(510, 16777215))
        self.a_and_e_VPCO.setStyleSheet(u"border:none;")
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
        self.page_3.setStyleSheet(u"")
        self.horizontalLayout_109 = QHBoxLayout(self.page_3)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 6)
        self.frame_29 = QFrame(self.page_3)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(528, 16777215))
        self.frame_29.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	border:none;\n"
"\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_29)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(-1, -1, -1, 9)
        self.verticalSpacer_15 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_15)

        self.frame_56 = QFrame(self.frame_29)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(450, 0))
        self.frame_56.setMaximumSize(QSize(450, 16777215))
        self.frame_56.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(239, 116, 100);\n"
"	border:2px solid white;\n"
"}")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_56)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(-1, 25, -1, 5)
        self.widget_2 = QWidget(self.frame_56)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(370, 40))
        self.widget_2.setMaximumSize(QSize(370, 40))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	\n"
"	\n"
"	border:none;\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.widget_2)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(180, 40))
        self.frame_30.setMaximumSize(QSize(180, 40))
        self.frame_30.setStyleSheet(u"background-color:white;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_30)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(180, 30))
        self.label_9.setMaximumSize(QSize(180, 16777215))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
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
        self.frame_38.setMinimumSize(QSize(190, 0))
        self.frame_38.setMaximumSize(QSize(190, 16777215))
        self.frame_38.setStyleSheet(u"background:none;\n"
"border:none;")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 0, 9, 0)
        self.VPCO_Input_a_lineedit = QLineEdit(self.frame_38)
        self.VPCO_Input_a_lineedit.setObjectName(u"VPCO_Input_a_lineedit")
        self.VPCO_Input_a_lineedit.setMinimumSize(QSize(130, 32))
        self.VPCO_Input_a_lineedit.setMaximumSize(QSize(130, 32))
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
        self.label_109.setMinimumSize(QSize(40, 0))
        self.label_109.setMaximumSize(QSize(45, 16777215))
        font12 = QFont()
        font12.setBold(True)
        font12.setWeight(75)
        self.label_109.setFont(font12)
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

        self.Semi_maj_ax_err_label = QLabel(self.frame_56)
        self.Semi_maj_ax_err_label.setObjectName(u"Semi_maj_ax_err_label")
        self.Semi_maj_ax_err_label.setStyleSheet(u"color:red;\n"
"background:none;\n"
"border:none;")
        self.Semi_maj_ax_err_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_75.addWidget(self.Semi_maj_ax_err_label)

        self.widget_3 = QWidget(self.frame_56)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(370, 40))
        self.widget_3.setMaximumSize(QSize(370, 40))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"	\n"
"	border:none;\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_78.setSpacing(6)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.widget_3)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(180, 0))
        self.frame_39.setMaximumSize(QSize(180, 16777215))
        self.frame_39.setStyleSheet(u"background-color:white;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_39)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(180, 30))
        self.label_12.setMaximumSize(QSize(180, 16777215))
        self.label_12.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
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
        self.frame_44.setStyleSheet(u"background:none;\n"
"border:none;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(9, 0, 9, 0)
        self.VPCO_Input_e_lineedit = QLineEdit(self.frame_44)
        self.VPCO_Input_e_lineedit.setObjectName(u"VPCO_Input_e_lineedit")
        self.VPCO_Input_e_lineedit.setMinimumSize(QSize(130, 32))
        self.VPCO_Input_e_lineedit.setMaximumSize(QSize(130, 32))
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

        self.label_116 = QLabel(self.frame_44)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(40, 0))
        self.label_116.setMaximumSize(QSize(45, 16777215))
        self.label_116.setFont(font12)
        self.label_116.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_80.addWidget(self.label_116)


        self.horizontalLayout_78.addWidget(self.frame_44)


        self.verticalLayout_75.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.Eccentricity_err_label = QLabel(self.frame_56)
        self.Eccentricity_err_label.setObjectName(u"Eccentricity_err_label")
        self.Eccentricity_err_label.setStyleSheet(u"color:red;\n"
"background:none;\n"
"border:none;")
        self.Eccentricity_err_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_75.addWidget(self.Eccentricity_err_label)


        self.verticalLayout_53.addWidget(self.frame_56, 0, Qt.AlignHCenter)

        self.verticalSpacer_13 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_13)

        self.frame_47 = QFrame(self.frame_29)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 50))
        self.frame_47.setMaximumSize(QSize(16777215, 50))
        self.frame_47.setStyleSheet(u"border:none;\n"
"background:none;")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.Maj_Body__Drop_VPCO = QComboBox(self.frame_47)
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.addItem("")
        self.Maj_Body__Drop_VPCO.setObjectName(u"Maj_Body__Drop_VPCO")
        self.Maj_Body__Drop_VPCO.setMinimumSize(QSize(300, 50))
        self.Maj_Body__Drop_VPCO.setMaximumSize(QSize(350, 50))
        self.Maj_Body__Drop_VPCO.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius:12px;\n"
"	color:#fff;\n"
"	background-color: #ef7464;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 2px solid #ef7464;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_82.addWidget(self.Maj_Body__Drop_VPCO)


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
        self.VPCO_Submit_button.setMinimumSize(QSize(125, 50))
        self.VPCO_Submit_button.setMaximumSize(QSize(150, 80))
        self.VPCO_Submit_button.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border:2px solid white;\n"
"	border-radius:10px;\n"
"	color:#fff;\n"
"	background-color: #04ae92;\n"
"	font-size:12px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgba(4, 167, 140, 80%);\n"
"	border: 1px solid #1d1d1d;\n"
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
        self.verticalLayout_60.setSpacing(15)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_64.setSpacing(15)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(12, 12, 12, 12)
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
        font13 = QFont()
        font13.setPointSize(10)
        font13.setBold(True)
        font13.setWeight(75)
        self.semi_major_axis_toggle_menu_lbl_4.setFont(font13)
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
        self.eccentricity_toggle_menu_lbl_4.setFont(font13)
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

        self.a_and_e_graph_VPCO = QStackedWidget(self.tab_container_frame_for_a_and_e)
        self.a_and_e_graph_VPCO.setObjectName(u"a_and_e_graph_VPCO")
        self.a_and_e_graph_VPCO.setStyleSheet(u"background-color:transparent;\n"
"border:none;")
        self.a_and_e_graph_VPCO.setFrameShape(QFrame.StyledPanel)
        self.a_and_e_graph_VPCO.setFrameShadow(QFrame.Raised)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_106 = QHBoxLayout(self.page_6)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(-1, 0, 0, 6)
        self.frame_12 = QFrame(self.page_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(430, 0))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	image:url(UI_Functions/Resources/Orbital Transfers.png);\n"
"	border:2px solid white;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_135 = QFrame(self.frame_12)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	border:2px solid white;\n"
"}")
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_135)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_136 = QFrame(self.frame_135)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setMinimumSize(QSize(250, 25))
        self.frame_136.setMaximumSize(QSize(300, 30))
        self.frame_136.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	border:none;\n"
"	\n"
"\n"
"}")
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_136)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_14 = QLabel(self.frame_136)
        self.semi_major_axis_toggle_menu_lbl_14.setObjectName(u"semi_major_axis_toggle_menu_lbl_14")
        self.semi_major_axis_toggle_menu_lbl_14.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_14.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_14.setFont(font8)
        self.semi_major_axis_toggle_menu_lbl_14.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_94.addWidget(self.semi_major_axis_toggle_menu_lbl_14, 0, Qt.AlignHCenter)


        self.verticalLayout_56.addWidget(self.frame_136, 0, Qt.AlignHCenter)

        self.label_21 = QLabel(self.frame_135)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font9)
        self.label_21.setFocusPolicy(Qt.NoFocus)
        self.label_21.setStyleSheet(u"color:grey;\n"
"border:none;")
        self.label_21.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_21.setWordWrap(True)

        self.verticalLayout_56.addWidget(self.label_21)


        self.verticalLayout_11.addWidget(self.frame_135)


        self.horizontalLayout_106.addWidget(self.frame_12)

        self.a_and_e_graph_VPCO.addWidget(self.page_6)
        self.a_and_e_graph_VPCOPage1 = QWidget()
        self.a_and_e_graph_VPCOPage1.setObjectName(u"a_and_e_graph_VPCOPage1")
        self.horizontalLayout_81 = QHBoxLayout(self.a_and_e_graph_VPCOPage1)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.graph_widget = QWidget(self.a_and_e_graph_VPCOPage1)
        self.graph_widget.setObjectName(u"graph_widget")
        self.graph_widget.setStyleSheet(u"QWidget{\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"}")

        self.horizontalLayout_81.addWidget(self.graph_widget)

        self.a_and_e_graph_VPCO.addWidget(self.a_and_e_graph_VPCOPage1)

        self.horizontalLayout_7.addWidget(self.a_and_e_graph_VPCO)


        self.verticalLayout_57.addWidget(self.tab_container_frame_for_a_and_e)

        self.Bottom_slider_VPCO_Output = QFrame(self.frame_3)
        self.Bottom_slider_VPCO_Output.setObjectName(u"Bottom_slider_VPCO_Output")
        sizePolicy1.setHeightForWidth(self.Bottom_slider_VPCO_Output.sizePolicy().hasHeightForWidth())
        self.Bottom_slider_VPCO_Output.setSizePolicy(sizePolicy1)
        self.Bottom_slider_VPCO_Output.setMinimumSize(QSize(0, 120))
        self.Bottom_slider_VPCO_Output.setMaximumSize(QSize(1677715, 120))
        self.Bottom_slider_VPCO_Output.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 255), stop:1 rgba(161, 161, 161, 255));\n"
"	\n"
"\n"
"}")
        self.Bottom_slider_VPCO_Output.setFrameShape(QFrame.StyledPanel)
        self.Bottom_slider_VPCO_Output.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.Bottom_slider_VPCO_Output)
        self.verticalLayout_58.setSpacing(8)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(5, 4, 5, 3)
        self.scrollArea_2 = QScrollArea(self.Bottom_slider_VPCO_Output)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setStyleSheet(u"/*QSrollArea{\n"
"background-color:#4e4f84;}*/\n"
"\n"
"/*Vertical Scrollbar*/\n"
"QScrollBar:vertical{\n"
"border:none;\n"
"background-color:rgb(59, 59, 90);\n"
"width:8px;\n"
"margin: 12px 0 12px 0;\n"
"}\n"
"\n"
"/* Handle Bar Vertical */\n"
"QScrollBar::handle:vertical{\n"
"background-color: rgb(80, 80, 122);\n"
"max-height: 1px;\n"
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
"background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/*"
                        " BTN BOTTOM - Scrollbar*/\n"
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
"margin: 12px 0 12px 0;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"/* Handle Bar Horizontal */\n"
"QScrollBar::handle"
                        ":horizontal{\n"
"background-color: rgb(80, 80, 122);\n"
"min-height: 10px;\n"
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
"subcontrol-position: bottom;\n"
"subc"
                        "ontrol-origin: margin;\n"
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
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 953, 205))
        self.horizontalLayout_183 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(15)
        self.widget_8 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(300, 35))
        self.widget_8.setMaximumSize(QSize(300, 35))
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
        self.VPCO_Radius_of_Peri_Label = QLabel(self.frame_65)
        self.VPCO_Radius_of_Peri_Label.setObjectName(u"VPCO_Radius_of_Peri_Label")
        self.VPCO_Radius_of_Peri_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Radius_of_Peri_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_112.addWidget(self.VPCO_Radius_of_Peri_Label)

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

        self.widget_9 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(300, 35))
        self.widget_9.setMaximumSize(QSize(300, 60))
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
        self.VPCO_Velocity_at_Periapis_Label = QLabel(self.frame_67)
        self.VPCO_Velocity_at_Periapis_Label.setObjectName(u"VPCO_Velocity_at_Periapis_Label")
        self.VPCO_Velocity_at_Periapis_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Velocity_at_Periapis_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_115.addWidget(self.VPCO_Velocity_at_Periapis_Label)

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


        self.gridLayout_3.addWidget(self.widget_9, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.widget_17 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(300, 35))
        self.widget_17.setMaximumSize(QSize(300, 35))
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
        self.VPCO_Semi_latus_Rectum_Label = QLabel(self.frame_83)
        self.VPCO_Semi_latus_Rectum_Label.setObjectName(u"VPCO_Semi_latus_Rectum_Label")
        self.VPCO_Semi_latus_Rectum_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Semi_latus_Rectum_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_139.addWidget(self.VPCO_Semi_latus_Rectum_Label)

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

        self.widget_19 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(300, 35))
        self.widget_19.setMaximumSize(QSize(300, 60))
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
        self.VPCO_Time_Period_Label = QLabel(self.frame_87)
        self.VPCO_Time_Period_Label.setObjectName(u"VPCO_Time_Period_Label")
        self.VPCO_Time_Period_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Time_Period_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_145.addWidget(self.VPCO_Time_Period_Label)

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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.widget_10 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(300, 35))
        self.widget_10.setMaximumSize(QSize(300, 35))
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
        self.VPCO_Vel_at_Semi_latus_re_Label = QLabel(self.frame_69)
        self.VPCO_Vel_at_Semi_latus_re_Label.setObjectName(u"VPCO_Vel_at_Semi_latus_re_Label")
        self.VPCO_Vel_at_Semi_latus_re_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Vel_at_Semi_latus_re_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_118.addWidget(self.VPCO_Vel_at_Semi_latus_re_Label)

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

        self.widget_15 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(300, 35))
        self.widget_15.setMaximumSize(QSize(300, 35))
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
        self.VPCO_Esc_Velocity_at_Periapsis_Label = QLabel(self.frame_79)
        self.VPCO_Esc_Velocity_at_Periapsis_Label.setObjectName(u"VPCO_Esc_Velocity_at_Periapsis_Label")
        self.VPCO_Esc_Velocity_at_Periapsis_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Esc_Velocity_at_Periapsis_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_133.addWidget(self.VPCO_Esc_Velocity_at_Periapsis_Label)

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

        self.widget_12 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(300, 35))
        self.widget_12.setMaximumSize(QSize(300, 60))
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
        self.VPCO_Esc_Velocity_at_Apoapsis_Label = QLabel(self.frame_73)
        self.VPCO_Esc_Velocity_at_Apoapsis_Label.setObjectName(u"VPCO_Esc_Velocity_at_Apoapsis_Label")
        self.VPCO_Esc_Velocity_at_Apoapsis_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Esc_Velocity_at_Apoapsis_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_124.addWidget(self.VPCO_Esc_Velocity_at_Apoapsis_Label)

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

        self.widget_11 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(300, 35))
        self.widget_11.setMaximumSize(QSize(300, 35))
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
        self.VPCO_Radius_of_Apo_Label = QLabel(self.frame_71)
        self.VPCO_Radius_of_Apo_Label.setObjectName(u"VPCO_Radius_of_Apo_Label")
        self.VPCO_Radius_of_Apo_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Radius_of_Apo_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_121.addWidget(self.VPCO_Radius_of_Apo_Label)

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

        self.widget_13 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(300, 35))
        self.widget_13.setMaximumSize(QSize(300, 35))
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
        self.VPCO_Sp_Mech_Energy_Label = QLabel(self.frame_75)
        self.VPCO_Sp_Mech_Energy_Label.setObjectName(u"VPCO_Sp_Mech_Energy_Label")
        self.VPCO_Sp_Mech_Energy_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Sp_Mech_Energy_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_127.addWidget(self.VPCO_Sp_Mech_Energy_Label)

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

        self.widget_20 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(300, 35))
        self.widget_20.setMaximumSize(QSize(300, 35))
        self.widget_20.setStyleSheet(u"background:none;")
        self.horizontalLayout_180 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_180.setSpacing(3)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(0, 0, 0, 0)
        self.frame_156 = QFrame(self.widget_20)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setMinimumSize(QSize(130, 35))
        self.frame_156.setMaximumSize(QSize(250, 16777215))
        self.frame_156.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_181 = QHBoxLayout(self.frame_156)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(6, 6, 6, 6)
        self.label_115 = QLabel(self.frame_156)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(100, 20))
        self.label_115.setMaximumSize(QSize(125, 20))
        self.label_115.setStyleSheet(u"QLabel{\n"
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
        self.label_115.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_181.addWidget(self.label_115, 0, Qt.AlignVCenter)


        self.horizontalLayout_180.addWidget(self.frame_156, 0, Qt.AlignVCenter)

        self.frame_157 = QFrame(self.widget_20)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setMinimumSize(QSize(0, 35))
        self.frame_157.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"border-radius:8px;")
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_182 = QHBoxLayout(self.frame_157)
        self.horizontalLayout_182.setSpacing(0)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(6, 6, 6, 6)
        self.VPCO_Sp_Angular_Mome_Label = QLabel(self.frame_157)
        self.VPCO_Sp_Angular_Mome_Label.setObjectName(u"VPCO_Sp_Angular_Mome_Label")
        self.VPCO_Sp_Angular_Mome_Label.setMinimumSize(QSize(85, 0))
        self.VPCO_Sp_Angular_Mome_Label.setMaximumSize(QSize(85, 16777215))
        self.VPCO_Sp_Angular_Mome_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Sp_Angular_Mome_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_182.addWidget(self.VPCO_Sp_Angular_Mome_Label)

        self.label_134 = QLabel(self.frame_157)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(30, 0))
        self.label_134.setMaximumSize(QSize(50, 16777215))
        self.label_134.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_182.addWidget(self.label_134)


        self.horizontalLayout_180.addWidget(self.frame_157)


        self.gridLayout_3.addWidget(self.widget_20, 3, 0, 1, 1)

        self.widget_16 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(300, 35))
        self.widget_16.setMaximumSize(QSize(300, 35))
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
        self.VPCO_Mean_Motion_Label = QLabel(self.frame_81)
        self.VPCO_Mean_Motion_Label.setObjectName(u"VPCO_Mean_Motion_Label")
        self.VPCO_Mean_Motion_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Mean_Motion_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_136.addWidget(self.VPCO_Mean_Motion_Label)

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

        self.widget_18 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(300, 35))
        self.widget_18.setMaximumSize(QSize(300, 35))
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
        self.VPCO_Velocity_of_Apoapsis_Label = QLabel(self.frame_85)
        self.VPCO_Velocity_of_Apoapsis_Label.setObjectName(u"VPCO_Velocity_of_Apoapsis_Label")
        self.VPCO_Velocity_of_Apoapsis_Label.setStyleSheet(u"QLabel{\n"
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
        self.VPCO_Velocity_of_Apoapsis_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_142.addWidget(self.VPCO_Velocity_of_Apoapsis_Label)

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


        self.gridLayout_3.addWidget(self.widget_18, 2, 2, 1, 1)


        self.horizontalLayout_183.addLayout(self.gridLayout_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_58.addWidget(self.scrollArea_2)


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
        self.horizontalLayout_105 = QHBoxLayout(self.a_and_e_VPCO_2)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.frame_57 = QFrame(self.a_and_e_VPCO_2)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(528, 16777215))
        self.frame_57.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_57)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(9, -1, -1, -1)
        self.verticalSpacer_19 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_19)

        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_58)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.widget_4 = QWidget(self.frame_58)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(410, 50))
        self.widget_4.setMaximumSize(QSize(410, 60))
        self.widget_4.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"}")
        self.horizontalLayout_98 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.frame_59 = QFrame(self.widget_4)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(200, 0))
        self.frame_59.setMaximumSize(QSize(250, 16777215))
        self.frame_59.setStyleSheet(u"background:none;")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.label_19 = QLabel(self.frame_59)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(150, 30))
        self.label_19.setMaximumSize(QSize(200, 16777215))
        self.label_19.setStyleSheet(u"QLabel{\n"
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
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_99.addWidget(self.label_19)


        self.horizontalLayout_98.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.widget_4)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setStyleSheet(u"background:none;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(9, 9, 9, 9)
        self.VPCO_Input_a_lineedit_2 = QLineEdit(self.frame_60)
        self.VPCO_Input_a_lineedit_2.setObjectName(u"VPCO_Input_a_lineedit_2")
        self.VPCO_Input_a_lineedit_2.setMinimumSize(QSize(130, 40))
        self.VPCO_Input_a_lineedit_2.setMaximumSize(QSize(200, 50))
        self.VPCO_Input_a_lineedit_2.setLayoutDirection(Qt.RightToLeft)
        self.VPCO_Input_a_lineedit_2.setStyleSheet(u"QLineEdit{\n"
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
        self.VPCO_Input_a_lineedit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_100.addWidget(self.VPCO_Input_a_lineedit_2)

        self.label_112 = QLabel(self.frame_60)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(40, 0))
        self.label_112.setMaximumSize(QSize(45, 16777215))
        self.label_112.setFont(font12)
        self.label_112.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_100.addWidget(self.label_112)


        self.horizontalLayout_98.addWidget(self.frame_60)


        self.verticalLayout_93.addWidget(self.widget_4, 0, Qt.AlignHCenter)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_93.addItem(self.verticalSpacer_20)

        self.widget_5 = QWidget(self.frame_58)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(410, 50))
        self.widget_5.setMaximumSize(QSize(410, 60))
        self.widget_5.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 93, 191, 255), stop:1 rgba(221, 161, 255, 255));\n"
"}")
        self.horizontalLayout_101 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.widget_5)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(200, 0))
        self.frame_61.setMaximumSize(QSize(250, 16777215))
        self.frame_61.setStyleSheet(u"background:none;")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_20 = QLabel(self.frame_61)
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

        self.horizontalLayout_102.addWidget(self.label_20)


        self.horizontalLayout_101.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.widget_5)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setStyleSheet(u"background:none;")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.VPCO_Input_e_lineedit_2 = QLineEdit(self.frame_62)
        self.VPCO_Input_e_lineedit_2.setObjectName(u"VPCO_Input_e_lineedit_2")
        self.VPCO_Input_e_lineedit_2.setMinimumSize(QSize(130, 40))
        self.VPCO_Input_e_lineedit_2.setMaximumSize(QSize(200, 50))
        self.VPCO_Input_e_lineedit_2.setLayoutDirection(Qt.RightToLeft)
        self.VPCO_Input_e_lineedit_2.setStyleSheet(u"QLineEdit{\n"
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
        self.VPCO_Input_e_lineedit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_103.addWidget(self.VPCO_Input_e_lineedit_2)

        self.label_133 = QLabel(self.frame_62)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMinimumSize(QSize(40, 0))
        self.label_133.setMaximumSize(QSize(45, 16777215))
        self.label_133.setFont(font12)
        self.label_133.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_103.addWidget(self.label_133)


        self.horizontalLayout_101.addWidget(self.frame_62)


        self.verticalLayout_93.addWidget(self.widget_5, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.frame_58)

        self.verticalSpacer_21 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_21)

        self.frame_63 = QFrame(self.frame_57)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 50))
        self.frame_63.setMaximumSize(QSize(16777215, 50))
        self.frame_63.setStyleSheet(u"border:none;\n"
"background:none;")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.maj_body_CoOE_3 = QComboBox(self.frame_63)
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.addItem("")
        self.maj_body_CoOE_3.setObjectName(u"maj_body_CoOE_3")
        self.maj_body_CoOE_3.setMinimumSize(QSize(300, 50))
        self.maj_body_CoOE_3.setMaximumSize(QSize(350, 50))
        self.maj_body_CoOE_3.setStyleSheet(u"QComboBox{\n"
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

        self.horizontalLayout_104.addWidget(self.maj_body_CoOE_3)


        self.verticalLayout_55.addWidget(self.frame_63)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_25)

        self.VPCO_Submit_button_2 = QPushButton(self.frame_57)
        self.VPCO_Submit_button_2.setObjectName(u"VPCO_Submit_button_2")
        sizePolicy2.setHeightForWidth(self.VPCO_Submit_button_2.sizePolicy().hasHeightForWidth())
        self.VPCO_Submit_button_2.setSizePolicy(sizePolicy2)
        self.VPCO_Submit_button_2.setMinimumSize(QSize(125, 50))
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

        self.verticalLayout_55.addWidget(self.VPCO_Submit_button_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_22 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_22)


        self.horizontalLayout_105.addWidget(self.frame_57)


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
        self.graph_stackedWidget_2 = QStackedWidget(self.a_and_e_graph_VPCO_2)
        self.graph_stackedWidget_2.setObjectName(u"graph_stackedWidget_2")
        self.graph_stackedWidget_2.setStyleSheet(u"QStackedWidget\n"
"{background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"border:none;}")
        self.graph_stackedWidget_2Page1 = QWidget()
        self.graph_stackedWidget_2Page1.setObjectName(u"graph_stackedWidget_2Page1")
        self.graph_stackedWidget_2.addWidget(self.graph_stackedWidget_2Page1)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.graph_stackedWidget_2.addWidget(self.page_5)

        self.horizontalLayout_15.addWidget(self.graph_stackedWidget_2)


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
        self.stackedWidget.addWidget(self.VPCO_output)
        self.COEnAOE = QWidget()
        self.COEnAOE.setObjectName(u"COEnAOE")
        self.horizontalLayout_43 = QHBoxLayout(self.COEnAOE)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(5, 0, 5, 0)
        self.COEnAOE_frame = QFrame(self.COEnAOE)
        self.COEnAOE_frame.setObjectName(u"COEnAOE_frame")
        self.COEnAOE_frame.setStyleSheet(u"QFrame{\n"
"	border: 2px solid white;\n"
"	background-color:#4e4f84;}")
        self.COEnAOE_frame.setFrameShape(QFrame.StyledPanel)
        self.COEnAOE_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.COEnAOE_frame)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(-1, -1, -1, 9)
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
"	border:none;\n"
"}\n"
"\n"
"\n"
"")
        self.PosNVelVector_inpt_frame.setFrameShape(QFrame.StyledPanel)
        self.PosNVelVector_inpt_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.PosNVelVector_inpt_frame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_77 = QFrame(self.PosNVelVector_inpt_frame)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(580, 0))
        self.frame_77.setMaximumSize(QSize(16777215, 16777215))
        self.frame_77.setStyleSheet(u"border:none;\n"
"background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_77)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 40, -1, -1)
        self.scrollArea_5 = QScrollArea(self.frame_77)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, -70, 558, 341))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_45 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(540, 35))
        self.widget_45.setMaximumSize(QSize(540, 35))
        self.widget_45.setStyleSheet(u"background:none;\n"
"\n"
"\n"
"border-radius:8px;")
        self.horizontalLayout_227 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_227.setSpacing(5)
        self.horizontalLayout_227.setObjectName(u"horizontalLayout_227")
        self.horizontalLayout_227.setContentsMargins(2, 0, 0, 0)
        self.frame_168 = QFrame(self.widget_45)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setMinimumSize(QSize(130, 30))
        self.frame_168.setMaximumSize(QSize(130, 35))
        self.frame_168.setStyleSheet(u"background-color: #ef7464;\n"
"border-radius:8px;\n"
"border:none;")
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_228 = QHBoxLayout(self.frame_168)
        self.horizontalLayout_228.setObjectName(u"horizontalLayout_228")
        self.horizontalLayout_228.setContentsMargins(0, 0, 0, 0)
        self.label_166 = QLabel(self.frame_168)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setMinimumSize(QSize(130, 35))
        self.label_166.setMaximumSize(QSize(130, 35))
        font14 = QFont()
        font14.setFamily(u"Arial")
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        self.label_166.setFont(font14)
        self.label_166.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_166.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_228.addWidget(self.label_166, 0, Qt.AlignVCenter)


        self.horizontalLayout_227.addWidget(self.frame_168, 0, Qt.AlignVCenter)

        self.frame_169 = QFrame(self.widget_45)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setMinimumSize(QSize(400, 0))
        self.frame_169.setMaximumSize(QSize(400, 16777215))
        self.frame_169.setStyleSheet(u"background-color: #ef7464;\n"
"border-radius:8px;")
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_169)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(6, 0, 6, 0)
        self.Ri_coe_n_aoe = QLineEdit(self.frame_169)
        self.Ri_coe_n_aoe.setObjectName(u"Ri_coe_n_aoe")
        self.Ri_coe_n_aoe.setMinimumSize(QSize(80, 25))
        self.Ri_coe_n_aoe.setMaximumSize(QSize(80, 16777215))
        self.Ri_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.Ri_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_129.addWidget(self.Ri_coe_n_aoe)

        self.label_188 = QLabel(self.frame_169)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setMinimumSize(QSize(10, 0))
        self.label_188.setMaximumSize(QSize(10, 16777215))
        self.label_188.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:blue;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_129.addWidget(self.label_188)

        self.label_176 = QLabel(self.frame_169)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setMinimumSize(QSize(20, 0))
        self.label_176.setMaximumSize(QSize(20, 16777215))
        self.label_176.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_129.addWidget(self.label_176)

        self.Rj_coe_n_aoe = QLineEdit(self.frame_169)
        self.Rj_coe_n_aoe.setObjectName(u"Rj_coe_n_aoe")
        self.Rj_coe_n_aoe.setMinimumSize(QSize(80, 25))
        self.Rj_coe_n_aoe.setMaximumSize(QSize(80, 16777215))
        self.Rj_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.Rj_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_129.addWidget(self.Rj_coe_n_aoe)

        self.label_167 = QLabel(self.frame_169)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMinimumSize(QSize(10, 0))
        self.label_167.setMaximumSize(QSize(10, 16777215))
        self.label_167.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:blue;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_129.addWidget(self.label_167)

        self.label_189 = QLabel(self.frame_169)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setMinimumSize(QSize(20, 0))
        self.label_189.setMaximumSize(QSize(20, 16777215))
        self.label_189.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_129.addWidget(self.label_189)

        self.Rk_coe_n_aoe = QLineEdit(self.frame_169)
        self.Rk_coe_n_aoe.setObjectName(u"Rk_coe_n_aoe")
        self.Rk_coe_n_aoe.setMinimumSize(QSize(80, 25))
        self.Rk_coe_n_aoe.setMaximumSize(QSize(80, 16777215))
        self.Rk_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.Rk_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_129.addWidget(self.Rk_coe_n_aoe)

        self.label_191 = QLabel(self.frame_169)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setMinimumSize(QSize(15, 0))
        self.label_191.setMaximumSize(QSize(15, 16777215))
        self.label_191.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:blue;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_129.addWidget(self.label_191)

        self.label_190 = QLabel(self.frame_169)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setMinimumSize(QSize(30, 0))
        self.label_190.setMaximumSize(QSize(45, 16777215))
        self.label_190.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_129.addWidget(self.label_190)


        self.horizontalLayout_227.addWidget(self.frame_169)


        self.verticalLayout_23.addWidget(self.widget_45)

        self.widget_46 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMinimumSize(QSize(540, 35))
        self.widget_46.setMaximumSize(QSize(540, 35))
        self.widget_46.setStyleSheet(u"background:none;\n"
"\n"
"\n"
"border-radius:8px;")
        self.horizontalLayout_229 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_229.setSpacing(5)
        self.horizontalLayout_229.setObjectName(u"horizontalLayout_229")
        self.horizontalLayout_229.setContentsMargins(2, 0, 0, 0)
        self.frame_170 = QFrame(self.widget_46)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setMinimumSize(QSize(130, 30))
        self.frame_170.setMaximumSize(QSize(130, 35))
        self.frame_170.setStyleSheet(u"background-color: #ef7464;\n"
"border-radius:8px;\n"
"border:none;")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_230 = QHBoxLayout(self.frame_170)
        self.horizontalLayout_230.setObjectName(u"horizontalLayout_230")
        self.horizontalLayout_230.setContentsMargins(0, 0, 0, 0)
        self.label_192 = QLabel(self.frame_170)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setMinimumSize(QSize(130, 35))
        self.label_192.setMaximumSize(QSize(130, 35))
        self.label_192.setFont(font14)
        self.label_192.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_192.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_230.addWidget(self.label_192, 0, Qt.AlignVCenter)


        self.horizontalLayout_229.addWidget(self.frame_170, 0, Qt.AlignVCenter)

        self.frame_171 = QFrame(self.widget_46)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setMinimumSize(QSize(400, 0))
        self.frame_171.setMaximumSize(QSize(400, 16777215))
        self.frame_171.setStyleSheet(u"background-color: #ef7464;\n"
"border-radius:8px;")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(6, 0, 6, 0)
        self.Vi_coe_n_aoe = QLineEdit(self.frame_171)
        self.Vi_coe_n_aoe.setObjectName(u"Vi_coe_n_aoe")
        self.Vi_coe_n_aoe.setMinimumSize(QSize(80, 25))
        self.Vi_coe_n_aoe.setMaximumSize(QSize(80, 16777215))
        self.Vi_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.Vi_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_130.addWidget(self.Vi_coe_n_aoe)

        self.label_193 = QLabel(self.frame_171)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setMinimumSize(QSize(10, 0))
        self.label_193.setMaximumSize(QSize(10, 16777215))
        self.label_193.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:blue;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_130.addWidget(self.label_193)

        self.label_194 = QLabel(self.frame_171)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setMinimumSize(QSize(20, 0))
        self.label_194.setMaximumSize(QSize(20, 16777215))
        self.label_194.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_130.addWidget(self.label_194)

        self.Vj_coe_n_aoe = QLineEdit(self.frame_171)
        self.Vj_coe_n_aoe.setObjectName(u"Vj_coe_n_aoe")
        self.Vj_coe_n_aoe.setMinimumSize(QSize(80, 25))
        self.Vj_coe_n_aoe.setMaximumSize(QSize(80, 16777215))
        self.Vj_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.Vj_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_130.addWidget(self.Vj_coe_n_aoe)

        self.label_195 = QLabel(self.frame_171)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setMinimumSize(QSize(10, 0))
        self.label_195.setMaximumSize(QSize(10, 16777215))
        self.label_195.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:blue;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_130.addWidget(self.label_195)

        self.label_196 = QLabel(self.frame_171)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setMinimumSize(QSize(20, 0))
        self.label_196.setMaximumSize(QSize(20, 16777215))
        self.label_196.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_130.addWidget(self.label_196)

        self.Vk_coe_n_aoe = QLineEdit(self.frame_171)
        self.Vk_coe_n_aoe.setObjectName(u"Vk_coe_n_aoe")
        self.Vk_coe_n_aoe.setMinimumSize(QSize(80, 25))
        self.Vk_coe_n_aoe.setMaximumSize(QSize(80, 16777215))
        self.Vk_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.Vk_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_130.addWidget(self.Vk_coe_n_aoe)

        self.label_212 = QLabel(self.frame_171)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setMinimumSize(QSize(15, 0))
        self.label_212.setMaximumSize(QSize(15, 16777215))
        self.label_212.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:blue;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_130.addWidget(self.label_212)

        self.label_213 = QLabel(self.frame_171)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setMinimumSize(QSize(40, 0))
        self.label_213.setMaximumSize(QSize(45, 16777215))
        self.label_213.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:13px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")

        self.horizontalLayout_130.addWidget(self.label_213)


        self.horizontalLayout_229.addWidget(self.frame_171)


        self.verticalLayout_23.addWidget(self.widget_46)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer)

        self.maj_body_CoOE = QComboBox(self.scrollAreaWidgetContents_4)
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
        self.maj_body_CoOE.setMinimumSize(QSize(0, 35))
        self.maj_body_CoOE.setMaximumSize(QSize(220, 40))
        self.maj_body_CoOE.setStyleSheet(u"QComboBox{\n"
"	background-color:#04ae92;\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 15px;\n"
"	border:5px solid #04ae92;}\n"
"\n"
"QFrame{\n"
"	background-color:#04ae92;\n"
"	border:2px solid white;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"/*QSrollArea{\n"
"background-color:#4e4f84;}*/\n"
"\n"
"/*Vertical Scrollbar*/\n"
"QScrollBar:vertical{\n"
"\n"
"background-color:white;\n"
"width:10px;\n"
"margin: 15px 1px 15px 1px;\n"
"\n"
"}\n"
"\n"
"/* Handle Bar Vertical */\n"
"QScrollBar::handle:vertical{\n"
"background-color: white;\n"
"min-height: 30px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vetical:hover{\n"
"background-color: white;\n"
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
"background-color: none;\n"
"height:15px;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
""
                        "}\n"
"\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - Scrollbar*/\n"
"QScrollBar::add-line:vertical{\n"
"border:none;\n"
"background-color:none;\n"
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
"background: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"/*Horizontal Scrollbar*/\n"
"QScrollBar:horizontal{\n"
""
                        "border:none;\n"
"background-color:rgb(59, 59, 90);\n"
"width:8px;\n"
"margin: 15px 0 15px 0;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"/* Handle Bar Horizontal */\n"
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
"bo"
                        "rder:none;\n"
"background-color: rgb(59, 59, 90);\n"
"height:15px;\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"subcontrol-position: bottom;\n"
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
"\n"
"\n"
"")

        self.verticalLayout_23.addWidget(self.maj_body_CoOE, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_2)

        self.Other_Body_input_frame_COEnAOE = QFrame(self.scrollAreaWidgetContents_4)
        self.Other_Body_input_frame_COEnAOE.setObjectName(u"Other_Body_input_frame_COEnAOE")
        self.Other_Body_input_frame_COEnAOE.setMinimumSize(QSize(0, 140))
        self.Other_Body_input_frame_COEnAOE.setMaximumSize(QSize(400, 140))
        self.Other_Body_input_frame_COEnAOE.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: #1b1b1b;\n"
"	\n"
"	\n"
"}")
        self.Other_Body_input_frame_COEnAOE.setFrameShape(QFrame.StyledPanel)
        self.Other_Body_input_frame_COEnAOE.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Other_Body_input_frame_COEnAOE)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Planet_name_display_COEnAOE = QLineEdit(self.Other_Body_input_frame_COEnAOE)
        self.Planet_name_display_COEnAOE.setObjectName(u"Planet_name_display_COEnAOE")
        self.Planet_name_display_COEnAOE.setMinimumSize(QSize(120, 30))
        self.Planet_name_display_COEnAOE.setMaximumSize(QSize(120, 30))
        self.Planet_name_display_COEnAOE.setStyleSheet(u"QLineEdit{\n"
"	font: 18px;\n"
"	color:#ef7464;\n"
"	background-color:white}")
        self.Planet_name_display_COEnAOE.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Planet_name_display_COEnAOE, 0, Qt.AlignHCenter)

        self.widget_47 = QWidget(self.Other_Body_input_frame_COEnAOE)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setMinimumSize(QSize(300, 35))
        self.widget_47.setMaximumSize(QSize(300, 35))
        self.widget_47.setStyleSheet(u"background:none;")
        self.horizontalLayout_232 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_232.setSpacing(3)
        self.horizontalLayout_232.setObjectName(u"horizontalLayout_232")
        self.horizontalLayout_232.setContentsMargins(0, 0, 0, 0)
        self.frame_173 = QFrame(self.widget_47)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setMinimumSize(QSize(130, 35))
        self.frame_173.setMaximumSize(QSize(250, 16777215))
        self.frame_173.setStyleSheet(u"background-color: #04ae92;\n"
"border-radius:8px;")
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_233 = QHBoxLayout(self.frame_173)
        self.horizontalLayout_233.setSpacing(0)
        self.horizontalLayout_233.setObjectName(u"horizontalLayout_233")
        self.horizontalLayout_233.setContentsMargins(0, 0, 0, 0)
        self.label_79 = QLabel(self.frame_173)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(150, 35))
        self.label_79.setMaximumSize(QSize(150, 35))
        self.label_79.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_233.addWidget(self.label_79, 0, Qt.AlignVCenter)


        self.horizontalLayout_232.addWidget(self.frame_173, 0, Qt.AlignVCenter)

        self.frame_174 = QFrame(self.widget_47)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setStyleSheet(u"background-color: #04ae92;\n"
"border-radius:8px;\n"
"")
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_234 = QHBoxLayout(self.frame_174)
        self.horizontalLayout_234.setObjectName(u"horizontalLayout_234")
        self.horizontalLayout_234.setContentsMargins(6, 6, 6, 6)
        self.Body_mass_coe_n_aoe = QLabel(self.frame_174)
        self.Body_mass_coe_n_aoe.setObjectName(u"Body_mass_coe_n_aoe")
        self.Body_mass_coe_n_aoe.setStyleSheet(u"QLabel{\n"
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
        self.Body_mass_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_234.addWidget(self.Body_mass_coe_n_aoe)

        self.Body_mass_coe_n_aoe_edit = QLineEdit(self.frame_174)
        self.Body_mass_coe_n_aoe_edit.setObjectName(u"Body_mass_coe_n_aoe_edit")
        self.Body_mass_coe_n_aoe_edit.setMinimumSize(QSize(84, 23))
        self.Body_mass_coe_n_aoe_edit.setMaximumSize(QSize(84, 23))
        self.Body_mass_coe_n_aoe_edit.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")

        self.horizontalLayout_234.addWidget(self.Body_mass_coe_n_aoe_edit)

        self.label_214 = QLabel(self.frame_174)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setMinimumSize(QSize(30, 0))
        self.label_214.setMaximumSize(QSize(45, 16777215))
        self.label_214.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_234.addWidget(self.label_214)


        self.horizontalLayout_232.addWidget(self.frame_174)


        self.verticalLayout_3.addWidget(self.widget_47)

        self.widget_48 = QWidget(self.Other_Body_input_frame_COEnAOE)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(300, 35))
        self.widget_48.setMaximumSize(QSize(300, 35))
        self.widget_48.setStyleSheet(u"background:none;")
        self.horizontalLayout_235 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_235.setSpacing(3)
        self.horizontalLayout_235.setObjectName(u"horizontalLayout_235")
        self.horizontalLayout_235.setContentsMargins(0, 0, 0, 0)
        self.frame_175 = QFrame(self.widget_48)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setMinimumSize(QSize(130, 35))
        self.frame_175.setMaximumSize(QSize(250, 16777215))
        self.frame_175.setStyleSheet(u"background-color: #04ae92;\n"
"border-radius:8px;")
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_236 = QHBoxLayout(self.frame_175)
        self.horizontalLayout_236.setSpacing(0)
        self.horizontalLayout_236.setObjectName(u"horizontalLayout_236")
        self.horizontalLayout_236.setContentsMargins(0, 0, 0, 0)
        self.label_88 = QLabel(self.frame_175)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(150, 35))
        self.label_88.setMaximumSize(QSize(150, 35))
        self.label_88.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#fff;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_88.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_236.addWidget(self.label_88, 0, Qt.AlignVCenter)


        self.horizontalLayout_235.addWidget(self.frame_175, 0, Qt.AlignVCenter)

        self.frame_176 = QFrame(self.widget_48)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setStyleSheet(u"background-color: #04ae92;\n"
"border-radius:8px;\n"
"")
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_237 = QHBoxLayout(self.frame_176)
        self.horizontalLayout_237.setObjectName(u"horizontalLayout_237")
        self.horizontalLayout_237.setContentsMargins(6, 6, 6, 6)
        self.Body_radius_coe_n_aoe = QLabel(self.frame_176)
        self.Body_radius_coe_n_aoe.setObjectName(u"Body_radius_coe_n_aoe")
        self.Body_radius_coe_n_aoe.setStyleSheet(u"QLabel{\n"
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
        self.Body_radius_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_237.addWidget(self.Body_radius_coe_n_aoe)

        self.Body_radius_coe_n_aoe_edit = QLineEdit(self.frame_176)
        self.Body_radius_coe_n_aoe_edit.setObjectName(u"Body_radius_coe_n_aoe_edit")
        self.Body_radius_coe_n_aoe_edit.setMinimumSize(QSize(84, 23))
        self.Body_radius_coe_n_aoe_edit.setMaximumSize(QSize(84, 23))
        self.Body_radius_coe_n_aoe_edit.setStyleSheet(u"QLineEdit{\n"
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
"QLineEdit:hover{\n"
"	\n"
"	border: 2px solid rgb(89, 91, 147);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")

        self.horizontalLayout_237.addWidget(self.Body_radius_coe_n_aoe_edit)

        self.label_215 = QLabel(self.frame_176)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setMinimumSize(QSize(30, 0))
        self.label_215.setMaximumSize(QSize(45, 16777215))
        self.label_215.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_237.addWidget(self.label_215)


        self.horizontalLayout_235.addWidget(self.frame_176)


        self.verticalLayout_3.addWidget(self.widget_48)


        self.verticalLayout_23.addWidget(self.Other_Body_input_frame_COEnAOE, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_3)

        self.cal_btn_coe_n_aoe = QPushButton(self.scrollAreaWidgetContents_4)
        self.cal_btn_coe_n_aoe.setObjectName(u"cal_btn_coe_n_aoe")
        self.cal_btn_coe_n_aoe.setMinimumSize(QSize(100, 30))
        self.cal_btn_coe_n_aoe.setMaximumSize(QSize(120, 30))
        font15 = QFont()
        font15.setPointSize(10)
        self.cal_btn_coe_n_aoe.setFont(font15)
        self.cal_btn_coe_n_aoe.setStyleSheet(u"QPushButton{\n"
"	background-color:#ef7464;\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 12px;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#ef7464;\n"
"	background-color: white;\n"
"}")

        self.verticalLayout_23.addWidget(self.cal_btn_coe_n_aoe, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_4)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_2.addWidget(self.scrollArea_5)


        self.horizontalLayout_22.addWidget(self.frame_77)

        self.frame_40 = QFrame(self.PosNVelVector_inpt_frame)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_40)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	image:url(UI_Functions/Resources/SOI.png);\n"
"	border:2px solid white;\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.verticalLayout_100.addWidget(self.frame_41)

        self.frame_172 = QFrame(self.frame_40)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	border:2px solid white;\n"
"}")
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_172)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(20, 20, 20, -1)
        self.frame_177 = QFrame(self.frame_172)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setMinimumSize(QSize(200, 30))
        self.frame_177.setMaximumSize(QSize(200, 30))
        self.frame_177.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_177)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_18 = QLabel(self.frame_177)
        self.semi_major_axis_toggle_menu_lbl_18.setObjectName(u"semi_major_axis_toggle_menu_lbl_18")
        self.semi_major_axis_toggle_menu_lbl_18.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_18.setMaximumSize(QSize(16777215, 20))
        font16 = QFont()
        font16.setFamily(u"Arial")
        font16.setPointSize(12)
        font16.setBold(False)
        font16.setItalic(False)
        font16.setWeight(50)
        self.semi_major_axis_toggle_menu_lbl_18.setFont(font16)
        self.semi_major_axis_toggle_menu_lbl_18.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_111.addWidget(self.semi_major_axis_toggle_menu_lbl_18, 0, Qt.AlignHCenter)


        self.verticalLayout_110.addWidget(self.frame_177, 0, Qt.AlignHCenter)

        self.label_33 = QLabel(self.frame_172)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font16)
        self.label_33.setFocusPolicy(Qt.NoFocus)
        self.label_33.setStyleSheet(u"color:grey;\n"
"border:none;")
        self.label_33.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_33.setWordWrap(True)

        self.verticalLayout_110.addWidget(self.label_33)


        self.verticalLayout_100.addWidget(self.frame_172)


        self.horizontalLayout_22.addWidget(self.frame_40)


        self.verticalLayout_49.addWidget(self.PosNVelVector_inpt_frame)

        self.CoOE_output_frame = QFrame(self.COEnAOE_frame)
        self.CoOE_output_frame.setObjectName(u"CoOE_output_frame")
        self.CoOE_output_frame.setMinimumSize(QSize(0, 220))
        self.CoOE_output_frame.setMaximumSize(QSize(30000, 220))
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
"	background-color:#f4717f;\n"
"	border-radius: 15px;\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"")
        self.CoOE_output_frame.setFrameShape(QFrame.StyledPanel)
        self.CoOE_output_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.CoOE_output_frame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.CoOE_output_stack = QStackedWidget(self.CoOE_output_frame)
        self.CoOE_output_stack.setObjectName(u"CoOE_output_stack")
        self.CoOE_output_stack.setStyleSheet(u"QStackedWidget{\n"
"	border:none;\n"
"	border:2px solid white;\n"
"}")
        self.CoOE_output_lbl_error_screen = QWidget()
        self.CoOE_output_lbl_error_screen.setObjectName(u"CoOE_output_lbl_error_screen")
        self.verticalLayout_25 = QVBoxLayout(self.CoOE_output_lbl_error_screen)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.CoOE_output_lbl_error = QLineEdit(self.CoOE_output_lbl_error_screen)
        self.CoOE_output_lbl_error.setObjectName(u"CoOE_output_lbl_error")
        self.CoOE_output_lbl_error.setMaximumSize(QSize(16777215, 30))
        self.CoOE_output_lbl_error.setFont(font10)
        self.CoOE_output_lbl_error.setStyleSheet(u"background-color:white;\n"
"color: #04ae92;\n"
"")
        self.CoOE_output_lbl_error.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.CoOE_output_lbl_error)

        self.CoOE_output_stack.addWidget(self.CoOE_output_lbl_error_screen)
        self.CoOE_output_parameters_screen = QWidget()
        self.CoOE_output_parameters_screen.setObjectName(u"CoOE_output_parameters_screen")
        self.verticalLayout_14 = QVBoxLayout(self.CoOE_output_parameters_screen)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 5, -1, -1)
        self.CoOE_output_para_lbl = QLineEdit(self.CoOE_output_parameters_screen)
        self.CoOE_output_para_lbl.setObjectName(u"CoOE_output_para_lbl")
        self.CoOE_output_para_lbl.setMaximumSize(QSize(16777215, 30))
        self.CoOE_output_para_lbl.setFont(font10)
        self.CoOE_output_para_lbl.setStyleSheet(u"background-color:white;\n"
"\n"
"color:#04ae92;\n"
"border-radius:8px;")
        self.CoOE_output_para_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.CoOE_output_para_lbl)

        self.frame_4 = QFrame(self.CoOE_output_parameters_screen)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_14 = QWidget(self.frame_4)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(380, 40))
        self.widget_14.setMaximumSize(QSize(380, 40))
        self.widget_14.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_207 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_207.setSpacing(6)
        self.horizontalLayout_207.setObjectName(u"horizontalLayout_207")
        self.horizontalLayout_207.setContentsMargins(0, 0, 0, 0)
        self.frame_180 = QFrame(self.widget_14)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setMinimumSize(QSize(180, 0))
        self.frame_180.setMaximumSize(QSize(180, 35))
        self.frame_180.setStyleSheet(u"background-color:white;")
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_240 = QHBoxLayout(self.frame_180)
        self.horizontalLayout_240.setObjectName(u"horizontalLayout_240")
        self.horizontalLayout_240.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_180)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(180, 30))
        self.label_17.setMaximumSize(QSize(180, 35))
        self.label_17.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_240.addWidget(self.label_17)


        self.horizontalLayout_207.addWidget(self.frame_180)

        self.frame_183 = QFrame(self.widget_14)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setStyleSheet(u"background:none;")
        self.frame_183.setFrameShape(QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_241 = QHBoxLayout(self.frame_183)
        self.horizontalLayout_241.setSpacing(0)
        self.horizontalLayout_241.setObjectName(u"horizontalLayout_241")
        self.horizontalLayout_241.setContentsMargins(0, 0, 0, 0)
        self.inclination_coe_n_aoe = QLineEdit(self.frame_183)
        self.inclination_coe_n_aoe.setObjectName(u"inclination_coe_n_aoe")
        self.inclination_coe_n_aoe.setMinimumSize(QSize(100, 28))
        self.inclination_coe_n_aoe.setMaximumSize(QSize(100, 28))
        self.inclination_coe_n_aoe.setLayoutDirection(Qt.RightToLeft)
        self.inclination_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	\n"
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
"	border: 2px solid white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.inclination_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_241.addWidget(self.inclination_coe_n_aoe)

        self.label_217 = QLabel(self.frame_183)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setMinimumSize(QSize(55, 0))
        self.label_217.setMaximumSize(QSize(55, 16777215))
        self.label_217.setFont(font14)
        self.label_217.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_241.addWidget(self.label_217)


        self.horizontalLayout_207.addWidget(self.frame_183)


        self.gridLayout_8.addWidget(self.widget_14, 2, 0, 1, 1)

        self.widget_21 = QWidget(self.frame_4)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(380, 40))
        self.widget_21.setMaximumSize(QSize(380, 40))
        self.widget_21.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_242 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_242.setSpacing(6)
        self.horizontalLayout_242.setObjectName(u"horizontalLayout_242")
        self.horizontalLayout_242.setContentsMargins(0, 0, 0, 0)
        self.frame_184 = QFrame(self.widget_21)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setMinimumSize(QSize(180, 0))
        self.frame_184.setMaximumSize(QSize(180, 35))
        self.frame_184.setStyleSheet(u"background-color:white;")
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_243 = QHBoxLayout(self.frame_184)
        self.horizontalLayout_243.setObjectName(u"horizontalLayout_243")
        self.horizontalLayout_243.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_184)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(180, 30))
        self.label_25.setMaximumSize(QSize(180, 35))
        self.label_25.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setWordWrap(True)

        self.horizontalLayout_243.addWidget(self.label_25)


        self.horizontalLayout_242.addWidget(self.frame_184)

        self.frame_185 = QFrame(self.widget_21)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setStyleSheet(u"background:none;")
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_244 = QHBoxLayout(self.frame_185)
        self.horizontalLayout_244.setSpacing(0)
        self.horizontalLayout_244.setObjectName(u"horizontalLayout_244")
        self.horizontalLayout_244.setContentsMargins(0, 0, 0, 0)
        self.RAAN_coe_n_aoe = QLineEdit(self.frame_185)
        self.RAAN_coe_n_aoe.setObjectName(u"RAAN_coe_n_aoe")
        self.RAAN_coe_n_aoe.setMinimumSize(QSize(100, 28))
        self.RAAN_coe_n_aoe.setMaximumSize(QSize(100, 28))
        self.RAAN_coe_n_aoe.setLayoutDirection(Qt.RightToLeft)
        self.RAAN_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	\n"
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
"	border: 2px solid white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.RAAN_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_244.addWidget(self.RAAN_coe_n_aoe)

        self.label_218 = QLabel(self.frame_185)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setMinimumSize(QSize(55, 0))
        self.label_218.setMaximumSize(QSize(55, 16777215))
        self.label_218.setFont(font14)
        self.label_218.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_244.addWidget(self.label_218)


        self.horizontalLayout_242.addWidget(self.frame_185)


        self.gridLayout_8.addWidget(self.widget_21, 0, 1, 1, 1)

        self.widget_28 = QWidget(self.frame_4)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(380, 40))
        self.widget_28.setMaximumSize(QSize(380, 40))
        self.widget_28.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_245 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_245.setSpacing(6)
        self.horizontalLayout_245.setObjectName(u"horizontalLayout_245")
        self.horizontalLayout_245.setContentsMargins(0, 0, 0, 0)
        self.frame_186 = QFrame(self.widget_28)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setMinimumSize(QSize(180, 0))
        self.frame_186.setMaximumSize(QSize(180, 35))
        self.frame_186.setStyleSheet(u"background-color:white;")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_246 = QHBoxLayout(self.frame_186)
        self.horizontalLayout_246.setObjectName(u"horizontalLayout_246")
        self.horizontalLayout_246.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_186)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(180, 30))
        self.label_26.setMaximumSize(QSize(180, 35))
        self.label_26.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(True)

        self.horizontalLayout_246.addWidget(self.label_26)


        self.horizontalLayout_245.addWidget(self.frame_186)

        self.frame_187 = QFrame(self.widget_28)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setStyleSheet(u"background:none;")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_247 = QHBoxLayout(self.frame_187)
        self.horizontalLayout_247.setSpacing(0)
        self.horizontalLayout_247.setObjectName(u"horizontalLayout_247")
        self.horizontalLayout_247.setContentsMargins(0, 0, 0, 0)
        self.arg_of_per_coe_n_aoe = QLineEdit(self.frame_187)
        self.arg_of_per_coe_n_aoe.setObjectName(u"arg_of_per_coe_n_aoe")
        self.arg_of_per_coe_n_aoe.setMinimumSize(QSize(100, 28))
        self.arg_of_per_coe_n_aoe.setMaximumSize(QSize(100, 28))
        self.arg_of_per_coe_n_aoe.setLayoutDirection(Qt.RightToLeft)
        self.arg_of_per_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	\n"
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
"	border: 2px solid white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.arg_of_per_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_247.addWidget(self.arg_of_per_coe_n_aoe)

        self.label_219 = QLabel(self.frame_187)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setMinimumSize(QSize(55, 0))
        self.label_219.setMaximumSize(QSize(55, 16777215))
        self.label_219.setFont(font14)
        self.label_219.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_247.addWidget(self.label_219)


        self.horizontalLayout_245.addWidget(self.frame_187)


        self.gridLayout_8.addWidget(self.widget_28, 2, 1, 1, 1)

        self.widget_49 = QWidget(self.frame_4)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(380, 40))
        self.widget_49.setMaximumSize(QSize(380, 40))
        self.widget_49.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_248 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_248.setSpacing(6)
        self.horizontalLayout_248.setObjectName(u"horizontalLayout_248")
        self.horizontalLayout_248.setContentsMargins(0, 0, 0, 0)
        self.frame_188 = QFrame(self.widget_49)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setMinimumSize(QSize(180, 0))
        self.frame_188.setMaximumSize(QSize(180, 35))
        self.frame_188.setStyleSheet(u"background-color:white;")
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_249 = QHBoxLayout(self.frame_188)
        self.horizontalLayout_249.setObjectName(u"horizontalLayout_249")
        self.horizontalLayout_249.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_188)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(180, 30))
        self.label_27.setMaximumSize(QSize(180, 35))
        self.label_27.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_27.setWordWrap(True)

        self.horizontalLayout_249.addWidget(self.label_27)


        self.horizontalLayout_248.addWidget(self.frame_188)

        self.frame_189 = QFrame(self.widget_49)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setStyleSheet(u"background:none;")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_250 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_250.setSpacing(0)
        self.horizontalLayout_250.setObjectName(u"horizontalLayout_250")
        self.horizontalLayout_250.setContentsMargins(0, 0, 0, 0)
        self.tru_ana_coe_n_aoe = QLineEdit(self.frame_189)
        self.tru_ana_coe_n_aoe.setObjectName(u"tru_ana_coe_n_aoe")
        self.tru_ana_coe_n_aoe.setMinimumSize(QSize(100, 28))
        self.tru_ana_coe_n_aoe.setMaximumSize(QSize(100, 32))
        self.tru_ana_coe_n_aoe.setLayoutDirection(Qt.RightToLeft)
        self.tru_ana_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	\n"
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
"	border: 2px solid white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.tru_ana_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_250.addWidget(self.tru_ana_coe_n_aoe)

        self.label_220 = QLabel(self.frame_189)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setMinimumSize(QSize(55, 0))
        self.label_220.setMaximumSize(QSize(55, 16777215))
        self.label_220.setFont(font14)
        self.label_220.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_250.addWidget(self.label_220)


        self.horizontalLayout_248.addWidget(self.frame_189)


        self.gridLayout_8.addWidget(self.widget_49, 4, 1, 1, 1)

        self.widget_6 = QWidget(self.frame_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(370, 40))
        self.widget_6.setMaximumSize(QSize(370, 40))
        self.widget_6.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_84 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_84.setSpacing(6)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.frame_137 = QFrame(self.widget_6)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setMinimumSize(QSize(180, 0))
        self.frame_137.setMaximumSize(QSize(180, 35))
        self.frame_137.setStyleSheet(u"background-color:white;")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_174 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_174.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_137)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(180, 35))
        self.label_15.setMaximumSize(QSize(180, 35))
        self.label_15.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_174.addWidget(self.label_15)


        self.horizontalLayout_84.addWidget(self.frame_137)

        self.frame_158 = QFrame(self.widget_6)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setStyleSheet(u"background:none;")
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_178 = QHBoxLayout(self.frame_158)
        self.horizontalLayout_178.setSpacing(0)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.semimajor_axis_coe_n_aoe = QLineEdit(self.frame_158)
        self.semimajor_axis_coe_n_aoe.setObjectName(u"semimajor_axis_coe_n_aoe")
        self.semimajor_axis_coe_n_aoe.setMinimumSize(QSize(100, 28))
        self.semimajor_axis_coe_n_aoe.setMaximumSize(QSize(100, 28))
        self.semimajor_axis_coe_n_aoe.setLayoutDirection(Qt.RightToLeft)
        self.semimajor_axis_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	\n"
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
"	border: 2px solid white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.semimajor_axis_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_178.addWidget(self.semimajor_axis_coe_n_aoe)

        self.label_156 = QLabel(self.frame_158)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setMinimumSize(QSize(40, 0))
        self.label_156.setMaximumSize(QSize(45, 16777215))
        self.label_156.setFont(font14)
        self.label_156.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_178.addWidget(self.label_156)


        self.horizontalLayout_84.addWidget(self.frame_158)


        self.gridLayout_8.addWidget(self.widget_6, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.frame_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(380, 40))
        self.widget_7.setMaximumSize(QSize(380, 40))
        self.widget_7.setStyleSheet(u"QWidget{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_179 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_179.setSpacing(6)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.frame_159 = QFrame(self.widget_7)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setMinimumSize(QSize(180, 0))
        self.frame_159.setMaximumSize(QSize(180, 35))
        self.frame_159.setStyleSheet(u"background-color:white;")
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_205 = QHBoxLayout(self.frame_159)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.horizontalLayout_205.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_159)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(180, 30))
        self.label_16.setMaximumSize(QSize(180, 35))
        self.label_16.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:15px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_205.addWidget(self.label_16)


        self.horizontalLayout_179.addWidget(self.frame_159)

        self.frame_179 = QFrame(self.widget_7)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setStyleSheet(u"background:none;")
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_206 = QHBoxLayout(self.frame_179)
        self.horizontalLayout_206.setSpacing(0)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.eccentricity_coe_n_aoe = QLineEdit(self.frame_179)
        self.eccentricity_coe_n_aoe.setObjectName(u"eccentricity_coe_n_aoe")
        self.eccentricity_coe_n_aoe.setMinimumSize(QSize(100, 28))
        self.eccentricity_coe_n_aoe.setMaximumSize(QSize(100, 28))
        self.eccentricity_coe_n_aoe.setLayoutDirection(Qt.RightToLeft)
        self.eccentricity_coe_n_aoe.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	border:2px solid rgb(78, 79, 132);\n"
"	\n"
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
"	border: 2px solid white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #ff99ff\n"
"}")
        self.eccentricity_coe_n_aoe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_206.addWidget(self.eccentricity_coe_n_aoe)

        self.label_216 = QLabel(self.frame_179)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setMinimumSize(QSize(55, 0))
        self.label_216.setMaximumSize(QSize(55, 16777215))
        self.label_216.setFont(font14)
        self.label_216.setStyleSheet(u"QLabel{\n"
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

        self.horizontalLayout_206.addWidget(self.label_216)


        self.horizontalLayout_179.addWidget(self.frame_179)


        self.gridLayout_8.addWidget(self.widget_7, 4, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_4)

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
        self.horizontalLayout_85.setContentsMargins(6, 2, 0, 0)
        self.Container_for_Type_of_Orbital_Transfer = QFrame(self.Orbital_Transfer)
        self.Container_for_Type_of_Orbital_Transfer.setObjectName(u"Container_for_Type_of_Orbital_Transfer")
        self.Container_for_Type_of_Orbital_Transfer.setMinimumSize(QSize(450, 0))
        self.Container_for_Type_of_Orbital_Transfer.setMaximumSize(QSize(16777215, 16777215))
        self.Container_for_Type_of_Orbital_Transfer.setStyleSheet(u"\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	border:2px solid white;\n"
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
        self.frame_45.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"")
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
"image:url(UI_Functions/Resources/Hohmann Transfer.png);\n"
"border:2px solid white;")
        self.verticalLayout_66 = QVBoxLayout(self.Orbit_Visualization_3)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(2, 0, 2, 2)
        self.filler_13 = QFrame(self.Orbit_Visualization_3)
        self.filler_13.setObjectName(u"filler_13")
        self.filler_13.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;\n"
"")
        self.filler_13.setFrameShape(QFrame.StyledPanel)
        self.filler_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout_66.addWidget(self.filler_13)

        self.slider_13 = QFrame(self.Orbit_Visualization_3)
        self.slider_13.setObjectName(u"slider_13")
        self.slider_13.setMinimumSize(QSize(446, 80))
        self.slider_13.setMaximumSize(QSize(450, 200))
        self.slider_13.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;\n"
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
"image:url(UI_Functions/Resources/Bi-Elliptical Hohmann Transfer.png);\n"
"border:2px solid white;")
        self.verticalLayout_54 = QVBoxLayout(self.Orbit_Visualization_2)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(2, 0, 2, 2)
        self.filler_12 = QFrame(self.Orbit_Visualization_2)
        self.filler_12.setObjectName(u"filler_12")
        self.filler_12.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;\n"
"\n"
"")
        self.filler_12.setFrameShape(QFrame.StyledPanel)
        self.filler_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_54.addWidget(self.filler_12)

        self.slider_12 = QFrame(self.Orbit_Visualization_2)
        self.slider_12.setObjectName(u"slider_12")
        self.slider_12.setMinimumSize(QSize(446, 80))
        self.slider_12.setMaximumSize(QSize(230, 200))
        self.slider_12.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;\n"
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
"image:url(UI_Functions/Resources/Phasing Maneuver.png);\n"
"border:2px solid white;")
        self.verticalLayout_72 = QVBoxLayout(self.Orbit_Visualization_5)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(2, 0, 2, 2)
        self.filler_16 = QFrame(self.Orbit_Visualization_5)
        self.filler_16.setObjectName(u"filler_16")
        self.filler_16.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"border:none;\n"
"")
        self.filler_16.setFrameShape(QFrame.StyledPanel)
        self.filler_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_72.addWidget(self.filler_16)

        self.slider_16 = QFrame(self.Orbit_Visualization_5)
        self.slider_16.setObjectName(u"slider_16")
        self.slider_16.setMinimumSize(QSize(446, 80))
        self.slider_16.setMaximumSize(QSize(230, 200))
        self.slider_16.setStyleSheet(u"background-color: rgba(0, 0, 0,60%);\n"
"image:none;\n"
"border:none;")
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
"\n"
"border:none;\n"
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
        self.semi_major_axis_toggle_menu_lbl_9.setFont(font8)
        self.semi_major_axis_toggle_menu_lbl_9.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
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
        self.label_5.setFont(font9)
        self.label_5.setFocusPolicy(Qt.NoFocus)
        self.label_5.setStyleSheet(u"color:grey;")
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
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
        self.semi_major_axis_toggle_menu_lbl_10.setFont(font8)
        self.semi_major_axis_toggle_menu_lbl_10.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
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
        self.label_6.setFont(font9)
        self.label_6.setFocusPolicy(Qt.NoFocus)
        self.label_6.setStyleSheet(u"color:grey;")
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
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
        self.semi_major_axis_toggle_menu_lbl_11.setFont(font8)
        self.semi_major_axis_toggle_menu_lbl_11.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
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
        self.label_13.setFont(font9)
        self.label_13.setFocusPolicy(Qt.NoFocus)
        self.label_13.setStyleSheet(u"color:grey;")
        self.label_13.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy3)
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
        self.semi_major_axis_toggle_menu_lbl_5.setFont(font13)
        self.semi_major_axis_toggle_menu_lbl_5.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
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
        sizePolicy3.setHeightForWidth(self.frame_95.sizePolicy().hasHeightForWidth())
        self.frame_95.setSizePolicy(sizePolicy3)
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
        self.semi_major_axis_toggle_menu_lbl_6.setFont(font13)
        self.semi_major_axis_toggle_menu_lbl_6.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
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
        font17 = QFont()
        font17.setPointSize(14)
        font17.setBold(True)
        font17.setWeight(75)
        self.semi_major_axis_toggle_menu_lbl_7.setFont(font17)
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
        sizePolicy3.setHeightForWidth(self.frame_96.sizePolicy().hasHeightForWidth())
        self.frame_96.setSizePolicy(sizePolicy3)
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
        self.semi_major_axis_toggle_menu_lbl_8.setFont(font13)
        self.semi_major_axis_toggle_menu_lbl_8.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
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
        sizePolicy3.setHeightForWidth(self.frame_138.sizePolicy().hasHeightForWidth())
        self.frame_138.setSizePolicy(sizePolicy3)
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
        self.semi_major_axis_toggle_menu_lbl_12.setFont(font13)
        self.semi_major_axis_toggle_menu_lbl_12.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
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
        sizePolicy3.setHeightForWidth(self.frame_152.sizePolicy().hasHeightForWidth())
        self.frame_152.setSizePolicy(sizePolicy3)
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
        self.semi_major_axis_toggle_menu_lbl_13.setFont(font13)
        self.semi_major_axis_toggle_menu_lbl_13.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
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
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	border:2px solid white;}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_6)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.upper_content_holder_frame_planetary_ephi = QFrame(self.frame_6)
        self.upper_content_holder_frame_planetary_ephi.setObjectName(u"upper_content_holder_frame_planetary_ephi")
        self.upper_content_holder_frame_planetary_ephi.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"background-color:none;}")
        self.upper_content_holder_frame_planetary_ephi.setFrameShape(QFrame.StyledPanel)
        self.upper_content_holder_frame_planetary_ephi.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.upper_content_holder_frame_planetary_ephi)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.frame_13 = QFrame(self.upper_content_holder_frame_planetary_ephi)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame{\n"
"background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_13)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.frame_10 = QFrame(self.frame_13)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(375, 0))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	border:2px solid white;}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.SOI_planet_name_2 = QComboBox(self.frame_10)
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

        self.verticalLayout_12.addWidget(self.SOI_planet_name_2, 0, Qt.AlignHCenter)

        self.scrollArea_4 = QScrollArea(self.frame_10)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}\n"
"QSrollArea{\n"
"border:none;}\n"
"\n"
"/*Vertical Scrollbar*/\n"
"QScrollBar:vertical{\n"
"border:none;\n"
"background-color:white;\n"
"width:8px;\n"
"margin: 15px 0 15px 0;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"/* Handle Bar Vertical */\n"
"QScrollBar::handle:vertical{\n"
"background-color: white;\n"
"min-height: 30px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vetical:hover{\n"
"background-color: white;\n"
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
"background-color: none;\n"
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
"background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* "
                        "BTN BOTTOM - Scrollbar*/\n"
"QScrollBar::add-line:vertical{\n"
"border:none;\n"
"background-color:none;\n"
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
"background: transparent;\n"
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
"/* Handle Bar Horizontal */\n"
"QScrollBar::handle:horizontal{\n"
"b"
                        "ackground-color: rgb(80, 80, 122);\n"
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
"subcontrol-position: bottom;\n"
"subcontrol-origin: mar"
                        "gin;\n"
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
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 336, 422))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(6, 6, 6, 6)
        self.frame_16 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(320, 250))
        self.frame_16.setMaximumSize(QSize(330, 250))
        self.frame_16.setStyleSheet(u"QFrame{\n"
"\n"
"border: transparent;\n"
"border-radius: 15px;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(168, 128, 243, 255), stop:1 rgba(108, 121, 240, 255));\n"
"\n"
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
        self.calendarWidget_PE = QCalendarWidget(self.frame_16)
        self.calendarWidget_PE.setObjectName(u"calendarWidget_PE")
        self.calendarWidget_PE.setMinimumSize(QSize(310, 200))
        self.calendarWidget_PE.setMaximumSize(QSize(320, 205))
        self.calendarWidget_PE.setStyleSheet(u"\n"
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
"	border:2px solid black;\n"
"	border-radius:4px;\n"
"}")

        self.verticalLayout_10.addWidget(self.calendarWidget_PE)


        self.verticalLayout_18.addWidget(self.frame_16)

        self.Date_time_frame_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.Date_time_frame_2.setObjectName(u"Date_time_frame_2")
        sizePolicy1.setHeightForWidth(self.Date_time_frame_2.sizePolicy().hasHeightForWidth())
        self.Date_time_frame_2.setSizePolicy(sizePolicy1)
        self.Date_time_frame_2.setMinimumSize(QSize(320, 150))
        self.Date_time_frame_2.setMaximumSize(QSize(330, 150))
        self.Date_time_frame_2.setFont(font3)
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
        self.label_136 = QLabel(self.Date_time_frame_2)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(160, 60, 101, 16))
        self.label_136.setFont(font4)
        self.label_136.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.PE_Cal_Btn = QPushButton(self.Date_time_frame_2)
        self.PE_Cal_Btn.setObjectName(u"PE_Cal_Btn")
        self.PE_Cal_Btn.setGeometry(QRect(90, 100, 151, 31))
        self.PE_Cal_Btn.setFont(font6)
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
        self.frame_19 = QFrame(self.Date_time_frame_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(30, 20, 271, 44))
        self.frame_19.setStyleSheet(u"background-color:none;\n"
"border:none;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_107.setSpacing(10)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(10, 0, 0, 0)
        self.label_110 = QLabel(self.frame_19)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setFont(font4)
        self.label_110.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")

        self.horizontalLayout_107.addWidget(self.label_110)

        self.timeEdit_PE = QTimeEdit(self.frame_19)
        self.timeEdit_PE.setObjectName(u"timeEdit_PE")
        self.timeEdit_PE.setMinimumSize(QSize(110, 30))
        self.timeEdit_PE.setFont(font3)
        self.timeEdit_PE.setStyleSheet(u"    /*spinbox lift style*/\n"
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
        self.timeEdit_PE.setAlignment(Qt.AlignCenter)
        self.timeEdit_PE.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.timeEdit_PE.setCurrentSection(QDateTimeEdit.HourSection)

        self.horizontalLayout_107.addWidget(self.timeEdit_PE)

        self.label_135 = QLabel(self.frame_19)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMaximumSize(QSize(40, 16777215))
        self.label_135.setFont(font4)
        self.label_135.setStyleSheet(u"border: none;\n"
"color: white;\n"
"background:none;")
        self.label_135.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_107.addWidget(self.label_135)


        self.verticalLayout_18.addWidget(self.Date_time_frame_2)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_12.addWidget(self.scrollArea_4)


        self.verticalLayout_109.addWidget(self.frame_10)


        self.horizontalLayout_86.addWidget(self.frame_13)

        self.frame_34 = QFrame(self.upper_content_holder_frame_planetary_ephi)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_34)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.frame_48 = QFrame(self.frame_34)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	image:url(UI_Functions/Resources/SOI.png);\n"
"	border:2px solid white;\n"
"}")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)

        self.verticalLayout_102.addWidget(self.frame_48)

        self.frame_191 = QFrame(self.frame_34)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setStyleSheet(u"QFrame{\n"
"	background-color:#1b1b1b;\n"
"	border:2px solid white;\n"
"}")
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_191)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(20, 20, 20, -1)
        self.frame_192 = QFrame(self.frame_191)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setMinimumSize(QSize(200, 30))
        self.frame_192.setMaximumSize(QSize(200, 30))
        self.frame_192.setStyleSheet(u"\n"
"QFrame{\n"
"	\n"
"	background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(78, 79, 132, 60%), stop:1 rgba(161, 161, 161, 60%));\n"
"	\n"
"\n"
"}")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_192)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.semi_major_axis_toggle_menu_lbl_16 = QLabel(self.frame_192)
        self.semi_major_axis_toggle_menu_lbl_16.setObjectName(u"semi_major_axis_toggle_menu_lbl_16")
        self.semi_major_axis_toggle_menu_lbl_16.setMinimumSize(QSize(0, 20))
        self.semi_major_axis_toggle_menu_lbl_16.setMaximumSize(QSize(16777215, 20))
        self.semi_major_axis_toggle_menu_lbl_16.setFont(font8)
        self.semi_major_axis_toggle_menu_lbl_16.setStyleSheet(u"QLabel{\n"
"color: rgba(131, 255, 160, 80%);\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.semi_major_axis_toggle_menu_lbl_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_104.addWidget(self.semi_major_axis_toggle_menu_lbl_16, 0, Qt.AlignHCenter)


        self.verticalLayout_103.addWidget(self.frame_192, 0, Qt.AlignHCenter)

        self.label_34 = QLabel(self.frame_191)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font9)
        self.label_34.setFocusPolicy(Qt.NoFocus)
        self.label_34.setStyleSheet(u"color:grey;\n"
"border:none;")
        self.label_34.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_34.setWordWrap(True)

        self.verticalLayout_103.addWidget(self.label_34)


        self.verticalLayout_102.addWidget(self.frame_191)


        self.horizontalLayout_86.addWidget(self.frame_34)


        self.verticalLayout_108.addWidget(self.upper_content_holder_frame_planetary_ephi)

        self.Bottom_slider_PE_Output = QFrame(self.frame_6)
        self.Bottom_slider_PE_Output.setObjectName(u"Bottom_slider_PE_Output")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Bottom_slider_PE_Output.sizePolicy().hasHeightForWidth())
        self.Bottom_slider_PE_Output.setSizePolicy(sizePolicy4)
        self.Bottom_slider_PE_Output.setMinimumSize(QSize(0, 200))
        self.Bottom_slider_PE_Output.setMaximumSize(QSize(16878, 200))
        self.Bottom_slider_PE_Output.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: #f4717f;\n"
"	\n"
"\n"
"}")
        self.Bottom_slider_PE_Output.setFrameShape(QFrame.StyledPanel)
        self.Bottom_slider_PE_Output.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.Bottom_slider_PE_Output)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(22, -1, 22, -1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(4)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setContentsMargins(4, 4, -1, 4)
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
        self.frame_110.setStyleSheet(u"background-color:  white;\n"
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
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_153.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_170.addWidget(self.label_153, 0, Qt.AlignVCenter)


        self.horizontalLayout_169.addWidget(self.frame_110, 0, Qt.AlignVCenter)

        self.frame_111 = QFrame(self.widget_27)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setStyleSheet(u"background-color:  white;\n"
"border-radius:8px;")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_171 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_171.setSpacing(4)
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.horizontalLayout_171.setContentsMargins(4, 4, 0, 4)
        self.label_154 = QLabel(self.frame_111)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setMaximumSize(QSize(75, 16777215))
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
        self.label_155.setMaximumSize(QSize(58, 16777215))
        self.label_155.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
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
        self.frame_120.setStyleSheet(u"background-color:white;\n"
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
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_168.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_185.addWidget(self.label_168)


        self.horizontalLayout_184.addWidget(self.frame_120, 0, Qt.AlignVCenter)

        self.frame_121 = QFrame(self.widget_32)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setStyleSheet(u"background-color: white;\n"
"border-radius:8px;\n"
"")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_186 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_186.setSpacing(4)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(4, 4, 0, 4)
        self.label_169 = QLabel(self.frame_121)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setMaximumSize(QSize(75, 1658758))
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
        self.label_170.setMinimumSize(QSize(54, 0))
        self.label_170.setMaximumSize(QSize(52, 16777215))
        self.label_170.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
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
        self.frame_106.setStyleSheet(u"background-color:  white;\n"
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
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_147.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_164.addWidget(self.label_147, 0, Qt.AlignVCenter)


        self.horizontalLayout_163.addWidget(self.frame_106, 0, Qt.AlignVCenter)

        self.frame_107 = QFrame(self.widget_25)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setStyleSheet(u"background-color: white;\n"
"border-radius:8px;")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_165 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_165.setSpacing(6)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalLayout_165.setContentsMargins(4, 4, 0, 4)
        self.label_148 = QLabel(self.frame_107)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMaximumSize(QSize(75, 16777215))
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
        self.label_149.setMinimumSize(QSize(54, 0))
        self.label_149.setMaximumSize(QSize(52, 16777215))
        self.label_149.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
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
        self.frame_100.setStyleSheet(u"background-color:  white;\n"
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
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_138.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_153.addWidget(self.label_138, 0, Qt.AlignVCenter)


        self.horizontalLayout_152.addWidget(self.frame_100, 0, Qt.AlignVCenter)

        self.frame_101 = QFrame(self.widget_22)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setStyleSheet(u"background-color:  white;\n"
"border-radius:8px;")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(4, 4, 0, 4)
        self.label_139 = QLabel(self.frame_101)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMaximumSize(QSize(75, 16777215))
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
        self.label_140.setMinimumSize(QSize(54, 0))
        self.label_140.setMaximumSize(QSize(52, 16777215))
        self.label_140.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
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
        self.frame_122.setStyleSheet(u"background-color:  white;\n"
"border-radius:8px;")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_188 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_188.setContentsMargins(2, 2, 2, 2)
        self.label_171 = QLabel(self.frame_122)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMinimumSize(QSize(125, 20))
        self.label_171.setMaximumSize(QSize(140, 20))
        self.label_171.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_171.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_188.addWidget(self.label_171, 0, Qt.AlignVCenter)


        self.horizontalLayout_187.addWidget(self.frame_122, 0, Qt.AlignVCenter)

        self.frame_123 = QFrame(self.widget_33)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setStyleSheet(u"background-color:  white;\n"
"border-radius:8px;")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_189 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_189.setSpacing(4)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_189.setContentsMargins(4, 4, 0, 4)
        self.label_172 = QLabel(self.frame_123)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMaximumSize(QSize(75, 16777215))
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
        self.label_173.setMaximumSize(QSize(58, 16777215))
        self.label_173.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
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
        self.frame_104.setStyleSheet(u"background-color: white;\n"
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
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_144.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_161.addWidget(self.label_144, 0, Qt.AlignVCenter)


        self.horizontalLayout_160.addWidget(self.frame_104, 0, Qt.AlignVCenter)

        self.frame_105 = QFrame(self.widget_24)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setStyleSheet(u"background-color:  white;\n"
"border-radius:8px;")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_162 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_162.setSpacing(4)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalLayout_162.setContentsMargins(4, 4, 0, 4)
        self.label_145 = QLabel(self.frame_105)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMaximumSize(QSize(75, 16777215))
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
        self.label_146.setMaximumSize(QSize(58, 16777215))
        self.label_146.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
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
        self.frame_114.setStyleSheet(u"background-color:  white;\n"
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
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_159.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_176.addWidget(self.label_159, 0, Qt.AlignVCenter)


        self.horizontalLayout_175.addWidget(self.frame_114, 0, Qt.AlignVCenter)

        self.frame_115 = QFrame(self.widget_29)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setStyleSheet(u"background-color:  white;\n"
"border-radius:8px;")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_177 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_177.setSpacing(4)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(4, 4, 0, 4)
        self.label_160 = QLabel(self.frame_115)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMaximumSize(QSize(75, 16777215))
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
        self.label_161.setMinimumSize(QSize(56, 0))
        self.label_161.setMaximumSize(QSize(52, 16777215))
        self.label_161.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
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
        self.frame_102.setStyleSheet(u"background-color: white;\n"
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
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_141.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.label_141, 0, Qt.AlignVCenter)


        self.horizontalLayout_155.addWidget(self.frame_102, 0, Qt.AlignVCenter)

        self.frame_103 = QFrame(self.widget_23)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setStyleSheet(u"background-color:  white;\n"
"border-radius:8px;")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_157 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(4, 4, 0, 4)
        self.label_142 = QLabel(self.frame_103)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMaximumSize(QSize(75, 16777215))
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
        self.label_143.setMinimumSize(QSize(54, 0))
        self.label_143.setMaximumSize(QSize(52, 16777215))
        self.label_143.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
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
        self.frame_108.setStyleSheet(u"background-color:  white;\n"
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
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:16px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_150.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_167.addWidget(self.label_150, 0, Qt.AlignVCenter)


        self.horizontalLayout_166.addWidget(self.frame_108, 0, Qt.AlignVCenter)

        self.frame_109 = QFrame(self.widget_26)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setStyleSheet(u"background-color:  white;\n"
"border-radius:8px;")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_168 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_168.setSpacing(4)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(4, 4, 0, 4)
        self.label_151 = QLabel(self.frame_109)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMinimumSize(QSize(75, 0))
        self.label_151.setMaximumSize(QSize(75, 23))
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
        self.label_152.setMinimumSize(QSize(58, 0))
        self.label_152.setMaximumSize(QSize(52, 16777215))
        self.label_152.setStyleSheet(u"QLabel{\n"
"	\n"
"	/*border:2px solid rgb(78, 79, 132);\n"
"	/*border-radius:15px;*/\n"
"	border:none;\n"
"	color:#04ae92;\n"
"	/*background-color: rgb(94, 96, 159);*/\n"
"	background-color: transparent;\n"
"	font-size:14px;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"	\n"
"}")
        self.label_152.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_168.addWidget(self.label_152)


        self.horizontalLayout_166.addWidget(self.frame_109)


        self.gridLayout_4.addWidget(self.widget_26, 1, 1, 1, 1)


        self.verticalLayout_71.addLayout(self.gridLayout_4)


        self.verticalLayout_108.addWidget(self.Bottom_slider_PE_Output)


        self.horizontalLayout_73.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.Planetary_Ephemeris)
        self.Incomplete_Features = QWidget()
        self.Incomplete_Features.setObjectName(u"Incomplete_Features")
        self.horizontalLayout_150 = QHBoxLayout(self.Incomplete_Features)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(6, 0, 6, 0)
        self.frame_134 = QFrame(self.Incomplete_Features)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setStyleSheet(u"background-color: rgb(78, 79, 132);\n"
"border:2px solid white;")
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_134)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_134)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(800, 100))
        self.label_14.setMaximumSize(QSize(800, 100))
        font18 = QFont()
        font18.setPointSize(26)
        self.label_14.setFont(font18)
        self.label_14.setStyleSheet(u"background-color:#36375c;")
        self.label_14.setScaledContents(False)

        self.verticalLayout_92.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.horizontalLayout_150.addWidget(self.frame_134)

        self.stackedWidget.addWidget(self.Incomplete_Features)

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
        font19 = QFont()
        font19.setFamily(u"Arial")
        font19.setPointSize(6)
        font19.setBold(False)
        font19.setItalic(False)
        font19.setWeight(50)
        self.label_credits.setFont(font19)
        self.label_credits.setStyleSheet(u"")
        self.label_credits.setPixmap(QPixmap(u"C:/Users/manjunath neelmath/.designer/backup/Users/manjunath neelmath/.designer/backup/GUI-test/Resources/MOPy Cover_transparent.png"))
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
        self.a_and_e_graph_VPCO.setCurrentIndex(0)
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
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"    MOPy ", None))
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
        self.Home_VPCO_Label.setText(QCoreApplication.translate("MainWindow", u"Various Parameters and Constants of an orbit", None))
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

        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Time:", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"UT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Digits of Accuracy:", None))
        self.calculate_btn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Julian Days", None))
        self.JulianDay_Result.setText(QCoreApplication.translate("MainWindow", u"12500.00", None))
        self.Error_state.setText("")
        self.semi_major_axis_toggle_menu_lbl_17.setText(QCoreApplication.translate("MainWindow", u"Julian Days", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"The Bi-Elliptical Hohmann Transfer(BEHT) uses two coaxial semi ellipses which extend beyond the outer target orbit. Each of the two ellipses is tangent to the one of the orbits (initial and final) and are tangent to each other too. This is usually done so that the point B is placed sufficiently far from the focus that the DeltaV will be very small. This is suitable when the deltaV_(BEHT) < deltaV_(HT). ", None))
        self.semi_major_axis_toggle_menu_lbl_15.setText(QCoreApplication.translate("MainWindow", u"Sphere of Influence", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"The Bi-Elliptical Hohmann Transfer(BEHT) uses two coaxial semi ellipses which extend beyond the outer target orbit. Each of the two ellipses is tangent to the one of the orbits (initial and final) and are tangent to each other too. This is usually done so that the point B is placed sufficiently far from the focus that the DeltaV will be very small. This is suitable when the deltaV_(BEHT) < deltaV_(HT). ", None))
        self.SOI_planet_name.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Major Body", None))
        self.SOI_planet_name.setItemText(1, QCoreApplication.translate("MainWindow", u"  Earth", None))
        self.SOI_planet_name.setItemText(2, QCoreApplication.translate("MainWindow", u"  Jupiter", None))
        self.SOI_planet_name.setItemText(3, QCoreApplication.translate("MainWindow", u"  Mercury", None))
        self.SOI_planet_name.setItemText(4, QCoreApplication.translate("MainWindow", u"  Venus", None))
        self.SOI_planet_name.setItemText(5, QCoreApplication.translate("MainWindow", u"  Mars", None))
        self.SOI_planet_name.setItemText(6, QCoreApplication.translate("MainWindow", u"  Saturn", None))
        self.SOI_planet_name.setItemText(7, QCoreApplication.translate("MainWindow", u"  Uranus", None))
        self.SOI_planet_name.setItemText(8, QCoreApplication.translate("MainWindow", u"  Neptune", None))
        self.SOI_planet_name.setItemText(9, QCoreApplication.translate("MainWindow", u"  Pluto", None))
        self.SOI_planet_name.setItemText(10, QCoreApplication.translate("MainWindow", u"  Other", None))

        self.Planet_name_display.setText(QCoreApplication.translate("MainWindow", u"Mars", None))
        self.Mass_of_the_Body_SOI.setText(QCoreApplication.translate("MainWindow", u"Mass of the Body", None))
        self.Mass_of_planet_SOI.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Kg", None))
        self.Dist_from_the_sun_SOI.setText(QCoreApplication.translate("MainWindow", u"Distance from the Sun", None))
        self.dist_from_sun_SOI.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dist_from_sun_unit_SOI.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.soi_cal.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Radius of Sphere of Influence", None))
        self.rSOI_of_planet_lbl.setText(QCoreApplication.translate("MainWindow", u"39358.61", None))
        self.SOI_unit.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.get_3D_soi.setText(QCoreApplication.translate("MainWindow", u"Get 3D Visualization", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Semi-major axis", None))
        self.VPCO_Input_a_lineedit.setText("")
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.Semi_maj_ax_err_label.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
        self.VPCO_Input_e_lineedit.setText("")
        self.label_116.setText("")
        self.Eccentricity_err_label.setText("")
        self.Maj_Body__Drop_VPCO.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Major Body", None))
        self.Maj_Body__Drop_VPCO.setItemText(1, QCoreApplication.translate("MainWindow", u"  Moon", None))
        self.Maj_Body__Drop_VPCO.setItemText(2, QCoreApplication.translate("MainWindow", u"  Earth", None))
        self.Maj_Body__Drop_VPCO.setItemText(3, QCoreApplication.translate("MainWindow", u"  Jupiter", None))
        self.Maj_Body__Drop_VPCO.setItemText(4, QCoreApplication.translate("MainWindow", u"  Mercury", None))
        self.Maj_Body__Drop_VPCO.setItemText(5, QCoreApplication.translate("MainWindow", u"  Venus", None))
        self.Maj_Body__Drop_VPCO.setItemText(6, QCoreApplication.translate("MainWindow", u"  Mars", None))
        self.Maj_Body__Drop_VPCO.setItemText(7, QCoreApplication.translate("MainWindow", u"  Saturn", None))
        self.Maj_Body__Drop_VPCO.setItemText(8, QCoreApplication.translate("MainWindow", u"  Uranus", None))
        self.Maj_Body__Drop_VPCO.setItemText(9, QCoreApplication.translate("MainWindow", u"  Neptune", None))
        self.Maj_Body__Drop_VPCO.setItemText(10, QCoreApplication.translate("MainWindow", u"  Pluto", None))
        self.Maj_Body__Drop_VPCO.setItemText(11, QCoreApplication.translate("MainWindow", u"  Other", None))

        self.VPCO_Submit_button.setText(QCoreApplication.translate("MainWindow", u"Plot Orbit", None))
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
        self.semi_major_axis_toggle_menu_lbl_14.setText(QCoreApplication.translate("MainWindow", u"Various Parameters of an Orbit", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"The Bi-Elliptical Hohmann Transfer(BEHT) uses two coaxial semi ellipses which extend beyond the outer target orbit. Each of the two ellipses is tangent to the one of the orbits (initial and final) and are tangent to each other too. This is usually done so that the point B is placed sufficiently far from the focus that the DeltaV will be very small. This is suitable when the deltaV_(BEHT) < deltaV_(HT). ", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Radius of Periapsis", None))
        self.VPCO_Radius_of_Peri_Label.setText(QCoreApplication.translate("MainWindow", u"12500.00", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Velocity at Periapsis", None))
        self.VPCO_Velocity_at_Periapis_Label.setText(QCoreApplication.translate("MainWindow", u"6.91", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Semi-latus Rectum", None))
        self.VPCO_Semi_latus_Rectum_Label.setText(QCoreApplication.translate("MainWindow", u"18750.00", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.VPCO_Time_Period_Label.setText(QCoreApplication.translate("MainWindow", u"39358.61", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Vel. at Semi-latus Rectum", None))
        self.VPCO_Vel_at_Semi_latus_re_Label.setText(QCoreApplication.translate("MainWindow", u"5.15", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Esc. Velocity at Periapsis", None))
        self.VPCO_Esc_Velocity_at_Periapsis_Label.setText(QCoreApplication.translate("MainWindow", u"7.98", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Esc. Velocity at Apoapsis", None))
        self.VPCO_Esc_Velocity_at_Apoapsis_Label.setText(QCoreApplication.translate("MainWindow", u"4.61", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Radius of Apoapsis", None))
        self.VPCO_Radius_of_Apo_Label.setText(QCoreApplication.translate("MainWindow", u"37500.00", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Sp. Mechanical Energy", None))
        self.VPCO_Sp_Mech_Energy_Label.setText(QCoreApplication.translate("MainWindow", u"-7.96", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"J/Kg", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Sp. Angular Momentum", None))
        self.VPCO_Sp_Angular_Mome_Label.setText(QCoreApplication.translate("MainWindow", u"39358.61", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Km^2/s", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Mean Motion", None))
        self.VPCO_Mean_Motion_Label.setText(QCoreApplication.translate("MainWindow", u"6264.12", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"rad/s", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Velocity at Apoapsis", None))
        self.VPCO_Velocity_of_Apoapsis_Label.setText(QCoreApplication.translate("MainWindow", u"2.30", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
        self.VPCO_tabs.setTabText(self.VPCO_tabs.indexOf(self.a_and_e_tab), QCoreApplication.translate("MainWindow", u"Semi-major axis and Eccentricity", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Radius of Periapsis", None))
        self.VPCO_Input_a_lineedit_2.setText("")
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Radius of Apoapsis", None))
        self.VPCO_Input_e_lineedit_2.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.maj_body_CoOE_3.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select the Major Body", None))
        self.maj_body_CoOE_3.setItemText(1, QCoreApplication.translate("MainWindow", u"  Moon", None))
        self.maj_body_CoOE_3.setItemText(2, QCoreApplication.translate("MainWindow", u"  Earth", None))
        self.maj_body_CoOE_3.setItemText(3, QCoreApplication.translate("MainWindow", u"  Jupiter", None))
        self.maj_body_CoOE_3.setItemText(4, QCoreApplication.translate("MainWindow", u"  Mercury", None))
        self.maj_body_CoOE_3.setItemText(5, QCoreApplication.translate("MainWindow", u"  Venus", None))
        self.maj_body_CoOE_3.setItemText(6, QCoreApplication.translate("MainWindow", u"  Mars", None))
        self.maj_body_CoOE_3.setItemText(7, QCoreApplication.translate("MainWindow", u"  Saturn", None))
        self.maj_body_CoOE_3.setItemText(8, QCoreApplication.translate("MainWindow", u"  Uranus", None))
        self.maj_body_CoOE_3.setItemText(9, QCoreApplication.translate("MainWindow", u"  Neptune", None))
        self.maj_body_CoOE_3.setItemText(10, QCoreApplication.translate("MainWindow", u"  Pluto", None))
        self.maj_body_CoOE_3.setItemText(11, QCoreApplication.translate("MainWindow", u"  Other", None))

        self.VPCO_Submit_button_2.setText(QCoreApplication.translate("MainWindow", u"Plot Orbital Transfer", None))
        self.VPCO_tabs.setTabText(self.VPCO_tabs.indexOf(self.ra_and_rp), QCoreApplication.translate("MainWindow", u"Radius of Periapsis and Radius of Apoapsis", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Position Vector", None))
        self.Ri_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"8250", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Rj_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"390", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"j", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Rk_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"6900", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"Velocity Vector", None))
        self.Vi_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"-0.7", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Vj_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"6.6", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"j", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Vk_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"-0.6", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"Km/s", None))
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

        self.Planet_name_display_COEnAOE.setText(QCoreApplication.translate("MainWindow", u"Mars", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Mass of the Body", None))
        self.Body_mass_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"Kg", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Radius of the Body", None))
        self.Body_radius_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.cal_btn_coe_n_aoe.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.semi_major_axis_toggle_menu_lbl_18.setText(QCoreApplication.translate("MainWindow", u"Sphere of Influence", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"The Bi-Elliptical Hohmann Transfer(BEHT) uses two coaxial semi ellipses which extend beyond the outer target orbit. Each of the two ellipses is tangent to the one of the orbits (initial and final) and are tangent to each other too. This is usually done so that the point B is placed sufficiently far from the focus that the DeltaV will be very small. This is suitable when the deltaV_(BEHT) < deltaV_(HT). ", None))
        self.CoOE_output_lbl_error.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Inclination", None))
        self.inclination_coe_n_aoe.setText("")
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RAAN", None))
        self.RAAN_coe_n_aoe.setText("")
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Arguement of Perapsis", None))
        self.arg_of_per_coe_n_aoe.setText("")
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"True Anomaly", None))
        self.tru_ana_coe_n_aoe.setText("")
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Semi-major Axis", None))
        self.semimajor_axis_coe_n_aoe.setText("")
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Eccentricity", None))
        self.eccentricity_coe_n_aoe.setText("")
        self.label_216.setText("")
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

        self.label_136.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.PE_Cal_Btn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Select Time:", None))
        self.timeEdit_PE.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"UT", None))
        self.semi_major_axis_toggle_menu_lbl_16.setText(QCoreApplication.translate("MainWindow", u"Planetary Ephemeris", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"The Bi-Elliptical Hohmann Transfer(BEHT) uses two coaxial semi ellipses which extend beyond the outer target orbit. Each of the two ellipses is tangent to the one of the orbits (initial and final) and are tangent to each other too. This is usually done so that the point B is placed sufficiently far from the focus that the DeltaV will be very small. This is suitable when the deltaV_(BEHT) < deltaV_(HT). ", None))
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
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Argt. of Periheilion", None))
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
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Coming Soon...", None))
        self.label_credits.setText("")
    # retranslateUi

