#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:yuuZhao
@CONTACT:yuuzhao@163.com
@HOME_PAGE:yuuzhao.top
@SOFTWERE:PyCharm
@FILE:Daystack.py
@TIME:2019/5/24 7:45 PM
@DES:
'''

from support import *
from config import *

class Daystack():
    def __init__(self,contactorid):
        self.ContactorID = contactorid

    def touchDay_low(self,touchdaylow):
        self.touchDay_low = touchdaylow

