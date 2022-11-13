import sys
from os import environ
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class Win(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Amicus Plato sed...')


def main():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())
