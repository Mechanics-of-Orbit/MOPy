
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sqlite3

# GUI FILE
from UI_Functions.Home_Page import Ui_MainWindow

# IMPORT FUNCTIONS
from UI_Functions.Home_Page_functions import *



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

    

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    # Screen switching defination
    def search(self):
        index = self.ui.combosearchbox.currentIndex()
        if index == 9:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif index == 3:
            self.ui.stackedWidget.setCurrentIndex(2)
    
    # SOI
    def SEARCH(self):
        db = sqlite3.connect("planetary_data_test/MajorBody_data.db")
        cursor = db.cursor()

        planet_name_soi = self.ui.SOI_planet_name.currentText()
        if planet_name_soi == "  Earth":
            planet_name = "Earth"
        planet_name_affect = self.ui.affect_planet_name.currentText()
 
        #command = ''' SELECT * from Parts_Table '''

        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[planet_name])
        

        #self.table.setRowCount(0) #Here table is the name we have to the first table containing 9 columns
       
        for row_number, row_data in enumerate(result):
            self.ui.soi_mass.setText(str(row_data[1]))
            print(row_data[1])
            #print(row_data[1])
            #self.table.insertRow(row_number)
            #for column_number, data in enumerate(row_data):
                #self.table.setItem(row_number, column_number,QTableWidgetItem(str(data)))

    
    # Home_btn
    def meth_Home_btn(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    # Julian Day Calculation
    def calendar_time(self):
        selected_date = self.ui.calendarWidget.selectedDate()
        year = selected_date.year()
        month = selected_date.month()
        day = selected_date.day()
        selected_time = self.ui.timeEdit.time()
        hour = selected_time.hour()
        minutes = selected_time.minute()
        seconds = selected_time.second()
        accuracy = self.ui.digits_accuracy.value()
        calendar = self.ui.type_of_calendar.currentText()
        if calendar == "  Gregorian Calendar":
            self.ui.Error_state.setText("")
            #julian day number from Gregorian calender date
            JDN = int((1461 * (year + 4800 + (month - 14)/12))/4) + int((367 * month - 2 - 12 * ((month - 14)/12))/12) - int((3 * ((year + 4900 + (month - 14)/12)/100))/4) + day - 32075
        elif calendar == "  Julian Calendar":
            self.ui.Error_state.setText("")
            #julian day number from julian calender date
            JDN = 367 * year - int((7 * (year + 5001 + (month - 9)/7))/4) + int((275 * month)/9) + day + 1729777
        elif calendar == "  Select the Type Of Calendar":
            self.ui.Error_state.setText("Please select the type of calendar")
                
        #JDN to JD
        JD = JDN + round(((hour - 12)/24),accuracy) + round((minutes/1440), accuracy) + round((seconds/86400), accuracy)
        self.ui.JulianDay_Result.setText(str(round(JD, accuracy))+ str(' Julian Days'))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
