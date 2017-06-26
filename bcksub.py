import cv2
import numpy as np


cam=cv2.VideoCapture(-1)


# while True:
# 	_,frame=cam.read()
# 	cv2.imshow('Video',frame)
# 	k=cv2.waitKey(10) & 0xFF
# 	if(k==ord(' ')):
# 		cv2.imwrite('arena_image.jpg',frame)
# 		break

#back_img=cv2.imread('arena_image.jpg')

fgbg = cv2.BackgroundSubtractorMOG2()

while True:
	retval,frame=cam.read()
	if retval:
		sub = fgbg.apply(frame)
		cv2.imshow('subbed',sub)
		cv2.imshow('Video',frame)
		k=cv2.waitKey(10) & 0xFF
		if(k==ord(' ')):
			break
cam.release()
cv2.destroyAllWindows()
