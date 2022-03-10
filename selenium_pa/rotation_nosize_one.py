import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import os

path = "C:/Users/Dero/Desktop/baidu_captcha_lines/1.png"

img = Image.open(path)
# 修改角度
dst5 = img.rotate(-90)
re_img = np.asarray(dst5)
# 图片大小为350*350
for i in range(0, 350):
    for j in range(0, 350):
        if (i-175)**2 + (j-175)**2 > 175**2:
            re_img[i][j] = 255

Image.fromarray(np.uint8(re_img))
img_save = cv2.cvtColor(np.asarray(re_img), cv2.COLOR_RGB2BGR)
cv2.imwrite(path, img_save)