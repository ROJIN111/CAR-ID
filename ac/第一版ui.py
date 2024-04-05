'''''
ui版待优化
'''''

from tkinter import messagebox
import tkinter.filedialog
# 导入cv相关库
import cv2 as cv2
from PIL import ImageFont
# 导入依赖包
import hyperlpr3 as lpr3
import tkinter as tk
import tkinter.filedialog
import mysql.connector
from datetime import datetime
from PIL import Image, ImageTk
import wee

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


def shujuku1(chepai):
  mydb = mysql.connector.connect(
    host="192.168.1.105", # 主机地址，端口默认 port="3306"
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
        image = wee.draw_plate_on_image(image, box, text, font=font_ch)
    # 显示检测结果
    # cv2.imshow("w", image)
    cv2.waitKey(0)


    lb2 = tk.Label(win, text='识别结果：', width=10, height=1, fg='green', font=16, justify='left', padx=10)
    lb2.config(bg="#E9C2A6")
    lb2.place(x=50, y=150)

    e = result
    lb2_2 = tk.Label(win, text=e, width=10, height=1, fg='green', font=200, justify='left', padx=10)
    lb2_2.config(bg="black")
    lb2_2.place(x=200, y=150)

    lb2_3 = tk.Label(win, text='车牌原图：', width=10, height=1, fg='green', font=200, justify='left', padx=10)
    lb2_3.config(bg="#E9C2A6")
    lb2_3.place(x=50, y=250)

    return result


def resize(w, h, w_box, h_box, pil_image):
  '''
  resize a pil_image object so it will fit into
  a box of size w_box times h_box, but retain aspect ratio
  对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
  '''
  f1 = 1.0*w_box/w # 1.0 forces float division in Python2
  f2 = 1.0*h_box/h
  factor = min([f1, f2])
  #print(f1, f2, factor) # test
  # use best down-sizing filter
  width = int(w*factor)
  height = int(h*factor)
  return pil_image.resize((width, height), Image.LANCZOS)

def aaa(path):
    pil_image = Image.open(path)
    w_box = 480
    h_box = 270
    w, h = pil_image.size

    pil_image_resized = resize(w, h, w_box, h_box, pil_image)

    tk_image = ImageTk.PhotoImage(pil_image_resized)
    return tk_image

def click_button3():
    messagebox.showinfo(title='车牌识别', message='放图片')
    path1 = tkinter.filedialog.askopenfilename()

    a = path1
    image1 = aaa(a)
    lb3 = tk.Label(win, image=image1,width=480, height=270)
    lb3.place(x=200, y=250)
    lb3.image = image1


    chepai1 = qidon1(path1)
    riqi,shij=time1()
    chepai = [(riqi, shij,chepai1)]
    shujuku1(chepai)

    print('++++++++++++')
    print(riqi)
    print(shij)
    # print(chepai1)
    # return chepai1


# 注册窗口
win = tk.Tk()
win.geometry('700x600')
win.title('车牌识别')

s = tk.Canvas(win,width=2000,height=1000)
d = Image.open(r'D:\pythonProject\STUDY\bishe\ac\4.gif')
p = ImageTk.PhotoImage(d)
s.create_image(300, 300, image = p)
s.pack()

lb1 = tk.Label(win, text='放入车牌图片----->>>>',width=25,height=1,fg='green',font=200,justify='left',padx=10)
lb1.config(bg="#E9C2A6")
lb1.place(x=50, y=60)

image = Image.open(r"D:\pythonProject\STUDY\bishe\ac\11.gif")
photo = ImageTk.PhotoImage(image)
but = tk.Button(win,image=photo,width=150,height=160,fg='red',command=click_button3)
but.place(x=500, y=25)

win.mainloop()