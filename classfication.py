import os
import cv2

# 51 49
picture_path = os.listdir(r"C:/Users/Dero/Desktop/try/wiki/train/")
for filelist in picture_path:
    open_path = "C:/Users/Dero/Desktop/try/wiki/train/" + filelist
    save_path1 = "C:/Users/Dero/Desktop/length/"
    img = cv2.imread(open_path)
    character = filelist.split("_")[1].split(".")[0]
    # print
    # 根据文件名找到对应的字符名
    # ch = filelist[-5]
    # save_path = save_path1 + ch + "/" + filelist
    # img = cv2.imread(open_path)
    if len(character) == 8:
        save_path = save_path1 + "8/" + filelist
    elif len(character) == 9:
        save_path = save_path1 + "9/" + filelist
    elif len(character) == 10:
        save_path = save_path1 + "10/" + filelist
    else:
        save_path = save_path1 + "1/" + filelist
    cv2.imwrite(save_path, img)
    # os.remove(save_path)