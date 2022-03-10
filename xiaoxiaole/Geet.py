from numpy import array
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
from skimage.metrics import structural_similarity
import pyautogui


def check_row(arr, i):
    flag = -1
    num = -1
    if arr[i, 0] == arr[i, 1]:
        num = arr[i, 0]
        flag = 2
    if arr[i, 0] == arr[i, 2]:
        num = arr[i, 0]
        flag = 1
    if arr[i, 1] == arr[i, 2]:
        num = arr[i, 1]
        flag = 0
    return num, flag


def check_column(arr, j):
    flag = -1
    num = -1
    if arr[0, j] == arr[1, j]:
        num = arr[0, j]
        flag = 2
    if arr[0, j] == arr[2, j]:
        num = arr[0, j]
        flag = 1
    if arr[1, j] == arr[2, j]:
        num = arr[1, j]
        flag = 0
    return num, flag


def check_main(arr):
    flag = -1
    num = -1
    if arr[0, 0] == arr[1, 1]:
        flag = 2
        num = arr[0, 0]
    if arr[1, 1] == arr[2, 2]:
        flag = 0
        num = arr[1, 1]
    if arr[0, 0] == arr[2, 2]:
        flag = 1
        num = arr[0, 0]
    return num, flag


def check_fu(arr):
    # flag代表行数
    flag = -1
    num = -1
    if arr[0, 2] == arr[1, 1]:
        flag = 2
        num = arr[0, 2]
    if arr[0, 2] == arr[2, 0]:
        flag = 1
        num = arr[0, 2]
    if arr[1, 1] == arr[2, 0]:
        flag = 0
        num = arr[1, 1]
    return num, flag


chrome_driver = r"C:/Users/Dero/anaconda3/envs/zy/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)  # 声明一个浏览器对象

browser.get("https://www.geetest.com/adaptive-captcha-demo")
browser.maximize_window()
browser.refresh()
butt = browser.find_element_by_xpath("//div[contains(@class, 'tab-item tab-item-3')]")
action = ActionChains(browser)

action.move_to_element(butt).perform()
action.click(butt).perform()

#
# action.click_and_hold(butt).perform()
# action.release(butt).perform()
# time.sleep(5)
time.sleep(1)
butt1 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_btn_click')]")
action.move_to_element(butt1).perform()
action.click(butt1).perform()
time.sleep(5)
image0 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_img-0 geetest_item_')]")
string0 = image0.get_attribute('style')[23:-3]
image1 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_img-1 geetest_item_')]")
string1 = image1.get_attribute('style')[23:-3]
image2 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_img-2 geetest_item_')]")
string2 = image2.get_attribute('style')[23:-3]
image3 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_img-3 geetest_item_')]")
string3 = image3.get_attribute('style')[23:-3]
image4 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_img-4 geetest_item_')]")
string4 = image4.get_attribute('style')[23:-3]
image5 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_img-5 geetest_item_')]")
string5 = image5.get_attribute('style')[23:-3]
image6 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_img-6 geetest_item_')]")
string6 = image6.get_attribute('style')[23:-3]
image7 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_img-7 geetest_item_')]")
string7 = image7.get_attribute('style')[23:-3]
image8 = browser.find_element_by_xpath("//div[contains(@class, 'geetest_img-8 geetest_item_')]")
string8 = image8.get_attribute('style')[23:-3]

click_list = [image0, image1, image2, image3, image4, image5, image6, image7, image8]
string_list = [string0, string1, string2, string3, string4, string5, string6, string7, string8]
for i in range(9):
    path = string_list[i]
    filepath = "C:/Users/Dero/Desktop/xiaoxiaole/"
    image_path = filepath + str(i) + ".png"
    r = requests.get(path)  # 请求图片地址，注意”r“
    with open(image_path, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)

image_list = []
for i in range(9):
    filepath = "C:/Users/Dero/Desktop/xiaoxiaole/"
    image_path = filepath + str(i) + ".png"
    iii = cv2.imread(image_path)
    image_list.insert(i, cv2.cvtColor(iii, cv2.COLOR_RGB2GRAY))

print(len(image_list))
count = 1
count_list = []
count_list.insert(0, 1)
for i in range(1, 9):
    j = 0
    flag = 0
    while j < i:
        (score, diff) = structural_similarity(image_list[j], image_list[i], full=True)
        if score == 1:
            count_list.insert(i,  count_list[j])
            flag = 1
            break
        j += 1
    if flag == 0:
        count += 1
        count_list.insert(i, count)

mat = array([[count_list[0], count_list[3], count_list[6]], [count_list[1], count_list[4], count_list[7]], [count_list[2], count_list[5], count_list[8]]])
p1 = p2 = (-1, -1)
i = 0
while i <= 2:
    num, j = check_row(mat, i)
    if num != -1:
        if i == 0 and num == mat[i+1, j]:
            p1 = (0, j)
            p2 = (1, j)
            break
        if i == 2 and num == mat[i-1, j]:
            p1 = (1, j)
            p2 = (2, j)
            break
        if i == 1 and num == mat[i-1, j]:
            p1 = (0, j)
            p2 = (1, j)
            break
        if i == 1 and num == mat[i+1, j]:
            p1 = (1, j)
            p2 = (2, j)
            break
    i += 1

j = 0
while j <= 2:
    num, i = check_column(mat, j)
    if num != -1:
        if j == 0 and num == mat[i, j+1]:
            p1 = (i, 0)
            p2 = (i, 1)
            break
        if j == 2 and num == mat[i, j - 1]:
            p1 = (i, 1)
            p2 = (i, 2)
            break
        if j == 1 and num == mat[i, j-1]:
            p1 = (i, 0)
            p2 = (i, 1)
            break
        if j == 1 and num == mat[i, j+1]:
            p1 = (i, 1)
            p2 = (i, 2)
            break
    j += 1

# num, i = check_main(mat)
# if num != -1:
#     if i == 0:
#         if mat[0, 1] == num:
#             p1 = (0, 0)
#             p2 = (0, 1)
#         if mat[1, 0] == num:
#             p1 = (0, 0)
#             p2 = (1, 0)
#     if i == 2:
#         if mat[2, 1] == num:
#             p1 = (2, 1)
#             p2 = (2, 2)
#         if mat[1, 2] == num:
#             p1 = (1, 2)
#             p2 = (2, 2)
#     if i == 1:
#         if mat[0, 1] == num:
#             p1 = (0, 1)
#             p2 = (1, 1)
#         if mat[1, 0] == num:
#             p1 = (1, 0)
#             p2 = (1, 1)
#         if mat[1, 2] == num:
#             p1 = (1, 1)
#             p2 = (1, 2)
#         if mat[2, 1] == num:
#             p1 = (1, 1)
#             p2 = (2, 1)
#
# num, i = check_fu(mat)
# if num != -1:
#     if i == 0:
#         if mat[0, 1] == num:
#             p1 = (0, 1)
#             p2 = (0, 2)
#         if mat[1, 2] == num:
#             p1 = (0, 2)
#             p2 = (1, 2)
#     if i == 2:
#         if mat[2, 1] == num:
#             p1 = (2, 0)
#             p2 = (2, 1)
#         if mat[1, 0] == num:
#             p1 = (1, 0)
#             p2 = (2, 0)
#     if i == 1:
#         if mat[0, 1] == num:
#             p1 = (0, 0)
#             p2 = (1, 1)
#         if mat[1, 0] == num:
#             p1 = (1, 0)
#             p2 = (1, 1)
#         if mat[1, 2] == num:
#             p1 = (1, 1)
#             p2 = (1, 2)
#         if mat[2, 1] == num:
#             p1 = (1, 1)
#             p2 = (2, 1)

print(p1, p2)
print(p1[0], p1[1], p2[0], p2[1])
click1 = p1[1] * 3 + p1[0]
click2 = p2[1] * 3 + p2[0]
pyautogui.scroll(-100)

pyautogui.moveTo(1200, 700, duration=0.25)
pyautogui.move(100*p1[1], 100*p1[0], duration=0.25)
time.sleep(0.5)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1200, 700, duration=0.25)
pyautogui.move(100*p2[1], 100*p2[0], duration=0.25)
time.sleep(0.5)
pyautogui.click()