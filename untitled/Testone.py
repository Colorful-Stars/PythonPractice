#!/usr/bin/env python
# -*- coding = utf-8 -*-
'''
L = []

for i in range(3):
    x = int(input('Please input three numbers: '))
    L.append(x)

L.sort()
print(L)[]
'''
s = [0, 1]
n= 10
for i in range(2,n):
    s.append(s[i-1] + s[i-2])
print(s)


