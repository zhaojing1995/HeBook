#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:yuuZhao
@CONTACT:yuuzhao@163.com
@HOME_PAGE:yuuzhao.top
@SOFTWERE:PyCharm
@FILE:CSocialAccount.py
@TIME:2019/5/24 7:50 PM
@DES:
'''

from support import *
from config import *
import database as db

class CSocialAccount():
    def __init__(self,spcountid,app,account,contactorid):
        self.SPcountID = spcountid
        self.APP = app
        self.Account = account
        self.ContactorID = contactorid

        db.INSERT('t_csocialaccount',['SPcountID','APP','Account','ContactorID'],[self.SPcountID,self.APP,self.Account,self.ContactorID])

        # self.CreateTime = get_current_time()

   # def Updatetime(self):

    def set_APP(self,app):
        self.APP = app
        db.MODIFIED('t_csocialaccount',self.SPcountID,['APP'],app)

    def set_Account(self,account):
        self.Account = account
        db.MODIFIED('t_csocialaccount',self.SPcountID,['Account'],account)

    def set_ContactorID(self,contactorid):
        self.ContactorID = contactorid
        db.MODIFIED('t_csocialaccount',self.SPcountID,['ContactorID'],contactorid)

    '''delete'''
    def delete_self(self):
        db.DELETE('t_csocialaccount', self.SPcountID)
