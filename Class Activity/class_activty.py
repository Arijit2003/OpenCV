import cv2 
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(figsize=(15,10))
def func_show(subplot:int,title:str,image):
    axis=fig.add_subplot(subplot)
    axis.set_title(title)
    plt.imshow(image,cmap="gray")

#  Different Blur techniques
#original image
image=cv2.imread("noisyimage.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
func_show(241,"Original Image",image);
# Average Blue
averagekernal=np.ones((3,3),dtype=np.uint8)/9
avg_image=cv2.filter2D(image,-1,averagekernal)
func_show(242,"Average FIlter",avg_image)

# Median BLur
medianImage=cv2.medianBlur(image,15)
func_show(243,"Median Blur",medianImage)


# Gaussian BLur
gaussianBlur=cv2.GaussianBlur(image,(3,3),15)
func_show(244,"Gaussian  Blur",medianImage)



# Morphological 
# dilation
#original Image
j_original=cv2.imread("j.jpg")
j_original=cv2.cvtColor(j_original,cv2.COLOR_BGR2GRAY)
func_show(245,"Image J",j_original)


# Dilation
kernal=np.ones((3,3),dtype=np.uint8)
dialtion=cv2.dilate(j_original,kernal)
func_show(246,"Dilation J",dialtion)


# Erosion
kernal=np.ones((3,3),dtype=np.uint8)
erosion=cv2.erode(j_original,kernal)
func_show(247,"Erosion J",erosion)
plt.show()
