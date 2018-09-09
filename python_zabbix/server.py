#!/usr/bin/python3
#coding=utf-8

import socket
import time
import json


#创建一个socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定ip地址
host = socket.gethostname()
port = 8888
serversocket.bind((host, port))

#设置最大链接数
serversocket.listen(5)

print('Server start...')

#开启死循环等待客户端链接
while True:
    print('等待下次链接...')
    #建立链接
    clientsocket, addr = serversocket.accept()
    #客户端地址
    print("此次链接的客户端地址：%s" % str(addr))

    msg = '探测本机信息开始...' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))

    print("---------获取信息开始--------")
    print("获取信息时间：%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    outfo = clientsocket.recv(1024)
    outfo = json.loads(outfo)
    print(outfo)

    print("-------本次信息获取结束--------")
    # clientsoctet.close