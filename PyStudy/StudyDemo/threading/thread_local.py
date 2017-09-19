#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

import threading


# 创建全局 ThreadLocal 对象
local_school = threading.local()


def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)


def process_thread(name):
    # 绑定 ThreadLocal 的 student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='T-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='T-B')
t1.start()
t2.start()
t1.join()
t2.join()

