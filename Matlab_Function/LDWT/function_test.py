#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Create Time: 2018/3/9
 @ Author: songpo.zhang
 @ Target:
"""
import numpy as np
import scipy.io as scio
from LDWT import LDWT

f = open("WLED_G_tmp_abs.txt",'r')
a = []
for line in f.readlines():
    a.append(line.strip("\n"))
f.close()
print(a)
print(len(a))
print("=================================================================")
a0 = scio.loadmat("WLED_G_tmp_abs.mat")['WLED_G_tmp_abs']
a1=[]
for ii in range(len(a0)):
    a1.append(a0[ii][0])
print(a1)
print(len(a1))
print("=================================================================")
b = LDWT(a1,6,6,25,1)
print("LDWT with Python:")
print(b)
print("=================================================================")
b0 = scio.loadmat("LED_G_win_DC.mat")['LED_G_win_DC']
b1=[]
for ii in range(len(b0)):
    b1.append(b0[ii][0])
print("LDWT with Matlab:")
print(b1)
print("=================================================================")