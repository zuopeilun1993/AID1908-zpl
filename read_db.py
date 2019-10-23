"""

read_db.py
pymysql 读操作演示


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

name=input("Name:")
sql="select * from class_1 where name='%s';"%name
cur.execute(sql)
# 执行数据库的读操作
# for i in cur:
#     print(i)

#获取一个查询结果
one_row=cur.fetchone()
print(one_row)

#获取前2个查询结果
# many_row=cur.fetchmany(2)
# print(many_row)


#获取所有查询结果
# all_row=cur.fetchall()
# print(all_row)

# 关闭游标与数据库连接
cur.close()
db.close()
