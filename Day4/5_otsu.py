import cv2

img = cv2.imread('./rice.png', cv2.IMREAD_GRAYSCALE)

th, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsh:', th)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
