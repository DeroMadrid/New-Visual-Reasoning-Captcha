import numpy as np
from PIL import Image
import cv2
import math
import matplotlib.pyplot as plt
from skimage import measure

# image1 = Image.open(openpath)
# img_array1 = np.asarray(image1)
#
#
# Image.fromarray(np.uint8(img_array1))
# img_save = cv2.cvtColor(np.asarray(img_array1), cv2.COLOR_RGB2BGR)
# cv2.imwrite(openpath, img_save)
#
# img = cv2.imread('C:/Users/Dero/Desktop/dingxiang_area/dilation/1_full.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # find contours of all the components and holes
# gray_temp = gray.copy()  # copy the gray image because function
# # findContours will change the imput image into another
# contours, hierarchy = cv2.findContours(gray_temp, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#
# # show the contours of the imput image
# cv2.drawContours(img, contours, -1, (0, 255, 255), 2)
# plt.figure('original image with contours'), plt.imshow(img, cmap='gray')
#
# # find the max area of all the contours and fill it with 0
# area = []
# for i in range(len(contours)):
#     area.append(cv2.contourArea(contours[i]))
# max_idx = np.argmax(area)
# cv2.fillConvexPoly(gray, contours[max_idx], 0)
# # show image without max connect components
# plt.figure('remove max connect com'), plt.imshow(gray, cmap='gray')
# plt.show()




# 输入二值图像mask
def largeConnectComponent(bw_image):
    labeled_img, num = measure.label(bw_image, background=0, return_num=True)
    # 这里返回的labeled_img是一幅图像，不再是一副二值图像，有几个连通域，最大值就是几，num是连通域个数，1个连通域的话num=1

    max_label = 0
    max_num = 0

    # 图像全黑，没有连通域num=0,或者是由一个连通域num=1，直接返回原图像
    if num == 0 or num == 1:
        return bw_image
    else:
        for i in range(1, num + 1):  # 注意这里的范围，为了与连通域的数值相对应
            # 计算面积，保留最大面积对应的索引标签，然后返回二值化最大连通域
            if np.sum(labeled_img == i) > max_num:
                max_num = np.sum(labeled_img == i)
                max_label = i
        lcc = (labeled_img == max_label)
        return lcc


openpath = "C:/Users/Dero/Desktop/dingxiang_area/dilation/1_full.png"
image1 = cv2.imread(openpath)
savepath = "C:/Users/Dero/Desktop/dingxiang_area/dilation/result.png"
output = largeConnectComponent(image1)
output = output.astype(int)
l = measure.label(image1)
r = measure.regionprops(l) # l is from previous approach
out = (l==(1+np.argmax([i.area for i in r]))).astype(int)
print(type(out))
# print(out)
plt.imshow(output)
plt.savefig("array1")
# Image.fromarray(np.uint8(output))
# img_save = cv2.cvtColor(np.asarray(output), cv2.COLOR_RGB2BGR)
# cv2.imwrite(savepath, img_save)
