import cv2
import numpy as np
import matplotlib.pylab as plt

fig=plt.figure(figsize=(15,5))
def func_show(subplot:int,image,title:str):
    axis=fig.add_subplot(subplot)
    axis.set_title(title)
    plt.imshow(image,cmap="gray")



image=cv2.imread("apple.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Original Image
func_show(141,image,"Original Image")

#Log Transformation
#s=c*(log(1+r))
c=np.max(image)/(np.log(1+np.max(image)))
log_trans=c*(np.log(1+np.float32(image)))
func_show(142,log_trans,"Log Transformation")

# Negative
negative=255-image
func_show(143,negative,"Negative")

#Gamma
#s=c*r^y
#c is used to make the pixel values between 0-1
binImage=image/255.0
gamma=cv2.pow(binImage,1.6)
func_show(144,gamma,"Gamma Transformation")
plt.show()
