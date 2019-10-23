"""

write_db.py

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

# 执行数据库的写操作
try:
    exe=[]
    for i in range(3):
        name=input("Name:")
        age=int(input('Age:'))
        score=float(input("Score:"))
        #执行增，删，改等语句
        exe.append((name,age,score))
    sql="insert into class_1 (name,age,score) values (%s,%s,%s);"

    # sql="update class_1 set sex='m' where name='Dave';"
    # sql="delete from class_1 where name='Dave';"
    cur.execute(sql,exe)
    db.commit()

except Exception as e:
    db.rollback()

    print(e)
# 关闭游标与数据库连接
cur.close()
db.close()



