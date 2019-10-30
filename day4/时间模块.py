import time,datetime
#2019-10-19 13:23:38
#13245232453
#时间戳 一串数字
#从计算机诞生那一秒到现在过了多少秒

# print(time.time()) #获取前时间戳
# print(time.strftime('%Y-%m-%d %H:%M:%S'))#当前格式化好的时间

#时间元组

#1、时间戳转格式化的时间

timestamp = 1571476513
# time_tuple = time.gmtime(timestamp)#以标准时区的时间转换
time_tuple = time.localtime(timestamp)#以当前时区的时间转换
result = time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)

def timestamp_to_str(timestamp=None,format='%Y-%m-%d %H:%M:%S'):
    '''时间戳转格式化好的时间，默认返回当前时间'''
    if timestamp:
        time_tuple = time.localtime(timestamp)  # 以当前时区的时间转换
        result = time.strftime(format,time_tuple)
    else:
        result = time.strftime(format)
    return result

def str_to_timestamp(string=None,format='%Y-%m-%d %H:%M:%S'):
    '''格式化好的字符串转时间戳，默认返回当前时间戳'''
    if string:
        time_tuple = time.strptime(string, format)  # 格式化好的时间，转时间元组的
        result = time.mktime(time_tuple)  # 把时间元组转成时间戳
    else:
        result = time.time()
    return int(result)

# s = '2019-10-19 17:15:13'
# time_tuple = time.strptime(s,'%Y-%m-%d %H:%M:%S')#格式化好的时间，转时间元组的
# result = time.mktime(time_tuple)#把时间元组转成时间戳
# print(result)

t1 = str_to_timestamp() + 60*60*24*13
