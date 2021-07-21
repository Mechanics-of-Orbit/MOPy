
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
        self.ui.Go_btn.clicked.connect(lambda: Home_Page_main.MainWindow.search(self))

        # When Calculate_but for Julian Day is clicked 
        self.ui.calculate_btn.clicked.connect(lambda: Home_Page_main.MainWindow.calendar_time(self))

        # When Home_btn is clicked
        self.ui.Home_btn.clicked.connect(lambda: Home_Page_main.MainWindow.meth_Home_btn(self))

        self.ui.SOI_planet_name.currentIndexChanged.connect(lambda:Home_Page_main.MainWindow.SEARCH(self))

        self.ui.soi_cal.clicked.connect(lambda:Home_Page_main.MainWindow.SOI(self))

        self.ui.get_3D_soi.clicked.connect(lambda:Home_Page_main.MainWindow.soi_graph(self))

        self.ui.input_type_go_btn_vpco.clicked.connect(lambda:Home_Page_main.MainWindow.vpco_go_btn(self))

        self.ui.Home_btn_2.clicked.connect(lambda:Home_Page_main.MainWindow.homebtn2(self))

        self.ui.orbit_type_btn_inpt_ae.clicked.connect(lambda:Home_Page_main.MainWindow.vpco_a_e(self))

        self.ui.go_btn_inpt_ae.clicked.connect(lambda:Home_Page_main.MainWindow.vpco_ae_cal_btn(self))

        self.ui.vpco_feature_back_btn.clicked.connect(lambda:Home_Page_main.MainWindow.vpco_feature_back_btn(self))

        self.ui.maj_body_CoOE.currentIndexChanged.connect(lambda:Home_Page_main.MainWindow.coeNaoe(self))

        self.ui.cal_btn_coe_n_aoe.clicked.connect(lambda:Home_Page_main.MainWindow.coeNaoe(self))

        event_released = self.ui.semi_major_axis_toggle_menu_slider.sliderMoved

        self.ui.semi_major_axis_toggle_menu_slider.sliderMoved.connect(lambda:Home_Page_main.MainWindow.slider_released(self, event_released))
        
        event_pressed = self.ui.semi_major_axis_toggle_menu_slider.sliderPressed

        self.ui.semi_major_axis_toggle_menu_slider.sliderPressed.connect(lambda:Home_Page_main.MainWindow.slider_pressed(self, event_pressed))
    def returnStatus():
        return GLOBAL_STATE

    def expand(self, maxwidth, enable):
        
        if enable:

            width = self.ui.VPCO_menu_toggle_frame.width()
            maxExtent = maxwidth
            standard = 40

            if width == standard:
                widthExtended = maxExtent

                self.ui.stackedWidget_2.setCurrentIndex(1)

                # self.ui.semi_major_axis_toggle_menu_lbl.setText('Semi-major axis')
                # self.ui.eccentricity_toggle_menu_lbl.setText('Eccentricity')
                # self.ui.inclination_toggle_menu_lbl.setText('Inclination')
                # self.ui.RAAN_toggle_menu_lbl.setText('RAAN')
                # self.ui.arg_of_per_toggle_menu_lbl.setText('Arg_of_Per')
                # self.ui.tru_ano_toggle_menu_lbl.setText('True_anomaly')

                self.ui.semi_major_axis_toggle_menu_spinbox.show()
                self.ui.eccentricity_toggle_menu_spinbox.show()
                self.ui.inclination_toggle_menu_spinbox.show()
                self.ui.RAAN_toggle_menu_spinbox.show()
                self.ui.arg_of_per_toggle_menu_spinbox.show()
                self.ui.tru_ano_toggle_menu_spinbox.show()

                self.ui.semi_major_axis_toggle_menu_slider.show()
                self.ui.eccentricity_toggle_menu_slider.show()
                self.ui.inclination_toggle_menu_slider.show()
                self.ui.RAAN_toggle_menu_slider.show()
                self.ui.arg_of_per_toggle_menu_slider.show()
                self.ui.tru_ano_toggle_menu_slider.show()
                
            elif width != standard:

                self.ui.stackedWidget_2.setCurrentIndex(1)

                widthExtended = standard
                self.ui.semi_major_axis_toggle_menu_lbl.setText('a')
                self.ui.eccentricity_toggle_menu_lbl.setText('e')
                self.ui.inclination_toggle_menu_lbl.setText('i')
                self.ui.RAAN_toggle_menu_lbl.setText('Ω')
                self.ui.arg_of_per_toggle_menu_lbl.setText('ω')
                self.ui.tru_ano_toggle_menu_lbl.setText('ν')

                self.ui.semi_major_axis_toggle_menu_spinbox.hide()
                self.ui.eccentricity_toggle_menu_spinbox.hide()
                self.ui.inclination_toggle_menu_spinbox.hide()
                self.ui.RAAN_toggle_menu_spinbox.hide()
                self.ui.arg_of_per_toggle_menu_spinbox.hide()
                self.ui.tru_ano_toggle_menu_spinbox.hide()

                self.ui.semi_major_axis_toggle_menu_slider.hide()
                self.ui.eccentricity_toggle_menu_slider.hide()
                self.ui.inclination_toggle_menu_slider.hide()
                self.ui.RAAN_toggle_menu_slider.hide()
                self.ui.arg_of_per_toggle_menu_slider.hide()
                self.ui.tru_ano_toggle_menu_slider.hide()

        
        self.animation = QPropertyAnimation(self.ui.VPCO_menu_toggle_frame,b"minimumWidth")
        self.animation.setDuration(200)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        # self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start() 