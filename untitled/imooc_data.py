#!/usr/bin/env python
# -*- coding = utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pymysql.cursors


resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")

soup = BeautifulSoup(resp,"html.parser")

listUrls = soup.findAll("a", href=re.compile("^/wiki/"))

for url in listUrls:
    if not re.search("\.(jpg|JPG)$",url["href"]):
        print(url.get_text()," <------> ","https://en.wikipedia.org" + url["href"])
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='782575191',
                             db='wikiurl',
                             charset='utf8mb4')
        try:
            with connection.cursor() as cursor:
                sql = "insert into `urls`(`urlname`,`urlhref`)values(%s,%s)"

                cursor.execute(sql,(url.get_text(),"https://en.wikipedia.org"+url["href"]))

                connection.commit()
        finally:
            connection.close()