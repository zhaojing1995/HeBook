#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:Interaction.py
@TIME:2019/5/24 19:58
@DES:
'''


from config import *
import support as sp
import database as db
import database as db

class Interaction():
    def __init__(self,level,conterID):
        '''下面是Interaction的内容'''
        self.InteractionID = conterID  # cannot change
        self.Level = level
        self.ProactiveCount = 0  # 主动联系次数
        self.PassiveCount = 0  # 被动联系次数
        self.ActiveDay = 1  # 有效日期
        self.TouchDay = 0  #每天都会传一个值给数据库
        db.INSERT('t_interaction',['InteractionID','Level','ProactiveCount','PassiveCount','ActiveDay','TouchDay'],
                  [self.InteractionID,self.Level,self.ProactiveCount,self.PassiveCount,self.ActiveDay,self.TouchDay])


    '''---------------下面是关于Interaction----------------'''

    def set_Level(self, level):  # 修改level
        self.Level = level
        db.MODIFIED('t_interaction',self.InteractionID,['Level'],level)

    def _update_ProactiveCount(self):  # 主动联系次数
        self.ProactiveCount += 1
        db.MODIFIED('t_interaction', self.InteractionID, ['ProactiveCount'],self.ProactiveCount)

    def _update_PassiveCount(self):  # 被动联系次数
        self.PassiveCount += 1
        db.MODIFIED('t_interaction', self.InteractionID, ['PassiveCount'],self.PassiveCount)

    def _update_ActiveDay(self):  # 有效天数
        if (self.ActiveDay >= config["validata_days"]):
            pass
        else:
            self.ActiveDay += 1
            db.MODIFIED('t_interaction', self.InteractionID, ['ActiveDay'],self.ActiveDay)

    def _update_TotalScore(self):  # 更新得分
        level_contro = (6 - self.Level) * 10
        frequ_contro = (self.ProactiveCount + self.PassiveCount) * 50 / self.ActiveDay
        self.TotalScore = level_contro + frequ_contro
        db.MODIFIED('t_interaction', self.InteractionID, ['TotalScore'],self.TotalScore)
        if (self.TotalScore > 100):
            return {'error': 'error！总分大于100分！'}

    def _update_UntouchDay(self):
        pass


    '''------------启用统一的自动更新-------------------'''

    def auto_update(self):
        self._update_ActiveDay()
        self._update_PassiveCount()
        self._update_ProactiveCount()
        self._update_TotalScore()
        self._update_UntouchDay()

    '''delete'''
    def delete_self(self):
        db.DELETE('t_interaction', self.InteractionID)




