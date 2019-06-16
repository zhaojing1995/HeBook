#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:yuuZhao
@CONTACT:yuuzhao@163.com
@HOME_PAGE:yuuzhao.top
@SOFTWERE:PyCharm
@FILE:JobDsc.py
@TIME:2019/5/18 8:48 PM
@DES:
'''

from support import *
import database as db

class JobDsc():
    def __init__(self,jobdscid,dsccontent,jobid):
        self.JobDscID = jobdscid
        self.DscContent = dsccontent
        self.JobID =  jobid

        if not  db.INSERT('t_jobsdc',['JobDscID','DscContent','JobID'],[self.JobDscID,self.DscContent,self.JobID]):
            print "Insert error!"


    def set_DscContent(self,dsccontent):
        self.DscContent = dsccontent

