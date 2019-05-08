
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    lower_range = np.array([130,50,50])
    upper_range = np.array([180,200,150])

    mask = cv2.inRange(hsv,lower_range,upper_range)
    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        
        break

cv2.destroyALLWindows()
cap.release()
