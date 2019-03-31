#!/usr/bin/python
# -*- coding:utf-8 -*-

#进程：运行的一个程序
#线程：属于进程的孩纸，共享运行环境，只做自己的事情，有需要再和其他的产生交互

import threading
from time import sleep
from datetime import datetime

loops = [4, 2]
date_time_format = '%y-%M-%d %H:%M:%s'

def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)

def loop(n_loop,n_sec):
    print('线程(', n_loop, ')开始执行:', date_time_str(datetime.now()), ', 先休眠 (', n_sec, ') 秒')
    sleep(n_sec)
    print('线程 (', n_loop, ') 休眠结束，结束于:', date_time_str(datetime.now()))

def main():
    print('---所有线程开始执行:', date_time_str(datetime.now()))
    threads = []
    n_loops =range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in n_loops:
        threads[i].start()

    for i in n_loops:
        threads[i].join()

    print('---所有线程结束于：', date_time_str(datetime.now()))


if __name__ == '__main__':
    main()


