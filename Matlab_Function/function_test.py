#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Create Time: 2018/3/6
 @ Author: songpo.zhang
 @ Target:
"""
import numpy as np
import matplotlib.pyplot as plt
# 读取.mat文件
import scipy.io as scio


f = open("1200-rawdata.txt", "r")

a=[]
for line in f.readlines():
    line = line.strip("\n")
    a.append(line)
f.close()
print(a)

# a1 = scio.loadmat("RawLED_R.mat")
# rawdata_r = a1['RawLED_R'][1:]
# print(type(rawdata_r))
# print(rawdata_r)

plt.plot(a,color="green")
# plt.plot(rawdata_r)
# print(len(a))
# print(a1)
# plt.plot(a1)
# print(len(a1))

from iirFilter import iirFilter
b = iirFilter(a)
print(b)
print(len(b))
plt.plot(b)
# plt.show()
#
b1 = scio.loadmat("LED_R_tmp.mat")
led_r_tmp = b1['LED_R_tmp'][1:]
print(led_r_tmp)
# print(len(led_r_tmp))
# plt.plot(led_r_tmp)


plt.show()


