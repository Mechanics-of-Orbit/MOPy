
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

        self.ui.get_mass.clicked.connect(lambda:Home_Page_main.MainWindow.SEARCH(self))

        self.ui.soi_cal.clicked.connect(lambda:Home_Page_main.MainWindow.SOI(self))

        self.ui.get_3D_soi.clicked.connect(lambda:Home_Page_main.MainWindow.soi_graph(self))
    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE
