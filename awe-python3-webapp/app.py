#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


[DEFAULT]
minSdkVersion = 15
targetSdkVersion = 24
versionName = 1.0.0
server action = yes

[luzhuo.me]
user = luzhuo

# This is a comments.
[mysql]
ip = 127.0.0.1
port = 3306
'''

def config_read():
    '''
    #解析配置文件
    '''

    # 读取
    config = configparser.ConfigParser()
    config.read('config.ini')

    lists_header = config.sections()  # 配置组名, ['luzhuo.me', 'mysql'] # 不含'DEFAULT'
    print(lists_header)

    boolean = 'luzhuo.me' in config  # 配置组是否存在
    boolean = config.has_section("luzhuo.me")
    print(boolean)

    user = config['luzhuo.me']['user']
    print(user)
    mysql = config['mysql']
    mysql_ip = mysql['ip']
    mysql_port = mysql['port']
    print(mysql_ip, ":", mysql_port)

    for key in config['luzhuo.me']:  # 遍历配置组的key, 与'DEFAULT'组的key
        print(key)

if __name__ == "__main__":
    config_write()
    config_read()


