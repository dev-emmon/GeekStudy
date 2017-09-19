#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/10


def triangles():
    L = [1]
    n = 1
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(n-1)] + [1]
        n += 1

for i, l in enumerate(triangles()):
    print l
    if i == 10:
        break

