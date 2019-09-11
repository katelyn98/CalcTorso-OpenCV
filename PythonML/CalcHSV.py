#calculating HSV for tracking pink and green circles
 
import cv2 as cv
import numpy as np

pink = np.uint8([[[247, 95, 163]]])
hsv_pink = cv.cvtColor(pink, cv.COLOR_BGR2HSV)
print(hsv_pink)

pink = np.uint8([[[255, 129, 190]]])
hsv_pink = cv.cvtColor(pink, cv.COLOR_BGR2HSV)
print(hsv_pink)

pink = np.uint8([[[255, 108, 182]]])
hsv_pink = cv.cvtColor(pink, cv.COLOR_BGR2HSV)
print(hsv_pink)

#255, 129, 190
#255, 130, 191
#255, 119, 176
#255, 108, 182

green = np.uint8([[[95, 208, 173]]])
hsv_green= cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)
    
green = np.uint8([[[68, 189, 153]]])
hsv_green= cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)
#88, 206, 173
#68, 186, 153
#82, 199, 160
#95, 208, 172
