import cv2
from skimage import filters
image=cv2.imread("images/balloons.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

sobel=cv2.Sobel(image,ddepth=-1,dx=1,dy=1)
canny=cv2.Canny(image,80,100)
prewitt=filters.prewitt(image)
robert=filters.roberts(image)
cv2.imshow("Sobel",sobel)
cv2.waitKey()
cv2.imshow("canny",canny)
cv2.waitKey()
cv2.imshow("Prewitt",prewitt)
cv2.waitKey()
cv2.imshow("Robert",robert)
cv2.waitKey()
