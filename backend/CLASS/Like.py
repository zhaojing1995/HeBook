#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:yuuZhao
@CONTACT:yuuzhao@163.com
@HOME_PAGE:yuuzhao.top
@SOFTWERE:PyCharm
@FILE:Like.py
@TIME:2019/5/18 8:30 PM
@DES:
'''
from support import *
import database as db
class Like():
    def __init__(self,likeid,likename,iscreatorhave,creatorid,config):
        self.LikeID = likeid
        self.LikeName = likename
        # self.CreateTime = get_current_time()
        self.CreatorID = creatorid
        self.isCreatorHave = iscreatorhave
        if not db.INSERT('t_like',['LikeID','LikeName','CreatorID','isCreatorHave'],[self.LikeID,self.LikeName,self.CreatorID,self.isCreatorHave]):
            print "Insert error!"
        else:
            for key in config:
                db.MODIFIED('t_like',self.LikeID,[key],[config[key]])

    def set_isDelete(self,isdelete):
        self.IsDelete = isdelete

    def set_isCreatorHave(self,iscreatorhave):
        self.isCreatorHave = iscreatorhave

    def set_LikeName(self,likename):
        self.LikeName = likename

    def set_CreatorID(self,creatorid):
        self.CreatorID = creatorid


    # def set_updata(self): # 更新所有的数据
    #     return 0

    '''其他功能'''