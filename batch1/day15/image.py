import cv2

# Load an color image in grayscale
img = cv2.imread('f1.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()