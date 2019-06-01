#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:config.py
@TIME:2019/5/18 21:20
@DES:
'''

config = {
    "validata_days": 365,
    "server_ip":"192.168.0.77",
    "database":"hebook"
}

# 表名称与表项ID间的映射，供修改数据时查找表使用
table_ID = {
    "a_contactor_flag":"ContactorID",
    "a_contactor_like":"ContactorID",
    "a_contactor_hate":"ContactorID",
    "t_contactor":"ContactorID",
    "t_csocialaccount":"SPcountID",
    "t_edubackdsc":"EduBackDscID",
    "t_educationbackground":"EduBackID",
    "t_flag":"FlagID",
    "t_hate":"HateID",
    "t_interaction":"InteractionID",
    "t_job":"JobID",
    "t_jobdsc":"JobDscID",
    "t_like":"LikeID",
    "t_remark":"RemarkID",
    "t_uscocialaccount":"SPcountID",
    "t_user":"UserID"
}