
import pymysql

db=pymysql.connect(host='localhost',#连接本地可以不写
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')

# 生成游标对象(操作数据库，执行sql语句)
cur=db.cursor()

# 存储图片
with open("springs.jpg",'rb') as f:
    data=f.read()
try:
    sql="insert into image values(1,%s,%s);"
    cur.execute(sql,['springs.jpg',data])
    db.commit()
except Exception:
    db.rollback()

# 关闭游标与数据库连接

cur.close()
db.close()
