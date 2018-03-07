#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Create Time: 2018/3/7
 @ Author: songpo.zhang
 @ Target:
"""


def LDWT(input, DecLevel, WaveRemain, Fs, Flag):
    Si = input
    N = len(input)

    a = -1.586134342
    b = -0.052980118
    c = 0.882911075
    d = 0.443506852
    e = 1.230174105
    S = []
    for jj in range(DecLevel):
        N = N / 2

        for ii in range(int(N)):
            S[ii] = Si[2 * (ii - 1) + 1]
            S[ii + N] = Si(2 * ii)

        for ii in range(int(N)):

            if ii == N:
                S[ii + N] = S[ii + N] + a * (S[ii] + S[ii] + S[ii] - S[ii - 1])
            else:
                S[ii + N] = S[ii + N] + a * (S[ii] + S[ii + 1])

    return
