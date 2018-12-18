#!/usr/bin/pathon3
# -*- coding: UTF-8 -*-
#实时读取日志，发现有返回码为404/502/500就发邮件通知
import json


from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

from_addr = 'mwteck@mwteck.com'
password = 'Uvz66331McG9FTjcTUN0'
to_addr = 'hezhenghua@mwteck.com'
smtp_server = 'smtp.exmail.qq.com'


def _format_add(s):
    name, addr = parseaddr(str(s))
    msg = MIMEText(str(s), 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header('异常响应码日志.....', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

    return formataddr((Header(name, "utf-8").encode(), addr))


error_status = {"404","500","502"}

with open('python-api.t5.2012iot.com.log', 'r+') as f:
    while True:
        line = f.readline()
        if line:
            load_data = json.loads(line)
            print(load_data)
            print(load_data["@fields"]['request'])
            print("request:", load_data["@fields"]["request"])
            print("status:", load_data["@fields"]["status"])
            print("request_time:", load_data["@fields"]["request_time"])


            status = load_data["@fields"]["status"]
            if status in error_status:
                _format_add(load_data["@fields"])




