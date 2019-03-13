#!/usr/bin/python3
#-*- coding:utf-8 -*-

def exp_exception(x,y):
    try:
        a = x/y
        print("a=",a)
        return a
    except Exception:
        print("程序出现异常,异常信息：被除数为0")


def mult_exception(x,y):
    try:
        # b = name
        a = x/y
    except:
        print("Error happened")
    else:
        print("it went as expected")
mult_exception(2,1)

class MyError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "this is self define error"
def my_error_test():
    try:
        raise MyError()
    except MyError as e:
        print("exception info:",e)
my_error_test()