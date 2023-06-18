import cv2
import numpy as np

image=cv2.imread("apple.jpg")

mblurredImage=cv2.medianBlur(image,51)
gBlurredImage=cv2.GaussianBlur(image,(5,5),51)



cv2.imshow("Original",image)
cv2.waitKey()

cv2.imshow("Median Blurred Image",mblurredImage)
cv2.waitKey()

cv2.bilateralFilter()

cv2.imshow("Gaussian Blurred Image",gBlurredImage)
cv2.waitKey()
print(image.shape)
print(mblurredImage.shape)
print(gBlurredImage.shape)


cv2.destroyAllWindows()
