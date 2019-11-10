class Car:

    
    def run(self):
        print("跑")

    def driver(self,name):
        print("%s在开车"%name)

# bmw = Car() #实例化
# #bmw 实例
# 
# bmw.run()
# bmw.driver("王庆柱")
import pymysql
class Db:
    #
    def __init__(self,host,user,password,db,port=3306,charset='utf8'):
        #构造函数，类在实例化的时候会自动执行构造函数
        self.db_info = {'user':user,'password':password,"db":db,"port":port,'charset':charset,
                        'autocommit':True,'host':host}
        self.__connect()
    def __del__(self):
        self.__close()
        print('关闭数据库')

    def __connect(self):
        try:
            self.conn = pymysql.connect(**self.db_info)  # 建立连接
        except Exception as e:
            print("连接不上数据库")
            raise Exception("连接不上数据库,请检查数据库连接信息")

        else:
            self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def execute_many(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def execute_one(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def __close(self):
        self.conn.close()
        self.cur.close()

    def export_excel(self,table_name):
        pass



mysql = Db('118.24.3.40','jxz','123456','jxz')
result = mysql.execute_one('select * from app_myuser;')
result = mysql.execute_one('select * from app_myuser;')
result = mysql.execute_one('select * from app_myuser;')
result = mysql.execute_one('select * from app_myuser;')
