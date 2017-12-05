#!/usr/bin/env python
# -*- coding = utf-8 -*-

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='782575191',
                             db='wikiurl',
                             charset='utf8mb4')

try:
    with connection.cursor() as cursor:
        sql = "select `urlname`,`urlhref` from `urls` where `id` is not null"
        count = cursor.execute(sql)
        print(count)

        result = cursor.fetchmany(size=3)
#       result = cursor.fetchall()
        print(result)
finally:
    connection.close()