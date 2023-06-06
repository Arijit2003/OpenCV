import numpy as np
import cv2
import matplotlib.pyplot as plt

image=np.random.randint(2,size=(3,500,500))
image[0:2,:,:]=255
image[2,:,:]=51
print(image)
print("\n")
print(image.T)
cv2.imwrite("image2.jpeg",image.T)


img=cv2.imread("image2.jpeg")
plt.imshow(img)
plt.show()
