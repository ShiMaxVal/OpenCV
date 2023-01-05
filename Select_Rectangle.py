import numpy as np
import cv2
fileName = 'Cross_back.jpg'
image = cv2.imread(fileName)
# capImg = cv2.VideoCapture(0)
hsv_img = cv2.cvtColor( image, cv2.COLOR_BGR2HSV )
hsv_min = np.array((50, 180, 0), np.uint8)
hsv_max = np.array((73, 205, 180), np.uint8)
hsv_msk = cv2.inRange( hsv_img, hsv_min, hsv_max )
contours, hierarchy = cv2.findContours( hsv_msk, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for icontour in contours:
    rect = cv2.minAreaRect(icontour)
    area = int(rect[1][0] * rect[1][1])
    if area > 1500:
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], -1, (255, 0, 0), 3)
        center = (int(rect[0][0]), int(rect[0][1]))
        cv2.putText(image, "%d, %d" % (center[0], center[1]), (center[0]-30, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.imshow('hsv', hsv_msk)
cv2.imshow('contours', image)
cv2.waitKey()
cv2.destroyAllWindows()