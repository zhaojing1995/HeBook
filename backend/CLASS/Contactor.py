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
from Interaction import *
# from support import *
from config import *
import support as sp
import database as db

class Contactor():
    def __init__(self, name, userid, level):
        self.ContactorID = db.get_current_id("Contactor")  # cannot change
        self.Name = name
        self.UserID = userid
        # self.CreateTime = sp.get_current_time()
        Interaction(level,self.ContactorID)   #初始化一个interaction

        db.INSERT('t_contactor',['ContactorID','Name','UserID','InteractionID'],
                  [self.ContactorID,self.Name,self.UserID,self.ContactorID])

    '''------------------set method-------------------'''

    def set_Name(self, name):
        self.Name = name
        db.MODIFIED('t_contactor',self.ContactorID,['Name'],[self.Name])

    def set_Gender(self, gender):
        self.Gender = gender
        db.MODIFIED('t_contactor', self.ContactorID, ['Gender'], [self.Gender])

    def set_BirthDate(self, birthdate):
        self.BrithDate = birthdate
        db.MODIFIED('t_contactor', self.ContactorID, ['BrithDate'], [self.BrithDate])

    def set_PhoneNumber1(self, phone1):
        self.PhoneNumer1 = phone1
        db.MODIFIED('t_contactor', self.ContactorID, ['PhoneNumer1'], [self.PhoneNumer1])

    def set_PhoneNumber2(self, phone2):
        self.PhoneNumer2 = phone2
        db.MODIFIED('t_contactor', self.ContactorID, ['PhoneNumer2'], [self.PhoneNumer2])

    def set_PhoneNumber3(self, phone3):
        self.PhoneNumer3 = phone3
        db.MODIFIED('t_contactor', self.ContactorID, ['PhoneNumer3'], [self.PhoneNumer3])

    def set_JobState(self, jobstate):
        self.JobState = jobstate
        db.MODIFIED('t_contactor', self.ContactorID, ['JobState'], [self.JobState])

    def set_NativePlace(self, nativeplace):
        self.NativePlace = nativeplace
        db.MODIFIED('t_contactor', self.ContactorID, ['NativePlace'], [self.NativePlace])

    def set_Residence(self, residence):
        self.Residence = residence
        db.MODIFIED('t_contactor', self.ContactorID, ['Residence'], [self.Residence])

    def set_Marriage(self, marriage):
        self.Marriage = marriage
        db.MODIFIED('t_contactor', self.ContactorID, ['Marriage'], [self.Marriage])


    # def set_updata(self):  # 更新所有的项目
    #     self.UpdateTime =
    #     # 执行数据库操作


    '''delete'''
    def delete_self(self):
        db.DELETE('t_contactor', self.ContactorID)





