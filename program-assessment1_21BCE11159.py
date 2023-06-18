import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

"""
1.How can OpenCV be used to perform basic image transformations 
such as resizing, cropping, and rotating an image?
(log/power log /negative transformer)   """

#create figure obj
fig=plt.figure(figsize=(15,10))
def func_show(subplot:int,image,title:str):
    axis=fig.add_subplot(subplot)
    axis.set_title(title)
    plt.imshow(image,cmap="gray")
    print(image.shape)



#original image
image=cv2.imread("nature.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
func_show(241,image,"Original Image")

# resize using resize() method
height,width=image.shape[:2]
resized_method_img=cv2.resize(image,(int(width*0.7),int(height*0.4)))
func_show(242,resized_method_img,"Resized Image")

#resize using filter/kernal
resize_kernal=np.float32([(1.5,0,0),(0,1.2,0),(0,0,1)])
resizedImg=cv2.warpPerspective(image,resize_kernal,(width,height))
func_show(243,resizedImg,"Resized Image-Kernal")


#cropping
newWidth=int(width*0.5)
newHeight=int(height*0.7)
croppedImg=image[:newHeight,:newWidth]
func_show(244,croppedImg,"Cropped Image")


# rotate
angle=np.radians(30)
rotate_kernal=np.float32([
    ( np.cos(angle),-(np.sin(angle)),0 ),
    ( np.sin(angle),np.cos(angle),0 ),
    ( 0,0,1)
])
rotateImg=cv2.warpPerspective(image,rotate_kernal,(width,height))
func_show(245,rotateImg,"30 deg rotation")


# log transformation--s=c*log(1+r)
#--normalize
normalize=image/100.0
log_img=cv2.log(1+normalize)
func_show(246,log_img,"Log Transformation")


#Negative Transformation
negative=cv2.bitwise_not(image) # or 255-image
func_show(247,negative,"Negative Transformation")
plt.show()




"""
2.What are some popular OpenCV algorithms or techniques used for 
image filtering and noise reduction?
(median filter/ morphological operations)
"""
# Ans: Linear Filter: Average Filter, Gaussian Filter, 
# Nonlinear Filter: Median Filter and Bilateral Filter--For noise reduction

fig2=plt.figure(figsize=(15,10))
def func_show2(subplot:int,image,title:str):
    axis=fig2.add_subplot(subplot)
    axis.set_title(title)
    plt.imshow(image,cmap="gray")
    print(image.shape)

def add_noise(img):
    row,col=img.shape[:2]
    number_of_pixels=random.randint(300,10000)
    # adding white pixels
    for i in range(number_of_pixels):
        ycord=random.randint(0,row-1)
        xcord=random.randint(0,col-1)
        img[ycord,xcord]=255
       
    number_of_pixels=random.randint(300,10000)
    # adding black pixels
    for i in range(number_of_pixels):
        ycord=random.randint(0,row-1)
        xcord=random.randint(0,col-1)
        img[ycord,xcord]=0
    return img



#original image
image=cv2.imread("apple.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image=add_noise(image)
func_show2(241,image,"Original Image")


# Average Filter
avg_kernal=(np.array([(1,1,1),(1,1,1),(1,1,1)],dtype=np.float32))/9.0
avg_image=cv2.filter2D(image,-1,avg_kernal) # -1 means output image's datatype will be the same as souce image's
func_show2(242,avg_image,"Average Filter-Blur")


#Gussian Filter--More Detail-Less Info loss
gaussianImg=cv2.GaussianBlur(image,(5,5),51)
func_show2(243,gaussianImg,"Gaussian Filter-Blur")


#Median Filter
medianImg=cv2.medianBlur(image,51)
func_show2(244,medianImg,"Median Filter-Blur")


#Bilateral Filter
bilateralImg=cv2.bilateralFilter(image,9,1.433,1)
func_show2(245,bilateralImg,"Bilateral Filter")


# Morphological operations
#Original
j=cv2.imread("j.jpg",cv2.IMREAD_GRAYSCALE)
func_show2(246,j,"Original Image")

#dilation
ones_kernal=np.ones(shape=(3,3),dtype=np.uint8)
dilation=cv2.dilate(j,ones_kernal)
func_show2(247,dilation,"Dilation")

#erosion
erosion=cv2.erode(j,ones_kernal)
func_show2(248,erosion,"Erosion")
plt.show()



"""
3.What are some common image enhancement techniques in OpenCV 
for adjusting image brightness and contrast to improve the overall 
appearance of an image?(ex: histogram equalizer)
"""

fig3=plt.figure(figsize=(15,10))
def func_show3(subplot:int,image,title:str):
    axis=fig3.add_subplot(subplot)
    axis.set_title(title)
    plt.imshow(image,cmap="gray")
    print(image.shape)

# Original Image
einstein=cv2.imread("einstein.jpg",cv2.IMREAD_GRAYSCALE)
func_show3(131,einstein,"Original")


# Histogram Equalizer
hist_einstein=cv2.equalizeHist(einstein)
func_show3(132,hist_einstein,"Histogram Equalize")



# PowerLaw / Gamma Transformartion
#normalize
normEinstein=einstein/255.0
outEinstein=cv2.pow(normEinstein,1.8)
func_show3(133,outEinstein,"Gamma Transformation")
plt.show()