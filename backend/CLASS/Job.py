#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:yuuZhao
@CONTACT:yuuzhao@163.com
@HOME_PAGE:yuuzhao.top
@SOFTWERE:PyCharm
@FILE:Job.py
@TIME:2019/5/18 8:58 PM
@DES:
'''
from support import *
import database as db

class Job():
    def __init__(self,jobid,contactorid,userid):
        self.JobID = jobid
        self.ContactorID = contactorid
        self.UserID = userid

        db.INSERT('t_job',['JobID','ContactorID','UserID'],[self.JobID,self.ContactorID,self.UserID])



    def set_StartTime(self,starttime):
        self.StartTime = starttime

    def set_EndTime(self,endtime):
        self.EndTime = endtime

    def set_Salary(self,salary):
        self.Salary = salary

    def set_SalaryUnit(self,salaryunit):
        self.SalaryUnit = salaryunit

    def set_Company(self,company):
        self.company = company

    def set_Position(self,position):
        self.Position = position

    def setContactorID(self,contactorid):
        self.ContactorID = contactorid


