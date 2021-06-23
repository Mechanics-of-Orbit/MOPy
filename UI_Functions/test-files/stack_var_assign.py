import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a Title
        self.setWindowTitle("Final Year Project")

        #Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        #Create a Label
        my_Label = qtw.QLabel("Select The Part")
        self.layout().addWidget(my_Label)

        #Change font Size of Labels
        my_Label.setFont(qtg.QFont('Helvatica',48))

        #Create a Combo box Box
        my_combo = qtw.QComboBox(self,
        editable=True,
        insertPolicy=qtw.QComboBox.InsertAtBottom)
        #Add Items to combo box
        my_combo.addItem("Part - 1","Part - 1.1")
        my_combo.addItem("Part - 2",2)
        my_combo.addItem("Part - 3", qtw.QWidget)
        my_combo.addItem("Part - 4")
        my_combo.addItem("Part - 5")
        my_combo.addItems(["Part - 6", "Part - 7", "Part - 8"])
        my_combo.insertItems(2, ["Extra Part", "Reamining Part"])

        #Put Combo Box on screen
        self.layout().addWidget(my_combo)

        #Create a Button
        my_button = qtw.QPushButton("Press Me!!",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)


        #******show the app Important ******
        self.show()
        def press_it():
            #add name to label
            my_Label.setText(f'You Picked {my_combo.currentText()}!!')
            #my_Label.setText(f'You Picked {my_combo.currentData()}!!')
            #my_Label.setText(f'You Picked {my_combo.currentIndex()}!!')
            



app = qtw.QApplication([])
mW = MainWindow()

#Run The App
app.exec_()