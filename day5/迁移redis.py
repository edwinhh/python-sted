import time

import redis
r = redis.Redis(host='118.24.3.40',password='HK139bc&*',port=6379,db=0,decode_responses=True)

#r2 = redis.Redis(host='118.24.3.40',password='HK139bc&*',port=6378,db=0,decode_responses=True)
#1、从aredis里面获取所有的key，
#2、判断key的类型
#3、根据key的类型，使用set /hset
#4、set到bredis里面

# for k in r.keys():
#     if r.type(k)=='string':
#         value = r.get(k)
#         r2.set(k,value)
#     if r.type(k)=='hash':
#         value = r.hgetall(k)
#         r2.hmset(k,value)#

#管道

l = range(500)
start_time = time.time()

pipeline = r.pipeline() #建立一个管道
for i in l:
    pipeline.set("key%s"%i,str(i))
    # r.set("key%s"%i,str(i))
pipeline.execute() #执行管道

print(time.time() - start_time)
