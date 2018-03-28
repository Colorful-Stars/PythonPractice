#!/usr/bin/env python
# -*- coding = utf-8 -*-
from numpy import std, sqrt, mean
import matplotlib.pyplot as plt
import math
from scipy.fftpack import fft

file_path = "RRI.txt"

def read_data(file_path):
    Raw_RRI_data = []
    with open('RRI.txt') as file:
        for line in file:
            line = line.strip('\n')
            Raw_RRI_data.append(float(line))
        return Raw_RRI_data

# win_length = 12*60 
# step = 30
# def process_data_in_time(raw_data):
#     SDNN = []
#     SDSD = []
#     rMSSD = []
#     diff_data = []
#     for i in range(0, len(raw_data), step):
#         win_data = raw_data[i:i+win_length]
#         SDNN.append(std(win_data))

#         sum_diff = 0
#         for j in range(len(win_data)-1):
#             diff = win_data[j+1] - win_data[j]
#             sum_diff += diff*diff
#             diff_data.append(diff)
#         rMSSD.append(sqrt(sum_diff/len(diff_data)))
#         SDSD.append(std(diff_data))

#     return SDNN, rMSSD, SDSD

raw_data = read_data(file_path)
fftdata = raw_data-mean(raw_data)
L = len(fftdata)
temp=fft(fftdata,L)
# A = abs(temp)/(L/2)
# A[1] = A[1]/2

f = [i/L for i in range(L)]
plt.plot(f[:int(L/2)],temp[:int(L/2)])
plt.show()




# SDNN, SDSD, rMSSD= process_data(raw_data)
# print(SDNN)
# print('\n')
# print(SDSD)
# print('\n')
# print(rMSSD)
# plt.plot(SDNN)
# plt.plot(SDSD)
# plt.plot(rMSSD)
# plt.show()



# def process_data_in_fre(raw_data):
#     raw_data=raw_data[5:]
#     fre_data = fft(raw_data)
#     # if fre_data>1000:
#     #     fre_data=0
#     return fre_data


# fre_data = process_data_in_fre(raw_data)
# print(fre_data)
# # plt.plot(raw_data,'*')
# plt.plot(fre_data[1:])
# plt.show()

