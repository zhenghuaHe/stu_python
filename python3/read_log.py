#!/usr/bin/pathon3
# -*- coding: UTF-8 -*-
import os
import json

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_add(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))

from_addr = 'mwteck@mwteck.com'
password = 'Uvz66331McG9FTjcTUN0'
to_addr = 'hezhenghua@mwteck.com'
smtp_server = 'smtp.exmail.qq.com'

# msg = MIMEText('hello.send by python', 'plain', 'utf-8')
# msg['From'] = _format_add(from_addr)
# msg['To'] = _format_add(to_addr)
# msg['Subject'] = Header('异常响应码日志.....', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

error_status = {"404","500","502"}

logfile = open("python-api.t5.2012iot.com.log")
line = json.loads(logfile.readline())
print(line["@fields"])
while line:
    print("request:", line["@fields"]["request"])
    print("status:", line["@fields"]["status"])
    status = line["@fields"]["status"]
    print("request_time:", line["@fields"]["request_time"])
    line = logfile.readline()

    if status in error_status:
        pass


logfile.close()




