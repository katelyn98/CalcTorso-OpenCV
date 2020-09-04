import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):

    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # lowerGreen = np.array([50, 50, 50])
    # upperGreen = np.array([80, 255, 255])
    lowerBlue = np.array([150, 77, 77])
    upperBlue = np.array([255, 200, 200])

    #gives us a binary image of black and white
    mask = cv.inRange(hsv, lowerBlue, upperBlue)

    #parameters: input, threshold value (used to classify pixel values), maxVal (value to assign if pixel is more or less than thresh val)
    ret, thresh = cv.threshold(mask, 120, 255, cv.THRESH_BINARY)

    #Find the contours
    #parameters: input, contour retrieval mode, contour approximation method
    #outputs an image, contours (a list of all the contours in the image),and hierarchy
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #parameters: input, contours to be passed in, draw all contours (-1) or index to a specific one, color, thickness
    img = cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

    # cv.imshow("Thresh", thresh)
    cv.imshow("contours", img)

    k = cv.waitKey(5) & 0xff

    if k == 27:
        break

cv.destroyAllWindows()