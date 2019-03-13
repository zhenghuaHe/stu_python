#!/usr/bin/python3
# -*- coding:utf-8 -*-
import  types

#获取对象信息的三种方法：
#type()函数  判断类型

print(type(123))

print(type(abs))

def func():
    pass

#使用isinstance()函数，判断继承关系
class Animai(object):
    pass

class Mammal(Animai):
    pass

an = Animai()
ma = Mammal()
print(isinstance(ma,Mammal))
print(isinstance(ma,Animai))

print(dir("123"))
dir("123")