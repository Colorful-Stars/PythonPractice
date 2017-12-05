import pymysql
#打开数据库连接
db = pymysql.connect("localhost","root","782575191","test")
#使用cursor()方法创建一个游标对象
cursor = db.cursor()

sql = "SELECT * FROM user"

try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for arr in results:
		id = arr[0]
		name = arr[1]
		print("id = %s, name = %s" % (id, name))
except:
	print("Error: unable to fetch data")

db.close