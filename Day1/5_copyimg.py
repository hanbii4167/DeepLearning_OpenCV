import cv2

img = cv2.imread('./dog.bmp')
#img_test = img
img_test = img.copy() # 메모리를 카피


img_test[90:210, 120:240] = (255,102,255)

cv2.imshow('img', img)
cv2.waitKey()
cv2.imshow('img_test', img_test)
cv2.waitKey()

