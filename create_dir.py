import re
import os

with open('C:/Users/Dero/Desktop/record.txt', 'r') as fp:
    for line in fp:
        # line = fp.readline()
        content = line[0]
        path = "C:/Users/Dero/Desktop/character_wiki/" + str(content)
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)