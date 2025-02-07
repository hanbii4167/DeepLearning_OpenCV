import cv2

print ('현재 OpenCV CV 버전 : ',cv2.__version__)

# 그레이스케일 영상
#img = cv2.imread('./dog.bmp',cv2.IMREAD_GRAYSCALE)
#print(img)

# 트루컬러 영상
img = cv2.imread('./dog.bmp') #IMREAD_COLOR 써도 되지만 생략해도 자동으로 트루컬러로 읽어온다.
print(img)


cv2.imshow('img',img)
cv2.waitKey()
