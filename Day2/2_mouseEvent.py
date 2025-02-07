import cv2
import numpy as np

oldx = oldy = 0

def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼이 눌렸어용!: %d, %d ' % (x, y))
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼이 떼졌어용!: %d, %d ' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            #print('드래그 중이에용! : %d, %d' % (x, y))
            cv2.line(img, (oldx, oldy), (x, y), (155, 51, 255), 3)
            cv2.imshow('img', img)
            oldx, oldy = x, y

img = np.ones((500,500,3), dtype=np.uint8) *255# 흰색 영상이 만들어짐
cv2.imshow('img',img)
cv2.setMouseCallback('img', on_mouse)
cv2.waitKey()