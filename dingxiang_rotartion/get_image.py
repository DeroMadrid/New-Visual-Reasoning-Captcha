import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
import preprocessing
import pyautogui
import math
import numpy as np
from PIL import Image
# storing the size of the screen
size = pyautogui.size()
print(size)
print(size.width)

from selenium.common import exceptions as EX
chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)  # 声明一个浏览器对象

browser.get("https://www.dingxiang-inc.com/business/captcha")

for count in range(175, 190):
    time.sleep(1)
    butt = browser.find_element_by_xpath("//li[contains(@class, 'item-9')]")
    action = ActionChains(browser)
    action.move_to_element(butt).perform()
    action.click(butt).perform()
    time.sleep(1)
    pyautogui.scroll(-500)
    pyautogui.click()
    time.sleep(1)
    butt1 = browser.find_element_by_xpath("//div[contains(@class, 'dx_captcha_rotate_sub-slider')]/img")
    time.sleep(1)
    image0 = butt1.get_attribute('src')
    filepath = "C:/Users/Dero/Desktop/dx/"
    image_path = filepath + str(count) + ".png"
    r = requests.get(image0)  # 请求图片地址，注意”r“
    with open(image_path, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
    browser.refresh()