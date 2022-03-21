import numpy as np
from skimage.measure import label
import cv2
import matplotlib.pyplot as plt


def getLargestCC(segmentation):
    labels = label(segmentation)
    assert (labels.max() != 0)  # assume at least 1 CC
    largestCC = labels == np.argmax(np.bincount(labels.flat)[1:]) + 1
    return largestCC


openpath = "C:/Users/Dero/Desktop/dingxiang_area/dilation/1.png"
image1 = cv2.imread(openpath)
o = getLargestCC(image1)

for i in range(0, 150):
    for j in range(0, 300):
        if o[i][j].all():
            o[i][j] = 1
        else:
            o[i][j] = 0
print(o)
# plt.imshow(o)
# plt.savefig("22")
