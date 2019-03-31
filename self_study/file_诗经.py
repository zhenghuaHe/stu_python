#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
#向文件中写一首诗

path = '/home/he/sh/诗经.txt'
new_path = '/home/he/sh/new_file.txt'


f_name = open(path, 'a')
print('add line:', f_name.write("关关雎鸠，在河之洲。"))
print('add line:', f_name.write('\n'))
print('add line:', f_name.write("窈窕淑女，君子好逑。"))
print('add line:', f_name.write('\n'))
f_name = open(path, 'r')
print('read f_name:', f_name.read())

f_new = open(new_path, 'a+')

while True:
    line = f_name.readline(1)
    print('line 类型:', type(line))
    print('输出行:', line)
    if "君子好逑" in line:
        line = line.replace("君子好逑", "where are QQ")
    if not line:
        break
    print(line)

f_new.write(line)
f_new.flush()

f_new = open(path, 'r')
print('read f_new:', f_new.read())

f_name.close()
f_new.close()

os.remove(path)
os.remove(new_path)


