#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
type() - 创建类
"""


class Hello(object):
    def hello(self, name='world'):
        print 'Hello, %s.' % name


# 先定义函数
def fn(self, name='world'):
    print 'Hello, %s.' % name


# 创建 Hello class
Hello = type('Hello', (object,), dict(hello=fn))

if __name__ == '__main__':
    h = Hello()
    h.hello()

    print type(Hello)
    print type(h)
