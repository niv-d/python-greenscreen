import sys
import time
import cv2
import numpy as np
from gsui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QThread)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super (MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    m = MainWindow()
    m.show()
    thread = AThread()
    thread.finished.connect(app.exit)
    thread.start()
    sys.exit (app.exec_())
class AThread(QThread):
    def setWebcam(self, index):
        self.webcam = index
    def setR(self, r):
        self.r = r
    def setG(self, g):
        self.g = g
    def setB(self, b):
        self.b = b
    def setShowWebcam(self, yesorno):
        self.showWebcam = yesorno
    def setKernelType(self, type):
        self.kernelType = type
    def setKernelSize(self, size):
        self.kernelSize = (size, size)
    def setThreshold(self, thresh):
        self.thresh = thresh
    def __init__(self):
        super(AThread, self).__init__()
        #Webcam Number
        self.webcam = 0

        #greenscreen color
        self.r = 0
        self.g = 255
        self.b = 0

        #Show the webcam instead of the greenscreen.
        self.showWebcam = False

        #0 = Ellipse
        #1 = Cross
        #2 = Rect
        self.kernelType = 0

        #The size of the kernel
        self.kernelSize = (30,30)

        #noise reduction kernel size
        self.noiseyKernel = (3,3)

        #threshold of the difference between
        self.thresh = 30
    def run(self):
        #Show the other windows, fgmask and raw webcam
        debug = False

        color = (self.r, self.g, self.b)

        #KEYS
        exitKey = 27 #27=ESC
        resetKey = 13 #13=Enter

        cap = cv2.VideoCapture(self.webcam)

        ret, orig = cap.read() #set the starting position 
        #NOTE: Usually the camera hasn't finished starting at this point
        #so you'll probabbly have to hit enter anyway

        grn_screen = np.zeros(orig.shape, np.uint8) #an array of bytes the same size as our image
        grn_screen[:] = color #Make all those bytes a color (green! blue! purple! who cares!)

        while True:
            ret, frame = cap.read()
            fgmask = self.find_dif(orig, frame, self.thresh)

            #Greenscreen creation
            bgmask = cv2.bitwise_not(fgmask) #invert foreground
            fgimg = cv2.bitwise_and(frame,frame, mask = fgmask) #cut out the foreground
            bgimg = cv2.bitwise_and(grn_screen,grn_screen, mask = bgmask) #cut out the background
            wgs = cv2.add(fgimg,bgimg) #combine each cut

            if self.showWebcam:
                wgs = frame

            if debug:
                cv2.imshow('orig', frame)
                cv2.imshow('mask', fgmask)
            cv2.imshow('result', wgs)

            k = cv2.waitKey(25) & 0xff
            if k == exitKey:
                break
            if k == resetKey:
                ret, orig = cap.read()
        cap.release()
        cv2.destroyAllWindows()
    def find_dif(self, orig, img, thr = 10):
        diff = cv2.absdiff(orig,img) #Find the difference
        diff[diff < thr] = 0 #Remove the difference if it meets the thresh
        mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) #make it black and white

        #noise reduction, circle seems best for this, no matter the circumstances
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, self.noiseyKernel)
        mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

        #"blob" reduction (the false positives inside the changed images)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, self.kernelSize)
        if self.kernelType == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, self.kernelSize)
        if self.kernelType == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, self.kernelSize)
        mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

        fgmask = mask.astype(np.uint8)
        fgmask[fgmask>0] = 255 #Convert to only white and black
        return fgmask
if __name__ == '__main__':
    main ()