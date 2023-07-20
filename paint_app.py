import cv2
import numpy as np
import math
mode=True  #mode=True means draw rectangle
draw=False
a,b=-1,-1
def onChange(value):
    global mode
    if(value==0):
        mode=True
    else:
        mode=False

def draw_circle(event,x,y,flags,param):
    global a,b,draw,mode
    if(event==cv2.EVENT_LBUTTONDOWN):
        a,b=x,y
        draw=True
    elif(event==cv2.EVENT_MOUSEMOVE):
        if(draw):
            if(mode==True):
                cv2.rectangle(canvas,(a,b),(x,y),(0,255,255),-1)
            elif(mode==False):
                cv2.circle(canvas,(x,y),(a-x),(0,255,12),-1)
    elif(event==cv2.EVENT_LBUTTONUP):
        draw=False
        if(mode):
            cv2.rectangle(canvas,(a,b),(x,y),(0,255,255),-1)
        else:
            cv2.circle(canvas,(x,y),(a-x),(0,255,12),-1)


cv2.namedWindow("Track")
cv2.createTrackbar("shape","Track",0,1,onChange)

cv2.namedWindow("PAINT")
cv2.setMouseCallback("PAINT",draw_circle)
canvas=np.zeros((700,700,3),np.uint8)

while(True):
    cv2.imshow("PAINT",canvas)
    if(cv2.waitKey(20)==ord('q')):
        break
cv2.destroyAllWindows()

