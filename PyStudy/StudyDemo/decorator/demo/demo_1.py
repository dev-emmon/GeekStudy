#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
装饰器 - 打印执行方法名
"""


# ================== 原 ================

def log_o(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log_o
def now_o():
    print '2013-12-25'


# ================== 修正 =============
def log(func):
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print '2013-12-25'


if __name__ == '__main__':
    now_o()
    now()
