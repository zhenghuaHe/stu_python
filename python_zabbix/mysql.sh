#!/bin/bash

#安装mysql５.６的包
echo "[mysql56-community]
name=MySQL 5.6 Community Server
baseurl=http://repo.mysql.com/yum/mysql-5.6-community/el/7/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql"

datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock