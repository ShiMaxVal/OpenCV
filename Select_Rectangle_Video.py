import numpy as np
import cv2
capImg = cv2.VideoCapture(0)
while(capImg.isOpened()):
    ret, frame = capImg.read()
    if frame is None:
        break
    hsv_img = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )
    hsv_min = np.array((0, 0, 0), np.uint8)
    hsv_max = np.array((180, 255, 245), np.uint8)
    hsv_msk = cv2.inRange( hsv_img, hsv_min, hsv_max )
    contours, hierarchy = cv2.findContours( hsv_msk, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for icontour in contours:
        rect = cv2.minAreaRect(icontour)
        area = int(rect[1][0] * rect[1][1])
        if area > 1500:
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    cv2.drawContours(frame, [box], -1, (255, 0, 0), 3)
    cv2.imshow('hsv', hsv_msk)
    cv2.imshow('contours', frame)
    key_press = cv2.waitKey(30)
    if key_press == ord('q'):
        break
capImg.release()
cv2.destroyAllWindows()