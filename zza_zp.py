#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cv2


class opencvs():

    def main(self):

        # 告诉OpenCV使用什么识别分类器
        classfier = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

        # 读取一张照片
        frame = cv2.imread("C:/Users/Dero/Desktop/3.jpg")
        # 显示方向
        # frame = cv2.flip(frame, 1)

        # 将当前帧转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 检测结果
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=2, minSize=(50, 150))

        # 第一个参数是灰度图像
        # 第三个参数是人脸检测次数，设置越高，误检率越低，但是对于迷糊图片，我们设置越高，越不易检测出来

        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), (0, 255, 0), 1)
                print("get one")

            if len(faceRects) >= 3:
                print("over 3")

        # 显示图像
        cv2.imshow(' ', frame)
        # 键盘Q键结束
        c = cv2.waitKey(10000)


if __name__ == '__main__':
    opencvs().main()

