#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
装饰品 - 打印方法名（可带/不带参）
"""


def log(text=None):
    import functools
    import types

    if isinstance(text, types.FunctionType):
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator


@log
def now():
    print '2013-12-25'


@log('abc')
def now_():
    print '2013-12-25'


if __name__ == '__main__':
    now()
    now_()

