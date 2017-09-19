#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
装饰品 - 打印执行方法名（带参）
"""


# ================== 原 ================
def log_o(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log_o
def now_o():
    print '2013-12-25'


# ================== 修正 =============
def log(text):
    def decorator(func):
        import functools

        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('abc')
def now():
    print '2013-12-25'


if __name__ == '__main__':
    now_o()
    now()


