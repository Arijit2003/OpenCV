import cv2 
import numpy as np
import matplotlib.pyplot as plt


image=np.array([
    (25,78,121,65,255),
    (34,94,10,15,87),
    (32,102,143,83,98),
    (123,104,75,204,176),
    (244,162,102,65,79),
    (253,145,75,155,100)
])
fig=plt.figure(figsize=(15,5))
#Original
axis=fig.add_subplot(141)
axis.set_title("Original Image")
plt.imshow(image,cmap="gray")
#Log Transformation
c=np.max(image)/np.log(1+np.max(image))
log=c*cv2.log(1+np.float32(image))
axis=fig.add_subplot(142)
axis.set_title("Log Transformation")
plt.imshow(log,cmap="gray")
#Power Law
#normalize
Image=image/255.0
powerLaw=cv2.pow(Image,0.5)
axis=fig.add_subplot(143)
axis.set_title("Power Law")
plt.imshow(powerLaw,cmap="gray")


#negative
negative=255-image
axis=fig.add_subplot(144)
axis.set_title("Nagative")
plt.imshow(negative,cmap="gray")
print(negative)
plt.show()