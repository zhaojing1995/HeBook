#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:yuuZhao
@CONTACT:yuuzhao@163.com
@HOME_PAGE:yuuzhao.top
@SOFTWERE:PyCharm
@FILE:Flag.py.py
@TIME:2019/5/24 7:13 PM
@DES:
'''

from support import *
from config import *

import database as db

class Flag():
    def __init__(self,flagid,flagname,creatorid):
        self.FlagID = flagid
        self.FlagName = flagname
        self.CreatorID = creatorid
        # self.CreateTime = get_current_time()

        db.INSERT('t_flag',['FlagID','FlagName','CreatorID','isCreatorHave'],
                  [self.FlagID,self.FlagName,self.CreatorID])



    def IsDelete(self,isdelete):
        self.IsDelete = isdelete

    def isCreatorHave(self,iscreatorhave):
        self.iscreatorhave = iscreatorhave


