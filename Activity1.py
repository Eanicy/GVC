import cv2


img = cv2.imread('image.jpg')


cv2.imshow('Normal', img)
cv2.imshow('Grayscale Flag', cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE))


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


pixel_val = img[100, 100]
print(f"Pixel value at (100,100): {pixel_val}")


_, bw_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Black and White', bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()