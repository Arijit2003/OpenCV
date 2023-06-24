import cv2

#Interpolation is the process of estimating values of a continuous function from 2 discrete samples
#5 types of interpolation
#Linear, Area, Cubic, Nearest Neighbour, Sinosoidal
image=cv2.imread("nature.jpg")

Linear=cv2.resize(image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
Area=cv2.resize(image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_AREA)
Cubic=cv2.resize(image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
Nearest=cv2.resize(image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_NEAREST)

cv2.imshow("Original",image)
cv2.waitKey()

cv2.imshow("Original",Linear)
cv2.waitKey()

cv2.imshow("Area",Area)
cv2.waitKey()

cv2.imshow("Cubic",Cubic)
cv2.waitKey()

cv2.imshow("Nearest",Nearest)
cv2.waitKey()

cv2.destroyAllWindows()