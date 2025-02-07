import cv2
import sys #시스템 관련

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없어용..")
    sys.exit()

print('카메라 연결 성공!!')
print('가로사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
      '세로사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('FPS: ', cap.get(cv2.CAP_PROP_FPS)) #frame per second

# ret: 영상을 읽어올수 있는 여부 -> true/false
# frame: 읽어온 영상 -> ndarray 로 저장 ( 이미지로 저장)
'''
ret,frame = cap.read()
cv2.imshow('frame',frame)
cv2.waitKey()

cap.release()
'''

while True:
    ret, frame = cap.read()
    if not ret :
        break
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) == 27: # 10을 넣으면 1000분의 10초 = 0.001초 / 키보드에서 27은 esc키 -> esc키를 누르면 멈추겠다!
        break

cap.release()