#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-03 10:36:56
# @Author  : songpo.zhang (songpo.zhang@foxmail.com)
# @Link    : https://github.com/zspo
# @Version : $Id$


import os

def eachFile(filepath):
    pathDir = os.listdir(filepath)      #获取当前路径下的文件名，返回List
    for s in pathDir:
        newDir=os.path.join(filepath,s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(newDir) :         #如果是文件
            if os.path.splitext(newDir)[1]==".txt":  #判断是否是txt
                readFile(newDir)                     #读文件
                pass
        else:
            eachFile(newDir)                #如果不是文件，递归这个文件夹的路径
