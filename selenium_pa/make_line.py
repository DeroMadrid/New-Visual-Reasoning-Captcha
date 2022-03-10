import time
from PIL import Image
import numpy as np
import cv2
import math
from scipy import ndimage
import os
import thresholdCaculating

images_path = os.listdir(r"C:/Users/Dero/Desktop/nooo")
for filelist in images_path:
    open_path = "C:/Users/Dero/Desktop/nooo/" + filelist
    save_path = "C:/Users/Dero/Desktop/rrr/" + filelist[:-4]

    img_before = cv2.imread(open_path)

    img_judge = cv2.imread(open_path, 0)
    # cv2.imshow("Before", img_before)
    # key = cv2.waitKey(0)
    threshold = thresholdCaculating.average_threshold(img_judge)
    ret, binary_result = cv2.threshold(img_judge, threshold, 255, cv2.THRESH_BINARY)
    (height, width) = binary_result.shape[:2]
    # 新建一个与图像长度一致的数组
    numofwhite = [0] * height
    # 循环统计每一列白色像素的个数
    for i in range(0, width):
        for j in range(0, height):
            if binary_result[i][j] == 255:  # change
                numofwhite[i] = numofwhite[i] + 1
    print(numofwhite)
    count_l = 0
    count_r = 0
    i = 0
    j = width - 1
    for i in range(0, int(width / 2)):
        count_l += numofwhite[i]

    for j in range(width - 1, int(width / 2)):
        count_r += numofwhite[j]

    if count_r > count_l:
        flag = 1
    else:
        flag = 0

    img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)

    # save_path1 = save_path + '.png'
    # cv2.imwrite(save_path1, img_gray)

    img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
    # 边缘检测
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 10, minLineLength=100, maxLineGap=5)
    # 检测标准霍夫变化的二值图像直线线条

    angles = []
    if lines is None:
        print(filelist[:-4])
        continue

    for [[x1, y1, x2, y2]] in lines:
        # cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        angles.append(angle)

    median_angle = np.median(angles)

    if median_angle > 0:
        if flag == 1:
            rotation_anger = median_angle - 360
        else:
            rotation_anger = median_angle - 180
    else:
        if flag == 1:
            rotation_anger = median_angle - 180
        else:
            rotation_anger = median_angle

    # img_rotated = ndimage.rotate(img_before, rotation_anger)
    img = Image.open(open_path)

    dst5 = img.rotate(rotation_anger)
    re_img = np.asarray(dst5)
    # 图片大小为350*350
    for i in range(0, 350):
        for j in range(0, 350):
            if (i - 175) ** 2 + (j - 175) ** 2 > 175 ** 2:
                re_img[i][j] = 255

    Image.fromarray(np.uint8(re_img))
    img_save = cv2.cvtColor(np.asarray(re_img), cv2.COLOR_RGB2BGR)
    save_path1 = save_path + '.png'
    cv2.imwrite(save_path1, img_save)
    # re_img.save(save_path1)