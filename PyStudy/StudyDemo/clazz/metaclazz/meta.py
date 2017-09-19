#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
使用 metaclass
"""


# metaclass 是创建类，所以必须从 type 类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    # 指示使用 ListMetaclass 来定制类
    __metaclass__ = ListMetaclass


if __name__ == '__main__':
    L = MyList()
    L.append(1)
    print L


