#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:regist.py
@TIME:2019/6/1 20:08
@DES:
'''

from User import  User


#考虑一个注册的流程
def fun_regist(config): #创建User
    user = User(config)
