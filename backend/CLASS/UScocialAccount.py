#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:yuuZhao
@CONTACT:yuuzhao@163.com
@HOME_PAGE:yuuzhao.top
@SOFTWERE:PyCharm
@FILE:UScocialAccount.py
@TIME:2019/5/18 8:01 PM
@DES:
'''
from support import *
class UScocialAccount():
    def __init__(self,spcountid,app,account,authority,userid):
        self.SPcountID = spcountid
        self.APP = app
        self.Account = account
        self.Authority = authority
        self.UserID = userid
        self.CreateTime = get_current_time()

        '''set methods'''
    def set_APP(self, app):
        self.APP = app

    def set_Account(self,account):
        self.Account = account

    def set_Authority(self,authority):
        self.Authority = authority


    def set_update(self): # 更新所有的数据
        self.UpdateTime = get_current_time()
        # 执行数据库操作

    '''其他功能'''


