#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn
@CONTACT:zhaojing17@foxmail.com
@SOFTWERE:PyCharm
@FILE:testfile.py
@TIME:2019/1/12 10:44
@DES:
'''


from database import  *
from Contactor import *
from User import *

if __name__ =="__main__":

    #
    # contactor = Contactor('zhaojing',2,5)
    # contactor.set_Name("zhaoyuyu")

    config={
        "Gender":0,
        "PhoneNumber1":17943233523,
        "JobState":2
    }
    user = User("zhaoyuyu","794253",config)