import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QThread, pyqtSignal)

class GreenThread(QThread):
    def reset(self):
        ret, self.orig = self.cap.read()
    def toggleShowWebcam(self):
        self.showWebcam = not self.showWebcam
    def setWebcam(self, index):
        self.webcam = index
        self.capUpdate = True
    def getWebcam(self):
        return self.webcam
    def setR(self, r_):
        self.r = r_
        self.setColor()
    def getR(self):
        return self.r
    def setG(self, g_):
        self.g = g_
        self.setColor()
    def getG(self):
        return self.g
    def setB(self, b_):
        self.b = b_
        self.setColor()
    def setColor(self):
        self.color = (self.b, self.g, self.r)
    def getB(self):
        return self.b
    def setShowWebcam(self, yesorno):
        self.showWebcam = yesorno
    def setThreshold(self, thresh):
        self.thresh = thresh
    def getThreshold(self):
        return self.thresh
    def setKernelType(self, type):
        self.kernelType = type
    def getKernelType(self):
        return self.kernelType
    def setKernelSize(self, size):
        self.kernelSize = (size, size)
    def getKernelSize(self):
        return self.kernelSize[0]
    def kill(self):
        self.running = False
        self.cap.release()
        cv2.destroyAllWindows()
    def __init__(self):
        super(GreenThread, self).__init__()
        #Webcam Number
        self.webcam = 0
        self.capUpdate = False
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
        self.color = (self.r, self.g, self.b)
    def run(self):
        #Show the other windows, fgmask and raw webcam
        debug = False

        #KEYS
        #exitKey = 27 #27=ESC
        #resetKey = 13 #13=Enter

        self.cap = cv2.VideoCapture(self.webcam)

        ret, self.orig = self.cap.read() #set the starting position 
        #NOTE: Usually the camera hasn't finished starting at this point
        #so you'll probabbly have to hit enter anyway

        grn_screen = np.zeros(self.orig.shape, np.uint8) #an array of bytes the same size as our image
        grn_screen[:] = self.color #Make all those bytes a color (green! blue! purple! who cares!)

        self.running = True #So we can kill it later
        while self.running:
            #if this code is running, we aren't connected to a camera, it just tries to connect to a camera
            self.cap.release()
            cv2.destroyAllWindows()
            self.cap = cv2.VideoCapture(self.webcam)
            while self.cap.isOpened(): #when connected to a camera do all this
                grn_screen[:] = self.color
                
                ret, frame = self.cap.read()
                fgmask = self.find_dif(self.orig, frame, self.thresh)

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
                cv2.imshow('Greenscreen', wgs)

                k = cv2.waitKey(25) & 0xff #delay for frames
                #if k == exitKey:
                #    break
                #if k == resetKey:
                #   ret, self.orig = self.cap.read()
                if self.capUpdate: #check and see if the user wants to change the camera
                    self.cap.release()
                    self.cap = cv2.VideoCapture(self.webcam)
                    self.capUpdate = False #finished changing camera

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