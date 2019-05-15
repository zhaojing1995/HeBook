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

class User():
    def __inti__(self,id,name,password):
        self.UserID = id
        self.Name = name
        self.Password = password
        self.CreateTime = get_current_time()

    '''set methods'''
    def set_Name(self,name):
        self.Name = name #前端来判断前后命名是否相同 和是否合法

    def set_Password(self,password):
        self.Password = password

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

    def set_updata(self):
        self.UpdateTime = get_current_time()
        # 执行数据库操作

    '''其他功能'''