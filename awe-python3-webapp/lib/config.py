#!/usr/bin/python3.7
# -*- coding:utf-8 -*-



import configparser
import os

def config_read():
    '''
    解析配置文件
    '''

    # 读取
    config = configparser.ConfigParser()
    config.read('../conf/config_default.ini')

    db_port = config['db']['db_port']
    db_user = config['db']['db_user']
    db_host = config['db']['db_host']
    db_passwd = config['db']['db_passwd']
    db_name = config['db']['db_name']

    print(db_port)
    print(db_user)
    print(db_host)
    print(db_passwd)
    print(db_name)





