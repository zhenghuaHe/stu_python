#!/usr/bin/pathon3
# -*- coding: UTF-8 -*-
import os
import json
import smtplib

def sendmessage():
    sender = "from@mwteck@mwteck.com"
    receivers = "hezhenghua@mwteck.com"

    message = """
    
    
    """

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
        sendmessage()


logfile.close()




