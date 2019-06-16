#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:Hate.py
@TIME:2019/5/20 16:32
@DES:
'''

from support import *
from config import *
import database as db

class Hete():
    def __init__(self,id,hatename,creatorid,iscreatorhave=False):
        self.HateID = id   #no change
        self.HateName = hatename
        # self.CreateTime = get_current_time()  #no change
        self.isDelete = False
        self.CreatorID = creatorid   #no change
        self.isCreatorHave = iscreatorhave

        db.INSERT('t_hate',['HateID','HateName','isDelete','CreatorID','isCreatorHave'],
                  [self.HateID,self.HateName,self.isDelete,self.CreatorID,self.isCreatorHave])



    '''----------------set methods---------------------'''
    def set_HateName(self,hatename):
        self.HateName = hatename

    def set_isDelete(self,isdelete):
        self.isDelete=isdelete

    def set_isCreatorHave(self,ishave):
        self.isCreatorHave = ishave




