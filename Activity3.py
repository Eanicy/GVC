import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('image.jpg')
img2 = cv2.imread('image.jpeg')

if img1 is None or img2 is None:
    print("Error: Ensure both image.jpg and image.jpeg are in the directory.")
else:
    plt.figure(figsize=(15, 10))
    colors = ('b', 'g', 'r')

    # --- IMAGE 1 ---
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title('Original: image.jpg')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img1], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
    plt.title('RGB Histogram: Image 1')

    # --- IMAGE 2 ---
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.title('Original: image.jpeg')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
    plt.title('RGB Histogram: Image 2')

    plt.tight_layout()
    plt.show()