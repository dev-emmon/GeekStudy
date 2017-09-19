#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
多进程
"""

import os, time, random
from multiprocessing import Pool


def long_time_task(name):
    print 'Run task %s (%s)' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    print 'Parents process %s.' % os.getpid()
    # 默认同时 4 个进程
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all sub_processes done...'
    p.close()
    p.join()
    print 'All sub_processes done.'

