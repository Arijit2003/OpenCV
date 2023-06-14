import cv2
import numpy
import random

def add_noise(img):
    row,col=img.shape
    number_of_pixels=random.randint(300,10000)
    # adding white pixels
    for i in range(number_of_pixels):
        ycord=random.randint(0,row-1)
        xcord=random.randint(0,col-1)
        img[ycord][xcord]=255
    number_of_pixels=random.randint(300,10000)
    # adding black pixels
    for i in range(number_of_pixels):
        ycord=random.randint(0,row-1)
        xcord=random.randint(0,col-1)
        img[ycord][xcord]=0

    return img

image=cv2.imread("apple.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Image", image)
cv2.waitKey()
cv2.destroyAllWindows()

noised_image=add_noise(image)
cv2.imshow("Noised Image", noised_image)
cv2.waitKey()
cv2.destroyAllWindows()

#Enhancing the image
# removing noise using medianBlur
imagewithoutnoise=cv2.medianBlur(noised_image,5)
cv2.imshow("Some noise removed",imagewithoutnoise)
cv2.waitKey()



    

