#!/urs/bin/python
# -*- coding:utf-8 -*-

import pymysql
conn = pymysql.connect(
    host='192.168.79.128',
    port=3306,
    user='root',
    passwd='root',
    db='test',
    charset='utf8'
)
cursor = conn.cursor()

sql_insert = "insert into user(userid, username) value(1, 'name1')"
sql_update = "update user set username='james' where userid=9"
sql_delete = "delete from user where userid<3"
try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

cursor.close()
conn.close()