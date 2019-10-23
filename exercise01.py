import pymysql
import re

db=pymysql.connect(host='localhost',#连接本地可以不写
                   port=3306,
                   user='root',
                   password='123456',
                   database='dict',
                   charset='utf8')

# 生成游标对象(操作数据库，执行sql语句)
cur=db.cursor()
f=open('dict.txt')


# 执行数据库的写操作

exe=[]

for line in f:
    tup=re.findall(r'(\S+)\s+(.*)',line)[0]
    print(tup)
    exe.append(tup)
f.close()
sql="insert into dictionary (word,mean) values (%s,%s);"

try:
    cur.executemany(sql,exe)
    db.commit()

except Exception as e:
    db.rollback()
    print(e)
# # 关闭游标与数据库连接
cur.close()
db.close()
