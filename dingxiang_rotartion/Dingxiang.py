import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
import preprocessing
import pyautogui
import math
import numpy as np
from PIL import Image
from selenium.common import exceptions as EX
# storing the size of the screen
size = pyautogui.size()
print(size)
print(size.width)


chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)  # 声明一个浏览器对象

browser.get("https://www.dingxiang-inc.com/business/captcha")
time.sleep(3)
while True:

    time.sleep(0.5)
    # (1163, 887) on the Desktop, and (1112, 699) on the cyl PC
    pyautogui.moveTo(1163, 887)
    butt = browser.find_element_by_xpath("//li[contains(@class, 'item-9')]")
    action = ActionChains(browser)
    action.move_to_element(butt).perform()
    action.click(butt).perform()
    time.sleep(0.5)
    pyautogui.scroll(-500)
    pyautogui.click()
    time.sleep(0.5)
    butt1 = browser.find_element_by_xpath("//div[contains(@class, 'dx_captcha_rotate_sub-slider')]/img")
    time.sleep(0.5)
    image0 = butt1.get_attribute('src')
    # action.move_to_element(butt1).perform()
    # action.click(butt1).perform()dx_captcha_rotate_bg
    butt2 = browser.find_element_by_xpath("//div[contains(@class, 'dx_captcha_rotate_bg')]/img")
    time.sleep(0.5)
    image1 = butt2.get_attribute('src')
    # image_list = [image0, image1]
    # i = 0
    # for path in image_list:
    #     i += 1
    #     filepath = "C:/Users/Dero/Desktop/dx/"
    #     image_path = filepath + str(i) + ".png"
    #     r = requests.get(path)  # 请求图片地址，注意”r“
    #     with open(image_path, 'wb') as fd:
    #         for chunk in r.iter_content():
    #             fd.write(chunk)
    filepath = "C:/Users/Dero/Desktop/dx/"
    image_path = filepath + str(111) + ".png"
    r = requests.get(image0)  # 请求图片地址，注意”r“
    with open(image_path, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)

    openpath = "C:/Users/Dero/Desktop/dx/111.png"
    savapath = "C:/Users/Dero/Desktop/dx/" + str(222) + ".png"
    preprocessing.binary(openpath, savapath, "fixed_threshold", 220)

    openpath = "C:/Users/Dero/Desktop/dx/222.png"
    # image1 = cv2.imread(openpath)
    image1 = Image.open(openpath)
    img_array1 = np.asarray(image1)
    count = 0
    num_x = 0
    num_y = 0
    for i in range(0, 160):
        for j in range(0, 160):
            if img_array1[i][j] == 255:
                if 81 ** 2 >= (i - 80) ** 2 + (j - 80) ** 2 >= 64 ** 2:
                    count += 1
                    num_x += i
                    num_y += j
                else:
                    img_array1[i][j] = 0
    # print((num_x, num_y, count))
    if count == 0:
        browser.refresh()
        continue
    avg_x = int(num_x / count)
    avg_y = int(num_y / count)

    # print((avg_x, avg_y))

    if avg_x != 80:
        tans = abs(avg_y - 80) / abs(avg_x - 80)
        x = math.atan(tans)
        xx = x * 180 / math.pi

    else:
        xx = 90
    print(xx)
    anger = 0
    if avg_x <= 80:
        if avg_y > 80:
            anger = 180 - xx
        else:
            anger = 180 + xx
    else:
        if avg_y > 80:
            anger = xx
        else:
            anger = 360 - xx

    print(anger)
    length = anger / 360 * 300
    print(length)

    time.sleep(0.2)
    pyautogui.mouseDown()
    pyautogui.dragRel(length, 0, 2)
    time.sleep(0.2)
    pyautogui.mouseUp()
    browser.refresh()
