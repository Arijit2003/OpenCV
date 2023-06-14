import cv2
import matplotlib.pylab as plt
import numpy as np

image=cv2.imread("apple.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# c=0.6
log_trans=0.6*(np.log(1+np.float32(image)))
fig=plt.figure(figsize=(15,5))

ax=fig.add_subplot(121)
ax.set_title("Original Image",fontsize=18)
plt.imshow(image,cmap="gray")

ax=fig.add_subplot(122)
ax.set_title("Log Transformation",fontsize=18)
plt.imshow(log_trans,cmap="gray")

plt.show()
