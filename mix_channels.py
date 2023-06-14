import cv2
import numpy as np


# The cv2.mixChannels function takes the following parameters:

# src: The source image or array of images from which the channels will be extracted.
# dst: The destination image or array of images where the channels will be transferred.
# fromTo: A list of index pairs specifying the source and destination channels to be mixed. Each pair contains two elements: the index of the source channel and the index of the destination channel.
# len(fromTo): The number of pairs provided in the fromTo list.
# dtype: An optional parameter that specifies the data type of the destination image. If not provided, the function will use the same data type as the source image.
# Here's an example usage of cv2.mixChannels:

#Create source and destination images
# src = np.array([[255, 0, 0],
#                 [0, 255, 0],
#                 [0, 0, 255]], dtype=np.uint8)
# dst = np.zeros((3, 3), dtype=np.uint8)

# Define the channel mixing configuration
# fromTo = [(0, 1), (1, 2), (2, 0)]  # Mix B to G, G to R, and R to B

# Mix the channels from src to dst
# cv2.mixChannels([src], [dst], fromTo)]
image = cv2.imread("apple.jpg")
cv2.imshow("Original Image",image)
cv2.waitKey()
cv2.destroyAllWindows()

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

blue_channel = np.zeros(image.shape,image.dtype)
green_channel = np.zeros(image.shape,image.dtype)
red_channel = np.zeros(image.shape,image.dtype)

cv2.mixChannels([image],[blue_channel],[0,0])
cv2.mixChannels([image],[green_channel],[1,1])
cv2.mixChannels([image],[red_channel],[2,2])

cv2.imshow("Blue Channel",blue_channel)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Green Channel",green_channel)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Red Channel",red_channel)
cv2.waitKey()
cv2.destroyAllWindows()

# Bluring the image
blurred_image_matrix=cv2.medianBlur(image,61) # second argument should be odd like 13, 61 etc
cv2.imshow("Blurred Image",blurred_image_matrix)
cv2.waitKey()
cv2.destroyAllWindows()