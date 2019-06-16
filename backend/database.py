#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql
import types
import time
from config import *

#插入语句
def INSERT(table_name, argv_list, value_list):
    """
    函数功能： 往特定数据库增加数据
    参数：
        # 参数名   | 参数类型                       |       解释
        db_connect: pymysql.connect()方法的返回值       数据库链接
        table_name: 字符串                              表的名称
        argv_list : 字符串列表                          属性                       
        value_list: 字符串列表                          属性对应值
    返回值
        插入成功: 返回 True
        插入失败: 返回 False
    """
    # 构造表
    table_string = " %s "%table_name

    # 构造属性
    argc_string = "`%s`"%argv_list[0]
    for ii in range(1,len(argv_list)):
        argc_string += ",`%s`"%argv_list[ii]
    argc_string += ", `CreateTime`, `UpdateTime`"
    argc_string = "(%s)"%argc_string

    # 构造时间
    t = time.strftime('%Y-%m-%d %H:%M:%S')

    # 构造属性值
    value_string = ""
    for ii in range(0,len(value_list)-1):
        if type(value_list[ii]) == str:
            value_string += "'%s', "%value_list[ii]
        else:
            value_string += "%s, "%value_list[ii]
    if type(value_list[len(value_list)-1]) == str:
        value_string += "'%s'"%value_list[len(value_list)-1]
    else:
        value_string += "%s"%value_list[len(value_list)-1]
    value_string += ", '%s', '%s'"%(t,t)

    value_string = "(%s)"%value_string
    
    # 定义SQL语句
    insert_sql = "INSERT INTO "+table_string + argc_string + " VALUES " + value_string
    
    db_connect = pymysql.connect(host=config["server_ip"], 
    port=3306,
    user="root", 
    password="123456", 
    database=config["database"])

    cursor = db_connect.cursor()
    try:
        #执行SQL语句
        cursor.execute(insert_sql)
        #提交到数据库执行
        db_connect.commit()
        return True
    except:
        #如果发生错误则回滚
        db_connect.rollback()
        return False

def MODIFIED(table_name, id, argv_list, value_list):
    """
    函数功能： 在特定数据库修改数据
    参数：
        # 参数名   | 参数类型                       |       解释
        db_connect: pymysql.connect()方法的返回值       数据库链接
        table_name: 字符串                              表的名称
        id        : int                                主属性
        argv_list : 字符串列表                          属性                          
        value_list: 字符串列表                          属性对应值
    返回值
        修改成功: 返回 True
        修改失败: 返回 False
    """
    key_value_string = ""

    for ii in range(0, len(argv_list)-1):
        if type(value_list[ii]) == str:
            key_value_string += "%s='%s', "%(argv_list[ii], value_list[ii])
        else:
            key_value_string += "%s=%s, "%(argv_list[ii], value_list[ii])

    last_index = len(argv_list)-1
    if type(value_list[last_index]) == str:
        key_value_string += "%s='%s'"%(argv_list[last_index], value_list[last_index])
    else:
        key_value_string += "%s=%s"%(argv_list[last_index], value_list[last_index])

    # 构造时间
    t = time.strftime('%Y-%m-%d %H:%M:%S')
    key_value_string += ",%s='%s'"%("`UpdateTime`", t)

    # 定义更新语句
    update_sql = "UPDATE %s SET %s WHERE %s=%s"%(table_name, key_value_string, table_ID[table_name], id)
    print(update_sql)
    db_connect = pymysql.connect(host=config["server_ip"], 
    port=3306,
    user="root", 
    password="123456", 
    database=config["database"])

    cursor = db_connect.cursor()
    try:
        #执行SQL语句
        cursor.execute(update_sql)
        #提交到数据库执行
        db_connect.commit()
        return True
    except:
        #如果发生错误则回滚
        db_connect.rollback()
        return False

def DELETE(table_name, id):
    """
    函数功能： 在特定数据库删除数据
    参数：
        # 参数名   | 参数类型                       |       解释
        db_connect: pymysql.connect()方法的返回值       数据库链接
        table_name: 字符串                              表的名称
        id        : int                                属性      
    返回值
        删除成功: 返回 True
        删除失败: 返回 False
    """
    delete_sql = "delete from %s where id='%s'"%(table_name, id)
    
    db_connect = pymysql.connect(host=config["server_ip"], 
    port=3306,
    user="root", 
    password="123456", 
    database=config["database"])

    cursor = db_connect.cursor()
    try:
        cursor.execute(delete_sql)
        db_connect.commit()
        return True
    except:
        db_connect.rollback()
        return False

def FIND(table_name, field, conditions):
    """
    函数功能： 在特定数据库寻找满足条件的数据
    参数：
        # 参数名   | 参数类型                       |       解释
        db_connect: pymysql.connect()方法的返回值       数据库链接
        table_name: 字符串                              表的名称
        field     : 列表                                需要查询的字段,全选填‘*’
        conditions: 列表                                条件      
    返回值
        查找成功: 返回 True
        查找失败: 返回 False
    """

    field_string = ''
    for ii in range(0,len(field)-1):
        field_string += "%s,"%field[ii]
    field_string += "%s"%field[len(field)-1]

    condition_string = ""
    for ii in range(0,len(conditions)-1):
        condition_string += "%s AND "%conditions[ii]
    condition_string += "%s"%field[len(conditions)-1]

    select_sql = "select from %s where id='%s'"%(table_name, id)
    
    db_connect = pymysql.connect(host=config["server_ip"], 
    port=3306,
    user="root", 
    password="123456", 
    database=config["database"])

    cursor = db_connect.cursor()
    try:
        cursor.execute(select_sql)
        db_connect.commit()
        return True
    except:
        db_connect.rollback()
        return False

def get_current_id(table_name):
    db = pymysql.connect(host=config["server_ip"], 
        port=3306,
        user="root", 
        password="123456", 
        database=config["database"])

    cursor = db.cursor()
    sql="SELECT COUNT(*) FROM %s;"%table_name

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()

    return results[0][0]+1


if __name__ == "__main__":
    db = pymysql.connect(host=config["server_ip"], 
        port=3306,
        user="root", 
        password="123456", 
        database=config["database"])

    cursor = db.cursor()

    # cursor.execute("drop table if exists user")
    # sql="""CREATE TABLE IF NOT EXISTS `user` ( 
    #     `id` int(11) NOT NULL AUTO_INCREMENT, 
    #     `name` varchar(255) NOT NULL, 
    #     `age` int(11) NOT NULL,
    #     `bin_da` binary(255),
    #     PRIMARY KEY (`id`) 
    #     ) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=0"""


    # cursor.execute(sql)

    #user插入数据
    sql="""INSERT INTO user (`name`, `age`) VALUES 
    ('test1', 1), 
    ('test2', 2), 
    ('test3', 3), 
    ('test4', 4), 
    ('test5', 5), 
    ('test6', 6);"""  
    t = time.strftime('%Y-%m-%d %H:%M:%S')
    print(t)
    # INSERT('t_contactor',['ContactorID','Name','UserID'],[2426,'Kitten',32532])
    MODIFIED('t_contactor', 2426, ['gender','birthdate'], [2,'1994-08-25'])

    # # 插入
    # INSERT('user', ['name','age'], ['test7',7])
    # # INSERT(db, 'user', ['name','age', 'bin_da'], ['test8', 8, '82364873628765837658736587'])
    # INSERT('user', ['name','age', 'bin_da'], ['test8', 8, 2342])

    # MODIFIED('user', 5, ['name'], ['Lony'])

    # # 删除
    # DELETE('user', 2)

    # # 修改
    # id = 3
    # sql = """update user set name='test37', age=31 WHERE id=%s;"""%(id)

    # try:
    #     cursor.execute(sql)
    #     db.commit()
    # except:
    #     db.rollback()

    # #查询
    # cursor.execute("select * from user")
    print(get_current_id("t_contactor"))
    # results = cursor.fetchall()
    # # 关于存储一年内联系天数的方法，存储binary信息，在python后台中使用int.from_bytes将其转换
    # # 成int类型数据进行处理
    # for row in results:
    #     name = row[1]
    #     age = row[2]
    #     # print(type(name), type(age), type(row[3]))
    #     bi = row[3]
    #     # if bi is not None:
    #     #     print(type(row[3]))
    #     #     print(bi)
    #     #     bi = int(bi, 16)
    #     print("name=%s, age=%s, data=%s"%(name, age, bi))