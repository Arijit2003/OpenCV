import cv2
import numpy as np

image=cv2.imread("apple.jpg")

blurredImage=cv2.medianBlur(image,51)

cv2.imshow("Original",image)
cv2.waitKey()

cv2.imshow("Blurred Image",blurredImage)
cv2.waitKey()


kernal_sharpen=np.array([(0,-1,0),(-1,5,-1),(0,-1,0)])
newImage=cv2.filter2D(blurredImage,-1,kernal_sharpen)

cv2.imshow("Next Image ",newImage)
cv2.waitKey()
cv2.destroyAllWindows()
