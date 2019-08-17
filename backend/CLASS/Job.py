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
    def __init__(self,job_id,person_id):
        self.JobID = job_id
        self.PersonID = person_id

        db.INSERT('job',['Job_ID','Person_ID'],[self.JobID,self.PersonID])

    def set_StartTime(self,starttime):
        self.StartTime = starttime
        db.MODIFIED('job',self.JobID,['Start_Time'],starttime)

    def set_EndTime(self,endtime):
        self.EndTime = endtime
        db.MODIFIED('job', self.JobID, ['End_Time'],endtime)

    def set_Company(self,company):
        self.Company = company
        db.MODIFIED('job', self.JobID, ['Company'],company)

    def set_Salary(self,salary):
        self.Salary = salary
        db.MODIFIED('job', self.JobID, ['Salary'],salary)

    def set_SalaryUnit(self,salaryunit):
        self.SalaryUnit = salaryunit
        db.MODIFIED('job', self.JobID, ['Salary_Unit'],salaryunit)

    def set_WorkPlace(self,workplace):
        self.WorkPlace = workplace
        db.MODIFIED('job', self.JobID, ['work_place'],workplace)

    def set_Position(self,position):
        self.Position = position
        db.MODIFIED('job', self.JobID, ['Position'],position)

    def setPersonID(self,PersonID):
        self.PersonID = PersonID
        db.MODIFIED('job', self.JobID, ['Person_ID'],PersonID)

    '''delete'''
    def delete_self(self):
        db.DELETE('job', self.JobID)
