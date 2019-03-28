import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    sucess,img =cap.read()
    cv2.imshow("img",img)
    k=cv2.waitKey(1)
    if k ==27:
        cv2.destoryAllwindow()
        break
    elif k==ord("s"):
        cv2.imwrite("image_.jpg",img)
        
        break
cap.release()


