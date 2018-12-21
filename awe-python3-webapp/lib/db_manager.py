#!/usr/bin/python3.7
# -*- coding:utf-8 -*-

import asyncio
import aiomysql

import logging
logging.basicConfig(level=logging.INFO)

from lib.config import config_read




def log(sql,args=()):
    logging.info('SQL:%s' %sql)

config_read

async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host = kw.get('host', 'localhost'),
        port = kw.get('port', 3306),
        user = kw.get('user'),
        passwd = kw.get('password'),
        dbname = kw.get('dbname'),
        charset = kw.get('charset', 'utf8'),
        loop=loop
    )



async def destory_pool():
    global __pool
    if __pool is not None:
        __pool.close()
        await __pool.wait_close()



async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute('?', '%s'),args or ()
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs



async def execute(sql,args):
    log(sql)
    with (await __pool) as conn:
        try:
            cul = await conn.cursor()
            await cul.execute(sql.replace('?', '%s'), args)
            await cul.commit()
            affected = cul.rowcount
            await cul.close()
            print('execute:', affected)
        except BaseException as e:
            raise
        return affected



from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class User(Base):
    #表名
    __tablename__ = 'user'

    #表结构
    id = Column(String(20), primary_key= True)
    name = Column(String(30))

# engine = create_engine('mysql+mysqlconnector://db_user:db_passwd@db_host:db_port/db_name')
# DBsession = sessionmaker(bind=engine)
