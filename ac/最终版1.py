'''''
加了错误检索功能
'''''
from tkinter import StringVar
from tkinter import *
import tkinter as tk
from tkinter import *
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
    try:
        results = catcher(image)
        print(results)
        result = results[0][0]
        print(result)
        e = result
        lb2_2 = tk.Label(root, text=e, width=10, height=1, fg='green', font=200, justify='left', padx=10)
        lb2_2.config(bg="black")
        lb2_2.place(x=250, y=150)

    except IndexError:
        # 处理索引超出范围的情况，或者可以不做任何处理，继续执行其他操作
        result='图片错误,请核实图片!'
        e = result
        lb2_2 = tk.Label(root, text=e, width=20, height=1, fg='red', font=200, anchor='center', padx=10)
        lb2_2.config(bg="black")
        lb2_2.place(x=250, y=150)
        print('处理索引超出范围的情况，或者可以不做任何处理，继续执行其他操作')
    # data = [['苏FM30Q1', 0.9984631, 0, [269, 177, 524, 262]]]
    # result = data[0][0]
    # print(result)  # 这将打印出 '苏FM30Q1'
    # for code, confidence, type_idx, box in results:
    #     # 解析数据并绘制
    #     text = f"{code} - {confidence:.2f}"
    #     image = wee.draw_plate_on_image(image, box, text, font=font_ch)
    # # 显示检测结果
    # # cv2.imshow("w", image)
    # cv2.waitKey(0)


    # lb2 = tk.Label(root, text='识别结果：', width=10, height=1, fg='green', font=16, justify='left', padx=10)
    # lb2.config(bg="#E9C2A6")
    # lb2.place(x=50, y=150)



    # lb2_3 = tk.Label(root, text='车牌原图：', width=10, height=1, fg='green', font=200, justify='left', padx=10)
    # lb2_3.config(bg="#E9C2A6")
    # lb2_3.place(x=50, y=250)

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


def ff():

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
        return current_date, current_time





    def callback():
        a = var.get()  # 通过变量get方法来获取文本

        b = var1.get()  # 通过变量get方法来获取文本

        c = var2.get()  # 通过变量get方法来获取文本

        d = var3.get()  # 通过变量get方法来获取文本


        mydb = mysql.connector.connect(
            host=a,  # 主机地址，端口默认 port="3306"
            user=b,  # 用户名
            password=c,  # 用户密码
            database=d  # 数据库名字
        )
        return mydb
    e = var4.get()
    def youbiao(chepai):
        # 创建一个 MySQL 游标

        a = callback()
        mycursor = a.cursor()
        sql = 'INSERT INTO'+' '+e+' '+'(年月日, 时间 ,车牌)VALUES (%s, %s, %s)'
        mycursor.executemany(sql, chepai)
        # 提交到数据库执行
        a.commit()
        # 打印插入的行数
        print(mycursor.rowcount, "行已插入.")

        messagebox.showinfo(title='数据库', message='数据已上传')

    def qidong():
        youbiao(chepai)
        print('数据已上传')

    messagebox.showinfo(title='车牌识别', message='放图片')
    path1 = tkinter.filedialog.askopenfilename()

    a = path1


    image1 = aaa(a)
    lb3 = tk.Label(root, image=image1, width=480, height=270)
    lb3.place(x=200, y=250)
    lb3.image = image1

    chepai1 = qidon1(path1)
    riqi, shij = time1()
    chepai = [(riqi, shij, chepai1)]
    if chepai1 != '图片错误':

        but = Button(root,text = '上传',command=qidong)
        but.place(x=50, y=525)
        but.config(bg="#E9C2A6")
        # but_set = Button(root, text="获 取", command=qidong)  # command参数来调用函数
        # but_set.pack(x=50,y=400)
        root.mainloop()



root = tk.Tk()
root.geometry('700x600')
root.resizable(0,0) #防止用户调整尺寸
root.title('车牌识别')


s = tk.Canvas(root, width=2000, height=1000)
d = Image.open(r'4.gif')
p = ImageTk.PhotoImage(d)
s.create_image(300, 300, image=p)
s.pack()

var = StringVar()  # 建立变量var为字符串变量
var.set('IP地址')  # 设置变量

var1 = StringVar()  # 建立变量var为字符串变量
var1.set('MySql用户')  # 设置变量

var2 = StringVar()  # 建立变量var为字符串变量
var2.set('密码88888')  # 设置变量

var3 = StringVar()  # 建立变量var为字符串变量
var3.set('数据库名')  # 设置变量

var4 = StringVar()  # 建立变量var为字符串变量
var4.set('数据库-表名')  # 设置变量

en1 = Entry(root, textvariable=var, width=20).place(x=50, y=400)  # 将变量与文本绑定在一起

en2 = Entry(root, textvariable=var1, width=20).place(x=50, y=425)  # 将变量与文本绑定在一起

en3 = Entry(root, textvariable=var2, width=20,show="*").place(x=50, y=450) # 将变量与文本绑定在一起

en4 = Entry(root, textvariable=var3, width=20).place(x=50, y=475)# 将变量与文本绑定在一起

en5 =  Entry(root, textvariable=var4, width=20).place(x=50, y=500)# 将变量与文本绑定在一起

lb1 = tk.Label(root, text='放入车牌图片----->>>>', width=25, height=1, fg='green', font=200, justify='left', padx=10)
lb1.config(bg="#E9C2A6")
lb1.place(x=50, y=60)

lb2 = tk.Label(root, text='识别结果：', width=10, height=1, fg='green', font=16, justify='left', padx=10)
lb2.config(bg="#E9C2A6")
lb2.place(x=50, y=150)

lb2_3 = tk.Label(root, text='车牌原图：', width=10, height=1, fg='green', font=200, justify='left', padx=10)
lb2_3.config(bg="#E9C2A6")
lb2_3.place(x=50, y=250)

lb2 = tk.Label(root, text='主机地址', width=10,  fg='green', font=5, justify='left', padx=10)
lb2.config(bg="#E9C2A6")
lb2.place(x=50, y=365)

image = Image.open(r"11.gif")
photo = ImageTk.PhotoImage(image)
but = tk.Button(root, image=photo, width=150, height=160, fg='red', command=ff)
but.place(x=500, y=30)
# but_set = Button(root, text="获 取", command=ff)  # command参数来调用函数
# but_set.pack(pady=10)

root.mainloop()