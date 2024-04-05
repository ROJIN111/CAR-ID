import cv2 as cv2
import numpy as np



# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"






from paddleocr import PaddleOCR
img_path = r"D:\pythonProject\STUDY\bishe\Pframe0.jpg"
ocr = PaddleOCR(use_angle_cls=True, lang="ch")
ocr.ocr(img_path, cls=True)
print(ocr)









# # 读取图片
# imagePath = r'D:\pythonProject\STUDY\bishe\shujuji\test\CBLPRD-330k\36710.jpg'
# img = cv2.imread(imagePath)
# # 转化成灰度图
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # 利用Sobel边缘检测生成二值图
# sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)
# # 二值化
# ret, binary = cv2.threshold(sobel, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
# # 膨胀、腐蚀
# element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 9))
# element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (24, 6))
# # 膨胀一次，让轮廓突出
# dilation = cv2.dilate(binary, element2, iterations=1)
# # 腐蚀一次，去掉细节
# erosion = cv2.erode(dilation, element1, iterations=1)
# # 再次膨胀，让轮廓明显一些
# dilation2 = cv2.dilate(erosion, element2, iterations=2)
#
# #  查找轮廓和筛选文字区域
# region = []
# contours, hierarchy = cv2.findContours(dilation2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for i in range(len(contours)):
#     cnt = contours[i]
#
#     # 计算轮廓面积，并筛选掉面积小的
#     area = cv2.contourArea(cnt)
#     if (area < 1000):
#         continue
#
#     # 找到最小的矩形
#     rect = cv2.minAreaRect(cnt)
#     print ("rect is: ")
#     print (rect)
#     # box是四个点的坐标
#     box = cv2.boxPoints(rect)
#     box = np.int0(box)
#     # 计算高和宽
#     height = abs(box[0][1] - box[2][1])
#     width = abs(box[0][0] - box[2][0])
#     # 根据文字特征，筛选那些太细的矩形，留下扁的
#     if (height > width * 1.3):
#         continue
#
#     region.append(box)
#
# # 绘制轮廓
# for box in region:
#     cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#









# lower_red = np.array([0, 127, 128]) # 红色阈值下界
# higher_red = np.array([10, 255, 255]) # 红色阈值上界
# lower_yellow = np.array([15, 230, 230]) # 黄色阈值下界
# higher_yellow = np.array([35, 255, 255]) # 黄色阈值上界
# lower_blue = np.array([85,240,140])
# higher_blue = np.array([100,255,165])
#
# # 1、读取图片，转灰度图
# img = cv2.imread(r'D:\pythonProject\STUDY\bishe\Pframe0.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)
# sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)
# cv2.imshow('1', sobel)
# car_blur = cv2.GaussianBlur(gray,(3,3),0)
# cv2.imshow('111', car_blur)
# # car_edge = cv2.Canny(car_blur,250,300)
# # cv2.imshow('111', car_edge)
# #
# # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,1))
# # car_dilation_2 = cv2.dilate(car_edge,kernel,iterations=2)
# # cv2.imshow('car_dilation_2',car_dilation_2)
#
#
# cv2.waitKey(0)











# import cv2
# import numpy as np
#
#
# # 滑动条的回调函数，获取滑动条位置处的值
# def empty(a):
#     h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
#     print(h_min, h_max, s_min, s_max, v_min, v_max)
#     return h_min, h_max, s_min, s_max, v_min, v_max
#
#
# path = r'D:\pythonProject\STUDY\bishe\Pframe0.jpg'
# # 创建一个窗口，放置6个滑动条
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars", 640, 240)
# cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
# cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
# cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
# cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
# cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
# cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
#
# while True:
#     img = cv2.imread(path)
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     # 调用回调函数，获取滑动条的值
#     h_min, h_max, s_min, s_max, v_min, v_max = empty(0)
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     # 获得指定颜色范围内的掩码
#     mask = cv2.inRange(imgHSV, lower, upper)
#     # 对原图图像进行按位与的操作，掩码区域保留
#     imgResult = cv2.bitwise_and(img, img, mask=mask)
#
#     cv2.imshow("Mask", mask)
#     cv2.imshow("Result", imgResult)
#
#     cv2.waitKey(1)

#
# # 1、读取图片，转灰度图
# img = cv2.imread(r'D:\pythonProject\STUDY\bishe\Pframe0.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('gray', gray)
#
#
# car_blur = cv2.GaussianBlur(gray,(3,3),0)
# car_edge = cv2.Canny(car_blur,250,300)
# cv2.imshow('111', car_edge)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,1))
# car_dilation_2 = cv2.dilate(car_edge,kernel,iterations=2)
# cv2.imshow('car_dilation_2',car_dilation_2)
#
#
# cv2.waitKey(0)