import cv2
import numpy as np

img = cv2.imread('test.py.png')

def nothing(x):
    pass

cv2.namedWindow("Trackbars1")

cv2.createTrackbar("L - H", "Trackbars1", 119, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars1", 28, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars1", 56, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars1", 229, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars1", 116, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars1", 124, 255, nothing)

cv2.namedWindow("Trackbars2")

cv2.createTrackbar("L - H", "Trackbars2", 0, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars2", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars2", 199, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars2", 140, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars2", 0, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars2", 248, 255, nothing)

while True:
    l_h = cv2.getTrackbarPos("L - H", "Trackbars1")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars1")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars1")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars1")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars1")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars1")

    lower = np.array([l_h,l_s,l_v])
    upper = np.array([u_h,u_s,u_v])
    mask1 = cv2.inRange(img, lower, upper)
    result1 = cv2.bitwise_and(img, img, mask = mask1)

    cv2.imshow("Mask1", mask1)

    cv2.imshow('result1', result1)




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

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

image1 = img.copy()
contours, _= cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image1 = cv2.drawContours(image1, contours, -1, (0,255,0), 2)
cv2.imshow('1', image1)

image2 = img.copy()
contours, _= cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image2 = cv2.drawContours(image2, contours, -1, (0,255,0), 2)
cv2.imshow('2', image2)

result = cv2.bitwise_and(image1, image2, mask = None)
# result_ = cv2.bitwise_and(img, img, mask = result)
cv2.imshow('Image', result)
# cv2.imshow('Image_', result_)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.namedWindow("Trackbars1")

cv2.createTrackbar("L - H", "Trackbars1", 119, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars1", 28, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars1", 56, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars1", 229, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars1", 116, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars1", 124, 255, nothing)

while True:
    l_h = cv2.getTrackbarPos("L - H", "Trackbars1")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars1")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars1")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars1")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars1")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars1")

    lower = np.array([l_h,l_s,l_v])
    upper = np.array([u_h,u_s,u_v])
    mask3 = cv2.inRange(result, lower, upper)
    result3 = cv2.bitwise_and(result, result, mask = mask3)

    cv2.imshow("Mask3", mask3)

    cv2.imshow('result3', result3)

    key = cv2.waitKey(1)
    if key == 27:
        break

# cv2.imwrite('RESULT.png', result)