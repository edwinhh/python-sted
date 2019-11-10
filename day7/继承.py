#面向对象
    #1、封装
    #2、继承
class Lw:
    money = 500000
    def make_money(self):
        print('挣钱 50000')
    def __driver(self): #siy
        print('开车')

class Ll:
    def cook(self):
        print('做饭')
    def make_money(self):
        print('挣钱一万')

class Xw(Lw,Ll):
    def make_money(self): #重写
        print('挣钱')




# xw = Xw()
# # print(Xw.mro())
# print(xw.money)
# xw.make_money()
# xw.cook()
import abc

class BaseDb:
    def __init__(self,host,password,port,db):
        self.db_info = {'host':host,'password':password,
                        'port':port,'db':db}

    def connect(self):

        return ''

class MySql(BaseDb):
    # def __init__(self,host):
    #     self.db_info['autocommit'] = True

    #在父类的方法基础上做扩展

    def __init__(self,host,password,port,db,user,charset='utf8'):
        super().__init__(host,password,port,db)
        self.db_info['user'] = user
        self.db_info['charset'] = charset
        self.db_info['autocommit'] = True

    def connect(self):
        pass






