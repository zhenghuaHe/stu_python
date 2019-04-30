#!/usr/bin/python
# -*- coding:utf-8 -*-

import telnetlib

def do_telnet(Host, username, password, finish, commands):
    tn = telnetlib.Telnet(Host, port=23, timeout=10)
    tn.set_debuglevel(2)

    tn.read_until('login:')
    tn.write(username + '\n')

    tn.read_until('password:')
    tn.write(password + '\n')

    tn.read_until(finish)
    for command in commands:
        tn.write('%s\n' % command)

    tn.read_until(finish)
    tn.close()

if __name__ == '__main__':
    Host = '172.16.2.147'
    username = 'he'
    password = '12345.'
    finish = ':~$'
    commands = ['echo "test"']
    do_telnet(Host, username, password, finish, commands)
