#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET 指IPv4协议
con.connect(('www.baidu.com', 80))

# con.send(b'GET /HTTPS/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')
con.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = con.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b"".join(buffer)

con.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('baidu.html', 'wb') as f:
    f.write(html)