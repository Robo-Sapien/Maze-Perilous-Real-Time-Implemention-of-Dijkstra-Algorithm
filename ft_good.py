import numpy as np
import cv2
import goodfeatures_example as gf
from matplotlib import pyplot as plt

font=cv2.FONT_HERSHEY_SIMPLEX

img=cv2.imread('newa4.jpg')
img1=cv2.imread('newa4.jpg')
corner= gf.get_corners(img)
corner=np.float32(corner)
cv2.imshow('img_init',img)
cv2.imwrite('corners.jpg',img)
cv2.waitKey(0) & 0xFF
Z=[]
xy_list=[]
for i in corner:
    x,y=i.ravel()
    Z.append((x,y))
# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
centroid_num=9
ret,label,center=cv2.kmeans(np.asarray(Z),centroid_num,criteria,1000,cv2.KMEANS_PP_CENTERS)
center=np.int32(center)
print center[:,0]
print center[:,1]
center=center[center[:,0].argsort()]
print "center=",center

for num,j in enumerate(center):
        #print num,j
        centx,centy = j.ravel()
        xy_list.append((centx,centy))
        centroid_color= img[j[1],j[0]]
        print "cc=",centroid_color
        compcolor=np.subtract([255,255,255],centroid_color)
        compcolor=[abs(i) for i in compcolor]
        cv2.putText(img,str(num)+','+str(centroid_color),(centx,centy), font, 0.5,(255,255,255),2)
        print int(compcolor[0]),type(compcolor[0])
        cv2.circle(img,(centx,centy),3,(int(compcolor[0]),int(compcolor[1]),int(compcolor[2])),-1)
       
cv2.imshow('kmeans',img)
cv2.imwrite('kmeans.jpg',img)
cv2.waitKey(0) & 0xFF

minslist=[]

for index,(p,q) in enumerate(xy_list):
    minim=99999999
    for k in range(0,centroid_num):
        g,h=int(xy_list[index][0]),int(xy_list[index][1])
        m,n=int(xy_list[k][0]),int(xy_list[k][1])
        xparts=np.linspace(g, m, 50)
        yparts=np.linspace(h,n,50)
        #print "xparts=",xparts
        #print yparts
        bothparts=[]
        for i,lol in enumerate(xparts):
            #print i
            point=(int(xparts[i]),int(yparts[i]))
            lolmaxx= img[yparts[i],xparts[i]]
            redcolor=[36,27,237]
            if(not np.allclose(lolmaxx,redcolor,atol=40)):
                bothparts.append(point)
                cv2.circle(img,point,3,(0,255,0),-1)
        #print bothparts    
        absdist=(g-m)**2+(h-n)**2
        #absdist=abs(g-m)+abs(h-n)
        #print index,k,absdist
        if(int(absdist)<minim and absdist!=0 and ((abs(g-m)<5)or(abs(h-n)<5))):
            minim=absdist
            ming,minh,minm,minn=g,h,m,n
    #print ming,minh,minm,minn,minim
    minslist.append(((ming,minh),(minm,minn)))
    #cv2.putText(img,str((ming,minh)),(ming,minh), font, 0.5,(255,255,255),2)
print "bothparts=",bothparts
print "minslist=",minslist
npminslist=np.array(minslist,dtype=np.int32)
print "npminslist=",npminslist


##for lineno,line in enumerate(npminslist):
##    print "line=",line
##
##    #print type(line[0][0])
##    cv2.line(img,(line[0][0],line[0][1]),(line[1][0],line[1][1]),(int(line[0][0]),int(line[0][1]),255),3)
##    
##    cv2.putText(img,str(lineno),((line[0][0]+line[1][0])/2,(line[0][1]+line[1][1])/2), font, 0.7,(255,255,255),2,True)
##
##    cv2.imshow('img_kmeans',img)
##    cv2.waitKey(0) & 0xFF

print len(center)
print center
for draw in range(0,len(center)-1):
    print draw
    print center[draw],center[draw+1]
    
    cv2.line(img,(center[draw][0],center[draw][1]),(center[draw+1][0],center[draw+1][1]),(255,255,255),3)
    cv2.imshow('img_kmeans',img)
    #cv2.waitKey(0) & 0xFF
        


    
#cv2.imwrite('progress-22-9.jpg',img)
#cv2.destroyAllWindows()


