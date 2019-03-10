#!/usr/bin/python
#-*- conding:utf-8 -*-

def donothing(str):
    print("我是傳入的參數:",str)

donothing("hello,world")


def table(name,age):
    print("姓名：",name)
    print("年齡：",age)

table(21,"小剛")
table("小明",12)
table(age=14,name="小荷")

def tim(name,age=18):
    print("嗨，我叫",name)
    print("我今年%s 歲 "%age)
                              

tim("小姐",12)
tim("小妹")