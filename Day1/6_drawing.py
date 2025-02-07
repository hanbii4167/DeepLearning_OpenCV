import cv2
import numpy as np

img = np.full((500, 500, 3), 255, dtype=np.uint8)
cv2.line(img, (70,70), (400,70), (0,0,255), 2) # 출발지(x,y), 도착지(x,y), 색(BGR), 두께
cv2.rectangle(img, (50,200,150,100), (155,102,255), 3) # ( 출발, 도착 (x,y) ), 색상, 두꼐
cv2.rectangle(img, (50,350,150,100), (155,102,255), -1) # -1로 하면 사각형 안이 채워진다
cv2.circle(img, (300,250), 50,(155,102,255), 4) # 원의 중심, 반지름, 색상, 두께
cv2.putText(img,'Hello OpenCV',(300,400),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)


cv2.imshow('img', img)
cv2.waitKey()