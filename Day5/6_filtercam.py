import cv2
import numpy as np

def blur_fileter(img):
    img = cv2.GaussianBlur(img, (0, 0), 3)
    return img

def canny_filter(img):
    med_val = np.median(img)
    lower = int(max(0, 0.7 * med_val))
    upper = int(min(255, 1.3 * med_val))
    dst = cv2.Canny(img, lower, upper, 3)
    return dst

cap = cv2.VideoCapture(0)

cam_mode = 0

while True:
    ret, frame = cap.read()

    if cam_mode == 1:
        frame = blur_fileter(frame)
    elif cam_mode == 2:
        frame = canny_filter(frame)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(10)
    if key == 27:
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0

cap.release()
