#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Creat Time: 2017/12/9
 @ Auther: songpo.zhang
 @ Target: 构建代理IP池，将本地读取到的txt中的IP读到一个列表中
"""
def proxypool(num):
    n = 1
    #os.chdir(r'/Users/apple888/PycharmProjects/proxy IP')
    fp = open('host.txt', 'r')
    proxys = list()
    ips = fp.readlines()
    while n<num:
        for p in ips:
            ip = p.strip('\n').split('\t')
            proxy = 'https://' + ip[0] + ':' + ip[1]
            proxies = {'http': proxy}
            #print(proxies)
            proxys.append(proxies)
            n+=1
    return proxys