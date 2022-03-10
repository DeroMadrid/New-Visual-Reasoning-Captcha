import os
import cv2


path = os.listdir(r"C:/Users/Dero/Desktop/baidu_captcha")
save_path = "C:/Users/Dero/Desktop/demo/"
for file in path:
    open_path = "C:/Users/Dero/Desktop/baidu_captcha/" + file
    # f = file[:-4]
    # save_path1 = save_path + f[-1] + "/" + file
    # image = Image.open(open_path)
    save_path1 = save_path + file
    image = cv2.imread(open_path)
    im2 = cv2.resize(image, (100, 100))
    cv2.imwrite(save_path1, im2)
#
#
# test_path = "C:/Users/Dero/Desktop/1.png"
# im1 = cv2.imread(test_path)
# im2 = cv2.resize(im1, (40, 70))
# save_path = "C:/Users/Dero/Desktop/2.png"
# cv2.imwrite(save_path, im2)