#!/usr/bin/python3.7

import  random

number = random.randint (1,100)

guess = 0

while True:
    num_input = input("please input 0-100 number:")
    guess +=1
    if not num_input.isdigit():
        print("please input number type is int")
    elif int(num_input) < 0 or int(num_input) >99:
        print("please input number   [1,99)")
    else:
           if  int(num_input) == number:
               print("win,num_input is : %s" %num_input)
               print("cai le  %s  ci" %guess)
               break
           elif int(num_input) > number:
               print("cai  da  le ")
           elif int(num_input) < number:
               print("cai  xiao  le ")
           else:
               print("system error")

