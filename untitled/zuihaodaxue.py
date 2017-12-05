#!/usr/bin/env python
# -*- coding = utf-8 -*-

import requests
from bs4 import BeautifulSoup
import bs4

def getHTML(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            td = tr('td')
            ulist.append([td[0].string, td[1].string, td[3].string])

def printUnivList(ulist, num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    print(tplt.format('排名', '大学名称', '总分', chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    ls = []
    url = 'http://rankings.betteredu.net/qs/world-university-rankings/latest/2016-2017.html'
    html = getHTML(url)
    fillUnivList(ls, html)
    printUnivList(ls, 20)
main()

