#!/usr/bin/env python
# _*_ coding=utf-8 _*_

from math import sqrt

for n in range(99, 1, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Nothing.")
