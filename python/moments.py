import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

font = cv.FONT_HERSHEY_SIMPLEX

while(1):

    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    """ lowerGreen = np.array([5, 50, 50])
    upperGreen = np.array([25, 255, 255]) """

    lowerYellow = np.array([20, 100, 100])
    upperYellow = np.array([35, 255, 255])
    
    lowerGreen = np.array([40, 100, 100])
    upperGreen = np.array([55, 255, 255])

    #gives us a binary image of black and white
    maskYellow = cv.inRange(hsv, lowerYellow, upperYellow)
    maskGreen = cv.inRange(hsv, lowerGreen, upperGreen)

    #parameters: input, threshold value (used to classify pixel values), maxVal (value to assign if pixel is more or less than thresh val)
    ret, thresh = cv.threshold(maskYellow, 127, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        maxcontour = max(contours, key = cv.contourArea)

        #outputs a dictionary of all moments calculated like area, centroid, etc
        M = cv.moments(maxcontour)

        if M['m00'] > 0 and cv.contourArea(maxcontour) > 1000:
            #calculation of centroid
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
        else:
            cx, cy = 700, 700
    else:
        cx, cy = 700, 700

    #draw contours
    img = cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

    #draw centroid
    centroid = cv.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
    cv.putText(frame, "Centroid", (cx - 25, cy -25), font, 1, (255, 255, 255), 2, cv.LINE_AA)

    #draw line from centroid
    line = cv.line(frame, (cx, cy), ((cx + 400), (cy + 400)), (255, 0 , 0), 5)

    cv.imshow("centroid & line", frame)

    k = cv.waitKey(5) & 0xff

    if k == 27:
        break

cv.destroyAllWindows()