import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while(cam.isOpened()):
    _,frame=cam.read()





    cv2.imshow('Video',frame)
    k=cv2.waitKey(10) & 0xFF
    if(k==ord(' ')):
        cam.release()
cv2.destroyAllWindows()
