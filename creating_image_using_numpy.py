import numpy as np
import cv2
import matplotlib.pyplot as plt


image= np.zeros((500,500))
image[:,:] = 100
image=image[:,:]+10
image[200:300,300:400] = 255
print(image[200:300,300:400])
cv2.imwrite("F:\FallSemester23to24\ComputerVision\Codes\image.jpg",image)
cv2.imread("F:\FallSemester23to24\ComputerVision\Codes\image.jpg")
cv2.waitKey(5000)


