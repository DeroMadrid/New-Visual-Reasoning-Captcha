import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import os

# 批量更改图片，旋转加更改大小
# for z in range(20, 340, 10):
images_path = os.listdir(r"C:/Users/Dero/Desktop/rrr")
for filelist in images_path:
    open_path = "C:/Users/Dero/Desktop/rrr/" + filelist
    save_path = "C:/Users/Dero/Desktop/test_new/" + filelist[:-4]
    img = Image.open(open_path)
    # 修改角度
    dst5 = img.rotate(10)
    re_img = np.asarray(dst5)
    # 图片大小为350*350
    for i in range(0, 350):
        for j in range(0, 350):
            if (i - 175) ** 2 + (j - 175) ** 2 > 175 ** 2:
                re_img[i][j] = 255

    Image.fromarray(np.uint8(re_img))
    img_save = cv2.cvtColor(np.asarray(re_img), cv2.COLOR_RGB2BGR)
    img_save = cv2.resize(img_save, (100, 100))
    path = save_path + "_" + str(4) + '.png'
    cv2.imwrite(path, img_save)


