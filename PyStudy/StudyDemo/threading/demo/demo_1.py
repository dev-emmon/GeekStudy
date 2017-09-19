#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
多线程
"""

import time
import threading


# 新线程执行代码
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name


if __name__ == '__main__':
    print 'thread %s is running...' % threading.currentThread().name
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print 'thread %s ended.' % threading.current_thread().name
