import cv2
from matplotlib import pyplot as plt
import os

filename = 'image.jpg'
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 100, 200)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original RGB")

plt.subplot(2,2,2)
plt.imshow(edges, cmap='gray')
plt.title("Edges")

plt.subplot(2,2,3)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")

plt.subplot(2,2,4)
plt.plot(hist)
plt.title("Histogram")
plt.show()

h, w, c = img.shape
print(f"--- Image Properties ---")
print(f"Filename: {filename}")
print(f"Format: {'RGB (BGR in OpenCV)'}")
print(f"Width: {w}px, Height: {h}px")
print(f"Size: {os.path.getsize(filename)} bytes")

print(f"Pixel (10,10) value: {img[10, 10]}")