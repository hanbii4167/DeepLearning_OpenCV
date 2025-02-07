import cv2

img = cv2.imread('./candies.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

'''
HSV에서의 녹색 계열
    : 50 <= H <= 80
    : 150 <= S <= 255
    : 0 <= V <= 255 
'''
dst = cv2.inRange(hsv, (50,150,0), (80,255,255))

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey()