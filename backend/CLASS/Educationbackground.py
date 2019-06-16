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

class Educationbackground():
    def __init__(self,id, degree,school,contactorid,userid,config):
        self.EduBackId = id  # no change
        self.Degree = degree
        self.School  = school
        self.ContactorID =contactorid    #no change
        self.UserID = userid      #no change
        
        db.INSERT('t_educationbackground',['EduBackID','Degree','School','ContactorID','UserID'],[self.EduBackId,self.Degree,self.School,self.ContactorID,self.UserID])

        if not  db.INSERT('t_educationbackground',['EduBackID','Degree','School','ContactorID','UserID'],[self.EduBackId,self.Degree,self.School,self.ContactorID,self.UserID]):
            print "Insert error!"
        else:
            for key in config:
                db.MODIFIED('t_educationbackground', self.EduBackId, [key], [config[key]])

    '''------------set methods-------------'''
    def set_Degree(self,degree):
        self.Degree = degree

    def set_School(self,school):
        self.School = school



