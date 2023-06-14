import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("einstein.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",image)
cv2.waitKey()

hist=cv2.equalizeHist(image)
cv2.imshow("Histogram Equalization",hist)
cv2.waitKey()
cv2.destroyAllWindows()
