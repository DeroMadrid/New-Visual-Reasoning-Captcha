from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import requests

# 导入ChromeDriver
chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)  # 声明一个浏览器对象
try:
    # 传入URL
    browser.get("https://wappass.baidu.com/static/captcha/tuxing.html?ak=2ef521ec36290baed33d66de9b16f625&backurl=http%3"
                "A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25C1%25AC%25BB%25B4%25D1%25EF%25D5%25F2%25CC%25FA%25C2%25B7%26fr%3Dal"
                "a0%26tpl%3D5%26dyTabStr%3DMCw2LDEsNCwzLDUsMiw3LDgsOQ%253D%253D&timestamp=1636966854&signature=a40e31edd78"
                "bde8c3c5665c080cd0730")

    time.sleep(3)
    count = 0
    while count < 1000:
        # 获取页面中图片的元素
        browser.refresh()
        time.sleep(1)
        image = browser.find_element_by_xpath("//img[contains(@id, 'vcode-spin-img')]")
        # 爬取图片src以及系统给他的编号
        img_path0 = image.get_attribute('src')
        img_name0 = image.get_attribute('id')

        filepath = "C:/Users/Dero/Desktop/baidu/"
        image_path= filepath + img_name0 + ".png"

        r = requests.get(img_path0)  # 请求图片地址，注意”r“

        with open(image_path, 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
        count += 1



finally:
    # browser.close()
    wait = WebDriverWait(browser, 100)  # 等待