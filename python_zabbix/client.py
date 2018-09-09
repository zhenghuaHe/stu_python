#coding=utf-8

import socket
import psutil
import json



#创建链接
#生成一个socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8888
#请求连接服务端
sk.connect((host, port))


#获取信息
#获取主机名
hostname = socket.getfqdn(socket.gethostname())
#获取主机IP地址
host_ip = socket.gethostbyname(hostname)
#获取内存使用率
host_memory = str(psutil.virtual_memory().percent)
#获取CPU的使用率
host_cpu = str(psutil.cpu_percent(0))
#本机登录用户
host_user = str(psutil.users())


#写入字典
info = {"主机名:": hostname,"主机IP地址:": host_ip,"内存使用率:": host_memory,"CPU使用率:": host_cpu,"登录用户详情:": host_user}
result = json.dumps(info)



#发送数据
# sk.send(bytes(dict))
sk.send(result.encode('utf8'))



#接受信息
#接受小于1024字节的数据
msg = sk.recv(1024)
print(msg.decode('utf-8'))


#关闭连接
sk.close()