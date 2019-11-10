class Person:
    def __init__(self):
        self.__base_price = 8000
        print('构造函数')
    def __del__(self):
        print('析构函数')
    def say(self):
        print('say')
    def set_price(self,discount):
        self.__base_price = self.__base_price - self.__base_price * discount
    def get_price(self):
        return self.__base_price

xh = Person()
