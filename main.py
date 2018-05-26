import sys
import time
import cv2
import numpy as np
from gsui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QThread, pyqtSignal)
from gs import GreenThread
import atexit
import configparser

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super (MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
thread = GreenThread()
filename = "greenscreen_settings.ini"
delay = 0
def main():
    app = QtWidgets.QApplication(sys.argv)
    m = MainWindow()
    m.show()
    thread.finished.connect(app.exit)
    thread.start()
    thread.setWebcam(0)

    try:
        config = configparser.ConfigParser()
        config.read(filename)
        mc = config['main']
        m.ui.spinBoxDelay.setValue(delay)
        thread.setWebcam(int(mc['camera']))
        m.ui.spinBoxCam.setValue(int(mc['camera']))
        thread.setB(int(mc['r'])) #for some reason these are backwards :p
        m.ui.spinBoxRed.setValue(int(mc['r']))
        thread.setG(int(mc['g']))
        m.ui.spinBoxGreen.setValue(int(mc['g']))
        thread.setR(int(mc['b']))
        m.ui.spinBoxBlue.setValue(int(mc['b']))
        thread.setThreshold(int(mc['threshold']))
        m.ui.horizontalSliderThresh.setValue(int(mc['threshold']))
        thread.setKernelType(int(mc['type']))
        m.ui.comboBoxNoise.setCurrentIndex(int(mc['type']))
        thread.setKernelSize(int(mc['noisereduction']))
        m.ui.horizontalSliderNoiseSize.setValue(int(mc['noisereduction']))
    except:
        print("No config!")



    m.ui.pushButtonReset.clicked.connect(lambda: reset(m.ui.spinBoxDelay.value()))
    m.ui.checkBoxGreenScreen.clicked.connect(thread.toggleShowWebcam)
    m.ui.spinBoxCam.valueChanged.connect(lambda: thread.setWebcam(m.ui.spinBoxCam.value()))
    m.ui.spinBoxRed.valueChanged.connect(lambda: thread.setB(m.ui.spinBoxRed.value()))
    m.ui.spinBoxGreen.valueChanged.connect(lambda: thread.setG(m.ui.spinBoxGreen.value()))
    m.ui.spinBoxBlue.valueChanged.connect(lambda: thread.setR(m.ui.spinBoxBlue.value()))
    m.ui.horizontalSliderThresh.valueChanged.connect(lambda: thread.setThreshold(m.ui.horizontalSliderThresh.value()))
    m.ui.comboBoxNoise.currentIndexChanged.connect(lambda: thread.setKernelType(m.ui.comboBoxNoise.currentIndex()))
    m.ui.horizontalSliderNoiseSize.valueChanged.connect(lambda: thread.setKernelSize(m.ui.horizontalSliderNoiseSize.value()))
    atexit.register(exit_handler)
    sys.exit (app.exec_())

def exit_handler():
    config = configparser.ConfigParser()
    config.add_section('main')
    config.set('main', 'delay', str(delay))
    config.set('main', 'camera', str(thread.getWebcam()))
    config.set('main', 'r', str(thread.getB()))
    config.set('main', 'g', str(thread.getG()))
    config.set('main', 'b', str(thread.getR()))
    config.set('main', 'threshold', str(thread.getThresh()))
    config.set('main', 'type', str(thread.getType()))
    config.set('main', 'noisereduction', str(thread.getKSize()))

    with open(filename, 'w') as f:
        config.write(f)

def reset(d):
    time.sleep(d)
    thread.reset()


if __name__ == '__main__':
    main ()