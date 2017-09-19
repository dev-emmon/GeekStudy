#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
进程间通信
"""

from multiprocessing import Process, Queue
import os, time, random


# 写入数据进程执行的代码
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


# 读取数据进程执行代码
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value


if __name__ == '__main__':
    # 父进程创建 Queue, 并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw, 写入
    pw.start()
    # 启动子进程pr, 读取
    pr.start()
    # 等待 pw 结束
    pw.join()
    # pr 进程是死循环，无法等待其结束，只能强行终止
    pr.terminate()


