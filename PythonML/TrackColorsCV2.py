from picamera import PiCamera
from time import sleep
import cv2 as cv
import numpy as np

#create video object
cap = cv.VideoCapture(0)


while(1):
    #take each frame
    _, frame = cap.read()
    
    #convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    #define range of blue in HSV
    #HSV = [Hue range, Saturation range, Value range]
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #Threshold in HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    #Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask= mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xff

    if k == 27:
        break

cv.destroyAllWindows()