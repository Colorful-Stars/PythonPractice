#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Creat Time: 2017/12/9
 @ Auther: songpo.zhang
 @ Target:
"""

import time
import requests
from bs4 import BeautifulSoup


# num获取num页 国内高匿ip的网页中代理数据
def fetch_proxy(num):
    api = 'http://www.xicidaili.com/nn/'
    # header = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    #     (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    # }
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
    # 保存到本地文件
    fp = open('host.txt', 'w', encoding=('utf-8'))
    j = 0
    for i in range(num + 1):
        api = api + str(i)
        respones = requests.get(url=api, headers=header)
        soup = BeautifulSoup(respones.text, 'html.parser')
        container = soup.find_all(name='tr', attrs={'class': 'odd'})
        for tag in container:
            try:
                con_soup = BeautifulSoup(str(tag), 'html.parser')
                td_list = con_soup.find_all('td')
                ip = str(td_list[1])[4:-5]
                port = str(td_list[2])[4:-5]
                IPport = ip + '\t' + port + '\n'
                fp.write(IPport)
                j = j+1
                print("获取到第 {0} 个IP".format(j))
            except Exception as e:
                print('No IP！')
                # 这里要控制爬取频率，友好爬虫
        time.sleep(1)

    fp.close()

if __name__ == '__main__':
    fetch_proxy(10)