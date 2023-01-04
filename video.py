import cv2
print (cv2.__version__)
capImg = cv2.VideoCapture(0)
while(True):
    ret, frame = capImg.read()
    cv2.imshow('Video', frame)
    key_press = cv2.waitKey(30)
    if key_press == ord('q'):
        break
capImg.release()
cv2.destroyAllWindows()