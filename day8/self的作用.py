class Person:
    country = 'China'

    def __init__(self,name):
        self.name = name
        print('内存地址',id(self))

    def say(self):
        print(self.name)


xm = Person('小明')
print('xm的内存地址',id(xm))
xm.say()

xh = Person("小红")
print('xh的内存地址',id(xh))
xh.say()