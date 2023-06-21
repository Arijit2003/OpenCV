import cv2
import matplotlib.pylab as plt
import numpy as np

image=cv2.imread("apple.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

fig=plt.figure(figsize=(15,5))

ax=fig.add_subplot(121)
ax.set_title("Original Image",fontsize=18)
plt.imshow(image,cmap="gray")
# s=c*r^y   here c=(1/255.0)
newImage=image/255.0
newImage=cv2.pow(newImage,1.5)

ax=fig.add_subplot(122)
ax.set_title("Power Transformation",fontsize=18)
plt.imshow(newImage,cmap="gray")

plt.show()
