import cv2

image=cv2.imread("scatter.png")
blue,green,red=cv2.split(image)
cv2.imshow("Blue-Gray Scale",blue)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Green-Gray Scale",green)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Red-Gray Scale",red)
cv2.waitKey()
cv2.destroyAllWindows()

