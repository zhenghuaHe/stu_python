#!/usr/bin/pythjon3
#-*- coding:utf-8-*-

class Default(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def info(self):
        print("姓名： %s,成績： %s",(self.__name,self.__score))

    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score = score


stu = Default("小荷",99)
print("修改錢分數： %s" % stu.get_score())
# stu.info()
stu.set_score(10)
print("修改後的分數: %s" % stu.get_score())
