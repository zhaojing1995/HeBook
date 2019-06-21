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
import database as db
class Job():
    def __init__(self,jobid,contactorid,userid):
        self.JobID = jobid
        self.ContactorID = contactorid
        self.UserID = userid

        db.INSERT('t_job',['JobID','ContactorID','UserID'],[self.JobID,self.ContactorID,self.UserID])



    def set_StartTime(self,starttime):
        self.StartTime = starttime
        db.MODIFIED('t_job',self.JobID,['StartTime'],starttime)

    def set_EndTime(self,endtime):
        self.EndTime = endtime
        db.MODIFIED('t_job', self.JobID, ['EndTime'],endtime)

    def set_Salary(self,salary):
        self.Salary = salary
        db.MODIFIED('t_job', self.JobID, ['Salary'],salary)

    def set_SalaryUnit(self,salaryunit):
        self.SalaryUnit = salaryunit
        db.MODIFIED('t_job', self.JobID, ['SalaryUnit'],salaryunit)

    def set_Company(self,company):
        self.Company = company
        db.MODIFIED('t_job', self.JobID, ['Company'],company)

    def set_Position(self,position):
        self.Position = position
        db.MODIFIED('t_job', self.JobID, ['Position'],position)

    def setContactorID(self,contactorid):
        self.ContactorID = contactorid
        db.MODIFIED('t_job', self.JobID, ['ContactorID'],contactorid)

    '''delete'''
    def delete_self(self):
        db.DELETE('t_job', self.JobID)
