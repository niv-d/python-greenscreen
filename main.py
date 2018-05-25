import sys
import time
import cv2
import numpy as np
from gsui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QThread, pyqtSignal)
from gs import GreenThread
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super (MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
thread = GreenThread()
def main():
    app = QtWidgets.QApplication(sys.argv)
    m = MainWindow()
    m.show()
    thread.finished.connect(app.exit)
    thread.start()
    thread.setWebcam(0)

    m.ui.pushButtonReset.clicked.connect(lambda: reset(m.ui.spinBoxDelay.value()))
    m.ui.checkBoxGreenScreen.clicked.connect(thread.toggleShowWebcam)
    m.ui.spinBoxCam.valueChanged.connect(lambda: thread.setWebcam(m.ui.spinBoxCam.value()))
    m.ui.spinBoxRed.valueChanged.connect(lambda: thread.setB(m.ui.spinBoxRed.value()))
    m.ui.spinBoxGreen.valueChanged.connect(lambda: thread.setG(m.ui.spinBoxGreen.value()))
    m.ui.spinBoxBlue.valueChanged.connect(lambda: thread.setR(m.ui.spinBoxBlue.value()))
    m.ui.horizontalSliderThresh.valueChanged.connect(lambda: thread.setThreshold(m.ui.horizontalSliderThresh.value()))
    m.ui.comboBoxNoise.currentIndexChanged.connect(lambda: thread.setKernelType(m.ui.comboBoxNoise.currentIndex()))
    m.ui.horizontalSliderNoiseSize.valueChanged.connect(lambda: thread.setKernelSize(m.ui.horizontalSliderNoiseSize.value()))
    
    sys.exit (app.exec_())
def reset(delay):
    count = 0
    while count < delay:
        time.sleep(1)
        count += 1
    thread.reset()


if __name__ == '__main__':
    main ()