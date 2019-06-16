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
def fun_regist(username,password,bundlephone,config): #创建User
    '''
    :param username:  用户昵称
    :param password:  密码
    :param bundlephone:  绑定的手机号
    :param config:  其他非必填数据项
    :return: 注册成功返回1，否则返回0
    '''
    user = User(username,password,bundlephone,config)

