import cv2 
import numpy as np
url = 'http://192.168.8.107:8080/video'
cap = cv2.VideoCapture(url)
img_counter = 0
while(True):
    ret, frame = cap.read()
    resize = cv2.resize(frame, (640, 480), interpolation = cv2.INTER_LINEAR) 
    cv2.imshow('frame',resize)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
    elif q == ord("s"):
        img_name = "opencv_frame_{}.jpeg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
cap.release()
cv2.destroyAllWindows()