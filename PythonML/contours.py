import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):

    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerBlue = np.array([110, 50, 50])
    upperBlue = np.array([145, 255, 255])

    #gives us a binary image of black and white
    mask = cv.inRange(hsv, lowerBlue, upperBlue)

    #parameters: input, threshold value (used to classify pixel values), maxVal (value to assign if pixel is more or less than thresh val)
    ret, thresh = cv.threshold(mask, 127, 255, cv.THRESH_BINARY)

    #Find the contours
    #parameters: input, contour retrieval mode, contour approximation method
    #outputs an image, contours (a list of all the contours in the image),and hierarchy
    image, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #parameters: input, contours to be passed in, draw all contours (-1) or index to a specific one, color, thickness
    img = cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cv.imshow("Thresh", thresh)
    cv.imshow("contours", img)

    k = cv.waitKey(5) & 0xff

    if k == 27:
        break

cv.destroyAllWindows()