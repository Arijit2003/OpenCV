import cv2
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(15,5))
def func_show(title:str,subplot:int,image):
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    axis=fig.add_subplot(subplot)
    axis.set_title(title)
    plt.imshow(image,cmap="gray")

image=cv2.imread("images/apple.jpg")

#Euclidan
theta=np.radians(20.0)
kernal = np.float32([
    (np.cos(theta),-np.sin(theta),34),
    (np.sin(theta),np.cos(theta),27)
])
rows,cols=image.shape[:2]
euclidean = cv2.warpAffine(image,kernal,(cols,rows))




func_show("Original Image",121,image=image)
func_show("Euclidean Image",122,image=euclidean)
plt.show()

