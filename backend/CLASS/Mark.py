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

class Mark():
    def __init__(self,markid,userid,markname,markholder):
        self.MarkID = db.get_current_id('mark')
        self.UserID = userid
        self.MarkName = markname
        self.Markholder = markholder
        if not db.INSERT('mark',['mark_id','user_id','mark_name','mark_holder'],\
            [self.MarkID,self.UserID,self.MarkName,self.Markholder]):
            print "Insert error！"