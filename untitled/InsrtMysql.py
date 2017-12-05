import pymysql

#打开数据库连接
db = pymysql.connect("localhost","root","782575191","test")
#使用cursor()方法创建一个游标对象
cursor = db.cursor()

#SQL插入语句
sql = """INSERT INTO user(id,name)
		VALUES ('2','Mac')"""

try:
	#执行sql语句
	cursor.execute(sql)
	#提交到数据库执行
	db.commit()
except:
	#如果发生错误则回滚
	db.rollback()

#关闭数据库连接
db.close()