import redis

#关系型数据库
#mysql  oracle sqlserver、sqlite


#非关系型数据库  NoSQL
#   mongodb
#   redis 每秒钟达到10w次的读写，存在内存里面
r = redis.Redis(host='118.24.3.40',password='HK139bc&*',port=6379,db=0,decode_responses=True)

r2 = redis.Redis(host='118.24.3.40',password='HK139bc&*',port=6378,db=0,decode_responses=True)

#字符串
# r.set('mjz_students','{"msg":"sdfsdfsd"}')
# info = r.get('mjz_students')
# r.expire('dabaobao',30)#设置失效时间
# r.delete('mjz_students')
# r.set('mjz_students','{"msg":"sdfsdfsd"}')

#哈希类型

r.hset("students",'wyj','{"money":500,"addr":"北京"}')
r.hset("students",'cj','{"money":500,"addr":"上海"}')
r.hset("students",'dcg','{"money":502,"addr":"北京"}')
r.hset("students",'wn','{"money":502,"addr":"北京"}')
r.hset("students",'wyj','{"money":502,"addr":"北京"}')

# r.hdel("students",'wyj')#删除
# print(r.hget("students","wn"))
# print(r.hgetall('students')) #获取所有的

d = {'qxh':'sfdsdfsf','liuying':'liy001'}
r.hmset('students',d)

#r.flushall() #清空所有数据库的所有内容
#r.flushdb() #清空当前数据库里面的数据
#r.exists('name') #判断key是否存在
# r.keys() #获取当前数据库所有的key
# r.type('name') #获取的key的类型

#1、从aredis里面获取所有的key，
#2、判断key的类型
#3、根据key的类型，使用set /hset
#4、set到bredis里面