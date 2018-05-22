#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-22 15:45:18
# @Author  : songpo.zhang (songpo.zhang@foxmail.com)
# @Link    : https://github.com/zspo
# @Version : $Id$

def read_data(file_path):
    reader = pd.read_csv(file_path, header=None, encoding='gbk', iterator=True)
    loop = True
    chunkSize = 1000
    chunks = []
    while loop:
        try:
            chunk = reader.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    df = pd.concat(chunks, ignore_index=True)
    return df.values
