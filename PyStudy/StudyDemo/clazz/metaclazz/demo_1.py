#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
type() - 查看一个类型或变量的类型
"""


class Hello(object):
    def hello(self, name='world'):
        print 'Hello, %s.' % name

if __name__ == '__main__':
    h = Hello()
    h.hello()

    print type(Hello)
    print type(h)

