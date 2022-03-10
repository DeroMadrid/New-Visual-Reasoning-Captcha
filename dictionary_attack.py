# 字典攻击
import itertools  # 迭代器
import datetime
import hashlib
import time


def generatelibary(library, length=8):
    libararys = itertools.product(library, repeat=length)
    dic = open("paswordlirbarys.txt", "w", encoding='utf-8')  # 写模式打开文件
    for i in libararys:
        dic.writelines(i)
        dic.writelines("\n")
    dic.close()


# x = hashlib.md5("123".encode(encoding="utf-8")).hexdigest()#hash算法存储密码
# 202cb962ac59075b964b07152d234b70
# print(x)
def dict_attack(path, password):
    file = open(path)
    for passwords in file:
        # print(passwords)
        passwords = passwords.split("\n")[0]
        if password == hashlib.md5(passwords.encode(encoding="utf-8")).hexdigest():
            print("已破解：")
            print("你的密码是：{}".format(passwords))
    file.close()


if __name__ == "__main__":
    lowercase = 'abcdefghijklmnopqrstuvwxyz'#字符组合
    uppercase = 'ABCDEFGHIJKLMNOPQRS'
    digits = '0123456789'
    # pword = "wanglo"
    pword = "WaNa109"
    # pword表示真实密码
    # print(hashlib.md5(pword.encode(encoding="utf-8")).hexdigest())
    # 得到真实密码的hash值
    special = """!"#$%&'( )*+,-./:;<=>?@[]^_`{|}~"""
    word = lowercase + uppercase + digits + special
    # word表示所有的字符序列
    starttime = datetime.datetime.now()  # 获取当前时间
    # print(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
    # generatelibary(pword, length=6)  # 生成6位数字字典
    dict_attack("paswordlirbarys.txt", "5092d6ca306eea961c6a2cdb37aa9744")
    endtime = datetime.datetime.now()
    # print(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
    print('The time cost: ')
    print(endtime - starttime)  # 时间
