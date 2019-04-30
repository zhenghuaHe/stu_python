#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import nmap

scan_row = []
input_data = input('Please input hosts and post:')
scan_row = input_data.split()
print(len(scan_row))
if len(scan_row) != 2:
    print("Input error,exampie \"192.168.1.0/24 80,443,22\"")

hosts = scan_row[0]
port = scan_row[1]


nm = nmap.PortScanner()
nm.scan('172.16.1.147', '22')
a = nm['172.16.1.147']    #返回主机的详细信息
print(a)

try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print("Nmap not found", sys.exc_info())
    sys.exit(0)
except:
    print('Unexpected error:', sys.exc_info()[0])
    sys.exit(0)

try:
    nm.scan(hosts=hosts, arguments=' -v -sS -p'+port)
except BaseException as e:
    print("scan erro:"+e)

for host in nm.all_hosts():
    print('----------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State: %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('--------------')
        print('Protocol :', proto)

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))




