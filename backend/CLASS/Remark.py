#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:yuuZhao
@CONTACT:yuuzhao@163.com
@HOME_PAGE:yuuzhao.top
@SOFTWERE:PyCharm
@FILE:Remark.py
@TIME:2019/5/18 8:24 PM
@DES:
'''
from support import *

class Remark():
    def __init__(self,remarkid,content,contactorid):
        self.RemarkID = remarkid
        self.Content = content
        self.ContactorID = contactorid
        self.CreateTime = get_current_time()

    def set_Content(self,content):
        self.Content =  content


    #def set_updata(self): # 更新所有的数据
