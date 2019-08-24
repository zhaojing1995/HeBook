#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:Contactor.py
@TIME:2019/5/15 23:18
@DES:
'''
# from CLASS import *
# from support import *
from config import *
import support as sp
import database as db

class Contactor():
    def __init__(self, name, userid, level):
        self.ContactorID = db.get_current_id("contact")  # cannot change
        self.Name = name
        self.UserID = userid
        # self.CreateTime = sp.get_current_time()

        db.INSERT('contact',['contact_id','Name','User_ID'],
                  [self.ContactorID,self.Name,self.UserID])

    '''------------------set method-------------------'''

    def set_Name(self, name):
        self.Name = name
        db.MODIFIED('contact',self.ContactorID,['Name'],[self.Name])

    def set_Gender(self, gender):
        self.Gender = gender
        db.MODIFIED('contact', self.ContactorID, ['Gender'], [self.Gender])

    def set_BirthDate(self, birthdate):
        self.BrithDate = birthdate
        db.MODIFIED('contact', self.ContactorID, ['BrithDate'], [self.BrithDate])

    def set_PhoneNumber1(self, phone1):
        self.PhoneNumer1 = phone1
        db.MODIFIED('contact', self.ContactorID, ['PhoneNumer1'], [self.PhoneNumer1])

    def set_PhoneNumber2(self, phone2):
        self.PhoneNumer2 = phone2
        db.MODIFIED('contact', self.ContactorID, ['PhoneNumer2'], [self.PhoneNumer2])

    def set_Status(self, status):
        self.Status = status
        db.MODIFIED('contact', self.ContactorID, ['Status'], [self.Status])

    def set_Residence(self, residence):
        self.Residence = residence
        db.MODIFIED('contact', self.ContactorID, ['Residence'], [self.Residence])

    def set_birthPlace(self, birthPlace):
        self.birthPlace = birthPlace
        db.MODIFIED('contact', self.ContactorID, ['birthPlace'], [self.birthPlace])

    def set_Marriage(self, marriage):
        self.Marriage = marriage
        db.MODIFIED('contact', self.ContactorID, ['Marital_status'], [self.Marriage])


    # def set_updata(self):  # 更新所有的项目
    #     self.UpdateTime =
    #     # 执行数据库操作


    '''delete'''
    def delete_self(self):
        db.DELETE('contact', self.ContactorID)





