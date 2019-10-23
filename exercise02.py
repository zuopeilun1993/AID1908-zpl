"""
模拟注册过程

"""
import pymysql

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',  # 连接本地可以不写
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='stu',
                                  charset='utf8')

        # 生成游标对象(操作数据库，执行sql语句)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标与数据库连接
        self.cur.close()
        self.db.close()

    def register(self, name, password):
        sql = "select name from user where name=%s;"
        self.cur.execute(sql, [name])
        result = self.cur.fetchone()
        if result:
            print("该用户存在")
            return
        try:
            sql="insert into user (name,password) values(%s,%s);"
            self.cur.execute(sql,[name,password])
            self.db.commit()
        except Exception as e:
            # self.db.rollback()
            print(e)
if __name__ == '__main__':
    db=Database()
    db.register('gals','1964')
    db.close()

