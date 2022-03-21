import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
import preprocessing
import pyautogui
import math
import numpy as np
from PIL import Image
from skimage import measure
# storing the size of the screen
size = pyautogui.size()
print(size)
print(size.width)

from selenium.common import exceptions as EX
chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)  # 声明一个浏览器对象

browser.get("https://www.dingxiang-inc.com/business/captcha")

while True:
    # 获取图片部分
    time.sleep(3)
    # (1163, 887) on the Desktop, and (1112, 699) on the cyl PC
    pyautogui.moveTo(1163, 887)
    time.sleep(0.5)
    butt = browser.find_element_by_xpath("//li[contains(@class, 'item-10')]")
    action = ActionChains(browser)
    action.move_to_element(butt).perform()
    action.click(butt).perform()
    time.sleep(0.5)
    pyautogui.scroll(-500)
    pyautogui.click()
    time.sleep(1)
    butt1 = browser.find_element_by_xpath("//div[contains(@class, 'dx_captcha_clickword_pic')]/img")
    time.sleep(0.5)
    image0 = butt1.get_attribute('src')
    filepath = "C:/Users/Dero/Desktop/dingxiang_area/dx/"
    image_path = filepath + str(111) + ".png"
    r = requests.get(image0)  # 请求图片地址，注意”r“
    with open(image_path, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
    binary_path = filepath + str(222) + ".png"
    # 图片二值化部分
    preprocessing.binary(image_path, binary_path, "fixed_threshold", 180)

    # 图像边界线膨胀部分
    erode_path = "C:/Users/Dero/Desktop/dingxiang_area/dx/full.png"
    place_path = "C:/Users/Dero/Desktop/dingxiang_area/dx/full.png"
    image1 = Image.open(binary_path)
    img_array1 = np.asarray(image1)
    image2 = Image.open(place_path)
    img_array2 = np.asarray(image2)
    for i in range(0, 150):
        for j in range(0, 150):
            img_array2[i][j] = 0
    # (300, 150), 长300，宽150。
    for i in range(0, 150):
        for j in range(0, 300):
            img_array2[i][j] = img_array1[i][j]
            if img_array1[i][j] == 255:
                for m in range(-10, 11):
                    for n in range(-10, 11):
                        if 150 > (i + m) >= 0 and 300 > (j + n) >= 0:
                            img_array2[i + m][j + n] = 255

    for i in range(0, 150):
        for j in range(0, 300):
            if img_array2[i][j] == 255:
                img_array2[i][j] = 0
            else:
                img_array2[i][j] = 255
    i11 = Image.fromarray(np.uint8(img_array2))
    # img_save = cv2.cvtColor(np.asarray(img_array2), cv2.COLOR_RGB2BGR)
    #
    # cv2.imwrite(savapath, img_save)
    i11.save(erode_path)

    # 获取点击区域的重心坐标
    image1 = Image.open(erode_path)
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
            point = prop.centroid

    print(point)
    point_i = 1126 + int(point[1])
    point_j = 657 + int(point[0])
    pyautogui.moveTo(point_i, point_j)
    pyautogui.click()
    time.sleep(2)
    # start-point 为(1126,423)on the Desktop
    browser.refresh()
