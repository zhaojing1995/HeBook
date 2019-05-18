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
from config import *

class Contactor():
    def __init__(self,id,name,userid,level):
        self.ContactorID = id  #cannot change
        self.Name = name
        self.UserID = userid
        self.CreateTime = get_current_time()


        '''下面是Interaction的内容'''
        self._InteractionID = id  #cannot change
        self._Level = level
        self._ProactiveCount = 0
        self._PassiveCount = 0
        self._ActiveDay = 1


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


    '''---------------下面是关于Interaction----------------'''
    def set_Level(self,level): #修改level
        self._Level = level

    def _update_ProactiveCount(self): #主动联系次数
        self._ProactiveCount +=1

    def _update_PassiveCount(self): #被动联系次数
        self._PassiveCount +=1

    def _update_ActiveDay(self): #有效天数
        if(self._ActiveDay >= config["validata_days"])

    def _update_TotalScore(self): #更新得分
        level_contro = (6-self._Level)*10
        frequ_contro = (self._ProactiveCount+self._PassiveCount)*50/self._ActiveDay
        self._TotalScore = level_contro+frequ_contro
        if(self._TotalScore>100):
            return {'error':'error！总分大于100分！'}

    def _update_UntouchDay(self):
        pass


