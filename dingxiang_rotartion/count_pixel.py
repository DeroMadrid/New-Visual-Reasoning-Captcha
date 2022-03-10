import numpy as np
from PIL import Image
import cv2
import math

openpath = "C:/Users/Dero/Desktop/dx/1245.png.png"
# image1 = cv2.imread(openpath)
image1 = Image.open(openpath)
img_array1 = np.asarray(image1)
count = 0
num_x = 0
num_y = 0
for i in range(0, 160):
    for j in range(0, 160):
        if img_array1[i][j] == 255:
            count += 1
            num_x += i
            num_y += j

avg_x = num_x / count
avg_y = num_y / count
print((avg_x, avg_y))

tans = abs(avg_y - 80) / abs(avg_x - 80)
x = math.atan(tans)
xx = x * 180 / math.pi
print(xx)
