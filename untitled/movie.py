#-*- coding:utf-8 -*-
# vim: set fileencoding=utf-8:
'''

Created on 2013��11��26��

@author: NotHinG
'''
import urllib
import urllib2
import re
import time
import pymongo

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
conn=pymongo.Connection('localhost',27017)
db=conn.douban

user=db["user"]
movieC=db['movie']

data=user.find()
movie=[]
for temp in data:
    m=temp['movie']
    for i in m:
        Id=i['id']
        if Id not in movie:
            movie.append(Id)
count=0
for Id in movie:
    try:
        url='http://movie.douban.com/subject/%s/' % Id
        req=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(req)
        html=response.read()   #读取完毕
        time.sleep(2)           #休眠2秒

        film={'id':Id}
    
        #电影名
        reg=re.compile(r'<span property="v:itemreviewed">(.*?)</span>',re.S)
        content=re.findall(reg,html)
        film['title']=content[0]
        #电影名

        #导演
        reg=re.compile(r'<span><span class=\'pl\'>导演</span>: (.*?)</span><br/>',re.S)
        content=re.findall(reg,html)
        if len(content)>0:
            s=content[0]
            reg=re.compile(r'<a href="/celebrity/(.*?)/" rel="v:directedBy">(.*?)</a>',re.S)
            content=re.findall(reg,s)
            film['director']=content
        else:
            film['director']=[]
        #导演
    
        #编剧
        reg=re.compile(r'<span><span class=\'pl\'>编剧</span>: (.*?)</span><br/>',re.S)
        content=re.findall(reg,html)
        if len(content)>0:
            s=content[0]
            reg=re.compile(r'<a href="/celebrity/(.*?)/">(.*?)</a>',re.S)
            content=re.findall(reg,s)
            film['playwriter']=content
        else:
            film['playwriter']=[]
        #编剧
    
        #主演
        reg=re.compile(r'<span><span class=\'pl\'>主演</span>: (.*?)</span><br/>',re.S)
        content=re.findall(reg,html)
        if len(content)>0:
            s=content[0]
            reg=re.compile(r'<a href="/celebrity/(.*?)/" rel="v:starring">(.*?)</a>',re.S)
            content=re.findall(reg,s)
            film['starring']=content
        else:
            film['starring']=[]
        #主演
    
        #类型、tag
        reg=re.compile(r'<span class="pl">类型:</span> (.*?)<br/>',re.S)
        content=re.findall(reg,html)
        if len(content)>0:
            s=content[0]
            reg=re.compile(r'<span property="v:genre">(.*?)</span>',re.S)
            content=re.findall(reg,s)
            film['genre']=content
        else:
            film['genre']=[]
        #类型、tag
    
        #制片地区
        reg=re.compile(r'<span class="pl">制片国家/地区:</span>(.*?)<br/>',re.S)
        content=re.findall(reg,html)
        if len(content)>0:
            film['region']=content[0]
        else:
            film['region']=''
        #制片地区
    
        #评分
        reg=re.compile(r'<strong class="ll rating_num" property="v:average">(.*?)</strong>',re.S)
        content=re.findall(reg,html)
        if len(content)>0:
            film['rating']=content[0]
        else:
            film['rating']=''
        #评分

        #简介
        reg=re.compile(r'<span property="v:summary" class="">(.*?)</span>',re.S)
        content=re.findall(reg,html)
        s=''
        if len(content)>0:
            s=content[0]
        else:
            reg=re.compile(r'<span class="all hidden">(.*?)</span>',re.S)
            content=re.findall(reg,html)
            if len(content)>0:
                s=content[0]
        reg=re.compile('<br />')
        s=reg.sub('',s)
        s=s.strip().replace('\t','').replace('\n','').replace(' ','')
        film['summary']=s      
        #简介

        #插入数据库
        count+=1
        movieC.insert(film)
        print(count)
        print(Id)
    except:
        print('null:%s' %Id)
print('End')
