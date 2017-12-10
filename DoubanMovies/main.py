#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 @ Creat Time: 2017/12/9
 @ Auther: songpo.zhang
 @ Target:
"""

import random
import time
import requests
from bs4 import BeautifulSoup
import pymysql



'''''
User-Agent
构建浏览器代理
'''
def getUA():
    UA_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; U; IntelMac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"]
    return UA_list


'''''
Cookie池

'''
def getCookie():
    cookie_list = [
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490333053.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334307.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334337.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334547.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334576.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=-2pPxf20f-A; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1490334617%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D6-V4k_jr0yx56VVthcFdBh1dsEw-fM_VidsCvjvnZDu%26wd%3D%26eqid%3Ddb5853390004c0f20000000258d4b38f%22%5D; _pk_id.100001.8cb4=cd9595388e4feada.1490334617.1.1490334617.1490334617.; _pk_ses.100001.8cb4=*; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.1.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334690.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334724.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334758.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334785.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        '__utmc=30149280; ll=118237; bid=BpRkUyl8224; __utma=30149280.2117353028.1490334856.1490334856.1490334856.1; __utmb=30149280.1.10.1490334856; __utmz=30149280.1490334856.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _vwo_uuid_v2=3DE3A5524E7D8D0F707D6C9AEB95A43B|da39a7ae190f4c2de62535e9911c57a6; __utma=223695111.747047863.1490334857.1490334857.1490334857.1; __utmb=223695111.0.10.1490334857; __utmc=223695111; __utmz=223695111.1490334857.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334858%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=0025ca3c57b38c6f.1490334858.1.1490334858.1490334858.; _pk_ses.100001.4cf6=*',
        '__utmc=30149280; ll=118237; bid=BpRkUyl8224; __utma=30149280.2117353028.1490334856.1490334856.1490334856.1; __utmb=30149280.1.10.1490334856; __utmz=30149280.1490334856.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _vwo_uuid_v2=3DE3A5524E7D8D0F707D6C9AEB95A43B|da39a7ae190f4c2de62535e9911c57a6; __utma=223695111.747047863.1490334857.1490334857.1490334857.1; __utmb=223695111.0.10.1490334857; __utmc=223695111; __utmz=223695111.1490334857.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334858%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=0025ca3c57b38c6f.1490334858.1.1490334918.1490334858.; _pk_ses.100001.4cf6=*']

    return cookie_list


'''''
构建代理IP池
'''
def proxypool(num):
    n = 1
    # os.chdir(r'/Users/apple888/PycharmProjects/proxy IP')
    fp = open('host.txt', 'r')
    proxys = list()
    ips = fp.readlines()
    while n < num:
        for p in ips:
            ip = p.strip('\n').split('\t')
            proxy = 'https://' + ip[0] + ':' + ip[1]
            proxies = {'http': proxy}
            # print(proxies)
            proxys.append(proxies)
            n += 1
    return proxys


''''' 
getMoviePakge() 
此函数用于获取电影列表页面的url链接 
返回值为列表pakge_urls 
'''
def getMoviePakge():
    pakge_urls = []
    for i in range(0, 7781, 20):
        url = 'https://movie.douban.com/tag/%E7%88%B1%E6%83%85?start=' + str(i) + '&type=T'
        # print(url)
        pakge_urls.append(url)
    return pakge_urls


''''' 
getMovieUrls() 
此函数用于获取电影的链接用于后面的信息的访问url入口 
返回一个列表，里面存储着电影链接 
'''
def getMovieUrls(pakgeurl, cookie, userAgent, proxys):
    movie_urls = []
    time.sleep(random.uniform(1.6, 2.1))
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': random.choice(cookie),
               'Host': 'movie.douban.com',
               'Referer': 'https://movie.douban.com/tag/',
               'User-Agent': random.choice(userAgent)}

    session = requests.Session()
    html = session.get(pakgeurl, headers=headers, proxies=random.choice(proxys))
    obj_bs = BeautifulSoup(html.text, 'html.parser')
    # 获取带有电影链接的html段
    movie_html = list(obj_bs.findAll("div", {"class": "pl2"}))
    for each_movie in movie_html:
        # 获取电影介绍的链接
        movie_url = each_movie.select('a')[0]['href']
        # print(movie_url)
        movie_urls.append(movie_url)
    return movie_urls


'''

'''

def getMovieData(movieurl, cookie, userAgent, proxys):
    global x
    time.sleep(random.uniform(1.6, 2.1))
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': random.choice(cookie),
               'Host': 'movie.douban.com',
               'Referer': 'https://movie.douban.com/tag/',
               'User-Agent': random.choice(userAgent)}

    moviename = '无'
    director = '无'
    screenwriter = '无'
    actor_name = '无'
    summary = '无'
    leixing = '无'
    country = '无'
    language = '无'
    showtime = '无'
    runtime = '无'
    people = 0
    grade = 0
    thismovieurl = '无'

    try:
        session = requests.Session()
        html = session.get(movieurl, headers=headers, proxies=random.choice(proxys))
        obj_bs = BeautifulSoup(html.text, 'html.parser')
        print(x)

        # 获取电影名字

        soup_movname = obj_bs.find("span", {"property": "v:itemreviewed"})
        moviename = soup_movname.get_text()
        print('电影名字：', moviename)

        # 获取电影导演的名字


        director = obj_bs.find("a", {"rel": "v:directedBy"}).get_text()
        print('导演：' + director)

        # 获取电影编剧名字

        soup_scenarist = list(obj_bs.findAll("span", {"class": "pl"})[1].next_siblings)[1:]
        screenwriter = ''
        for scenarist in soup_scenarist:
            scenarist_name = scenarist.select("a")
            for bianju in scenarist_name:
                screenwriter = screenwriter + bianju.get_text() + '/'
        print('编剧：' + screenwriter)


        # 获取主演的名字
        # 将所有演员名字变成字符串，便于存储入数据库
        soup_actor = obj_bs.find("span", {"class": "actor"}).find("span", {"class": "attrs"}).findAll("a")
        actor_name = ''
        for actor in soup_actor:
            # print(actor.get_text())
            actor_name = actor_name + actor.get_text() + '/'
        print('主演：' + actor_name)

        # 获取电影简介
        soup_summary = obj_bs.find("span", {"property": "v:summary"})
        summary = soup_summary.get_text()
        print('电影简介： ' + summary)

        # 获取电影类型

        soup_type = obj_bs.findAll("span", {"property": "v:genre"})
        leixing = ''
        for type_moive in soup_type:
            leixing = leixing + type_moive.get_text() + '/'
        print('类型：' + leixing)

        # 获取电影的制片国家
        # 这个比较有难度

        country = list(obj_bs.findAll("span", {"class": "pl"})[4].next_siblings)[0]
        print('制片国家：' + country)

        # 语言

        language = list(obj_bs.findAll("span", {"class": "pl"})[5].next_siblings)[0]
        print('语言：' + language)

        # 上映日期

        soup_showtime = obj_bs.find("span", {"property": "v:initialReleaseDate"})
        if soup_showtime != None:
            showtime = soup_showtime.get_text()
            print('上映日期：' + showtime)

        # 电影时长

        soup_runtime = obj_bs.find("span", {"property": "v:runtime"})
        if soup_runtime != None:
            runtime = soup_runtime.get_text()
            print("时长：" + runtime)


         # 电影的评价人数
        soup_people = obj_bs.find("span", {"property": "v:votes"})
        if soup_people != None:
            people = int(soup_people.get_text())
            print('评论人数：', people)

        # 豆瓣评分
        # float类型的grade表示分数

        soup_grade = obj_bs.find("strong", {"class": "ll rating_num"})
        if soup_grade != None:
            grade = float(soup_grade.get_text())
            print('评分：', grade)

        thismovieurl = movieurl
        print(thismovieurl)

        cur.execute(
            "INSERT INTO love(moviename, director, screenwriter, actor_name, summary, leixing, country, language, showtime,runtime, people, grade, thismovieurl)\
             VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')"\
            %(moviename, director, screenwriter, actor_name, summary, leixing, country, language, showtime, runtime, people, grade, thismovieurl)
            )
        connect.commit()
    except:
        print('************此条爬取有问题************')
    x = x + 1


'''
运行函数 
'''
start = time.clock()
x = 1
connect = pymysql.connect("localhost", "root", "782575191", "doubanmovie", charset="utf8")
cur = connect.cursor()
for pakgeurl in getMoviePakge():
    for movieurl in getMovieUrls(pakgeurl, getCookie(), getUA(), proxypool(150)):
        getMovieData(movieurl, getCookie(), getUA(), proxypool(150))
        print('《=========================*********==============================》')
cur.close()
connect.close()
end = time.clock()
print('获取到 {} 个电影的数据，共用时 {:.2f} s'.format(x,(end - start)))