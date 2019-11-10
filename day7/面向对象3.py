# class Student(object):
#     pass

class Person: #经典类
    #属性就是变量
    #功能就是函数
    country = 'China' #类变量
    base_price = 8000
    discount = 0.1

    def __del__(self):
        pass

    @staticmethod
    def help():
        print("这个类是造机器人的")

    @classmethod
    def getClassname(cls):
        print('Person')

    @classmethod
    def sayCountry(cls):
        #代表的本身这个类
        cls.getClassname()
        print(cls.country)

    def __init__(self,uid,name):
        print('self的内存地址:',id(self))
        self.id = uid #实例变量
        self.name = name #pep8

    def cook(self):
        print('%s鱼香肉丝'%self.name)

    def housework(self):
        print('%s正在做家务'%self.name)
        print('国籍是%s'%self.country)

    @property
    def price(self,):
        return self.base_price - self.base_price * self.discount




# Person.country = 'USA'
# Person.sayCountry()
# Person.help()

xh = Person(1,'小黑')  #__init__(xh,1,'小黑')
# xh.housework() #housework(xh)
# xh.housework()
# xh.sayCountry()
# xh.help()
# print(xh.country)
#
# xb = Person(2,'小白')
# xb.cook()
# xb.cook()
# print(xb.country)

import abc

class BaseCar(metaclass=abc.ABCMeta): #这个是一个抽象类，只是用来继承的
    def __init__(self,uid):
        self.uid = uid

    @abc.abstractmethod #如果抽象类里面的函数通过abstractmethod修饰，那就在子类里面必须实现
    def run(self):
        pass


class Bmw(BaseCar):
    def run(self):
        print('run')


m = Bmw('uid')
m.run()
