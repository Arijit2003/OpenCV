import cv2
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(15,5))
def func_show(sub_plot:int,title:str,imageM):
    axis=fig.add_subplot(sub_plot)
    axis.set_title(title)
    plt.imshow(imageM,cmap="gray")

image=cv2.imread("j.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
func_show(141,"Orginal Image",image)
#Erosion--Removes pixels from the boundary
kernal=np.ones(shape=(5,5),dtype=np.uint8)
erosion=cv2.erode(image,kernal)
func_show(142,"Eorde Image",erosion)

#Dilation
kernal=np.ones(shape=(5*5),dtype=np.uint8)
dilation=cv2.dilate(image,kernal)
func_show(143,"Dilation Image",dilation)


#Reduce contrast
reduce_constrast=cv2.bitwise_not(image)
func_show(144,"Reduced Contrast",reduce_constrast)
plt.show()
cv2.destroyAllWindows()
