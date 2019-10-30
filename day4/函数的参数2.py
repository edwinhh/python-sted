def send_sms(*args):#可变参数，参数组
    print('phones',args)

def say(word,*args):
    print(word)
    print(args)
# say('nihao',123,138)

#关键字参数
def kwfunc(**kwargs):
    print(kwargs)

#kwfunc(age='123',name='小黑')

def t1(word,country='China',*args,**kwargs):
    print(word)
    print(country)
    print(args)
    print(kwargs)
#t1('哈哈','Japan',138,120,name='小和',addr='北京')
#t1('哈哈','Japan',138,120,name='小和',addr='北京')

def redis(ip,password,port=6379):
    print('连接redis')
    print(ip)
    print(port)
    print(password)
    print('='*10)
#redis_info = ['127.0.0.1','123456',1234]
#redis(redis_info[0],redis_info[1],redis_info[2])
#redis(*redis_info) #拆包
redis_info2 = {'ip':'127.0.0.1','password':'123456','port':1234}

#redis(redis_info2['ip'],redis_info2['password'],redis_info2['port'])
redis(**redis_info2)
# redis(ip='127.0.0.1',password='123456',port=1234)