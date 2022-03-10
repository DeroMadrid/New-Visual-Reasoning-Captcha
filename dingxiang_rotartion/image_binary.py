import preprocessing
import cv2
import os
import numpy as np
from PIL import Image
import math


images_path = os.listdir(r"C:/Users/Dero/Desktop/dx")
for filelist in images_path:
    print(filelist[:-4])
    openpath = "C:/Users/Dero/Desktop/dx/" + filelist
    image1 = cv2.imread(openpath)
    savepath = "C:/Users/Dero/Desktop/dxx/" + filelist[:-4] + "220.png"
    preprocessing.binary(openpath, savepath, "fixed_threshold", 220)
    image1 = Image.open(savepath)
    img_array1 = np.asarray(image1)
    count = 0
    num_x = 0
    num_y = 0
    for i in range(0, 160):
        for j in range(0, 160):
            if img_array1[i][j] == 255:
                if 81 ** 2 >= (i - 80) ** 2 + (j - 80) ** 2 >= 64 ** 2:
                    count += 1
                    num_x += i
                    num_y += j
                else:
                    img_array1[i][j] = 0
    # print((num_x, num_y, count))
    if count == 0:
        continue
    avg_x = int(num_x / count)
    avg_y = int(num_y / count)

    # print((avg_x, avg_y))
    img_array1[avg_x][avg_y] = 150
    img_array1[avg_x - 1][avg_y] = 150
    img_array1[avg_x + 1][avg_y] = 150
    img_array1[avg_x][avg_y - 1] = 150
    img_array1[avg_x][avg_y + 1] = 150
    img_array1[avg_x-2][avg_y] = 150
    img_array1[avg_x+2][avg_y] = 150
    img_array1[avg_x][avg_y+2] = 150
    img_array1[avg_x][avg_y-2] = 150

    if avg_x != 80:
        tans = abs(avg_y - 80) / abs(avg_x - 80)
        x = math.atan(tans)
        xx = x * 180 / math.pi
    # print(xx)
    else:
        xx = 90

    anger = 0
    if avg_x <= 80:
        if avg_y > 80:
            anger = 180 - xx
        else:
            anger = 180 + xx
    else:
        if avg_y > 80:
            anger = xx
        else:
            anger = 360 - xx

    # print(anger)
    length = anger / 340 * 260
    # print(length)
    Image.fromarray(np.uint8(img_array1))
    img_save = cv2.cvtColor(np.asarray(img_array1), cv2.COLOR_RGB2BGR)
    # savepath = "C:/Users/Dero/Desktop/dxx/" + filelist[:-4] + "220.png"
    cv2.imwrite(savepath, img_save)
