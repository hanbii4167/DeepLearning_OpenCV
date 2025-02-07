import cv2
import sys

cap = cv2.VideoCapture('./monkey.mp4')

if not cap.isOpened():
    print("동영상을 열 수 없어용..")
    sys.exit()

print('동영상 불러오기 성공!!')
print('가로사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
      '세로사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('FPS: ', cap.get(cv2.CAP_PROP_FPS)) #frame per second
print('총 프레임수: ', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

'''
ret,frame = cap.read()
cv2.imshow('frame',frame)
cv2.waitKey()
'''

while True :
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) == 27:
        break


cap.release()
