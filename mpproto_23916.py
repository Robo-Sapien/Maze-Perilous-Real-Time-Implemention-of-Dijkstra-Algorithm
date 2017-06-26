import numpy as np
import cv2
import goodfeatures_example as gf
import shortest_path_algorithm as spa
import new091016 as botmover
#import serial
from sys import exit

#comport=str(raw_input("Enter port name     ")).upper()
#btbaudrate=int(raw_input("Enter baudrate     "))
#print comport,btbaudrate
#try:
#   ser=serial.Serial(port=comport,baudrate=btbaudrate)
 #   print "Serial comm initialized"
#except:
    #comport='COM5'
    #ser=serial.Serial(port=comport,baudrate=btbaudrate)
    #print "Error"
#exit()
    
font = cv2.FONT_HERSHEY_SIMPLEX

cam=cv2.VideoCapture(-1)
while(cam.isOpened()):
    _,initframe=cam.read()
    cv2.imshow('Image',initframe)
    
    k=cv2.waitKey(0) & 0xFF
    if(k==ord('c')):
        cv2.imwrite('arena_image.jpg',initframe)
        cam.release()
       
image_of_arena='newa4.jpg' #change this to 'arena_image.jpg' during actual run
       
img = cv2.imread(image_of_arena)
ht, wt, ch = img.shape  #get height,width,channel of the image
img1 = img.copy()

corner = gf.get_corners(img)

corner = np.float32(corner)

cv2.imshow('img_init',img)

cv2.imwrite('corners.jpg',img)

cv2.waitKey(1) & 0xFF

Z = []
xy_list = []
for i in corner:
    x, y = i.ravel()
    Z.append((x, y))
# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
centroid_num = 9
ret,label,center = cv2.kmeans(np.asarray(Z),centroid_num,criteria,1000,cv2.KMEANS_PP_CENTERS)
center = np.int32(center)
center = center[center[:,0].argsort()]
print "center=",center
dict_of_centres = {}

for num, j in enumerate(center):
        ###print num,j
        centx,centy = j.ravel()       
        xy_list.append((centx,centy))
        key=chr(num+97)
        dict_of_centres.update({key:(centx,centy)})
        cv2.putText(img,key,(centx,centy), font, 0.5,(255,255,255),2)

        centroid_color= img[j[1],j[0]]
        ###print "cc=",centroid_color
        compcolor=np.subtract([255,255,255],centroid_color)
        compcolor=[abs(i) for i in compcolor]
        cv2.circle(img,(centx,centy),3,(int(compcolor[0]),int(compcolor[1]),int(compcolor[2])),-1)

print dict_of_centres
cv2.imshow('kmeans',img)
cv2.waitKey(1) & 0xFF

connected_centres=[]
threshold=40000

edges_list=[]

def dist((x1,y1),(x2,y2)):
    return ((x2-x1)**2+(y2-y1)**2)

edges_with_keys=[]
print 'Working......'
for i in range(0,len(center)):
    for j in range(i,len(center)):
        #print "i,j=",(i,j)
        if(i!=j):
                ##print center[i] ,center[j]
                p=img.copy()
                
                cv2.line(p,(center[i][0],center[i][1]),(center[j][0],center[j][1]),[0,0,0],2)
                bkgsub=img-p
                #cv2.imshow('line image',bkgsub)
                #cv2.imshow('bc',bkgsub)
                #cv2.waitKey(10)
                summation= np.sum(np.sum(bkgsub))
                #print summation
                if(summation<=threshold):
                    connected_centres.append(((center[i][0],center[i][1]),(center[j][0],center[j][1])))
                    
                    lolz1=dict_of_centres.keys()[dict_of_centres.values().index((center[i][0],center[i][1]))]
                    lolz2=dict_of_centres.keys()[dict_of_centres.values().index((center[j][0],center[j][1]))]
                    edges_with_keys.append((lolz1,lolz2,dist((center[i][0],center[i][1]),(center[j][0],center[j][1]))))
                    cv2.waitKey(1)

print "connected_centres=",connected_centres

print "**********************edges list*******************************"
print edges_with_keys

##for y,_ in enumerate(connected_centres):
##    cv2.line(img,connected_centres[y][0],connected_centres[y][1],(255,255,255),2)
##    #cv2.putText(img,str(y)+' '+str(connected_centres[y][0]),connected_centres[y][0], font, 0.5,(64,64,255),2)
##    #cv2.imshow('lines',img)
##    cv2.waitKey(1)

routemap=[('a','e'),('e','i'),('i','c')]
for route in routemap:
    graph_obj=spa.Graph()

    for ver in dict_of_centres:
        graph_obj.add_vertex(ver)
        ##print qer
    for bc in edges_with_keys:
        ##print bc
        graph_obj.add_edge(bc[0],bc[1],bc[2])


    #print route
    spa.dijkstra(graph_obj, graph_obj.get_vertex(route[0]), graph_obj.get_vertex(route[1])) 

    target = graph_obj.get_vertex(route[1])
    #print "target=" ,target
    path = [target.get_id()]
    #print "path=",path 
    spa.shortest(target, path)
    if(route[0]!=path[0] and route[1]!=path[-1]):
        path.reverse() 
    print 'The shortest path : %s' %(path)
    #for pat in path:
        #cv2.circle(img1,dict_of_centres[pat],10,(255,255,255),1)
        #print "pat=",dict_of_centres[pat]
    #print len(path)
    for index in range(len(path)-1):
        goto=dict_of_centres[path[index]]
        goal=dict_of_centres[path[index+1]]
        pos_threshold=50
        while((abs(goto[0]-goal[0])>=pos_threshold)or(abs(goto[1]-goal[1])>=pos_threshold)):
            print abs(goto[0]-goal[0]),abs(goto[1]-goal[1])
            print botmover.next_pos(img,goto,goal)
            (goto,xdir,ydir)=botmover.next_pos(img,goto,goal)
            print "goto=",goto
            print "xdir=",xdir,"  ydir=",ydir
            cv2.imshow('passing image',img)
            cv2.circle(img,goto,index,(0,255,0),1)
            pose_of_bot=None
            # assume bot is in +y direction
            if(xdir==0 and ydir>0):
                print "Straight"
                #ser.write(bytes('F'))
            elif(xdir>0 and ydir==0):
                print "Right"
                #send bot right
                #ser.write('R')
            elif (xdir<0 and ydir==0):
                # send bot left
                print "Left"
                #ser.write('L')
            elif (xdir==0 and ydir<0):
                # send bot back
                 print "Back"
                 #ser.write(bytes('B'))
            cv2.waitKey(1000) & 0xFF

print "Program finished."
cv2.imshow('kmeans' , img)
#ser.write('Z')
cv2.waitKey(5000) & 0xFF

#cv2.destroyAllWindows()
