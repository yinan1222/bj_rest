#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import MySQLdb.cursors
#global bj_rest
#bj_rest = 1
#filename = str(bj_rest)+'.txt'

# 打开数据库连接
db = MySQLdb.connect("localhost","root","password","bj_rest" )

# 使用cursor()方法获取操作游标
#查询smartgoods的数量
cursor = db.cursor()
sql = "SELECT COUNT(*) from smart_goods"
sql2 = "SELECT COUNT(*) from smart_store_info"
# 使用execute方法执行SQL语句
cursor.execute(sql)
data = cursor.fetchone()
print "Amounts of Smart_goods number before change is %s " % data
cursor.execute(sql2)
# 使用 fetchone() 方法获取一条数据库。
# data = cursor.fetchone()
print "Amounts of Smart_store_info number before change is %s " % data
try:


    sql_index= "create index index_smart_goods on smart_goods(store_id);"
    cursor.execute(sql_index)
    sql_index2= "create index index_smart_store on smart_store(id);"
    cursor.execute(sql_index)
    ##建立索引
    sql_delete= "DELETE smart_goods FROM smart_goods LEFT JOIN smart_store on smart_goods.store_id = smart_store.id WHERE smart_store.id IS NULL"
    #删除语句
    cursor.execute(sql_delete)
    db.commit()
    sql = "SELECT COUNT(*) from smart_goods"
    sql2 = "SELECT COUNT(*) from smart_store_info"
    cursor.execute(sql)
    data = cursor.fetchone()
    print "Amounts of smart_goods number after change is %s " % data
    cursor.execute(sql2)
    data = cursor.fetchone()
    print "Smart_store_info number before change is %s " % data
except:
    print "update failed"
#查询smartgoods的数量2
db.close()

#执行以上脚本输出结果如下：

#Database version : 5.0.45

# coding:UTF-8


#conn = MySQLdb.Connect(
#                        host = '127.0.0.1',
#                        port = 3306,
#                        user = 'root',
#                        passwd = '',
#                        db = 'bj_rest'
#                        )
#
#cursor = conn.cursor()
#
#sql = "select * from smart_goods"
#cursor.execute(sql)
