import numpy as np
import cv2
import math
from scipy import ndimage

img_before = cv2.imread('C:/Users/Dero/Desktop/baidu_captcha/vcode-spin-img108.png')

cv2.imshow("Before", img_before)
key = cv2.waitKey(0)

img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", img_gray)
key = cv2.waitKey(0)
img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
# 边缘检测
lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 80, minLineLength=100, maxLineGap=5)
# 检测标准霍夫变化的二值图像直线线条

angles = []

for [[x1, y1, x2, y2]] in lines:
    cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles.append(angle)

cv2.imshow("Detected lines", img_before)
key = cv2.waitKey(0)

median_angle = np.median(angles)
img_rotated = ndimage.rotate(img_before, median_angle)

print(f"Angle is {median_angle:.04f}")
rotation_angel = round(median_angle, 2)
print(rotation_angel)
cv2.imwrite('rotated.jpg', img_rotated)

# 结果为负数，表示需要顺时针旋转角度，正为逆时针旋转
#