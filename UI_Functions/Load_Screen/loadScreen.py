import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.setWindowFlags(Qt.WindowStayOnTopHint | Qt.customizeWindowHint)

        self.label_animation = QLabel(self)
        self.movie = QMovie('C:/Users/manjunath neelmath/Desktop/test/Rotating_earth_(large).gif')
        self.label_animation.setMovie(self.movie)

        timer =QTimer(self)

        self.startAnimation()
        timer.singleShot(3000, self.stopAnimation())

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.loading_screen = LoadingScreen()

        self.show()

app = QApplication(sys.argv)
demo = AppDemo()
app.exit(app.exec_())