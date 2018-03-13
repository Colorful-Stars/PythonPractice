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


# f = open("1200-rawdata.txt", "r")
# #
# a=[]
# for line in f.readlines():
#     line = line.strip("\n")
#     a.append(line)
# # f.close()
# print(a)

a0 = scio.loadmat("RawLED_R.mat")['RawLED_R']
a1=[]
for ii in range(len(a0)):
    a1.append(a0[ii][0])

print(a1)

# plt.plot(a,color="green")
# plt.plot(rawdata_r)
# print(len(a))
# print(a1)
# plt.plot(a1)
# print(len(a1))

from iirFilter import iirFilter
b = iirFilter(a1)
print("IIR_Filter with Python:")
print(b)

# plt.plot(b)
# plt.show()
#
b0 = scio.loadmat("LED_R_tmp.mat")['LED_R_tmp']
b1=[]
for ii in range(len(b0)):
    b1.append(b0[ii][0])
print("IIR_Filter with Matlab:")
print(b1)
# print(len(led_r_tmp))
# plt.plot(led_r_tmp)


# plt.show()


