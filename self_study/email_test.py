#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1931753662@qq.com'
pwd = 'mmldrvhjrgphdfhf'
receivers = ['hezhenghua@mwteck.com']

message = MIMEText('python email test', 'plain', 'utf-8')
message['From'] = Header("email_test", 'utf-8')
message['To'] = Header("test", 'utf-8')

subject = "Python SMTP 邮件测试"
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('smtp.qq.com', 25)
    smtpObj.login(sender, pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print('Error：无法发送邮件.Case:%s' % e)



