#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:User.py
@TIME:2019/5/15 22:15
@DES:
'''
from support import *
import database as db

class User():
    def __init__(self,name,password,account,config):
        self.UserID = db.get_current_id('user')
        self.Name = name
        self.Password = password
        self.Account = account
        if not db.INSERT('user',['User_ID','Name','Password','account'],[self.UserID,self.Name,self.Password,self.Account]):
            print "Insert error！"
        else:
            for key in config:
                db.MODIFIED('user',self.UserID,[key],[config[key]])


    '''set methods'''
    def set_Name(self,name):
        self.Name = name #前端来判断前后命名是否相同 和是否合法
        # 写入数据库
        db.MODIFIED('user',self.UserID,['Name'],[name])

    def set_Password(self,password):
        self.Password = password
        db.MODIFIED('user',self.UserID,['Password'],password)

    def set_Gender(self,gender):
        self.Gender = gender
        db.MODIFIED('user', self.UserID,['Gender'],gender)

    def set_BirthDate(self,birthdate):
        self.BirthDate = birthdate
        db.MODIFIED('user', self.UserID,['BirthDate'],birthdate)

    def set_PhoneNumber1(self,phone1):
        self.PhoneNumer1 = phone1
        db.MODIFIED('user', self.UserID,['PhoneNumber1'],phone1)

    def set_PhoneNumber2(self,phone2):
        self.PhoneNumer2 = phone2
        db.MODIFIED('user', self.UserID,['PhoneNumber2'],phone2)

    def set_Status(self,status):
        self.Status = status
        db.MODIFIED('user', self.UserID,['Status'],self.Status)
    
    def set_Residence(self,residence):
        self.Residence = residence
        db.MODIFIED('user', self.UserID,['Residence'],residence)

    def set_BirthPlace(self,birthplace):
        self.BirthPlace = birthplace
        db.MODIFIED('user', self.UserID,['birthPlace'],birthplace)


    def set_Marriage(self,marriage):
        self.Marriage = marriage
        db.MODIFIED('user', self.UserID,['Marital_status'],marriage)

    # def set_updata(self): # 更新所有的数据
    #     self.UpdateTime = get_current_time()
    #     # 执行数据库操作

    '''delete'''
    def delete_self(self):
        db.DELETE('user', self.UserID)


    '''get methods'''
