#!/usr/bin/python3
#-*- coding:utf-8 -*-


class  MyClass(object):
    i=123
    def __init__(self,name):
        self.name = name

    def  f(self):
        return  "hello."+ self.name

use_class = MyClass("小明")

print("調用類的屬性：",use_class.i)
print("調用類的方法：",use_class.f())
