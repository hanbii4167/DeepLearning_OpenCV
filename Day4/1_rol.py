import cv2

img = cv2.imread('./sun.jpg')

#x, y, w, h
x = 182
y = 21
w = 120
h = 110

# 태양을 복사
roi = img[y:y+h, x:x+w]
roi_copy = roi.copy()

img[y: y+h, x+w: x+w+w] = roi

# 두 태양을 박스로 감싸기
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0), 3)

cv2.imshow('img', img)
cv2.imshow('roi_copy', roi_copy)
cv2.waitKey()