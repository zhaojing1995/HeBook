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
    "authorization":"authorization_id",
    "contact":"Contact_ID",
    "contact_description":"descript_id",
    "contact_mark":"contact_id",
    "contact_prefer":"contact_id",
    "education":"education_id",
    "job":"Job_ID",
    "mark":"mark_ID",
    "prefer":"prefer_id",
    "social_app":"social_id",
    "user":"User_ID"
}