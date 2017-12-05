#!/usr/bin/env python
# -*- coding = utf-8 -*-

import requests
from bs4 import BeautifulSoup
import bs4
import re

def getHtml(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def infoSave(url, fpath):
    html = getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find('div', attrs={'class':'list'})

    # temp = info.decode('utf8')
    print(info)
    # xx = u"([/u4e00-/u9fa5]+)"
    # z = re.compile(xx)
    # a = z.findall(temp)
    # for i in a:
    #     print(i)
    # with open(fpath, 'a', encoding='utf-8') as f:
    #     f.write(str(list) + '\n')

def main():
    url = "http://www.cndzys.com/shicai/roulei/"
    output_file = 'roulei.txt'
    infoSave(url, output_file)

main()
