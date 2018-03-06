#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Create Time: 2018/3/6
 @ Author: songpo.zhang
 @ Target:
"""
import matplotlib.pyplot as plt
f = open("1200-rawdata.txt", "r")
a=[]
for line in f.readlines():
    line = line.strip("\n")
    a.append(line)
f.close()
print(a)
plt.plot(a)
print(len(a))

from iirFilter import iirFilter
b = iirFilter(a)
print(b)
plt.plot(b)
plt.show()



