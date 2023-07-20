import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(image,(x,y),20,(0,255,0),-1)

image=np.zeros((700,800,3),np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_circle)
while(True):
    cv2.imshow("image",image)
    if(cv2.waitKey(20)==ord('q')):
        break
cv2.destroyAllWindows()