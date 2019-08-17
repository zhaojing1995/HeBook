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

class Prefer():
    def __init__(self,preferid,userid,prefername,prefertype,preferholder):
        self.PreferID = db.get_current_id('prefer')
        self.UserID = userid
        self.PreferName = prefername
        self.PreferType = prefertype
        self.Preferholder = preferholder
        if not db.INSERT('prefer',['prefer_id','user_id','prefer_name','prefer_type','prefer_holder'],\
            [self.PreferID,self.UserID,self.PreferName,self.PreferType,self.Preferholder]):
            print "Insert error！"