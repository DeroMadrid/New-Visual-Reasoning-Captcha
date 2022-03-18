import numpy as np
from PIL import Image
import cv2
import math

openpath = "C:/Users/Dero/Desktop/dingxiang_area/dilation/5.png"
# image1 = cv2.imread(openpath)
savapath = "C:/Users/Dero/Desktop/dingxiang_area/dilation/1_full.png"
image1 = Image.open(openpath)
img_array1 = np.asarray(image1)
image2 = Image.open(savapath)
img_array2 = np.asarray(image2)
for i in range(0, 150):
    for j in range(0, 150):
        img_array2[i][j] = 0
# (300, 150), 长300，宽150。
for i in range(0, 150):
    for j in range(0, 300):
        img_array2[i][j] = img_array1[i][j]
        if img_array1[i][j] == 255:
            for m in range(-10, 11):
                for n in range(-10, 11):
                    if 150 > (i+m) >= 0 and 300 > (j+n) >= 0:
                        img_array2[i+m][j+n] = 255

Image.fromarray(np.uint8(img_array2))
img_save = cv2.cvtColor(np.asarray(img_array2), cv2.COLOR_RGB2BGR)

cv2.imwrite(savapath, img_save)
