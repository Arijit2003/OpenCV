import cv2
import numpy as np

#canavs
canvas=np.zeros(shape=(600,600,3))

# polygon-array
poly=np.array([[100,80],[10,200],[270,400],[490,350],[290,110],[90,150]],dtype=np.int32)
poly=poly.reshape((-1,1,2))

cv2.polylines(canvas,[poly],True,(255,0,255),3)
cv2.imshow("Polygon",canvas)
cv2.waitKey()
