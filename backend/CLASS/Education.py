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
import database as db

class Education():
    def __init__(self,id, academic,school,person_id):
        self.Education_id = id  # no change
        self.Academic = academic
        self.School  = school
        self.Person_id = person_id    #no change
        
        db.INSERT('education',['Education_id','academic','School','person_id'],\
            [self.Education_id,self.Academic,self.School,self.Person_id])


    '''------------set methods-------------'''
    def set_Academic(self,academic):
        self.Academic = academic
        db.MODIFIED('education',self.Education_id,['academic'],academic)

    def set_School(self,school):
        self.School = school
        db.MODIFIED('education', self.Education_id, ['School'],school)

    '''delete'''
    def delete_self(self):
        db.DELETE('education', self.Education_id)




