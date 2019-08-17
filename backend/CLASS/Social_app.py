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

class Social_app():
    def __init__(self,socialid,contactid,social_platform,social_account):
        self.SocialID = db.get_current_id('mark')
        self.ContactID = contactid
        self.SocialPlatform = social_platform
        self.SocialAccount = social_account
        if not db.INSERT('social_app',['social_id','contact_id','social_platform','social_account'],\
            [self.SocialID,self.ContactID,self.SocialPlatform,self.SocialAccount]):
            print "Insert error！"