import cv2

img = cv2.imread('./airplane.bmp')
mask = cv2.imread('./mask_plane.bmp')
dst = cv2.imread('./field.bmp')

temp = cv2.copyTo(img, mask)
cv2.copyTo(img, mask, dst) #img, mask 를 마스크 연산을 한 결과를 dst 에 넣을 수 있다.

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('temp',temp)
cv2.imshow('dst',dst)
cv2.waitKey()