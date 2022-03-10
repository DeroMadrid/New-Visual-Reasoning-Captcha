# -*- encoding: utf-8 -*-
import cv2 as cv
import numpy as np

import thresholdCaculating

"""
Preprocess Integration
将各种不同的预处理方法整合在一起
包括二值化，腐蚀，膨胀，旋转等方法
"""


# 二值化
# threshold 是阈值
def binary(open_path, save_path, threMethod, fixedThre=220):
    image = cv.imdecode(np.fromfile(open_path, dtype=np.uint8), 0)  # 用于处理中文路径的图片
    # image = cv.imread(open_path, 0)
    # 选取二值化方法
    if (threMethod == "GetPTileThreshold"):  # 输入通道有要求
        threshold = thresholdCaculating.GetPTileThreshold(image)
    elif (threMethod == "average_threshold"):  # 输入通道有要求
        threshold = thresholdCaculating.average_threshold(image)
    elif (threMethod == "Iterative_best_threshold"):
        threshold = thresholdCaculating.average_threshold(image)
    elif (threMethod == "MaxEntropy_1D"):  # 输入通道有要求
        threshold = thresholdCaculating.average_threshold(image)
    elif (threMethod == "GetIntermodesThreshold"):  # 输入通道有要求
        threshold = thresholdCaculating.average_threshold(image)
    elif (threMethod == "mean_threshold"):
        threshold = thresholdCaculating.mean_threshold(image)
    elif (threMethod == "fixed_threshold"):
        threshold = fixedThre
    ret, binary_result = cv.threshold(image, threshold, 255, cv.THRESH_BINARY)
    save_path_binary = save_path
    # cv.imwrite(save_path_binary, binary_result)
    kernel = np.ones((2, 2), np.uint8)
    b1 = cv.erode(binary_result, kernel)
    d1 = cv.dilate(b1, kernel)
    cv.imencode('.png', d1)[1].tofile(save_path_binary)  # 保存带中文的路径


# 旋转相关
# 检测图像的左上角，判断是图像需要顺时针旋转还是逆时针旋转
def clockwise_or_anticlockwise(open_path):
    # image = cv.imread(open_path, 0)
    image = cv.imdecode(np.fromfile(open_path, dtype=np.uint8), 0)  # 用于处理中文路径的图片
    sum = 0
    for i in range(100):
        for j in range(30):
            if image[i][j] == 0:
                sum = sum + 1
    if sum > 1:
        print(open_path + "逆时针")
        return -1
    else:
        print(open_path + "顺时针")
        return 1


# 旋转图像
# 旋转之后图像补成一个更大的矩形框，填补的区域填充为白色
def rotate_bound(open_path, save_path, angle):
    # image = cv.imread(open_path, 0)
    image = cv.imdecode(np.fromfile(open_path, dtype=np.uint8), 0)  # 用于处理中文路径的图片
    (h, w) = image.shape[:2]
    # 旋转中心为图像中心
    (cX, cY) = (w / 2, h / 2)
    # 获取旋转矩阵
    angle = angle * clockwise_or_anticlockwise(open_path)
    # 顺时针旋转，1.0位图像放缩参数
    M = cv.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # 计算图像旋转之后的新边界
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # 调整旋转矩阵的移动距离
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # 实际旋转图像，确保图像没有被截断
    # borderValue为缺失背景填充颜色，默认是黑色(0,0,0)
    img = cv.warpAffine(image, M, (nW, nH), borderValue=(255, 255, 255))
    cv.imwrite(save_path, img)


# 膨胀   111
def dilation(open_path, save_path):
    # image = cv.imread(open_path, 0) #  参数为flag -1为保留原始色彩 而0为更改为灰度
    image = cv.imdecode(np.fromfile(open_path, dtype=np.uint8), 0)  # 用于处理中文路径的图片
    kernel = np.ones((2, 2), np.uint8)
    dilation = cv.dilate(image, kernel)
    # cv.imwrite(save_path, dilation)
    cv.imencode('.png', dilation)[1].tofile(save_path)  # 保存带中文的路径


# 自定义 111
def pinghua(open_path, save_path):
    image = cv.imread(open_path, -1)
    kernel = np.ones((2, 2), np.uint8)
    picIma = cv.dilate(image, kernel)
    picIma = cv.dilate(picIma, kernel)
    picIma = cv.dilate(picIma, kernel)
    # cv.imwrite(save_path, picIma)
    cv.imencode('.png', picIma)[1].tofile(save_path)  # 保存带中文的路径

# 腐蚀加粗  111
def erosion_line(open_path, save_path):
    image = cv.imread(open_path, 0)
    kernel = np.ones((2, 2), np.uint8)
    erosion = cv.erode(image, kernel)
    cv.imwrite(save_path, erosion)
    cv.imencode('.png', erosion)[1].tofile(save_path)  # 保存带中文的路径

# 去除噪线
# k1size k2size 分别是第一次和第二次操作的卷积核的大小
def get_noiseline(open_path, save_path, first, k1size, k2size):
    # image = cv.imread(open_path, -1)
    image = cv.imdecode(np.fromfile(open_path, dtype=np.uint8), 0)  # 用于处理中文路径的图片
    kernel1 = np.ones((k1size, k1size), np.uint8)
    kernel2 = np.ones((k2size, k2size), np.uint8)
    # 先膨胀去除字符提取噪线，再腐蚀恢复噪线-----》具有填充物体内细小空洞，连接邻近物体和平滑边界的作用
    if first == "dilation":
        dilation = cv.dilate(image, kernel1)
        erosion = cv.erode(dilation, kernel2)
        # cv.imwrite(save_path, erosion)
        cv.imencode('.png', erosion)[1].tofile(save_path)  # 保存带中文的路径
    # 直接腐蚀后膨胀------》消除细小物体，在纤细处分离物品
    else:
        erosion = cv.erode(image, kernel1)
        dilation = cv.dilate(erosion, kernel2)
        # cv.imwrite(save_path, dilation)
        cv.imencode('.png', dilation)[1].tofile(save_path)  # 保存带中文的路径

# 根据获得的噪线原图去除噪线
def remove_noiseline(open_path1, open_path2, save_path):
    # image1 = cv.imread(open_path1, 0)
    # image2 = cv.imread(open_path2, 0)
    image1 = cv.imdecode(np.fromfile(open_path1, dtype=np.uint8), 0)  # 用于处理中文路径的图片
    image2 = cv.imdecode(np.fromfile(open_path2, dtype=np.uint8), 0)  # 用于处理中文路径的图片
    (height, width) = image1.shape
    for i in range(height):
        for j in range(width):
            if image1[i][j] != 255:
                image1[i][j] = 0
            if image2[i][j] == 0:
                image1[i][j] = 255
    # cv.imwrite(save_path, image1)
    cv.imencode('.png', image1)[1].tofile(save_path)  # 保存带中文的路径


# 原图上去除噪线再二值化
def remove_lines(path1, path2, path3):
    # img1是噪线
    # img1 = cv.imread(path1)
    img1 = cv.imdecode(np.fromfile(path1, dtype=np.uint8), 0)  # 用于处理中文路径的图片
    # img2是原图
    # img2 = cv.imread(path2)
    img2 = cv.imdecode(np.fromfile(path2, dtype=np.uint8), 0)  # 用于处理中文路径的图片
    (height, width) = img1.shape
    for i in range(height):
        for j in range(width):
            # for k in range(channel):
                if img1[i][j] == 0:
                    img2[i][j] = 255
    Img = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    ret, Img2 = cv.threshold(Img, 220, 255, cv.THRESH_BINARY)
    # cv.imwrite(path3, Img2)
    cv.imencode('.png', Img2)[1].tofile(path3)  # 保存带中文的路径

# 360_gray去除背景
# 360gray验证码有三种不同的背景，分别是直线、斜线、波浪线组成的线条背景
# 背景噪线颜色和字符颜色相近，很难通过二值化的方法直接去除。需要提取出背景模板，通过做差的方式去除背景
def remove_backgroud_360gray(open_path, save_path):
    image = cv.imread(open_path, 0)
    # 获取三种背景图片
    Img1 = cv.imread("D:/CAPTCHA_Papers/Code/real-world/360gray/break_line.jpg", 0)
    Img2 = cv.imread("D:/CAPTCHA_Papers/Code/real-world/360gray/oblique_line.jpg", 0)
    Img3 = cv.imread("D:/CAPTCHA_Papers/Code/real-world/360gray/transverse_line.jpg", 0)
    img = image[2:10, 2:10]
    img1 = Img1[2:10, 2:10]
    img2 = Img2[2:10, 2:10]
    img3 = Img3[2:10, 2:10]
    flag1 = 0
    flag2 = 0
    flag3 = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if abs(int(img[i][j]) - int(img1[i][j])) <= 30:
                flag1 = flag1 + 1
            if abs(int(img[i][j]) - int(img2[i][j])) <= 30:
                flag2 = flag2 + 1
            if abs(int(img[i][j]) - int(img3[i][j])) <= 30:
                flag3 = flag3 + 1
    (height, width) = image.shape
    Image = image[3:height - 3, 3:width - 3]
    h, w = Image.shape[:2]
    if flag1 > flag2 and flag1 > flag3:
        Image1 = Img1[3:height - 3, 3:width - 3]
        for i in range(h):
            for j in range(w):
                if abs(int(Image[i][j]) - int(Image1[i][j])) <= 30:
                    Image[i][j] = 255
        cv.imwrite(save_path, Image)

    elif flag2 > flag1 and flag2 > flag3:
        Image2 = Img2[3:height - 3, 3:width - 3]
        for i in range(h):
            for j in range(w):
                if abs(int(Image[i][j]) - int(Image2[i][j])) <= 30:
                    Image[i][j] = 255
        cv.imwrite(save_path, Image)
    elif flag3 > flag1 and flag3 > flag2:
        Image3 = Img3[3:height - 3, 3:width - 3]
        for i in range(h):
            for j in range(w):
                if abs(int(Image[i][j]) - int(Image3[i][j])) <= 30:
                    Image[i][j] = 255
        cv.imwrite(save_path, Image)


# 有背景噪声，且字符为白色，但是背景和字符分明，直接提取白色字符在转换成黑色
# 相当于一个伪二值化过程
def binary_jd(open_path, save_path):
    # 第一步，获取一维灰度直方图
    image = cv.imread(open_path, 0)
    (height, width) = image.shape
    img = np.zeros((height, width), np.uint8)
    for i in range(height):
        for j in range(width):
            img[i][j] = 255
    for i in range(height):
        for j in range(width):
            if image[i][j] == 255:
                img[i][j] = 0
    cv.imwrite(save_path, img)


# 由于microsoft验证码没有噪线干扰，且背景近似于白色，可以不用二值化只需要简单的颜色转换
def binary_ms(open_path, save_path):
    image = cv.imread(open_path, 0)
    ret, binary_result = cv.threshold(image, 245, 255, cv.THRESH_BINARY)
    cv.imwrite(save_path, binary_result)


# 二值化，提取黑色字符
def binary_apple(open_path, save_path):
    image = cv.imread(open_path, 0)
    (height, width) = image.shape
    for i in range(height):
        for j in range(width):
            if image[i][j] >= 7:
                image[i][j] = 255
    cv.imwrite(save_path, image)


if __name__ == "__main__":
    open_path = 'C:/Users/Dero/Desktop/it168/test/1_查拉什整.png'
    save_path = "C:/Users/Dero/Desktop/it168/binary/2_中文.png"
    # # open_path = 'C:/Users/Dero/Desktop/p2.jpg'
    # save_path = "C:/Users/Dero/Desktop/p10.jpg"
    # path = "C:/Users/Dero/Desktop/p11.jpg"
    # # threMethod = "GetPTileThreshold"
    # # binary(open_path, save_path, threMethod, 200)
    # pinghua(open_path, save_path)  # 膨胀

    binary(open_path, save_path, "MaxEntropy_1D", 220)
    # rotate_bound(open_path, save_path, 90)
    # remove_noiseline(open_path, save_path, path)
    # get_noiseline(open_path, save_path, "dilation", 4, 3)

    # pic = 'C:/Users/Dero/Desktop/p2.png'
    # picture = cv.imread(pic)
    # result = cv.bitwise_not(picture)
    # cv.imwrite('C:/Users/Dero/Desktop/picture1.png', result)

    # image = cv.imread('C:/Users/Dero/Desktop/picture1.png', 0)
    # (height, width) = (image.shape[0], image.shape[1])
    # cv.imshow('img', image)
    # cv.waitKey(0)
    # for i in range(height):
    #     for j in range(width):
    #         image[i][j] = 0
    # cv.imshow('img', image)
    # cv.waitKey(0)
