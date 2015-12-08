#!/usr/bin/python3
# -*- coding:utf8 -*-
__author__ = 'zejun_liu'

import asyncio

from www import orm
from models import User


def test(loop):
    yield from orm.create_pool(loop=loop, user='root', password='root',db='awesome')
    u = User(name='test2', email='test2@example.com', passwd='1243',image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
