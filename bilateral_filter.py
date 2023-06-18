import cv2
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(20,5))
def func_show(subplot:int,image,title:str):
    axis=fig.add_subplot(subplot)
    axis.set_title(title)
    plt.imshow(image,cmap="gray")



image=cv2.imread("noisyimage.jpg")
func_show(141,image,"Original Image with noise")

# Gaussian Blur
gaussianB=cv2.GaussianBlur(image,(5,5),0.79)
func_show(142,gaussianB,"Gaussian Blur")

# Median BLur
medianB=cv2.medianBlur(image,5)
func_show(143,medianB,"Median Blur")

# Bilateral Filter
bilateralImg=cv2.bilateralFilter(image,50,60,40)
func_show(144,bilateralImg,"Bilateral Filter")
plt.show()