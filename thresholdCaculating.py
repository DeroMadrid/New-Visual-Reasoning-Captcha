import cv2 as cv
import numpy as np
import math

'''
Binarization  Integration
将各种二值化不同阈值选取的方法整合在一起
'''

# 百分比阈值法，能较好地保留噪线，返回每张图片的二值化阈值
def GetPTileThreshold(image):
    # image = cv.imread(path)
    # 把BGR图像转化成灰度图像
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 如果图片已经是单通道的灰度图则不需要下面语句，二选一
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = image
    # 获得灰度直方图以便调整算法的使用
    size = gray.shape[0] * gray.shape[1]
    # 压缩矩阵，将二维的灰度直方图压缩成一维
    HistGram = gray.ravel()
    HistGram_1D = [0] * 256
    # 统计直方图，得到灰度值的统计直方图
    for i in range(size):
        index = HistGram[i]
        HistGram_1D[index] = HistGram_1D[index] + 1
    amount = 0
    sum = 0
    for i in range(0,256):
        amount = amount + HistGram_1D[i]
    for i in range(0,256):
        sum = sum + HistGram_1D[i]
        if sum >= (amount / 10):
            return i
    return -1


# 基于灰度平均值的阈值，返回每张图片的二值化阈值
def average_threshold(image):
    # 把BGR图像转化成灰度图像
    # 获得灰度直方图以便调整算法的使用

    # 如果图片已经是单通道的灰度图则不需要下面语句，二选一
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = image
    size = gray.shape[0] * gray.shape[1]
    # 压缩矩阵，将二维的灰度直方图压缩成一维
    HistGram = gray.ravel()
    HistGram_1D = [0] * 256
    # 统计直方图，得到灰度值的统计直方图
    for i in range(size):
        index = HistGram[i]
        HistGram_1D[index] = HistGram_1D[index] + 1
    sum = 0
    amount = 0
    for i in range(0, 256):
        amount = amount + HistGram_1D[i]
        sum = sum + i * HistGram_1D[i]
    return sum/amount


# 迭代阈值法
def Iterative_best_threshold(image):
    # 第一步，获取一维灰度直方图
    # image = cv.imread(open_path,0)
    size = image.shape[0] * image.shape[1]
    # 压缩矩阵，将二维的灰度直方图压缩成一维
    HistGram = image.ravel()
    HistGram_1D = [0] * 256
    # 统计直方图，得到灰度值的统计直方图
    for i in range(size):
        index = HistGram[i]
        HistGram_1D[index] = HistGram_1D[index] + 1
    # 第二步，迭代计算阈值
    minvalue = 0
    maxvalue = 255
    for minvalue in range(0, 255):
        if HistGram_1D[minvalue] == 0:
            continue
        else:
            break
    for maxvalue in range(255, minvalue, -1):
        if HistGram_1D[maxvalue] == 0:
            continue
        else:
            break
    # 只有一种颜色
    if minvalue == maxvalue:
        return maxvalue
    # 只有两种颜色
    if minvalue + 1 == maxvalue:
        return minvalue
    print(minvalue, maxvalue)
    threshold = minvalue
    newthreshold = (int(minvalue + maxvalue)) >> 1
    # 当前后两次阈值相同时停止迭代
    Iter = 0
    while(threshold != newthreshold):
        Sum_one = 0
        Sum_Integer_one = 0
        Sum_two = 0
        Sum_Integer_two = 0
        threshold = newthreshold
        # 将图像分为前景和背景两部分，求出两部分的平均值
        for i in range(minvalue,threshold+1):
            Sum_Integer_one = Sum_Integer_one + HistGram_1D[i] * i
            Sum_one = Sum_one + HistGram_1D[i]
        meanvalue_one = Sum_Integer_one / Sum_one
        for i in range(threshold+1,maxvalue+1):
            Sum_Integer_two = Sum_Integer_two + HistGram_1D[i] * i
            Sum_two = Sum_two + HistGram_1D[i]
        meanvalue_two = Sum_Integer_two / Sum_two
        # 求出新的阈值
        newthreshold = (int(meanvalue_one + meanvalue_two)) >> 1
        Iter = Iter + 1
        if Iter >= 1000:
            return -1
        # ret,binary = cv.threshold(image,threshold,255,cv.THRESH_BINARY)
        # cv.imwrite(save_path,binary)
    return threshold


# 一维最大熵阈值法
# 熵在图像中可以理解为图像信息的多少。方法思想：给定阈值q将图像分割为P0和P1（前景和背景），分别计算出每一灰度值出现的概率，再计算前景和背景对应的熵并求和，遍历0-255找出最大熵
# 一维最大熵二值化能准确保留噪线
def MaxEntropy_1D(image):
    # 第一步，获取一维灰度直方图
    # image = cv.imread(open_path)
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = image
    size = gray.shape[0] * gray.shape[1]
    # 压缩矩阵，将二维的灰度直方图压缩成一维
    HistGram = gray.ravel()
    HistGram_1D = [0] * 256
    # 统计直方图，得到灰度值的统计直方图
    for i in range(size):
        index = HistGram[i]
        HistGram_1D[index] = HistGram_1D[index] + 1
    # 第二步,获取最大熵时的阈值
    minvalue = 0
    maxvalue = 255
    for minvalue in range(0, 255):
        if HistGram_1D[minvalue] == 0:
            continue
        else:
            break
    for maxvalue in range(255, minvalue, -1):
        if HistGram_1D[maxvalue] == 0:
            continue
        else:
            break
    # 只有一种颜色
    if minvalue == maxvalue:
        return maxvalue
    # 只有两种颜色
    if minvalue + 1 == maxvalue:
        return minvalue
    print(minvalue, maxvalue)
    amount = 0
    for i in range(minvalue, maxvalue+1):
        amount = amount + HistGram_1D[i]
    # 统计每一灰度级出现的频率
    HistGramD = [0.0] * 256
    for i in range(minvalue, maxvalue+1):
        HistGramD[i] = float(HistGram_1D[i] / amount)
    # 初始化一维最大熵
    maxEntropy = 0.0
    # 初始化阈值
    thresh = 0
    for i in range(minvalue+1, maxvalue):
        SumIntegral = 0.0
        EntropyBack = 0.0
        EntropyFore = 0.0
        for j in range(minvalue, i+1):
            SumIntegral = SumIntegral + HistGramD[j]
        # 背景图像的熵
        for j in range(minvalue, i+1):
            if HistGramD[j] != 0:
                EntropyBack = EntropyBack + (-HistGramD[j] / SumIntegral * math.log(HistGramD[j] / SumIntegral))
        # 前景图像的熵
        for j in range(i+1, maxvalue+1):
            if HistGramD[j] != 0:
                EntropyFore = EntropyFore + (-HistGramD[j] / (1 - SumIntegral) * math.log((HistGramD[j]) / (1 - SumIntegral)))
        if maxEntropy < (EntropyFore + EntropyBack):
            thresh = i
            maxEntropy = EntropyBack + EntropyFore
    # print(thresh)
    return thresh


# 判断直方图是否是双峰曲线
def IsDimodal(HistGram):
    # 对直方图的峰进行计数，只有峰数为2才为双峰
    Count = 0
    for Y in range(1, 255):
        if HistGram[Y - 1] < HistGram[Y] and HistGram[Y + 1] < HistGram[Y]:
            Count = Count + 1
            if Count > 2:
                return False
    if Count == 2:
        return True
    else:
        return False


# 双峰阈值
def GetIntermodesThreshold(image):
    # image = cv.imread(open_path,0)
    # 获得灰度直方图以便调整算法的使用
    size = image.shape[0] * image.shape[1]
    # 压缩矩阵，将二维的灰度直方图压缩成一维
    HistGram = image.ravel()
    HistGram_1D = [0] * 256
    # 统计直方图，得到灰度值的统计直方图
    for i in range(size):
        index = HistGram[i]
        HistGram_1D[index] = HistGram_1D[index] + 1
    # HistGrams是返回平滑后的直方图
    HistGramS = [float(0)] * 256
    HistGramC = [float(0)] * 256
    HistGramCC = [float(0)] * 256
    # double类型的数据，基于精度问题，一定要用浮点数聊处理，否则得不到正确的结果
    # 为什么赋值一份数据：求均值的过程会破坏前面的数据
    for i in range(256):
        HistGramC[i] = float(HistGram_1D[i])
        HistGramCC[i] = float(HistGram_1D[i])
    Iter = 0

    # 通过三点求均值来平滑直方图
    # 判断是否已经是双峰的图像了
    while IsDimodal(HistGramCC) == False:
        # 三点求均值使用的第一点
        HistGramCC[0] = float((HistGramC[0] + HistGramC[0] + HistGramC[1]) / 3)
        for Y in range(1, 255):
            # 三点求均值使用的中间的点
            HistGramCC[Y] = float((HistGramC[Y - 1] + HistGramC[Y] + HistGramC[Y + 1]) / 3)
        # 三点求均值使用的最后一点
        HistGramCC[255] = float((HistGramC[254] + HistGramC[255] + HistGramC[255]) / 3)
        HistGramC = HistGramCC[:]
        Iter = Iter + 1
        # 直方图无法平滑为双峰的，返回错误代码
        if Iter >= 1000:
            return -1
    for Y in range(1, 256):
        # 阈为双峰之间的最小值
        HistGramS[Y] = int(HistGramCC[Y])
    Index = 0
    Peak = [None] * 2
    for Y in range(1, 255):
        if HistGramCC[Y - 1] < HistGramCC[Y] and HistGramCC[Y + 1] < HistGramCC[Y]:
            Peak[Index] = Y - 1
            Index = Index + 1
    binary_thresh = int((Peak[0] + Peak[1]) / 2)
    # ret,binary_result = cv.threshold(image,binary_thresh,255,cv.THRESH_BINARY)
    # cv.imwrite(save_path,binary_result)
    # return ((Peak[0] + Peak[1]) / 2), HistGramS  # 阈值，平滑后的数组
    return binary_thresh


# 均值法二值化
# 和灰度二值化的区别似乎只有 没有进行灰度图像的转换
def mean_threshold(image):
    # image = cv.imread(open_path,0)
    height, width =image.shape[:2]
    m = np.reshape(image, [1,width * height])
    mean_binary = m.sum()/(width * height)
    # ret, binary_result = cv.threshold(image, mean_binary, 255, cv.THRESH_BINARY)
    # cv.imwrite(save_path,binary_result)
    return mean_binary