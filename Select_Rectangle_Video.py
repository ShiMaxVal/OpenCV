import numpy as np
import cv2
green_rect = 0
cross_way =[{}]*4
cross_way[0] = {"Forward"}
cross_way[1] = {"Left"}
cross_way[2] = {"Right"}
cross_way[3] = {"Backward"}
capImg = cv2.VideoCapture(0)
while(capImg.isOpened()):
    ret, frame = capImg.read()
    if frame is None:
        break
    hsv_img = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )
    hsv_min = np.array((55, 165, 196), np.uint8)
    hsv_max = np.array((93, 212, 248), np.uint8)
    hsv_msk = cv2.inRange( hsv_img, hsv_min, hsv_max )
    contours, hierarchy = cv2.findContours( hsv_msk, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for icontour in contours:
        rect = cv2.minAreaRect(icontour)
        area = int(rect[1][0] * rect[1][1])
        if area > 1500:
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(frame, [box], -1, (255, 0, 0), 3)
            center = (int(rect[0][0]), int(rect[0][1]))
            cv2.putText(capImg, "%d, %d" % (center[0], center[1]), (center[0] - 30, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
            if center[0] < 400:
                green_rect += 1
            else:
                green_rect += 2
   # cv2.putText(capImg, str(cross_way[green_rect]), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('hsv', hsv_msk)
    cv2.imshow('contours', frame)
    key_press = cv2.waitKey(30)
    if key_press == ord('q'):
        break
capImg.release()
cv2.destroyAllWindows()