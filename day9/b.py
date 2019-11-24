class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        print(args)
        if cls.instance:
            return cls.instance
        cls.instance = super().__new__(cls)  #
        return cls.instance


import pymysql
from utils.mysql_util import mysql
r = mysql.execute_one('select * from litemall_address where id = 80;')
print(r)