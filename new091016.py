import numpy as np
import cv2

def dist((x1,y1),(x2,y2)):
    return ((x2-x1)**2+(y2-y1)**2)
    
def next_pos(img,bot_pos,goal):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    ret,thresh2 = cv2.threshold(gray,75,255,cv2.THRESH_BINARY_INV)
    ht,wd,ch=img.shape
    cv2.imshow('thresh',thresh2)
    cv2.waitKey(1)
    
    #bot_pos = current position of bot
    # goal = where you have to go
    botx,boty=bot_pos[0],bot_pos[1]
    goalx,goaly=goal[0],goal[1]
    # x,y coords of bot,goal
    frsqrs=[(botx+20,boty),(botx-20,boty),(botx,boty+20),(botx,boty-20)]
    # consider boundary of four squares,with distance +/- 30 from botx,boty
    
    allow=[]
    # allowed points where bot can go

    for f in frsqrs:  
        if(f[0]<ht and f[1]<wd):
            # check so that boundary doesn't shoot image dimensions
            # cv2.circle(img,f,5,(0,255,255),-1)
            
            if(thresh2[f[1],f[0]]==255):
                allow.append(f)
                # append allowed points to a list
                # allowed points are the points which have value 255(aka white) on thresholded image
                # aka black path on main image

    minallow=99999999999
    next_bot_pos=bot_pos
    
    for a in allow:
        #cv2.circle(img,a,5,(255,255,255),1)
        distance=dist(a,goal)
        # distance between current position and goal
        if(distance<minallow):
            # choose the point minimal distance from goal 
            minallow=distance
            next_bot_pos=a
    return (next_bot_pos,next_bot_pos[0]-bot_pos[0],next_bot_pos[1]-bot_pos[1])

if __name__=='__main__':
    img=cv2.imread('newa4.jpg')

    dict_centres={'a': (125, 110), 'c': (246, 24), 'b': (140, 285), 'e': (247, 180), 'd': (247, 110), 'g': (293, 371), 'f': (247, 269), 'i': (402, 109), 'h': (394, 287)}

    centres=[(125,110),(140,285),(246,24),(247,110),(247,180),(247,269),(293,371),(394,287),(402,109)]

    #for i in centres:
        # cv2.circle(img,i,3,(255,255,255),-1)

    bot_pos=dict_centres['a']
    #starting bot position
    # cv2.circle(img,bot_pos,4,(255,255,255),1)

    goal=dict_centres['e']
    #goal
    print "goal=",goal

    cv2.imshow('image',img)
    cv2.waitKey(0) & 0xFF

    #print next_pos(img,bot_pos,goal)
    goto=bot_pos
    # goto is to where bot should go
    pos_threshold=30
    
    
        # cv2.circle(img,goto,5,(255,0,0),1)
    cv2.imshow('image',img)
    cv2.waitKey(100)
    ## cv2.circle(img,next_bot_pos,3,(0,255,0),-1)
    cv2.imshow('final',img)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
