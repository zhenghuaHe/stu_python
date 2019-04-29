#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())

pid = os.fork()
if pid == 0:
    print('i am child process (%s) and my parent is.' % (os.getpid(), os.getppid()))
else:
    print('i (%s) just created a child process (%s).' % (os.getpid(), pid))