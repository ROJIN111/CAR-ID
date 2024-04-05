import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Scrollbar, Frame
import pandas as pd
from tkinter.ttk import Treeview

def ad():
    root = tk.Tk()
    root.geometry('800x600')
    root.resizable(0, 0)  # 防止用户调整尺寸
    root.title('车牌识别1')

    sb = Scrollbar(root)
    sb.pack(side=RIGHT, fill=Y)

    lb = Listbox(root, width=200,height=500, yscrollcommand=sb.set)  # 设置yscrollcommand选项为Scrollbar的set()方法

    b = open('a.txt',mode = 'r',encoding='utf-8')
    for i in b:
        lb.insert(END,str(i))


    lb.pack()

    sb.config(command=lb.yview)  # 设置comand参数为组件的yview()方法

    root.mainloop()

    # frame = Frame(root)
    #
    # frame.place(x=10, y=10, width=500, height=200)
    #
    # scrollBar = tk.Scrollbar(frame)
    #
    # scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
    #
    # tree = Treeview(frame,
    #
    #                 columns=('c1', 'c2', 'c3'),
    #
    #                 show="headings",
    #
    #                 yscrollcommand=scrollBar.set)
    #
    # tree.column('c1', width=150, anchor='center')
    #
    # tree.column('c2', width=150, anchor='center')
    #
    # tree.column('c3', width=150, anchor='center')
    #
    #
    # # 设置每列表头标题文本
    #
    # tree.heading('c1', text='姓名')
    #
    # tree.heading('c2', text='性别')
    #
    # tree.heading('c3', text='年龄')
    #
    # tree.pack(side=tk.LEFT, fill=tk.Y)
    #
    # # Treeview组件与垂直滚动条结合
    #
    # scrollBar.config(command=tree.yview)
    #
    # # 定义并绑定Treeview组件的鼠标单击事件
    #
    # def treeviewClick(event):
    #     pass
    #
    # tree.bind('<Button-1>', treeviewClick)
    #
    # # 插入演示数据
    # ww = pd.read_csv("text.csv")
    # for i in ww:
    #     tree.insert('', i, values=[str(i)] * 6)
    #
    # #运行程序，启动事件循环







root = tk.Tk()
root.geometry('700x600')
root.resizable(0,0) #防止用户调整尺寸
root.title('车牌识别')

but_set = Button(root, text="历史记录", command=ad)  # command参数来调用函数
but_set.place(x=410, y=150)





root.mainloop()




# # 原始数据显示
# Label(root, text="初始样本数据").grid(row=0, sticky=W)
# listBox = ttk.Treeview(page, height=15, columns=self.header, show='headings')  # 创建表格
# VScroll = ttk.Scrollbar(page, orient='vertical', command=self.listBox.yview)  # 创建滚动条
# listBox.configure(yscrollcommand=VScroll.set)  # 滚动条与表格控件关联
# VScroll.grid(row=1, column=5, sticky=)  # 滚动条放置位置
# for col in self.header:  # 显示表头以及设置列宽
#     self.listBox.column(col, width=100, anchor='center')
#     self.listBox.heading(col, text=col)
# self.listBox.grid(row=1, column=0, columnspan=4)  # 表格放置位置