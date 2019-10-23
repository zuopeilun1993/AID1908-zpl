import pymysql

db=pymysql.connect(host='localhost',#连接本地可以不写
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')

# 生成游标对象(操作数据库，执行sql语句)
cur=db.cursor()
sql="select filename,img from image where filename='springs.jpg';"
cur.execute(sql)
data=cur.fetchone()
with open(data[0],'wb') as f:
    f.write(data[1])
cur.close()
db.close()
