#!/usr/bin/env python
# -*- coding = utf-8 -*-

from functools import reduce

def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    s1, s2 = s.split('.')
    return reduce(lambda x,y:x*10+y, map(char2num, s1)) + reduce(lambda x,y:x*10+y, map(char2num, s2))/(10**len(s2))

print(str2float('123.4567'))