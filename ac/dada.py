import pymssql
import pandas as pd
import mysql.connector

# e = []
# c = set()

mydb = mysql.connector.connect(
    host="192.168.1.101",  # 主机地址，端口默认 port="3306"
    user="1111",  # 用户名
    password="123456",  # 用户密码
    database="runoob"  # 数据库名字
)
mycursor = mydb.cursor()
sql = "SELECT DISTINCT 年月日, 时间, 车牌 FROM chepi;"
df = pd.read_sql(sql, mydb)

df.to_(path_or_buf="text.csv", float_format=8, header=False, index=False)
# sql = "select 年月日, 时间, 车牌 from chepi"
mycursor.execute(sql)
print(df)
# alldata = mycursor.fetchall()
# for rec in alldata:
#     e.append(rec[0])
#     e.append(rec[1])
#     e.append(rec[2])
#     a = str(e)
#     c.add(a)
# print(c)
w = open("text.csv",'r').readlines
w = str(w)
print(w)









































# def conn():
#     # 后续如果出现乱码 请调整此处的 charset 换成utf-8
#     connect = pymssql.connect('192.168.1.102', '1111', '123456', 'runoob', charset='utf-8 ')
#     if connect:
#         print("连接成功")
#     return connect
# # 第一种方式
# for i in range(len(df)):
#     id = df['ID'].values[i]
#     name = df['NAME'].values[i]
#     height = df['HEIGHT'].values[i]
#     weight = df['WEIGHT'].values[i]
#
#     strsql = f"INSERT INTO testinfo SELECT {id},'{name}',{height},{weight}"
#     print(strsql)
#
# print('1 ↑\n\n2 ↓')
#
# # 第二种方式
# # 通过 iloc 寻找固定行列值
# for i in range(len(df)):
#     id = df.iloc[i][0]
#     name = df.iloc[i][1]
#     height = df.iloc[i][2]
#     weight = df.iloc[i][3]
#
#     strsql = f"INSERT INTO testinfo SELECT {id},'{name}',{height},{weight}"
#     print(strsql)
#











#
# conn = pymssql.connect(host="192.168.1.102", user="1111", password="123456", database="runoob", charset='utf8')
# # 创建一个 MySQL 游标
# # mycursor = mydb.cursor()
# # sql = "INSERT INTO chepi (年月日, 时间 ,车牌) VALUES (%s, %s, %s)"
# # mycursor.executemany(sql, chepai)
# # # 提交到数据库执行
# # mydb.commit()
# # # 打印插入的行数
# # print(mycursor.rowcount, "行已插入.")
# sql = "SELECT DISTINCT 年月日, 时间, 车牌 FROM chepi;"
# df = pd.read_sql(sql, conn)
# df.to_csv(path_or_buf="text.csv", float_format=8, header=False, index=False)
#
# # conn = pymssql.connect(host="192.168.1.102", user="1111", password="123456", database="runoob", charset='utf8')
# # sql = "select 年月日, 时间, 车牌  from chepi;"
# # df = pd.read_sql(sql,conn).readlines
# # df.to_csv(path_or_buf="./data/test.csv", float_format=8, header=False, index=False)