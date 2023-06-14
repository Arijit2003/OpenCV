import cv2

image=cv2.imread("scatter.png",cv2.IMREAD_COLOR)
gray1=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(gray1)

newimage=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
gray2=cv2.cvtColor(newimage,cv2.COLOR_BGR2GRAY)
print("\n\n")
print(gray2)

cv2.imshow("Image Viewer",gray2)
cv2.waitKey()