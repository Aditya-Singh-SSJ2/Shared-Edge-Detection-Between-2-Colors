#!/usr/bin/env python
"""This script prompts a user to enter 2 ranges of color using the trackbars,
and returns only the shared edges between the 2 colors if any in the input image."""

import cv2
import numpy as np

# Input image here.
img = cv2.imread('input.png')

def nothing(x):
    pass

# Create Trackbars Windows to Thresholding 1st color.
cv2.namedWindow("Trackbars1")

cv2.createTrackbar("L - H", "Trackbars1", 119, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars1", 28, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars1", 56, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars1", 229, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars1", 116, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars1", 124, 255, nothing)

# Create Trackbars Windows to Thresholding 2nd color.
cv2.namedWindow("Trackbars2")

cv2.createTrackbar("L - H", "Trackbars2", 0, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars2", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars2", 199, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars2", 140, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars2", 0, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars2", 248, 255, nothing)

while True:
    # Trackbar inputs (user input) assigned to variables
    l_h = cv2.getTrackbarPos("L - H", "Trackbars1")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars1")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars1")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars1")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars1")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars1")

    # Assigned variables turned into arrays 
    lower = np.array([l_h,l_s,l_v])
    upper = np.array([u_h,u_s,u_v])

    # Arrays passed to inRange function
    mask1 = cv2.inRange(img, lower, upper)
    result1 = cv2.bitwise_and(img, img, mask = mask1)

    # Displaying the mask and the result
    cv2.imshow("Mask1", mask1)
    cv2.imshow('result1', result1)

    # Repeat for user to input 2nd color range
    l_h = cv2.getTrackbarPos("L - H", "Trackbars2")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars2")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars2")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars2")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars2")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars2")

    lower = np.array([l_h,l_s,l_v])
    upper = np.array([u_h,u_s,u_v])
    mask2 = cv2.inRange(img, lower, upper)
    result2 = cv2.bitwise_and(img, img, mask = mask2)

    cv2.imshow("Mask2", mask2)
    cv2.imshow('result2', result2)

    # Break when 'ESC' key pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# CLose all windows
cv2.destroyAllWindows()

# Draw contour for the first mask (user input range for color 1)
image1 = img.copy()
contours, _= cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image1 = cv2.drawContours(image1, contours, -1, (0,255,0), 2)   # Border width = 2, and color = 'green'

# Draw contour for the first mask (user input range for color 2)
image2 = img.copy()
contours, _= cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image2 = cv2.drawContours(image2, contours, -1, (0,255,0), 2)   # Border width = 2, and color = 'green'

# bitwise intersect the 2 images obtained after drawing the contours
result = cv2.bitwise_and(image1, image2, mask = None)

# Lower and Upper threshold values for Green, BOUNDARY COLOR
lower = np.array([0,255,0])
upper = np.array([0,255,0])

# Inrange value to draw the mask
Result = cv2.inRange(result, lower, upper)

# Output the mask as result
cv2.imshow("OUTPUT", Result)

# Wait for user key press
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("output.png",Result)
