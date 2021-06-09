# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home_PageuWorET.ui'
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
        MainWindow.resize(1108, 663)
        MainWindow.setMinimumSize(QSize(750, 0))
        MainWindow.setMaximumSize(QSize(1108, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(50, 47, 111, 255), stop:0.488636 rgba(28, 30, 72, 255));\n"
"border-radius: 15px")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
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
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(25, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_10)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(35, 0))
        self.frame_27.setMaximumSize(QSize(35, 16777215))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_27)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Home_btn = QPushButton(self.frame_27)
        self.Home_btn.setObjectName(u"Home_btn")
        self.Home_btn.setMinimumSize(QSize(0, 36))
        self.Home_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px;\n"
"	image:url(UI_Functions/Resources/Home_btn.png);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 0.2em 0.2em 0.2em 0.2em;\n"
"	\n"
"}")

        self.verticalLayout_2.addWidget(self.Home_btn)


        self.verticalLayout_3.addWidget(self.frame_27)


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
"")

        self.horizontalLayout_14.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(0, 40))
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamily(u"MS Serif")
        self.frame_btns.setFont(font2)
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(40, 20, 18, 18))
        self.btn_minimize.setMinimumSize(QSize(18, 18))
        self.btn_minimize.setMaximumSize(QSize(11, 11))
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
"}")
        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(70, 20, 18, 18))
        self.btn_close.setMinimumSize(QSize(18, 18))
        self.btn_close.setMaximumSize(QSize(12, 12))
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
"")

        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: None")
        self.content_bar.setFrameShape(QFrame.NoFrame)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content_bar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color:none")
        self.Home_Page_Screen = QWidget()
        self.Home_Page_Screen.setObjectName(u"Home_Page_Screen")
        self.verticalLayout_4 = QVBoxLayout(self.Home_Page_Screen)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.Home_Page_Screen)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.NoFrame)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_content_home)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_15)

        self.frame_17 = QFrame(self.frame_content_home)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 310))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Search_logo_frame = QFrame(self.frame_17)
        self.Search_logo_frame.setObjectName(u"Search_logo_frame")
        self.Search_logo_frame.setMinimumSize(QSize(380, 300))
        self.Search_logo_frame.setMaximumSize(QSize(380, 400))
        self.Search_logo_frame.setFrameShape(QFrame.StyledPanel)
        self.Search_logo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Search_logo_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 1)
        self.Search_logo = QLabel(self.Search_logo_frame)
        self.Search_logo.setObjectName(u"Search_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search_logo.sizePolicy().hasHeightForWidth())
        self.Search_logo.setSizePolicy(sizePolicy)
        self.Search_logo.setMinimumSize(QSize(350, 250))
        self.Search_logo.setMaximumSize(QSize(390, 300))
        self.Search_logo.setStyleSheet(u"")
        self.Search_logo.setPixmap(QPixmap(u"UI_Functions/Resources/MOPy Cover_transparent.png"))
        self.Search_logo.setScaledContents(True)
        self.Search_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.Search_logo)


        self.horizontalLayout_4.addWidget(self.Search_logo_frame)


        self.verticalLayout_7.addWidget(self.frame_17)

        self.search_frame = QFrame(self.frame_content_home)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setEnabled(True)
        self.search_frame.setMaximumSize(QSize(16777215, 200))
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.search_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Search_combo_frame = QFrame(self.search_frame)
        self.Search_combo_frame.setObjectName(u"Search_combo_frame")
        self.Search_combo_frame.setMinimumSize(QSize(0, 40))
        self.Search_combo_frame.setMaximumSize(QSize(16777215, 40))
        self.Search_combo_frame.setFrameShape(QFrame.NoFrame)
        self.Search_combo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Search_combo_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 1, -1, 150)
        self.combosearchbox = QComboBox(self.Search_combo_frame)
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.addItem("")
        self.combosearchbox.setObjectName(u"combosearchbox")
        self.combosearchbox.setMinimumSize(QSize(533, 35))
        self.combosearchbox.setMaximumSize(QSize(533, 35))
        self.combosearchbox.setFocusPolicy(Qt.NoFocus)
        self.combosearchbox.setStyleSheet(u"QComboBox{\n"
"	border: 5px solid rgb(255, 170, 0);\n"
"	font: 12pt \"Arial\";\n"
"	border-radius: 17px;}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: 4px solid rgb(2, 119, 189);\n"
"}")

        self.horizontalLayout_5.addWidget(self.combosearchbox)


        self.verticalLayout_6.addWidget(self.Search_combo_frame)

        self.Go_btn_frame = QFrame(self.search_frame)
        self.Go_btn_frame.setObjectName(u"Go_btn_frame")
        self.Go_btn_frame.setMinimumSize(QSize(0, 50))
        self.Go_btn_frame.setMaximumSize(QSize(16777215, 50))
        self.Go_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.Go_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Go_btn_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.Go_btn_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.Go_btn_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(167, 300))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Go_btn = QPushButton(self.frame_3)
        self.Go_btn.setObjectName(u"Go_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Go_btn.sizePolicy().hasHeightForWidth())
        self.Go_btn.setSizePolicy(sizePolicy1)
        self.Go_btn.setMinimumSize(QSize(150, 40))
        self.Go_btn.setMaximumSize(QSize(200, 40))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setWeight(50)
        self.Go_btn.setFont(font3)
        self.Go_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}")

        self.verticalLayout_13.addWidget(self.Go_btn)


        self.horizontalLayout_8.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.Go_btn_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.Go_btn_frame)


        self.verticalLayout_7.addWidget(self.search_frame)

        self.frame_16 = QFrame(self.frame_content_home)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_16)


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
"}")

        self.verticalLayout_9.addWidget(self.type_of_calendar)


        self.horizontalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame_18 = QFrame(self.frame_content_Julian_calculation)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 20))
        self.frame_18.setMaximumSize(QSize(16777215, 20))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_18)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_24)

        self.label_5 = QLabel(self.frame_18)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(1050, 0))
        self.label_5.setMaximumSize(QSize(1050, 16777215))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"border: none;\n"
"color: white;")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.frame_34 = QFrame(self.frame_18)
        self.frame_34.setObjectName(u"frame_34")
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
        font5 = QFont()
        font5.setPointSize(10)
        self.Error_state.setFont(font5)
        self.Error_state.setStyleSheet(u"color:rgb(255, 0, 0);")

        self.verticalLayout_17.addWidget(self.Error_state)


        self.horizontalLayout_7.addWidget(self.frame_34)


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
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Date_time_frame.sizePolicy().hasHeightForWidth())
        self.Date_time_frame.setSizePolicy(sizePolicy2)
        self.Date_time_frame.setMinimumSize(QSize(320, 250))
        self.Date_time_frame.setMaximumSize(QSize(340, 250))
        font6 = QFont()
        font6.setPointSize(15)
        self.Date_time_frame.setFont(font6)
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
        self.digits_accuracy.setGeometry(QRect(180, 120, 61, 31))
        self.digits_accuracy.setFont(font3)
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
        self.digits_accuracy.setMaximum(8)
        self.label = QLabel(self.Date_time_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 111, 16))
        self.label.setFont(font4)
        self.label.setStyleSheet(u"border: none;\n"
"color: white;")
        self.timeEdit = QTimeEdit(self.Date_time_frame)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(120, 30, 141, 31))
        self.timeEdit.setFont(font6)
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
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.label_2 = QLabel(self.Date_time_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 40, 41, 16))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"border: none;\n"
"color: white;")
        self.label_3 = QLabel(self.Date_time_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 70, 101, 16))
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: white;")
        self.label_4 = QLabel(self.Date_time_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 171, 31))
        self.label_4.setFont(font4)
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
"	border: 5px solid rgb(34, 14, 36);\n"
"	border-radius: 15px;\n"
"	color: white;\n"
"	background-color: rgb(34, 14, 36);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 3px solid white;\n"
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
        self.horizontalLayout_10 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_25)

        self.label_6 = QLabel(self.frame_20)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(1060, 0))
        self.label_6.setMaximumSize(QSize(700, 16777215))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"border: none;\n"
"color: white;")

        self.horizontalLayout_10.addWidget(self.label_6)


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
        self.frame_23.setFrameShape(QFrame.StyledPanel)
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
        self.label_7 = QLabel(self.frame_33)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 10, 61, 16))
        font8 = QFont()
        font8.setPointSize(11)
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"color: white;")

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
        self.label_8.setGeometry(QRect(190, 30, 171, 21))
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"color: white;\n"
"border:none;")
        self.lbl_mass = QLabel(self.frame_35)
        self.lbl_mass.setObjectName(u"lbl_mass")
        self.lbl_mass.setGeometry(QRect(20, 130, 141, 21))
        self.lbl_mass.setFont(font8)
        self.lbl_mass.setLayoutDirection(Qt.LeftToRight)
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
        self.SOI_planet_name.setGeometry(QRect(410, 20, 211, 41))
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
        self.lbl_dist_frm_sun.setGeometry(QRect(420, 130, 221, 21))
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
        self.get_mass = QPushButton(self.frame_35)
        self.get_mass.setObjectName(u"get_mass")
        self.get_mass.setGeometry(QRect(350, 70, 101, 41))
        font9 = QFont()
        font9.setPointSize(12)
        self.get_mass.setFont(font9)
        self.get_mass.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}")
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
        self.soi_cal = QPushButton(self.frame_35)
        self.soi_cal.setObjectName(u"soi_cal")
        self.soi_cal.setGeometry(QRect(350, 170, 101, 41))
        self.soi_cal.setFont(font9)
        self.soi_cal.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}")

        self.verticalLayout_18.addWidget(self.frame_35)


        self.verticalLayout_16.addWidget(self.frame_32)

        self.frame_26 = QFrame(self.SOI_frame_content)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 30))
        self.frame_26.setMaximumSize(QSize(16777215, 30))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_26)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(60, 10, 61, 16))
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"color: white;")

        self.verticalLayout_16.addWidget(self.frame_26)

        self.frame_28 = QFrame(self.SOI_frame_content)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(280, 0, 280, 0)
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
        self.pushButton = QPushButton(self.frame_36)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 100, 254, 41))
        self.pushButton.setFont(font9)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(2, 119, 189);\n"
"	color:rgb(245, 255, 179);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}")
        self.label_17 = QLabel(self.frame_36)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(470, 20, 111, 41))
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"color: white;\n"
"border:none;")
        self.label_18 = QLabel(self.frame_36)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 30, 181, 21))
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"color: white;\n"
"border:none;")
        self.soi_rad = QLabel(self.frame_36)
        self.soi_rad.setObjectName(u"soi_rad")
        self.soi_rad.setGeometry(QRect(220, 20, 241, 41))
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

        self.horizontalLayout_15.addWidget(self.frame_36)


        self.verticalLayout_16.addWidget(self.frame_28)


        self.horizontalLayout_17.addWidget(self.SOI_frame_content)

        self.stackedWidget.addWidget(self.SOI_Screen)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(0, 40))
        self.credits_bar.setMaximumSize(QSize(16777215, 40))
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
        font10 = QFont()
        font10.setFamily(u"Arial")
        font10.setPointSize(6)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.label_credits.setFont(font10)
        self.label_credits.setStyleSheet(u"image:url(UI_Functions/Resources/MOPy Cover_transparent.png);")
        self.label_credits.setPixmap(QPixmap(u"GUI-test/Resources/MOPy Cover_transparent.png"))
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


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.Home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
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
#if QT_CONFIG(tooltip)
        self.Search_logo_frame.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Search_logo.setText("")
#if QT_CONFIG(tooltip)
        self.Search_combo_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Click on drop down Button", None))
#endif // QT_CONFIG(tooltip)
        self.combosearchbox.setItemText(0, "")
        self.combosearchbox.setItemText(1, QCoreApplication.translate("MainWindow", u"    COE and AOE of an Orbit", None))
        self.combosearchbox.setItemText(2, QCoreApplication.translate("MainWindow", u"    Sensitive Analysis ", None))
        self.combosearchbox.setItemText(3, QCoreApplication.translate("MainWindow", u"    Sphere of Influence", None))
        self.combosearchbox.setItemText(4, QCoreApplication.translate("MainWindow", u"    Information about some of the Major bodies", None))
        self.combosearchbox.setItemText(5, QCoreApplication.translate("MainWindow", u"    Euler Angles", None))
        self.combosearchbox.setItemText(6, QCoreApplication.translate("MainWindow", u"    Ground Tracking Visualization", None))
        self.combosearchbox.setItemText(7, QCoreApplication.translate("MainWindow", u"    State Vector and Velocity Vector Calculation", None))
        self.combosearchbox.setItemText(8, QCoreApplication.translate("MainWindow", u"    Orbital Transfer Graph sketcher", None))
        self.combosearchbox.setItemText(9, QCoreApplication.translate("MainWindow", u"    Calculation of Julian Day and Local Side real day", None))
        self.combosearchbox.setItemText(10, QCoreApplication.translate("MainWindow", u"    Position of one spacecraft relative to other", None))
        self.combosearchbox.setItemText(11, QCoreApplication.translate("MainWindow", u"    Caculating whether a satellite is in Planet's Shadow", None))
        self.combosearchbox.setItemText(12, QCoreApplication.translate("MainWindow", u"    Halo Orbit Visualization", None))
        self.combosearchbox.setItemText(13, QCoreApplication.translate("MainWindow", u"    Various Parameters Calculation at a given point in Orbit ", None))
        self.combosearchbox.setItemText(14, QCoreApplication.translate("MainWindow", u"    Lagrangian Coefficients", None))
        self.combosearchbox.setItemText(15, QCoreApplication.translate("MainWindow", u"    3-Body Problem ", None))

#if QT_CONFIG(tooltip)
        self.combosearchbox.setToolTip(QCoreApplication.translate("MainWindow", u"Click on drop down arrow to Reveal the Options to choose", None))
#endif // QT_CONFIG(tooltip)
        self.Go_btn.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.label_title_2.setText(QCoreApplication.translate("MainWindow", u"   JulianDay Calculation:", None))
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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Inputs:", None))
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
        self.get_mass.setText(QCoreApplication.translate("MainWindow", u"Get Data", None))
        self.soi_mass.setText("")
        self.dist_frm_sun.setText("")
        self.soi_cal.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Outputs:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Get 3D Visualization", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Km", None))
        self.label_18.setText("")
        self.soi_rad.setText("")
        self.label_credits.setText("")
    # retranslateUi

