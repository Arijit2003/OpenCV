import cv2
import numpy as np

image=cv2.imread("images/apple.jpg")
rows,cols=image.shape[:2]
kernal_x=cv2.getGaussianKernel(cols,200)
kernal_y=cv2.getGaussianKernel(rows,200)
# rows*cols
kernal=kernal_y*kernal_x.T
#normalize the kernal
kernal=kernal/np.linalg.norm(kernal)

mask=255*kernal
output=np.copy(image)
for i in range(3):
    output[:,:,i]=output[:,:,i]*mask


cv2.imshow("Original Image",image)
cv2.waitKey()

cv2.imshow("Vignette Image",output)
cv2.waitKey()
cv2.destroyAllWindows()