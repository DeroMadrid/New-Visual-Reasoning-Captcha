import time
from selenium import webdriver
import pyautogui

chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)  # 声明一个浏览器对象

browser.get("https://www.dingxiang-inc.com/business/captcha")
time.sleep(3)
(x, y) = pyautogui.position()
print((x, y))
