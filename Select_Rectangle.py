import numpy as np
import cv2
fileName = 'rec_img1.jpg'
image = cv2.imread(fileName)
# capImg = cv2.VideoCapture(0)
hsv_img = cv2.cvtColor( image, cv2.COLOR_BGR2HSV )
hsv_min = np.array((0, 0, 0), np.uint8)
hsv_max = np.array((180, 255, 245), np.uint8)
hsv_msk = cv2.inRange( hsv_img, hsv_min, hsv_max )
contours, hierarchy = cv2.findContours( hsv_msk, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for icontour in contours:
    rect = cv2.minAreaRect(icontour)
    area = int(rect[1][0] * rect[1][1])
    if area > 150:
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], -1, (255, 0, 0), 3)
cv2.imshow('hsv', hsv_msk)
cv2.imshow('contours', image)
cv2.waitKey()
cv2.destroyAllWindows()