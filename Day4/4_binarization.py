import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./cells.png', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])

# a: thresh, 100
s, dst1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# b: thresh, 210
b, dst2 = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)

cv2.imshow('img',img)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)

plt.plot(hist)
plt.show()
cv2.waitKey()