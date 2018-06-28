#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-28 21:59:30
# @Author  : songpo.zhang (songpo.zhang@foxmail.com)
# @Link    : https://github.com/zspo
# @Version : $Id$

import pandas as pd


# 
def get_chunck_data(path, chunkSize):
    loop = True
    # chunkSize = 100000
    chunks = []

    reader = pd.read_csv(path, iterator=True)
    while loop:
        try:
            chunk = reader.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    df = pd.concat(chunks, ignore_index=True)
    print("chunk data done !")
    return df

######################################################
# 解决chunk切割带来的风险
# 针对DF_pingan赛

for data in pd.read_csv(path_data, chunksize=chunksize):
    # 取出块中最有一个TerminalNo
    last_terminal_no = data.tail(1)['TERMINALNO'].values[0]
    # 取出块中除了最后一个TermianlNo的其他数据
    data_chuck = data[data.TERMINALNO != last_terminal_no].copy()

    # 拼接数据上次遗留的数据
    if i > 0:
        data_chuck = pd.concat([re_pd, data_chuck])
    # 保存最后一个TerminalNo，下次使用
    re_pd = data[data.TERMINALNO == last_terminal_no].copy()

    # 数据处理
    preprocess_data_chunk(data_chuck)
    i += 1

# 最后一个TerminalNo
preprocess_data_chunk(re_pd)
######################################################
