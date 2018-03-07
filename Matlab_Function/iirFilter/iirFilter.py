#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Create Time: 2018/3/6
 @ Author: songpo.zhang
 @ Target: iirFilter
        This IIR filter is used for light raw data only
        This filter will filter all the raw data because all raw data will
        input to the function. This is not same as actual system
"""
import numpy as np

def iirFilter(rawData):
    numerator = [
                 0.773838953566480,
                 - 3.86919476783240,
                 7.73838953566480,
                 - 7.73838953566480,
                 3.86919476783240,
                 - 0.773838953566480
                 ]

    denominator = [
                   1,
                   - 4.48803366687931,
                   8.08074931273576,
                   - 7.29452405497775,
                   3.30071275348357,
                   - 0.598826726050982
                   ]

    L = len(numerator)
    Ls = len(rawData)

    iir_cx = np.ones(L)    # Initialize the filter
    iir_cy = np.ones(L)
    iirData = np.zeros(Ls)

    for ii in range(Ls):
        for jj in range(L - 2, -1, -1):
            iir_cx[jj + 1] = iir_cx[jj]
            iir_cy[jj + 1] = iir_cy[jj]

        iir_cx[0] = rawData[ii]
        iir_cy[0] = sum(numerator * iir_cx) - sum(denominator[1:]*iir_cy[1:])
        iir_cy[0] = iir_cy[0] / denominator[0]
        iirData[ii] = iir_cy[0]

    return iirData
