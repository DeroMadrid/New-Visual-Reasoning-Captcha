import requests
count = 1
while count <= 6:
    img_path0 = "https://static.geetest.com/nerualpic/v4_test/v4_match_test/emoji/emoji"
    path = img_path0 + str(count) + ".png"
    filepath = "C:/Users/Dero/Desktop/xiaoxiaole/"
    image_path = filepath + str(count) + ".png"
    count += 1
    r = requests.get(path)  # 请求图片地址，注意”r“
    with open(image_path, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)