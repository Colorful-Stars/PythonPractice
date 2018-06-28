#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-28 21:59:30
# @Author  : songpo.zhang (songpo.zhang@foxmail.com)
# @Link    : https://github.com/zspo
# @Version : $Id$

import pandas as pd

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
