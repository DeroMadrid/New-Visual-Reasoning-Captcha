import preprocessing
import cv2
import os
import numpy as np
from PIL import Image
import math

images_path = os.listdir(r"C:/Users/Dero/Desktop/dingxiang_area/dx")
for filelist in images_path:
    openpath = "C:/Users/Dero/Desktop/dingxiang_area/dx/" + filelist
    image1 = cv2.imread(openpath)
    savepath = "C:/Users/Dero/Desktop/dingxiang_area/binary/" + filelist[:-4] + ".png"
    savepath1 = "C:/Users/Dero/Desktop/dingxiang_area/dilation/" + filelist[:-4] + ".png"
    # savepath1 = "C:/Users/Dero/Desktop/dxxx/" + filelist[:-4] + "220.png"
    preprocessing.binary(openpath, savepath, "fixed_threshold", 180)
    preprocessing.dilation(savepath, savepath1)
