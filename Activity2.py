import cv2
import numpy as np

img = cv2.imread('image.jpg')


print(f"Dimensions: {img.shape}")
print(f"Pixel at (50,50) BGR: {img[50, 50]}")


edge1 = cv2.Canny(img, 50, 150)
edge2 = cv2.Canny(img, 100, 200)
edge3 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5) 
edge4 = cv2.Laplacian(img, cv2.CV_64F)           


b, g, r = cv2.split(img)

zeros = np.zeros(img.shape[:2], dtype="uint8")
red_only = cv2.merge([zeros, zeros, r])
green_only = cv2.merge([zeros, g, zeros])
blue_only = cv2.merge([b, zeros, zeros])

cv2.imshow('Red Channel', red_only)
cv2.imshow('Green Channel', green_only)
cv2.imshow('Blue Channel', blue_only)

cv2.imshow('Canny 1', edge1)
cv2.imshow('Canny 2', edge2)
cv2.imshow('Sobel', edge3)
cv2.imshow('Laplacian', edge4)
cv2.waitKey(0)