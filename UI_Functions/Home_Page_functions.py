
## ==> GUI FILE
import Home_Page_main
from Home_Page_main import *


## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    


    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Maximize")
    


    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        #self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        #self.ui.btn_maximize.setIcon(QIcon('C:\Python Course For App making\Final_Year_Project\MOPy\GUI-test\Resources\close.svg'))

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        #When Go_btn clicked
        ##########=>>>self.ui.Go_btn.clicked.connect(lambda: Home_Page_main.MainWindow.search(self))

        # When Calculate_but for Julian Day is clicked 
        self.ui.calculate_btn.clicked.connect(lambda: Home_Page_main.MainWindow.calendar_time(self))

        # When Home_btn is clicked
        self.ui.Home_btn.clicked.connect(lambda: Home_Page_main.MainWindow.meth_Home_btn(self))

        self.ui.SOI_planet_name.currentIndexChanged.connect(lambda:Home_Page_main.MainWindow.SEARCH(self))

        self.ui.soi_cal.clicked.connect(lambda:Home_Page_main.MainWindow.SOI(self))

        self.ui.get_3D_soi.clicked.connect(lambda:Home_Page_main.MainWindow.soi_graph(self))

        #self.ui.input_type_go_btn_vpco.clicked.connect(lambda:Home_Page_main.MainWindow.vpco_go_btn(self))

        #self.ui.Home_btn_2.clicked.connect(lambda:Home_Page_main.MainWindow.homebtn2(self))

        #self.ui.orbit_type_btn_inpt_ae.clicked.connect(lambda:Home_Page_main.MainWindow.vpco_a_e(self))

        #self.ui.go_btn_inpt_ae.clicked.connect(lambda:Home_Page_main.MainWindow.vpco_ae_cal_btn(self))

        self.ui.vpco_feature_back_btn.clicked.connect(lambda:Home_Page_main.MainWindow.vpco_feature_back_btn(self))

        self.ui.maj_body_CoOE.currentIndexChanged.connect(lambda:Home_Page_main.MainWindow.coeNaoe(self))

        self.ui.cal_btn_coe_n_aoe.clicked.connect(lambda:Home_Page_main.MainWindow.coeNaoe(self))

        

        self.ui.ecce_dial.valueChanged.connect(lambda :Home_Page_main.MainWindow.ecce_dial_changed(self))

        
        self.ui.Semi_dial.valueChanged.connect(lambda :Home_Page_main.MainWindow.semi_dial_changed(self))

        self.ui.semi_major_axis_toggle_menu_slider.valueChanged.connect(lambda :Home_Page_main.MainWindow.semi_slider_single_step(self))

        self.ui.eccentricity_toggle_menu_slider.valueChanged.connect(lambda :Home_Page_main.MainWindow.ecce_slider_single_step(self))

        self.ui.type_of_input_toggle.currentIndexChanged.connect(lambda:Home_Page_main.MainWindow.toggle_option_index(self))

        

    def returnStatus():
        return GLOBAL_STATE
    
    ###############################################################################################
    #--<<Hover_Effect>>--#

    def toggleMenu_VPCO(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.Home_VPCO_Slider.height()
            maxExtend = maxHeight
            standard = 91
            

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
                self.ui.Home_VPCO_Label.setText("Calculation of Various Parameters\n----------------------------\n Calculation of various parameters of an orbit in space, such as escape velocity, Specific angular moment, etc.")
            else:
                heightExtended = standard
                self.ui.Home_VPCO_Label.setText("Various Parameters at any given point and Constants in orbit")
            # ANIMATION
            self.animation_1 = QPropertyAnimation(self.ui.Home_VPCO_Slider, b"minimumHeight")
            self.animation_1.setDuration(100)
            self.animation_1.setStartValue(height)
            self.animation_1.setEndValue(heightExtended)
            self.animation_1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_1.start() 
            

    def toggleMenu_Julian_Day(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.slider_2.height()
            maxExtend = maxHeight
            standard = 91

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
                #self.ui.Home_VPCO_Label.setText(
            else:
                heightExtended = standard
            # ANIMATION
            self.animation_2 = QPropertyAnimation(self.ui.slider_2, b"minimumHeight")
            self.animation_2.setDuration(100)
            self.animation_2.setStartValue(height)
            self.animation_2.setEndValue(heightExtended)
            self.animation_2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_2.start()   

    def toggleMenu_Orbital_Elements(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.slider_6.height()
            maxExtend = maxHeight
            standard = 91

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
            else:
                heightExtended = standard
            # ANIMATION
            self.animation_3 = QPropertyAnimation(self.ui.slider_6, b"minimumHeight")
            self.animation_3.setDuration(100)
            self.animation_3.setStartValue(height)
            self.animation_3.setEndValue(heightExtended)
            self.animation_3.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_3.start() 
        
    def toggleMenu_SOI(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.slider_7.height()
            maxExtend = maxHeight
            standard = 91

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
            else:
                heightExtended = standard
            # ANIMATION
            self.animation_4 = QPropertyAnimation(self.ui.slider_7, b"minimumHeight")
            self.animation_4.setDuration(100)
            self.animation_4.setStartValue(height)
            self.animation_4.setEndValue(heightExtended)
            self.animation_4.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_4.start() 
    
    def toggleMenu_Orbit_Visualization(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.slider_3.height()
            maxExtend = maxHeight
            standard = 91

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
            else:
                heightExtended = standard
            # ANIMATION
            self.animation_5 = QPropertyAnimation(self.ui.slider_3, b"minimumHeight")
            self.animation_5.setDuration(100)
            self.animation_5.setStartValue(height)
            self.animation_5.setEndValue(heightExtended)
            self.animation_5.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_5.start() 
        
    def toggleMenu_Ground_Track(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.slider_4.height()
            maxExtend = maxHeight
            standard = 91

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
            else:
                heightExtended = standard
            # ANIMATION
            self.animation_6 = QPropertyAnimation(self.ui.slider_4, b"minimumHeight")
            self.animation_6.setDuration(100)
            self.animation_6.setStartValue(height)
            self.animation_6.setEndValue(heightExtended)
            self.animation_6.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_6.start() 
        
    def toggleMenu_Planet_in_Shadow(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.slider_5.height()
            maxExtend = maxHeight
            standard = 91

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
            else:
                heightExtended = standard
            # ANIMATION
            self.animation_7 = QPropertyAnimation(self.ui.slider_5, b"minimumHeight")
            self.animation_7.setDuration(100)
            self.animation_7.setStartValue(height)
            self.animation_7.setEndValue(heightExtended)
            self.animation_7.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_7.start() 
        
    def toggleMenu_Planetary_Ephimeris(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.slider_8.height()
            maxExtend = maxHeight
            standard = 91

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
            else:
                heightExtended = standard
            # ANIMATION
            self.animation_8 = QPropertyAnimation(self.ui.slider_8, b"minimumHeight")
            self.animation_8.setDuration(100)
            self.animation_8.setStartValue(height)
            self.animation_8.setEndValue(heightExtended)
            self.animation_8.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_8.start() 
        
    def toggleMenu_Numerical_integ(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.slider_9.height()
            maxExtend = maxHeight
            standard = 91

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
            else:
                heightExtended = standard
            # ANIMATION
            self.animation_9 = QPropertyAnimation(self.ui.slider_9, b"minimumHeight")
            self.animation_9.setDuration(100)
            self.animation_9.setStartValue(height)
            self.animation_9.setEndValue(heightExtended)
            self.animation_9.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_9.start() 
        
    def toggleMenu_Orbital_transfer(self, maxHeight, enable):
        if enable:

            # GET WIDTH
            height = self.ui.slider_10.height()
            maxExtend = maxHeight
            standard = 91

            # SET MAX WIDTH
            if height == 91:
                heightExtended = maxExtend
            else:
                heightExtended = standard
            # ANIMATION
            self.animation_10 = QPropertyAnimation(self.ui.slider_10, b"minimumHeight")
            self.animation_10.setDuration(100)
            self.animation_10.setStartValue(height)
            self.animation_10.setEndValue(heightExtended)
            self.animation_10.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_10.start() 
        
    def toggleMenu_Eulers_Angle(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.slider_11.width()
            maxExtend = maxWidth
            standard = 245

            # SET MAX WIDTH
            if width == 245:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            # ANIMATION
            self.animation_11 = QPropertyAnimation(self.ui.slider_11, b"minimumWidth")
            self.animation_11.setDuration(100)
            self.animation_11.setStartValue(width)
            self.animation_11.setEndValue(widthExtended)
            self.animation_11.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_11.start() 