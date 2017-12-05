#!/usr/bin/env python
# -*- coding = utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import traceback

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst, stockUrl):
    html = getHTMLText(stockUrl)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

def getStockInfo(lst, stockUrl, filePath):
    count = 0
    for stock in lst:
        url = stockUrl + stock + ".html"
        html = getHTMLText(url)
        try:
            if html==" ":
                continue
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            infoDict = {}
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value

            with open(filePath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end="")
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'F:/BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()