#-*- coding:utf-8 -*-
import os

def BianLi(Dir):
    for root,dirs,files in os.walk(Dir):
        for file in files:
            print(os.path.join(root,file))
        for dir in dirs:
            BianLi(dir)

# dict = {BianLi("/")}
#
# for i in dict:
#      print(os.system('ls -l　dict[i]'))

# import psutil
#
# Pid = psutil.pids()
#
#
# for p in Pid:
#     print(psutil.Process(p).name())
#     print(psutil.Process(p).memory_percent())
















