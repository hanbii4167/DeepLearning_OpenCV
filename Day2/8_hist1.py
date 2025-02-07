import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./dog.bmp',cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img],[0],None,[256],[0,255])

cv2.imshow('img',img)
plt.hist(hist)
plt.show()
cv2.waitKey() # waitkey를 imshow 밑에 바로 넣으면 키 누를때가지 멈추므로 히스토그램이 안나오고 키를 아무거나 눌러야 히스토그램이 뜬다!