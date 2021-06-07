from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUiType

import sys

from os import path

FORM_CLASS,_= loadUiType(path.join(path.dirname('__file__'),"GUI_Planet.ui")) 
import sqlite3

class Main(QMainWindow, FORM_CLASS):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
    
    def Handel_Buttons(self):
        self.Get_Data_btn.clicked.connect(self.SEARCH)

    def SEARCH(self):
        db = sqlite3.connect("MajorBody_data.db")
        cursor = db.cursor()

        name = self.Planet_Name.text()
        #command = ''' SELECT * from Parts_Table '''

        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[name])

        self.table.setRowCount(0) #Here table is the name we have to the first table containing 9 columns
       
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number,QTableWidgetItem(str(data[2])))

           
    #Above code is common for all the Apps and actual code for our case starts from here.


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()