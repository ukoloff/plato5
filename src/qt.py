import sys
from os import environ
from PyQt5.QtWidgets import QApplication, QMainWindow

from .gl import GLX

class Win(QMainWindow, GLX):
    def __init__(self):
        super().__init__()

        self.initGL()

        self.setWindowTitle('Amicus Plato sed...')
        # self.startPos()
        self.show()

    def startPos(self):
        R = QDesktopWidget().availableGeometry()
        c = R.center()
        R.setSize(R.size() / 1.618)
        R.moveCenter(c)
        self.move(R.topLeft())
        self.resize(R.size())


def main():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

    app = QApplication(sys.argv)
    win = [Win() for i in range(5)]
    sys.exit(app.exec())
