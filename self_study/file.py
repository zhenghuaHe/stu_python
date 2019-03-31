#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

path = '/home/he/note.txt'
f_name = open(path, 'a')
print(f_name.write("\ni love you"))

f_name = open(path, 'r')
print(f_name.readlines())

f_name.close()


with open(path, 'w') as f :
    f_name = open(path, 'w')
    print('write length:', f_name.write("i miss you"))

# os.rename('/home/he/test.txt','/home/he/test1.txt')

try:
    print('remove file:', os.remove('/home/he/test1.txt'))
except Exception:
    print('file not found')

f_name = open(path)
for line in f_name:
   print('line is', line)
f_name.close()