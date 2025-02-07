import cv2
import sys

cap1 = cv2.VideoCapture('./monkey.mp4')
cap2 = cv2.VideoCapture('./cow.mp4')

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps1= cap1.get(cv2.CAP_PROP_FPS)
fps2= cap2.get(cv2.CAP_PROP_FPS)

'''
print(w)
print(h)
print(frame_cnt1)
print(frame_cnt2)
print(fps1)
print(fps2)
'''

fourcc = cv2.VideoWriter.fourcc(*'DIVX') #압축
out = cv2.VideoWriter('mix.avi', fourcc, fps1, (w, h))

for i in range(frame_cnt1): #영상 읽어오기 -> 하나의 동영상이 끝나기전까지 프레임가져와서 저장하고를 반복
    ret, frame = cap1.read()
    cv2.imshow('output',frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break


for i in range(frame_cnt2):
    ret, frame = cap2.read()
    cv2.imshow('output',frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break

cap1.release()
cap2.release()
out.release()  #저장하고 메모리에서 제거
