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
        print(insert_sql)
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
        print(update_sql)
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
        field     : 列表                                需要查询的字段,全选填 [‘*’]
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
    condition_string += "%s"%conditions[len(conditions)-1]

    select_sql = "select %s from %s WHERE %s"%(field_string, table_name, condition_string)
    
    db_connect = pymysql.connect(host=config["server_ip"], 
    port=3306,
    user="root", 
    password="123456", 
    database=config["database"])

    cursor = db_connect.cursor()
    try:
        cursor.execute(select_sql)
        results = cursor.fetchall()
        return results
    except:
        return False

def FIND_ALL(table_name, field):
    """
    函数功能： 在特定数据库寻找满足条件的数据
    参数：
        # 参数名   | 参数类型                       |       解释
        db_connect: pymysql.connect()方法的返回值       数据库链接
        table_name: 字符串                              表的名称
        field     : 列表                                需要查询的字段,全选填‘*’     
    返回值
        查找成功: 返回 True
        查找失败: 返回 False
    """

    field_string = ''
    for ii in range(0,len(field)-1):
        field_string += "%s,"%field[ii]
    field_string += "%s"%field[len(field)-1]

    select_sql = "select %s from %s"%(field_string, table_name)
    
    db_connect = pymysql.connect(host=config["server_ip"], 
    port=3306,
    user="root", 
    password="123456", 
    database=config["database"])

    cursor = db_connect.cursor()
    try:
        cursor.execute(select_sql)
        results = cursor.fetchall()
        return results
    except:
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

    # 插入
    print(INSERT('t_user',['userID','Name','password','bundlephone'],[1,'Kitten','32532',18570744251]))
    print(INSERT('t_uscocialaccount',['SPcountID','UserID','APP','Account','Authority'],[1,1,3,'haha','nudt']))
    print(INSERT('t_remark',['RemarkID','ContactorID','Content'],[1,2,'Kitten haha']))
    print(INSERT('t_like',['LikeID','CreatorID','LikeName','IsDelete','isCreatorHave'],[1,2,'Kitten',2,1]))
    print(INSERT('t_jobdsc',['JobDscID','DscContent','JobID'],[1,'she is a journalist',2]))
    print(INSERT('t_job',['JobID','ContactorID','UserID'],[1,2,3]))
    print(INSERT('t_interaction',['InteractionID','Level','Touchday'],[1,5,'100010']))
    print(INSERT('t_hate',['HateID','HateName','CreatorID','isCreatorHave'],[1,'potato',3,4]))
    print(INSERT('t_flag',['flagID','FlagName','CreatorID','isCreatorHave'],[1,'potato',3,4]))
    print(INSERT('t_educationbackground',['EduBackID','Degree','School','ContactorID','UserID'],\
        [1,4,'hehehe',4,5]))
    print(INSERT('t_edubackdsc',['EduBackDscID','DscContent','EduBackID'],[1,'we have a world',5]))
    print(INSERT('t_csocialaccount',['SPcountID','APP','Account','ContactorID'],[1,1,'haha',4]))
    print(INSERT('t_contactor',['ContactorID','Name','UserID'],[2426,'Kitten',32532]))
    print(INSERT('a_contactor_like',['ContactorID','LikeID'],[2,4]))
    print(INSERT('a_contactor_hate',['ContactorID','hateID'],[1,2]))
    print(INSERT('a_contactor_flag',['ContactorID','flagID'],[2,8]))

    # 修改
    print(MODIFIED('t_user',1,['gender','birthdate','phonenumber1'], [0,'1994-08-25','18570744251']))
    print(MODIFIED('t_uscocialaccount',1,['UserID','APP','Account','Authority'],[1,3,'zhangbiwei','nudt']))
    print(MODIFIED('t_remark',1,['ContactorID','Content'],[2,'Kitten i like you']))
    print(MODIFIED('t_like',1,['CreatorID','LikeName','IsDelete','isCreatorHave'],[2,'Kitten OK',2,1]))
    print(MODIFIED('t_jobdsc',1,['DscContent','JobID'],['she is a journalist, too',2]))
    print(MODIFIED('t_job',1,['ContactorID','UserID'],[2,3]))
    print(MODIFIED('t_interaction',1,['Level','Touchday'],[5,'10010100100010']))
    print(MODIFIED('t_hate',1,['HateName','CreatorID','isCreatorHave'],['potato',3,4]))
    print(MODIFIED('t_flag',1,['flagID','FlagName','CreatorID','isCreatorHave'],[1,'tomato',3,4]))
    print(MODIFIED('t_educationbackground',1,['Degree','School','ContactorID','UserID'],\
        [4,'hehehe',4,5]))
    print(MODIFIED('t_edubackdsc',1,['DscContent','EduBackID'],['we have a world',5]))
    print(MODIFIED('t_csocialaccount',1,['APP','Account','ContactorID'],[1,'haha',4]))
    print(MODIFIED('t_contactor', 2426, ['gender','birthdate'], [2,'1994-08-25']))

    # 查询
    print(FIND('t_user',['*'],['%s=%d'%(table_ID['t_user'],1)]))
    print(FIND('t_uscocialaccount',['*'],['%s=%d'%(table_ID['t_uscocialaccount'],1)]))
    print(FIND('t_remark',['*'],['%s=%d'%(table_ID['t_remark'],1)]))
    print(FIND('t_like',['*'],['%s=%d'%(table_ID['t_like'],1)]))
    print(FIND('t_jobdsc',['*'],['%s=%d'%(table_ID['t_jobdsc'],1)]))
    print(FIND('t_job',['*'],['%s=%d'%(table_ID['t_job'],1)]))
    print(FIND('t_interaction',['*'],['%s=%d'%(table_ID['t_interaction'],1)]))
    print(FIND('t_hate',['*'],['%s=%d'%(table_ID['t_hate'],1)]))
    print(FIND('t_flag',['*'],['%s=%d'%(table_ID['t_flag'],1)]))
    print(FIND('t_educationbackground',['*'],['%s=%d'%(table_ID['t_educationbackground'],1)]))
    print(FIND('t_edubackdsc',['*'],['%s=%d'%(table_ID['t_edubackdsc'],1)]))
    print(FIND('t_csocialaccount',['*'],['%s=%d'%(table_ID['t_csocialaccount'],1)]))
    print(FIND('t_contactor',['*'],['%s=%d'%(table_ID['t_contactor'],2426)]))

    
    # # 关于存储一年内联系天数的方法，存储binary信息，在python后台中使用int.from_bytes将其转换
    # # 成int类型数据进行处理