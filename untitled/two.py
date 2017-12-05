#!/usr/bin/env python
# -*- coding = utf-8 -*-

import math



def quadratic(a, b, c):
    r = b*b - 4*a*c
    if r < 0:
        print('方程没有实根')
    elif r == 0:
        print('方程只有一个实根：', -b/(2*a))
    else:
        print('方程有两个实根：')
        print('x1 = ', (-b + math.sqrt(r)) / (2 * a))
        print('x2 = ', (-b - math.sqrt(r)) / (2 * a))

def main():
    a = int(input('请输入第一个系数：'))
    b = int(input('请输入第二个系数：'))
    c = int(input('请输入第三个系数：'))
    quadratic(a, b, c)


main()

