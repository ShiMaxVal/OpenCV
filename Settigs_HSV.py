import numpy as np
import cv2
def nothing(*arg):
 pass
cv2.namedWindow('Set')
cv2.createTrackbar('h1', 'Set', 0, 180, nothing)
cv2.createTrackbar('s1', 'Set', 0, 255, nothing)
cv2.createTrackbar('v1', 'Set', 0, 255, nothing)
cv2.createTrackbar('h2', 'Set', 180, 180, nothing)
cv2.createTrackbar('s2', 'Set', 255, 255, nothing)
cv2.createTrackbar('v2', 'Set', 255, 255, nothing)
capImg = cv2.VideoCapture(0)
while(capImg.isOpened()):
    ret, frame = capImg.read()
    if frame is None:
        break
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
    cl_pr = False
    while True:
        h1 = cv2.getTrackbarPos('h1', 'Set')
        s1 = cv2.getTrackbarPos('s1', 'Set')
        v1 = cv2.getTrackbarPos('v1', 'Set')
        h2 = cv2.getTrackbarPos('h2', 'Set')
        s2 = cv2.getTrackbarPos('s2', 'Set')
        v2 = cv2.getTrackbarPos('v2', 'Set')
        h_min = np.array((h1, s1, v1), np.uint8)
        h_max = np.array((h2, s2, v2), np.uint8)
        RealTimeMask = cv2.inRange(frame_hsv, h_min, h_max)
        cv2.imshow('Original', frame)
        cv2.imshow('result', RealTimeMask)
        key_press = cv2.waitKey(30)
        if key_press == ord('n'):
            break
        elif key_press == ord('q'):
            # нужно сделать сохранение настроек в файл
            cl_pr = True
            break
    if cl_pr:
        break
capImg.release()
cv2.destroyAllWindows()

