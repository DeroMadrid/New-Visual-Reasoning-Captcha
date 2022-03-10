import os
import cv2

# 51 49 D:\A验证码数据集\English_nosegment\alipay\train
# picture_path = os.listdir(r"D:/ACaptchaSet/English_nosegment/360/train")
picture_path = os.listdir(r"C:/Users/Dero/Desktop/try/apple/image_erosion_train/")
for filelist in picture_path:
    open_path = "C:/Users/Dero/Desktop/try/apple/image_erosion_train/" + filelist
    save_path1 = "C:/Users/Dero/Desktop/apple_pre_train/"
    img = cv2.imread(open_path)
    character = filelist.split("_")[1].split(".")[0]
    save_path = save_path1 + str(character) + ".png"
    im2 = cv2.resize(img, (72, 24))
    cv2.imwrite(save_path, im2)
    # print
    # 根据文件名找到对应的字符名
    # ch = filelist[-5]
    # save_path = save_path1 + ch + "/" + filelist
    # img = cv2.imread(open_path)