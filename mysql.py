"""
mysql.py
db = pymysql.connect(参数列表)
host ：主机地址,本地 localhost
port ：端口号,默认3306
user ：用户名
password ：密码
database ：库
charset ：编码方式,推荐使用 utf8
数据库连接对象(db)的方法
cur = db.cursor() 返回游标对象,用于执行具体SQL命令
db.commit() 提交到数据库执行
db.rollback() 回滚，用于当commit()出错是回复到原来的数据形态
db.close() 关闭连接
2019/10/21 Mysql
file:///C:/Users/lvze/Desktop/备课/课程下发/MySQL/Mysql.html 45/45
游标对象(cur)的方法
"""
import pymysql

db=pymysql.connect(host='localhost',#连接本地可以不写
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')

# 生成游标对象(操作数据库，执行sql语句)
cur=db.cursor()

# 执行各种数据库的读写操作
cur.execute()

# 关闭游标与数据库连接
cur.close()
db.close()




























