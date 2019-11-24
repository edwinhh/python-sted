import pymysql
from config.setting import mysql_info
from .utils import Singleton
class Mysql(Singleton):
    def __init__(self,host,user,password,db,port=3306,charset='utf8'):
        #构造函数，类在实例化的时候会自动执行构造函数
        self.db_info = {'user':user,'password':password,"db":db,"port":port,'charset':charset,
                        'autocommit':True,'host':host}
        self.__connect()
    def __del__(self):
        self.__close()

    def __connect(self):
        try:
            self.conn = pymysql.connect(**self.db_info)  # 建立连接
        except Exception as e:
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




mysql = Mysql(**mysql_info)