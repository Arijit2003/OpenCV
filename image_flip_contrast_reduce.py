import cv2
import numpy
image=cv2.imread("scatter.png")
# cv2.imshow("Image Viewer",image)
# cv2.waitKey()
#flipped_image=cv2.flip(image,1) #flipcode=1 means the image will be flipped horizontally(180 degree)
#flipped_image=cv2.flip(image,0) #flipcode=0 means the image will be flipped vertically(180 degree)
flipped_image=cv2.flip(image,-1) #flipcode=-1 means the image will be flipped both vertically and diagonally(180 degree)
print(flipped_image.shape)

#finding height and width
height=flipped_image.shape[1]
width=flipped_image.shape[0]
#resizing image
flipped_image=cv2.resize(flipped_image,(int(height*0.4),int(width*0.4)))
print(flipped_image.shape)

# cv2.imshow("Image Viewer",flipped_image)
# cv2.waitKey()

# reducing constrast
reducedImage=cv2.bitwise_not(image)
reducedImage=cv2.resize(reducedImage,(int (height*0.4),int (width*0.4)))
cv2.imshow("Image Viewer",reducedImage)

cv2.waitKey()
print(image)
print("\n\n")
print(reducedImage)


