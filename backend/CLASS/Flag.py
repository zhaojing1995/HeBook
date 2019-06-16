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
    def __init__(self,flagid,flagname,creatorid,config,iscreatorhave=False):
        self.FlagID = flagid
        self.FlagName = flagname
        self.CreatorID = creatorid
        self.isCreatorHave = iscreatorhave
        # self.CreateTime = get_current_time()


        if not db.INSERT('t_flag',['FlagID','FlagName','CreatorID','isCreatorHave'],
                  [self.FlagID,self.FlagName,self.CreatorID,self.isCreatorHave]):
            print "Insert error!"
        else:
            for key in config:
                db.MODIFIED('t_flag', self.FlagID, [key], [config[key]])


    def IsDelete(self,isdelete):
        self.IsDelete = isdelete

    def isCreatorHave(self,iscreatorhave):
        self.iscreatorhave = iscreatorhave


