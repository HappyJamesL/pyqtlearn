#!/urs/bin/python
# -*- coding:utf-8 -*-

import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
conn = MySQLdb.Connect(
    host='192.168.79.128',
    port=3306,
    user='root',
    passwd='root',
    db='test',
    charset='utf8'
)
cursor = conn.cursor()
sql = "select * from user "
cursor.execute(sql)

print(cursor.rowcount)
# rs = cursor.fetchone()
# print(rs)
#
# rs = cursor.fetchmany(1)
# print(rs)
# rs = cursor.fetchmany(2)
# print(rs)
rs = cursor.fetchall()

for row in rs:
    print("userid: %s, username:%s" % row)

cursor.close()
conn.close()