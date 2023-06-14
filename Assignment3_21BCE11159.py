import cv2
import matplotlib.pyplot as plt
import numpy as np

# create an object of figure
fig=plt.figure(figsize=(15,10))
axis=fig.add_subplot(241)
axis.set_title("Original Image")

image=cv2.imread("apple.jpg")
height,width,channel=image.shape
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image,cmap="gray")


#translation
translation_filter=np.float32([(1,0,60),(0,1,60),(0,0,1)])
transImage=cv2.warpPerspective(image,translation_filter,(width,height))
axis=fig.add_subplot(242)
axis.set_title("Translated Image")
plt.imshow(transImage,cmap="gray")


#Image Scaling
scale_matrix=np.float32([(0.9,0,0),(0,0.7,0),(0,0,1)])
scaleImage=cv2.warpPerspective(image,scale_matrix,(width,height))
axis=fig.add_subplot(243)
axis.set_title("Scaled Image")
plt.imshow(scaleImage,cmap="gray")

#Image Shearing --Shearing in X direction
shearing_kernal = np.float32([(1,0.5,0),(0,1,0),(0,0,1)])
shearedImage=cv2.warpPerspective(image,shearing_kernal,(width,height))
axis=fig.add_subplot(244)
axis.set_title("Image Shearing")
plt.imshow(shearedImage,cmap="gray")

#Reflection in x axis
reflect_kernal=np.float32([(1,0,0),(0,-1,height),(0,0,1)])
reflectedImage=cv2.warpPerspective(image,reflect_kernal,(width,height))
axis=fig.add_subplot(245)
axis.set_title("Reflected Image")
plt.imshow(reflectedImage,cmap="gray")

#Rotation
angle=np.radians(10)
rotation_kernal=np.float32([
                    [np.cos(angle), -(np.sin(angle)), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1]])

rotated_image=cv2.warpPerspective(image,rotation_kernal,(width,height))
axis=fig.add_subplot(246)
axis.set_title("Roation")
plt.imshow(rotated_image,cmap="gray")


#crop image
cropped_image=image[100:600,100:600]
axis=fig.add_subplot(247)
axis.set_title("Cropped Image")
plt.imshow(cropped_image,cmap="gray")

# Morphological Operations
ones_kernal=np.ones((3,3),np.uint8)
dilation=cv2.dilate(image,ones_kernal)
axis=fig.add_subplot(248)
axis.set_title("Dilation")
plt.imshow(dilation,cmap="gray")



plt.show()




