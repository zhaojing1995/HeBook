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

class CSocialAccount():
    def __init__(self,spcountid,app,account,contactorid):
        self.SPcountID = spcountid
        self.APP = app
        self.Account = account
        self.ContactorID = contactorid
        # self.CreateTime = get_current_time()

   # def Updatetime(self):
