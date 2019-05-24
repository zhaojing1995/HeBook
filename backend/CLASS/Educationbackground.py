#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:Educationbackground.py
@TIME:2019/5/24 19:37
@DES:
'''

from support import *
from config import *

class Educationbackground():
    def __init__(self,id, degree,school,contactorid,userid):
        self.EduBackId = id  # no change
        self.Degree = degree
        self.School  = school
        self.ContactorID =contactorid    #no change
        self.UserID = userid      #no change

    '''------------set methods-------------'''
    def set_Degree(self,degree):
        self.Degree = degree

    def set_School(self,school):
        self.School = school



