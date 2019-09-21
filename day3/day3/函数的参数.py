def hhh(name): #默认值参数
    print(name)

def op_file(file_name,content=None):
    if content:
        f = open(file_name,'w',encoding='utf-8')
        f.write(content)
    else:
        f = open(file_name,encoding='utf-8')
        return f.read()

def abc(name,age,phone,addr,money):
    print(name)
    print(age)
    print(phone)
    print(addr)
    print(money)
#abc('xiaohei',18,110,'beijing',9000)
#abc(age=18,addr='beijing',money=500,phone=111,name='111')
#abc('xiaobai',addr='123',phone=1111,money=11111,age=13)
# abc(age=13,'xiaohei')#这种传参方式是不对滴


file_name = 'users.json' #全局变量
def func():
    global file_name
    file_name = 'abc.json'
    print(file_name)
func()

print(file_name)

#常量
PI = 3.14
money = 500
def test(consume):
    return money - consume

def test1(money):
    return test(money) + money

money = test1(money)
print(money)




