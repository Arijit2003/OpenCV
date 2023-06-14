import cv2
import matplotlib.pylab as plt

image=cv2.imread("apple.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
fig=plt.figure(figsize=(15,5))
ax=fig.add_subplot(121)
ax.set_title("Original",fontsize=18)
plt.imshow(image,cmap="gray")

ax=fig.add_subplot(122)
negative=255-image
ax.set_title("Negative Image",fontsize=18)
plt.imshow(negative,cmap="gray")

plt.show()
