#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

import random, time, Queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = Queue.Queue()
# 接收结果的队列
result_queue = Queue.Queue()


# 从 BaseManager 继承的 QueueManager
class QueueManager(BaseManager):
    pass


# 把两个 Queue 都注册到网络上，callback 参数关联了 Queue 对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口 5000，设置验证码 'abc'
manager = QueueManager(address=('', 5000), authkey='abc')
# 启动 Queue
manager.start()
# server = manager.get_server()
# server.serve_forever()
# 获得通过网络访问的 Queue 对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
for i in range(10):
    n = random.randint(0, 100000)
    print 'Put task %d...' % n
    task.pu(n)

# 人 result 队列读取结果
print 'Try get results...'
for i in range(10):
    r = result.get(timeout=10)
    print 'Result: %s' % r

# 关闭
manager.shutdown()
