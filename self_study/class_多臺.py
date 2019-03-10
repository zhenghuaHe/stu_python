#!/usr/bin/python3
#-*- coding:utf-8 -*-

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

std = Student("小荷",99)
def info(std):
    print("姓名：%s,成績： %s" % (std.name,std.score))

info(std)