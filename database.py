#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn
@CONTACT:zhaojing17@foxmail.com
@SOFTWERE:PyCharm
@FILE:testfile.py
@TIME:2019/1/12 10:44
@DES:
'''



import pymysql
import types

db = pymysql.connect("192.168.0.77", "root", "123456", "hebook")

cursor = db.cursor()

# cursor.execute("drop table if exists a_contactor_like")
# sql="""CREATE TABLE IF NOT EXISTS `user` (
#       `id` int(11) NOT NULL AUTO_INCREMENT,
#       `name` varchar(255) NOT NULL,
#       `age` int(11) NOT NULL,
#       PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=0"""

# cursor.execute(sql)


def test_database():
    #user插入数据
    sql="""INSERT INTO `a_contactor_like` (`ContactorID`, `LikeID`) VALUES 
    (00022, 1), 
    (00011, 2);"""

    try:
        #执行SQL语句
        cursor.execute(sql)
        #提交到数据库执行
        db.commit()
    except:
        #如果发生错误则回滚
        db.rollback()

# #删除
# id = 2
# sql = "delete from user where id='%s'"%(id)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#
# #查询
# cursor.execute("select * from user")
#
# results = cursor.fetchall()
# for row in results:
#     name = row[0]
#     age = row[1]
#     print("name=%s, age=%s"%(name, age))