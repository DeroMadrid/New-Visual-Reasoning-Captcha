import preprocessing
import cv2
import os
import numpy as np
from PIL import Image
import math

images_path = os.listdir(r"C:/Users/Dero/Desktop/dx")
for filelist in images_path:
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
                if 80 ** 2 >= (i - 80) ** 2 + (j - 80) ** 2 >= 64 ** 2:
                    count += 1
                    num_x += i
                    num_y += j
                else:
                    img_array1[i][j] = 0
    if count == 0:
        continue
    avg_x = int(num_x / count)
    avg_y = int(num_y / count)

    print((avg_x, avg_y))
    img_array1[avg_x][avg_y] = 150
    img_array1[avg_x - 1][avg_y] = 150
    img_array1[avg_x + 1][avg_y] = 150
    img_array1[avg_x][avg_y - 1] = 150
    img_array1[avg_x][avg_y + 1] = 150
    img_array1[avg_x - 2][avg_y] = 150
    img_array1[avg_x + 2][avg_y] = 150
    img_array1[avg_x][avg_y + 2] = 150
    img_array1[avg_x][avg_y - 2] = 150

    # 这个地方加上依托均值点找中心点
    length1 = 0
    length2 = 0
    x1 = x2 = avg_x
    y1 = y2 = avg_y
    for i in range(0, 160):
        for j in range(0, 160):
            if img_array1[i][j] == 255:
                if (avg_y - 80)*i + (80 - avg_x)*j + 80*avg_x - 80*avg_y > 0:  # 判断 点 和 直线（均值点和圆心的连线） 的方位
                    if (i - avg_x) ** 2 + (j - avg_y) ** 2 > length1:
                        x1 = i
                        y1 = j
                        length1 = (i - avg_x) ** 2 + (j - avg_y) ** 2
                else:
                    if (i - avg_x) ** 2 + (j - avg_y) ** 2 > length2:
                        x2 = i
                        y2 = j
                        length2 = (i - avg_x) ** 2 + (j - avg_y) ** 2
    cen_x = (x1 + x2)/2
    cen_y = (y1 + y2)/2
    print("center : ", cen_x, cen_y)
    cen_x = int(cen_x)
    cen_y = int(cen_y)
    img_array1[cen_x][cen_y] = 150
    img_array1[cen_x - 1][cen_y] = 150
    img_array1[cen_x + 1][cen_y] = 150
    img_array1[cen_x][cen_y - 1] = 150
    img_array1[cen_x][cen_y + 1] = 150
    img_array1[cen_x - 2][cen_y] = 150
    img_array1[cen_x + 2][cen_y] = 150
    img_array1[cen_x][cen_y + 2] = 150
    img_array1[cen_x][cen_y - 2] = 150

    if cen_x == 80:
        xx = 90
    else:
        tans = abs(cen_y - 80) / abs(cen_x - 80)
        x = math.atan(tans)
        xx = x * 180 / math.pi
    print(xx)

    anger = 0
    if cen_x <= 80:
        if cen_y > 80:
            anger = 180 - xx
        else:
            anger = 180 + xx
    else:
        if cen_y > 80:
            anger = xx
        else:
            anger = 360 - xx

    print(anger)
    # anger是图像需要顺时针旋转的角度
    length = anger / 340 * 260
    print(length)
    Image.fromarray(np.uint8(img_array1))
    img_save = cv2.cvtColor(np.asarray(img_array1), cv2.COLOR_RGB2BGR)
    # savepath11 = "C:/Users/Dero/Desktop/dx_adjust/" + filelist[:-4] + "220.png"
    cv2.imwrite(savepath, img_save)
    path = openpath
    img = Image.open(path)
    # 修改角度
    dst5 = img.rotate(-anger)
    re_img = np.asarray(dst5)
    # 图片大小为350*350
    # for i in range(0, 350):
    #     for j in range(0, 350):
    #         if (i - 175) ** 2 + (j - 175) ** 2 > 175 ** 2:
    #             re_img[i][j] = 255

    Image.fromarray(np.uint8(re_img))
    img_save = cv2.cvtColor(np.asarray(re_img), cv2.COLOR_RGB2BGR)
    path1 = "C:/Users/Dero/Desktop/dx_adjust/" + filelist

    cv2.imwrite(path1, img_save)
