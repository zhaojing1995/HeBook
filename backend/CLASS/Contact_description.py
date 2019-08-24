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

class Contact_description():
    def __init__(self,descriptid,contactid,descriptcontent):
        self.DescriptID = db.get_current_id('prefer')
        self.ContactID = contactid
        self.DescriptContent = descriptcontent
        if not db.INSERT('contact_description',['descript_id','contact_id','descript_content'],\
            [self.DescriptID,self.ContactID,self.DescriptContent]):
            print "Insert error！"