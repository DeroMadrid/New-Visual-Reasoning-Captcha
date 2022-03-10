from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import requests

# crack = CrackGeetest()
# crack.crack()
chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)  # 声明一个浏览器对象
try:
    # browser.get("https://www.baidu.com")  # 传入URL

    browser.get("https://wappass.baidu.com/static/captcha/tuxing.html?ak=2ef521ec36290baed33d66de9b16f625&backurl=http%3A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25C1%25AC%25BB%25B4%25D1%25EF%25D5%25F2%25CC%25FA%25C2%25B7%26fr%3Dala0%26tpl%3D5%26dyTabStr%3DMCw2LDEsNCwzLDUsMiw3LDgsOQ%253D%253D&timestamp=1636966854&signature=a40e31edd78bde8c3c5665c080cd0730")
    # vcode - spin - button - p918
    time.sleep(3)
    while True:
        browser.refresh()
        time.sleep(3)
        input = browser.find_element_by_xpath("//div[contains(@id, 'vcode-spin-button')]")

        # 这部分是对按钮进行操作
        action = ActionChains(browser)

        action.click_and_hold(input).perform()
        action.move_by_offset(xoffset=130, yoffset=0).perform()
        action.release().perform()


finally:
    # browser.close()
    wait = WebDriverWait(browser, 100)  # 等待