import numpy as np
import scipy.ndimage as ndi
from skimage import measure, color
import matplotlib.pyplot as plt
from PIL import Image

# # 编写一个函数来生成原始二值图像
# def microstructure(l=256):
#     n = 5
#     x, y = np.ogrid[0:l, 0:l]  # 生成网络
#     mask = np.zeros((l, l))
#     generator = np.random.RandomState(1)  # 随机数种子
#     points = l * generator.rand(2, n ** 2)
#     mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
#     mask = ndi.gaussian_filter(mask, sigma=l / (4. * n))  # 高斯滤波
#     return mask > mask.mean()
#
#
# data = microstructure(l=128) * 1  # 生成测试图片

openpath = "C:/Users/Dero/Desktop/dingxiang_area/dilation/10.png"
image1 = Image.open(openpath)
img_array1 = np.asarray(image1)
labels = measure.label(img_array1, connectivity=2)  #

# 筛选连通区域大于５００的
properties = measure.regionprops(labels)
valid_label = set()
num = 0
for prop in properties:
    if prop.area > num:
        max_one = prop.label
        num = prop.area

valid_label.add(max_one)
current_bw = np.in1d(labels, list(valid_label)).reshape(labels.shape)

# dst = color.label2rgb(current_bw)  # 根据不同的标记显示不同的颜色
print('regions number:', current_bw.max() + 1)  # 显示连通区域块数(从0开始标记)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(img_array1, plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.imshow(current_bw, plt.cm.gray, interpolation='nearest')
ax2.axis('off')
# ax3.imshow(dst, interpolation='nearest')
# ax3.axis('off')

fig.tight_layout()
plt.show()

