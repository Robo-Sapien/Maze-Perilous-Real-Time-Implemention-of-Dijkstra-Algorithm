import numpy as np
import cv2
from math import sqrt
img=cv2.imread('newa4.jpg')

refPt = []
nax=[0,0,0]
min=[255,255,255]
cropping = False
#<<<<<<< HEAD
def threshold(image):
    global nax,min
    
    print nax,min
    #blur = cv2.bilateralFilter(image,9,75,75)
    #display_image(blur)
    xx=cv2.GaussianBlur(img,(5,5),0)
    #xx=cv2.cvtColor(xx,cv2.COLOR_BGR2HSV)
    [hmin,smin,vmin]=[min[0],min[1],min[2]]
    [hmax,smax,vmax]=[nax[0],nax[1],nax[2]]
    min1=np.array([hmin, smin, vmin],np.uint8)
    max1=np.array([hmax,smax,vmax],np.uint8)
    obj=cv2.inRange(xx,min1,max1)
    return obj

#=======

#are changes working 1234562234
	
#>>>>>>> refs/remotes/nikhil-97/master
def click_and_crop_max(event,x,y,flags,params):#, x, y, flags, param):
            global refPt, cropping,px,px1,nax,min
            if event == 1:
                            cropping = True
                            print 'click and crop maxx'
            if event == 4:
                            cropping = False
                            #print "y"
                            #print nax,min
            if cropping==True :
                            #px1=px
                            px=img[y,x]
                            #print px1,px
                            #print px
                            #print nax
                            for i in range(0,3):
                                if(px[i]>nax[i]):
                                    nax[i]=px[i]
                                if(px[i]<min[i]):
                                    min[i]=px[i]
                            print "nax from for=",nax
                            print "min from for=",min
                            
def click_and_crop_min(event, x, y, flags, param):
            #global refPt, cropping,px,px1,min
            print "in here"                            


def distance(x1,y1,x2,y2):
    dist=sqrt((x2-x1)**2)+((y2-y1)**2)
    return dist

def draw_triangle(x1,y1,x2,y2,x3,y3,img1):
    cv2.line(img1, (x1, y1), (x2, y2), (0,0,255))
    cv2.line(img1, (x2, y2), (x3, y3), (0,0,255))
    cv2.line(img1, (x3, y3), (x1, y1), (0,0,255))

def get_mid_points(x1,y1,x2,y2):
    return [(x1+x2)/2 , (y1+y2)/2]

def get_pointer(x1,y1,x2,y2,x3,y3,img1):
     #changes yet to be made to denote get_pointer
     #gmp0=
     #gmp1=get_mid_points(x1,y1,x2,y2)[1]
     a=distance(x3,y3,get_mid_points(x1,y1,x2,y2)[0],get_mid_points(x1,y1,x2,y2)[1])
     b=distance(x2,y2,get_mid_points(x1,y1,x3,y3)[0],get_mid_points(x1,y1,x3,y3)[1])
     c=distance(x1,y1,get_mid_points(x3,y3,x2,y2)[0],get_mid_points(x3,y3,x2,y2)[1])
     ar=[a,b,c]
     print np.amin(ar),(x1,y1),(x2,y2),(x3,y3),(get_mid_points(x2,y2,x3,y3)[0],get_mid_points(x2,y2,x3,y3)[1])
#<<<<<<< HEAD
#<<<<<<< HEAD
     if (np.amin(ar)==ar[0]):
         cv2.line(img1,(x2,y2),(get_mid_points(x2,y2,x3,y3)[0],get_mid_points(x2,y2,x3,y3)[1]),(0,0,255))
def check_key(char):
    a=cv2.waitKey(0)
    if(a==ord(char)):
        print "working"
#=======
#=======
#>>>>>>> refs/remotes/nikhil-97/master
if (np.amax(ar)==ar[2]):
 cv2.line(img1,(x1,y1),(get_mid_points(x2,y2,x3,y3)[0],get_mid_points(x2,y2,x3,y3)[1]),(0,255,0))
if (np.amax(ar)==ar[1]):
 cv2.line(img1,(x2,y2),(get_mid_points(x2,y2,x3,y3)[0],get_mid_points(x2,y2,x3,y3)[1]),(0,255,0))
if (np.amax(ar)==ar[0]):
 cv2.line(img1,(x3,y3),(get_mid_points(x2,y2,x1,y1)[0],get_mid_points(x2,y2,x1,y1)[1]),(0,255,0))
#<<<<<<< HEAD

#>>>>>>> origin/master
#=======
def temp_thresh(hmin,vmin,smin,hmax,vmax,smax,image):
    min=np.array([hmin, smin, vmin],np.uint8)
    max=np.array([hmax,smax,vmax],np.uint8)
    obj=cv2.inRange(image,min,max)
    return obj
#>>>>>>> refs/remotes/nikhil-97/master
def display_image(image):
    cv2.imshow('image',image)
    cv2.setMouseCallback("image",click_and_crop_max)
    print 'showing image'
    k = cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

#<<<<<<< HEAD
#<<<<<<< HEAD
draw_triangle(1,45,23,56,6,47,img)
k=cv2.waitKey(0) & 0xFF
print k
print distance(1,2,34,56),get_pointer(1,45,23,56,6,47,img)
#=======
draw_triangle(34,78,21,45,90,56,img)
print distance(1,2,34,56),get_pointer(34,78,21,45,90,56,img)
#>>>>>>> origin/master
display_image(img)
m=cv2.waitKey(0) & 0xFF
if (m):
    print "coming here"
    T=threshold(img)
    display_image(T)
    cv2.waitKey(0) & 0xFF
print "I'm here lol"
#=======
draw_triangle(34,78,21,45,90,56,img)
print distance(1,2,34,56),get_pointer(34,78,21,45,90,56,img)
display_image(img)
thresh=temp_thresh(0,0,0,255,255,255,img)
display_image(thresh)

#>>>>>>> refs/remotes/nikhil-97/master
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
display_image(gray)
