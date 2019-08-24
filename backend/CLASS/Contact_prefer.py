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

class Contact_prefer():
    def __init__(self,contactid,preferid):
        self.PreferID = preferid
        self.ContactID = contactid
        if not db.INSERT('contact_prefer',['contact_id','prefer_id'],\
            [self.ContactID,self.PreferID]):
            print "Insert error！"