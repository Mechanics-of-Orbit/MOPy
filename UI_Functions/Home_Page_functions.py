
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


        self.ui.maj_body_CoOE.currentIndexChanged.connect(lambda:Home_Page_main.MainWindow.coeNaoe(self))

        self.ui.cal_btn_coe_n_aoe.clicked.connect(lambda:Home_Page_main.MainWindow.coeNaoe(self))

        self.ui.VPCO_Submit_button.clicked.connect(lambda:Home_Page_main.MainWindow.Sliding_animation(self, 300, 'true'))

        self.ui.PE_Cal_Btn.clicked.connect(lambda:Home_Page_main.MainWindow.Sliding_animation(self, 200, "true"))

        self.ui.Orbital_Transfer_plot_button.clicked.connect(lambda:Home_Page_main.MainWindow.Sliding_animation(self, 522, 'true'))

        self.ui.Orbital_Transfer_plot_button.clicked.connect(lambda:Home_Page_main.MainWindow.trial(self))

        self.ui.ecce_dial.valueChanged.connect(lambda :Home_Page_main.MainWindow.ecce_dial_changed(self))

        #self.ui.btn_go_back.clicked.connect(lambda :Home_Page_main.MainWindow.Sliding_animation(self,0,'true'))

        self.ui.Semi_dial.valueChanged.connect(lambda :Home_Page_main.MainWindow.semi_dial_changed(self))

        self.ui.semi_major_axis_toggle_menu_slider.valueChanged.connect(lambda :Home_Page_main.MainWindow.semi_slider_single_step(self))

        self.ui.eccentricity_toggle_menu_slider.valueChanged.connect(lambda :Home_Page_main.MainWindow.ecce_slider_single_step(self))

        self.ui.type_of_input_toggle.currentIndexChanged.connect(lambda:Home_Page_main.MainWindow.toggle_option_index(self))

        

    def returnStatus():
        return GLOBAL_STATE
    


    
            