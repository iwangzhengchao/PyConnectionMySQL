#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-7 15:43
# @Author  : Z.C.Wang
# @Email   : iwangzhengchao@gmail.com
# @File    : PyConnectionMySQL.py
# @Software: PyCharm Community Edition
"""
Description :
pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(sql, args)     执行一个数据库的查询命令
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
close()         关闭游标对象
"""
import pymysql

# 连接数据库
connection = pymysql.connect(host='localhost', user='root', password='root',
                             db='test', charset='utf8')

if connection.open:
    print('the connection is open...')

# 清空users表
cursor = connection.cursor()
cursor.execute("truncate table users")
connection.commit()

# (1)批量插入
record = []
for i in range(10):
    email = "mail_" + str(i) + "@qq.com"
    password = "xxx_" + str(i)
    record.append((email, password))

try:
    sql = "insert into users (email, password) values (%s, %s)"
    rows = cursor.executemany(sql, record)
    connection.commit()
    print("insert success. affected rows : %d" % rows)
except:
    print("insert ERROR.")
    connection.rollback()

# (2)删除记录
try:
    sql = "delete from users where id=1"
    rows = cursor.execute(sql)
    connection.commit()
    print("delete success. affected rows : %d" % rows)
except:
    print("delete ERROR.")
    connection.rollback()

# (3)修改记录
try:
    sql = "update users set password='yyy' where id=5"
    rows = cursor.execute(sql)
    connection.commit()
    print("update success. affected rows : %d" % rows)
except:
    print("update ERROR.")
    connection.rollback()

# (4)查询记录
try:
    sql = 'select * from users'
    count = cursor.execute(sql)
    print("number of record in users: %d" % count)
    result = cursor.fetchall()
    for row in result:
        print(row)
    connection.commit()
except:
    print("query ERROR.")
    connection.rollback()

# 关闭连接
cursor.close()
connection.close()
print("connection close.")

