#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:Contactor.py
@TIME:2019/8/17 19:48
@DES:
'''
import database as db

class Authorization():
    def __init__(self,userid,appname,appaccount):
        self.AuthorizationID = db.get_current_id('Authorization')
        self.UserID = userid
        self.AppName = appname
        self.AppAccount = appaccount
        if not db.INSERT('authorization',['authorization_id','user_id','app_name','app_account'],\
            [self.AuthorizationID,self.UserID,self.AppName,self.AppAccount]):
            print "Insert error！"
        
    def set_AuthorizationCode(self,AuthorizationCode):
        self.AuthorizationCode = AuthorizationCode
        db.MODIFIED('authorization',self.AuthorizationID,['Authorization_Code'],[AuthorizationCode])
