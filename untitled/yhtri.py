#!/usr/bin/env python
# -*- coding = utf-8 -*-

def tri():
    L = [1]
    while True:
        yield L
        L.append(0)  #精髓
        L = [L[i-1] + L[i] for i in range(len(L))]

n = 0
for m in tri():
    print(m)
    n = n + 1
    if n == 10:
        break