#-*- coding: UTF-8 -*-
import pymysql

#打开数据库连接
connect = pymysql.connect("localhost", "root", "782575191", "doubanmovie",charset="utf8")
#使用cursor()方法创建一个游标对象
cur = connect.cursor()
moviename = '无'
director = '无'
screenwriter = '无'
actor_name = '无'
summary = '无'
leixing = '无'
soup_country = '无'
soup_language = '无'
showtime = '无'
runtime = '无'
people = 0
grade = 0
thismovieurl = '无'
cur.execute(
            "INSERT INTO love(moviename, director, screenwriter, actor_name, summary, leixing, soup_country, soup_language, showtime, runtime, people, grade, thismovieurl)\
             VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')"\
            %(moviename, director, screenwriter, actor_name, summary, leixing, soup_country, soup_language, showtime, runtime, people, grade, thismovieurl)
            )
connect.commit()
cur.close()
connect.close()

#SQL插入语句
