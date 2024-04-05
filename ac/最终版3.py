from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
# 导入cv相关库
import cv2 as cv2
# 导入依赖包
import hyperlpr3 as lpr3
import tkinter as tk
import tkinter.filedialog
import mysql.connector
from datetime import datetime
from PIL import Image, ImageTk
import csv
from tkinter import ttk

##################################################添加错误检索,不会因为图片错误导致异常。####################################
def qidon1(path1):
    # 中文字体加载
    print('路径', path1)
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
        lb2_2 = tk.Label(root, text=e, width=20, height=1, fg='green', font=200, justify='left', padx=10)
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
        pass  # pass 表示什么也不做，直接跳过这个异常
    except Exception as baocuo1:
        print('111')
        result = '路径异常!'
        e = result
        lb2_2 = tk.Label(root, text=e, width=20, height=1, fg='red', font=200, anchor='center', padx=10)
        lb2_2.config(bg="black")
        lb2_2.place(x=250, y=150)
        messagebox.showinfo(title='可能是中文路径导致的异常', message=baocuo1)
        pass  # pass 表示什么也不做，直接跳过这个异常

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
  width = int(w*factor)
  height = int(h*factor)
  return pil_image.resize((width, height), Image.LANCZOS)

def aaa(path):

    try:
        pil_image = Image.open(path)
        w_box = 480
        h_box = 270
        w, h = pil_image.size
        pil_image_resized = resize(w, h, w_box, h_box, pil_image)
        tk_image = ImageTk.PhotoImage(pil_image_resized)

    except Exception as baocuo1:
        print('3错误')
        messagebox.showinfo(title='输入异常:仅支持图片格式', message=baocuo1)
        lb2_2 = tk.Label(root, text='输入文件异常', width=20, height=1, fg='red', font=200, anchor='center', padx=10)
        lb2_2.config(bg="black")
        lb2_2.place(x=250, y=150)

        a = (r'4.gif')

        image1 = aaa(a)
        lb3 = tk.Label(root, image=image1, width=480, height=270)
        lb3.place(x=200, y=250)
        lb3.image = image1
        pass  # pass 表示什么也不做，直接跳过这个异常

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
            database=d, # 数据库名字
            auth_plugin = 'mysql_native_password'  # 防止mysql版本太高报错的解决办法
        )
        return mydb
    e = var4.get()
    def youbiao(chepai):
        # 创建一个 MySQL 游标
        try:
            a = callback()
            mycursor = a.cursor()
            sql = 'INSERT INTO'+' '+e+' ' +'(年月日, 时间 ,车牌) VALUES (%s, %s, %s)'
            mycursor.executemany(sql, chepai)
            # # 提交到数据库执行
            a.commit()
            # 打印插入的行数
            print(mycursor.rowcount, "行已插入.")
            messagebox.showinfo(title='数据库', message='发送成功')
        except IndexError:
            # 处理索引超出范围的情况，或者可以不做任何处理，继续执行其他操作
            print('处理索引超出范围的情况，或者可以不做任何处理，继续执行其他操作')
            messagebox.showinfo(title='数据库:索引超出范围的情况', message='理论上来说没有触发这个报错的可能性  @.@')
            pass  # pass 表示什么也不做，直接跳过这个异常

        except Exception as baocuo:
            print(baocuo)
            messagebox.showinfo(title='数据库', message=baocuo)
            pass  # pass 表示什么也不做，直接跳过这个异常


    def qidong():
        a1 = var.get()  # 通过变量get方法来获取文本
        if a1 != 'IP地址':
            youbiao(chepai)
        else :
            print('数据不上传1111')
            messagebox.showinfo(title='上传模式:本地模式', message='本地保存成功')
        #输入到本地记录的内容
        riqi1, shij2 = time1()
        chepaibendi = [{'日期': riqi1, '时间': shij2, '车牌': chepai1}]
        listbendi = chepaibendi
    #########################################################################################
        file_path = 'text.csv'
            # 打开文件以追加模式写入
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['日期', '时间', '车牌'])
            # 如果文件为空，先写入表头
            if file.tell() == 0:
                writer.writeheader()
            # 写入新数据
            for data in listbendi:
                writer.writerow(data)
            print("数据已成功追加到文件中！")
    ############################################################################################
    messagebox.showinfo(title='车牌识别', message='放图片')
    path1 = tkinter.filedialog.askopenfilename()

    a = (path1)

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
        root.mainloop()

def ad():

    window = tk.Tk()
    window.title('历史记录')

    table = ttk.Treeview(window)
    table["columns"] = ("col1", "col2", "col3")
    table.heading("col1", text="日期")
    table.heading("col2", text="时间")
    table.heading("col3", text="车牌")

    with open("text.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            table.insert("", tk.END, values=row)

    table.pack()
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
but_set = Button(root, text="历史记录", command=ad)  # command参数来调用函数
but_set.place(x=410, y=50)
root.mainloop()