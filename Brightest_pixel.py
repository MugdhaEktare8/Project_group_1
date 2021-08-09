import numpy as np
import cv2
cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
image = cv2.imread("pixel.jpg") 
original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (41,41), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = original.copy()
#cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.circle(image, maxLoc, 41, (0, 0, 255), 5)
cv2.imshow("output", image)
cv2.waitKey(0)