import cv2
import numpy as np
#Webcam Number
webcam = 0

#Show the other windows, fgmask and raw webcam
debug = False

#greenscreen color
r = 0
g = 255
b = 0
color = (r, g, b)

#Show the webcam instead of the greenscreen.
showWebcam = False

#0 = Ellipse
#1 = Cross
#2 = Rect
kernelType = 0

#The size of the kernel
kernelSize = (30,30)

#noise reduction kernel size
noiseyKernel = (3,3)

#threshold of the difference between
thresh = 30

#KEYS
exitKey = 27 #27=ESC
resetKey = 13 #13=Enter

cap = cv2.VideoCapture(webcam)

ret, orig = cap.read() #set the starting position 
#NOTE: Usually the camera hasn't finished starting at this point
#so you'll probabbly have to hit enter anyway

grn_screen = np.zeros(orig.shape, np.uint8) #an array of bytes the same size as our image
grn_screen[:] = color #Make all those bytes a color (green! blue! purple! who cares!)

def find_dif(orig, img, thr = 10):
    diff = cv2.absdiff(orig,img) #Find the difference
    diff[diff < thr] = 0 #Remove the difference if it meets the thresh
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) #make it black and white

    #noise reduction, circle seems best for this, no matter the circumstances
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, noiseyKernel)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    #"blob" reduction (the false positives inside the changed images)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,kernelSize)
    if kernelType == 1:
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,kernelSize)
    if kernelType == 2:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,kernelSize)
    mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    fgmask = mask.astype(np.uint8)
    fgmask[fgmask>0] = 255 #Convert to only white and black
    return fgmask

#main loop
while True:
    ret, frame = cap.read()
    fgmask = find_dif(orig, frame, thresh)

    #Greenscreen creation
    bgmask = cv2.bitwise_not(fgmask) #invert foreground
    fgimg = cv2.bitwise_and(frame,frame, mask = fgmask) #cut out the foreground
    bgimg = cv2.bitwise_and(grn_screen,grn_screen, mask = bgmask) #cut out the background
    wgs = cv2.add(fgimg,bgimg) #combine each cut

    if showWebcam:
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