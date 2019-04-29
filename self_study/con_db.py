#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __bablename__ = 'user'

    id = Column()
    name = Column()
