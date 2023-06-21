import cv2
import numpy as np;

canvas=np.ones(shape=(1000,1000,3),dtype=np.uint8)
#LINE_4 and LINE_8 are drawn by Bresenham Algorithm
#LINE_4-->Alised  No extra boundaries--broken line 
#LINE_AA--> Antialised line---Drawn by Gaussian Filtering--Antialised=smooth line=some boundaries are added

#LINE_4
cv2.line(canvas,(0,0),(400,400),(0,255,0),6,cv2.LINE_4)
#LINE_8
cv2.line(canvas,(0,20),(400,420),(255,255,0),6,cv2.LINE_8)
#LINE_AA
cv2.line(canvas,(0,40),(400,440),(0,255,0),6,cv2.LINE_AA)


#Rectangle
cv2.rectangle(canvas,(400,400),(570,550),color=(0,255,0),thickness=-10) # any negative thickness the fills the rectangle

#circle
cv2.circle(canvas,(600,300),70,(255,0,0),5)

#arrowed line
cv2.arrowedLine(canvas,(700,600),(900,600),(255,255,255),3,tipLength=0.4)
cv2.imshow("LINE_4",canvas);

cv2.waitKey()
