#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-28 17:10:47
# @Author  : songpo.zhang (songpo.zhang@foxmail.com)
# @Link    : https://github.com/zspo
# @Version : $Id$

#python抓取携程酒店全国数据
import requests,urllib2,urllib,re,time
headers={
    "Host":"hotels.ctrip.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
}
quanguo_url="http://hotels.ctrip.com/domestic-city-hotel.html"
quanguo_html=requests.get(quanguo_url).content
quanguo_html=re.findall(' <div class="pinyin_filter">([\s\S]*?)<div id="base_ft">',quanguo_html)[0]
X=re.findall('<a title=".*?" href="/hotel/.*?(\d+)">(.*?)</a>',quanguo_html)
for Y in range(0,1096):#  共1096个城市
    # print '城市ID是：',X[Y][0],'   对应城市名称是：',X[Y][1]          # 前面是城市ID  后面是对应城市    共1096个城市

    url='http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'    # 抓包获取酒店信息url

    post_data={
        "cityId":X[Y][0],  #城市ID
        "page":"1",   #第几页

    }

    post_data=urllib.urlencode(post_data)
    req=urllib2.Request(url=url,data=post_data,headers=headers)
    html=urllib2.urlopen(req).read()
    html=re.findall('"totalMsg":([\s\S]*?)"}}}',html)[0]
    # print html

    jiudian_num=re.findall('"hotelAmount":(\d+),"sortHeader',html)[0] #酒店总数

    page_num=re.findall('data-pagecount=(\d+) name',html)[0]
    page_num=int(str(page_num))

    # print page_num   #总页数

    for num in range(1,page_num+1):
        post_data={

            "cityId":X[Y][0],  #城市ID
            "page":num,   #第几页
            }
        post_data=urllib.urlencode(post_data)
        req=urllib2.Request(url=url,data=post_data,headers=headers)
        html=urllib2.urlopen(req).read()
        html=re.findall('"totalMsg":([\s\S]*?)"}}}',html)[0]

        ids=re.findall(r'id=\\"(\d+)\\" data-index',html)   #URL ID列表

        print '当前抓取城市：',X[Y][1],'  城市ID是：',X[Y][0],'  总共',page_num,'页','合计',jiudian_num,'家酒店','  现在正在抓取第',num,'页的酒店数据'

        for id in ids:
            jiudian_url='http://hotels.ctrip.com/hotel/%s.html'%id  #拼接酒店详情页URL
            print '正在抓取',X[Y][1],'酒店','的URL是：',jiudian_url,' 10秒后抓取下一条'

            time.sleep(10)
