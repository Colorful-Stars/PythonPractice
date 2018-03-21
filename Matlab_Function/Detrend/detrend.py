#!/usr/bin/env python
# -*- coding = utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
def detrend(x):
    N = len(x)
    bp = [1,N]
    lbp = len(bp)
    a = np.zeros([N,lbp])
    a[:N,1] = [j/N for j in range(N)]
    for i in range(1,lbp):
        M = N - bp[i]
        a[bp[i] +1:,i] = [j/M for j in range(M)]
    a[:N,-1] = 1
    a = np.matrix(a)
    y = x - a*((a.I)*x)
    return y

f= open('LED_G_win.txt','r')
x=[]
for line in f.readlines():
    line = line.strip('\n')
    x.append(int(line))
f.close()
x = np.matrix(x)
x = x.T
y = detrend(x)
plt.plot(x,'-')
plt.plot(y,'*')
plt.show()




# a = np.zeros([10,2])

# print(a)
# a[:10,1] = 
# print(a[:10,1])

# print([i/10 for i in range(10)])