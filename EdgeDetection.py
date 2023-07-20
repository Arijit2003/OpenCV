import cv2

#Sobel 1st order derivative
image=cv2.imread("images/apple.jpg")
sobelImagex=cv2.Sobel(image,ddepth=-1,dx=1,dy=0)
cv2.imshow("Edge Detection--Sobel X",sobelImagex)
cv2.waitKey()

sobelImagey=cv2.Sobel(image,ddepth=-1,dx=0,dy=1)
cv2.imshow("Edge Detection--Sobel Y",sobelImagey)
cv2.waitKey()

sobelXY=cv2.addWeighted(sobelImagex,0.5,sobelImagey,0.5,0)
cv2.imshow("Edge Detection--Sobel XY",sobelXY)
cv2.waitKey()

#Scharr  1st order derivative
scharrImage=cv2.Scharr(image,ddepth=-1,dx=0,dy=1)
cv2.imshow("Edge Detection--Scharr",scharrImage)
cv2.waitKey()

#Laplacian -- 2nd Order derivative
laplacianImage=cv2.Laplacian(image,ddepth=-1,ksize=3)
cv2.imshow("Edge Detection-Laplacian",laplacianImage)
cv2.waitKey()

#Canny Edge
cannyImage=cv2.Canny(image,70,100)
cv2.imshow("Edge Detection-Laplacian",cannyImage)
cv2.waitKey()