import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog
# 导入cv相关库
import cv2
import numpy as np
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
# 导入依赖包
import hyperlpr3 as lpr3
import tkinter as tk
import tkinter.filedialog
import mysql.connector
from datetime import datetime

# win = tk.Tk()
# win.title("label")
# #显示图片(注意这里默认支持的图片格式为GIF)
# img_gif = tk.PhotoImage(file = '11.gif')
# img_gif0 = tk.PhotoImage(file = '22.gif')#这是给按钮准备的
# # 将图片放在主窗口的右边
# label_img = tk.Label(win,image=img_gif)#这是图片
# label_img.pack(side="right")#这是图片位置
# # 显示文字，设置文本格式
# text_var = tk.StringVar()
# text_var.set("C语言中文网欢迎您,\n"
#              "这里有精彩的教程,\n "
#              "这里有数不尽的知识宝藏")
# lab_text =tk.Label(win,textvariable=text_var,fg ='#7CCD7C',font=('微软雅黑',15,'italic'),justify='left',padx=10).pack(side='left')
# im = tk.PhotoImage(file='6.gif')
def time1():
    # 获取当前日期和时间
    current_date_time = datetime.now()
    # 仅获取当前日期
    current_date = current_date_time.date()
    # print("当前日期和时间:", current_date_time)
    print("当前日期:", current_date)
    # 格式化当前时间，只保留到秒
    current_time = current_date_time.strftime("%H:%M:%S")
    print("当前时间:", current_time)
    return current_date,current_time
def draw_plate_on_image(img, box, text, font):
    x1, y1, x2, y2 = box
    cv2.rectangle(img, (x1, y1), (x2, y2), (139, 139, 102), 2, cv2.LINE_AA)
    cv2.rectangle(img, (x1, y1 - 20), (x2, y1), (139, 139, 102), -1)
    data = Image.fromarray(img)
    draw = ImageDraw.Draw(data)
    draw.text((x1 + 1, y1 - 18), text, (0, 255, 0), font=font)
    res = np.asarray(data)
    return res
def qidon1(path1):
    # 中文字体加载
    # path = tkinter.filedialog.askopenfilename()
    # path.set(path)
    print('路径', path1)
    font_ch = ImageFont.truetype("font/simsun.ttc", 20, 0)
    # 实例化识别对象
    catcher = lpr3.LicensePlateCatcher(detect_level=lpr3.DETECT_LEVEL_HIGH)
    # 读取图片
    image = cv2.imread(path1)
    # 执行识别算法
    results = catcher(image)
    print(results)
    result = results[0][0]
    print(result)
    # data = [['苏FM30Q1', 0.9984631, 0, [269, 177, 524, 262]]]
    # result = data[0][0]
    # print(result)  # 这将打印出 '苏FM30Q1'
    for code, confidence, type_idx, box in results:
        # 解析数据并绘制
        text = f"{code} - {confidence:.2f}"
        image = draw_plate_on_image(image, box, text, font=font_ch)
    # 显示检测结果
    cv2.imshow("w", image)
    cv2.waitKey(0)
    return result
def shujuku1(chepai):
  mydb = mysql.connector.connect(
    host="192.168.182.128", # 主机地址，端口默认 port="3306"
    user="1111", # 用户名
    password="123456", # 用户密码
    database="runoob" #数据库名字
  )
  # 创建一个 MySQL 游标
  mycursor = mydb.cursor()
  sql = "INSERT INTO chepi (年月日, 时间 ,车牌) VALUES (%s, %s, %s)"
  mycursor.executemany(sql, chepai)
  # 提交到数据库执行
  mydb.commit()
  # 打印插入的行数
  print(mycursor.rowcount, "行已插入.")
def click_button3():
    messagebox.showinfo(title='车牌识别', message='放图片')
    path1 = tkinter.filedialog.askopenfilename()
    chepai1 = qidon1(path1)
    riqi,shij=time1()
    chepai = [(riqi, shij,chepai1)]
    shujuku1(chepai)
    print('++++++++++++')
    print(riqi)
    print(shij)
    print(chepai1)
#
# button3 = tk.Button(win,image=im,command=click_button3).pack()
# # 启动窗口
# win.mainloop()