from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import requests
import numpy as np
import cv2
import math
from scipy import ndimage
import thresholdCaculating

chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)  # 声明一个浏览器对象

browser.get("https://wappass.baidu.com/static/captcha/tuxing.html?ak=2ef521ec36290baed33d66de9b16f625&backurl=http%3"
                "A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25C1%25AC%25BB%25B4%25D1%25EF%25D5%25F2%25CC%25FA%25C2%25B7%26fr%3Dal"
                "a0%26tpl%3D5%26dyTabStr%3DMCw2LDEsNCwzLDUsMiw3LDgsOQ%253D%253D&timestamp=1636966854&signature=a40e31edd78"
                "bde8c3c5665c080cd0730")

time.sleep(1)
while True:
    browser.refresh()
    time.sleep(1)
    image = browser.find_element_by_xpath("//img[contains(@id, 'vcode-spin-img')]")
    # 爬取图片src以及系统给他的编号
    img_path0 = image.get_attribute('src')
    img_name0 = image.get_attribute('id')

    filepath = "C:/Users/Dero/Desktop/baidu/"
    image_path = filepath + img_name0 + ".png"

    r = requests.get(img_path0)  # 请求图片地址，注意”r“

    with open(image_path, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)

    img_before = cv2.imread(image_path)
    img_judge = cv2.imread(image_path, 0)
    # cv2.imshow("Before", img_before)
    # key = cv2.waitKey(0)
    threshold = thresholdCaculating.average_threshold(img_judge)
    ret, binary_result = cv2.threshold(img_judge,  threshold, 255, cv2.THRESH_BINARY)
    (height, width) = binary_result.shape[:2]
    # 新建一个与图像长度一致的数组
    numofwhite = [0] * height
    # 循环统计每一列白色像素的个数
    for i in range(0, width):
        for j in range(0, height):
            if binary_result[i][j] == 255:  # change
                numofwhite[i] = numofwhite[i] + 1
    print(numofwhite)
    count_l = 0
    count_r = 0
    i = 0
    j = width - 1
    for i in range(0, int(width/2)):
        count_l += numofwhite[i]

    for j in range(width-1, int(width/2)):
        count_r += numofwhite[j]

    if count_r > count_l:
        flag = 1
    else:
        flag = 0

    img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
    # 边缘检测
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 20, minLineLength=50, maxLineGap=5)
    # 检测标准霍夫变化的二值图像直线线条

    angles = []
    if lines is None:
        continue

    for [[x1, y1, x2, y2]] in lines:
        cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        angles.append(angle)

    # cv2.imshow("Detected lines", img_before)
    # key = cv2.waitKey(0)

    median_angle = np.median(angles)
    img_rotated = ndimage.rotate(img_before, median_angle)

    print(f"Angle is {median_angle:.04f}")
    # cv2.imwrite('rotated.jpg', img_rotated)

    # 计算旋转角度与滑动距离的关系：

    if median_angle > 0:
        if flag == 1:
            rotation_anger = median_angle - 360
        else:
            rotation_anger = median_angle - 180
    else:
        if flag == 1:
            rotation_anger = median_angle - 180
        else:
            rotation_anger = median_angle

    rotation_anger = -1.0 * rotation_anger
    print(f"Angle is {rotation_anger:.04f}")
    rotation_anger = 360-rotation_anger
    distance = 1.0 * rotation_anger / 360 * 220
    print(distance)

    input = browser.find_element_by_xpath("//div[contains(@id, 'vcode-spin-button')]")

    # 这部分是对按钮进行操作
    action = ActionChains(browser)

    action.click_and_hold(input).perform()
    action.move_by_offset(xoffset=distance, yoffset=0).perform()
    action.release().perform()
    time.sleep(1)