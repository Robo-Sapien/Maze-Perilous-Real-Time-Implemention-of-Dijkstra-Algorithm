import cv2
import numpy as np

cam=cv2.VideoCapture(-1)

while(cam.isOpened()):
    _,frame=cam.read()
    cv2.imshow('Video',frame)
    k=cv2.waitKey(10) & 0xFF
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray',gray)
    k=cv2.waitKey(10) & 0xFF
    _,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x,y,w,h = cv2.boundingRect(cnt)
    print x,y,w,h
    crop = frame[y:y+h,x:x+w]
    cv2.imshow('Crop',crop)
    k=cv2.waitKey(10) & 0xFF
    if(k==ord('s')):
        cv2.imwrite('cropped_arena.jpg',crop)
    
    if(k==ord(' ')): 
        cam.release()
cv2.destroyAllWindows()
