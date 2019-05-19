
import pymysql
import types

# db = pymysql.connect(host="127.0.0.1", 
#     port=3306,
#     user="root", 
#     password="123456", 
#     database="python")

db = pymysql.connect(host="127.0.0.1", 
    port=3306,
    user="root", 
    password="123456", 
    database="python")

cursor = db.cursor()

cursor.execute("drop table if exists user")
sql="""CREATE TABLE IF NOT EXISTS `user` ( 
      `id` int(11) NOT NULL AUTO_INCREMENT, 
      `name` varchar(255) NOT NULL, 
      `age` int(11) NOT NULL, 
      PRIMARY KEY (`id`) 
    ) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=0"""


cursor.execute(sql)

# 插入语句
def INSERT(db_connect, table_name, argv_list, value_list):
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
    table_string = "%s"%table_name

    # 构造属性
    argc_string = "`%s`"%argv_list[0]
    for ii in range(1,len(argv_list)):
        argc_string += ",`%s`"%argv_list[ii]
    argc_string = "(%s)"%argc_string

    # 构造属性值
    value_string = '%s'%value_list[0]
    for ii in range(1,len(value_list)):
        value_string += ', %s'%value_list[ii]
    value_string = "(%s)"%value_string
    
    # 定义SQL语句
    insert_sql = "INSERT INTO "+table_string+ argc_string + " VALUES " + value_string
    print(insert_sql)

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

def MODIFIED(db_connect, table_name, id, argv_list, value_list):
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
        插入成功: 返回 True
        插入失败: 返回 False
    """
    key_value_string = "%s=%s"%(argv_list[0], value_list[0])

    for ii in range(1, len(argv_list)):
        key_value_string += ", %s=%s"%(argv_list[ii], value_list[ii])

    update_sql = "UPDATE %s SET %s WHERE %s"%(table_name, key_value_string, id)

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

def DELETE(db_connect, table_name, id):
    """
    函数功能： 在特定数据库删除数据
    参数：
        # 参数名   | 参数类型                       |       解释
        db_connect: pymysql.connect()方法的返回值       数据库链接
        table_name: 字符串                              表的名称
        id        : int                                属性      
    返回值
        插入成功: 返回 True
        插入失败: 返回 False
    """
    delete_sql = "delete from %s where id='%s'"%(table_name, id)
    
    cursor = db_connect.cursor()
    try:
        cursor.execute(delete_sql)
        db_connect.commit()
        return True
    except:
        db_connect.rollback()
        return False


INSERT(db, 'user', ['name','age'], ['test7',7])

# MODIFIED(db, )

#user插入数据
sql="""INSERT INTO user (`name`, `age`) VALUES 
('test1', 1), 
('test2', 2), 
('test3', 3), 
('test4', 4), 
('test5', 5), 
('test6', 6);"""  

try:
    #执行SQL语句
    cursor.execute(sql)
    # cursor.execute(insert_sql)
    #提交到数据库执行
    db.commit()
except:
    #如果发生错误则回滚
    db.rollback()

#删除
DELETE(db, 'user', 2)

#修改
id = 3
sql = """update user set name='test37', age=31 WHERE id=%s;"""%(id)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

#查询
cursor.execute("select * from user")

results = cursor.fetchall()
for row in results:
    name = row[1]
    age = row[2]
    print("name=%s, age=%s"%(name, age))