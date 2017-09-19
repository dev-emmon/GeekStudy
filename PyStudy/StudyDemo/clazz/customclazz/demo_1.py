#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/17


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __repr__(self):
        return 'Student object (name: %s)' % self.name

if __name__ == '__main__':
    print Student('Ne co')




