import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1); plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); plt.title('Original')
plt.subplot(2, 2, 2); plt.imshow(gray, cmap='gray'); plt.title('Grayscale')
plt.subplot(2, 2, 3); plt.plot(hist); plt.title('Grayscale Histogram')
plt.subplot(2, 2, 4); plt.imshow(edges, cmap='gray'); plt.title('Edges')

plt.tight_layout()
plt.show()