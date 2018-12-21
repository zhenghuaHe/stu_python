#!/usr/bin/python3.7
# -*- coding:utf-8 -*-

import os
import sys
import requests

import logging
logging.basicConfig(level=logging.INFO)

import asyncio
from aiohttp import web

def index():
    return web.Response(text='<h1>welcome to python3</h1>')

def _init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    logging.info('server started at http://127.0.0.1:8080....')
    web.run_app(app)


@asyncio.coroutine
def handle_url_xxx(request):
    pass





_init()

