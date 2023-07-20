import cv2

img = cv2.imread("apple.jpg") 
rows,cols=img.shape[:2]
img=cv2.resize(img,(int(0.7*cols),int(0.8*rows)))
  
t_lower = 100 # Lower Threshold
t_upper = 200 # Upper threshold
aperture_size = 5 # Aperture size
L2Gradient = True # Boolean
  
# Applying the Canny Edge filter with L2Gradient = True
edge = cv2.Canny(img, t_lower, t_upper, L2gradient = L2Gradient )
  
cv2.imshow('original', img)
cv2.imshow('edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()