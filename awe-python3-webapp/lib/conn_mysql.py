#!/usr/bin/python3
#-*- coding: utf-8 -*-

from lib.orm import create_pool

from lib.models import User, Blog, Comment

def test_conn():
    yield from create_pool(user='www-data', password='www-data', database = 'awesome')

    u = User(name='Test', email='test@exampie.com', passwd='123456', images='about:blank')

    yield from u.save()

for x in test_conn():
    pass