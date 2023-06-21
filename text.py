import cv2
import numpy as np

#canvas
canvas=np.zeros(shape=(500,500,3))

fonts = [cv2.FONT_HERSHEY_COMPLEX,
         cv2.FONT_HERSHEY_COMPLEX_SMALL,
         cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
         cv2.FONT_HERSHEY_DUPLEX,
         cv2.FONT_HERSHEY_PLAIN,
         cv2.FONT_HERSHEY_SIMPLEX,
         cv2.FONT_HERSHEY_TRIPLEX,
         cv2.FONT_HERSHEY_SCRIPT_COMPLEX]

position=(10,40)
for i in range(8):
    cv2.putText(canvas,"Hi I am Arijit",position,fonts[i],1.5,(225,225,225),2,cv2.LINE_AA)
    position=(position[0],position[1]+40)

cv2.imshow("Text",canvas)
cv2.waitKey(0)