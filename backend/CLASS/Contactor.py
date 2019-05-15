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
from support import *

class Contactor():
    def __init__(self,id,name,userid):
        self.ContactorID = id
        self.Name = name
        self.UserID = userid
        self.CreateTime = get_current_time()
        self.InteractionID = id

    '''------------------set method-------------------'''
    def set_Name(self,name):
        self.Name = name

    def set_Gender(self,gender):
        self.Gender = gender

    def set_BirthDate(self,birthdate):
        self.BrithDate = birthdate

    def set_PhoneNumber1(self,phone1):
        self.PhoneNumer1 = phone1

    def set_PhoneNumber2(self,phone2):
        self.PhoneNumer2 = phone2

    def set_PhoneNumber3(self,phone3):
        self.PhoneNumer3 = phone3

    def set_JobState(self,jobstate):
        self.JobState = jobstate

    def set_NativePlace(self,nativeplace):
        self.NativePlace = nativeplace

    def set_Residence(self,residence):
        self.Residence = residence

    def set_Marriage(self,marriage):
        self.Marriage = marriage

    def set_updata(self): #更新所有的项目
        self.UpdateTime = get_current_time()
        # 执行数据库操作
