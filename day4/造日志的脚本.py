def timestamp_to_str(timestamp=None,format='%Y-%m-%d %H:%M:%S'):
    '''时间戳转格式化好的时间，如果没有传时间戳，就获取当前的格式化时间'''
    if timestamp:
        time_tuple = time.localtime(timestamp) #把时间戳转成时间元组
        result = time.strftime(format,time_tuple) #把时间元组转成格式化好的时间
        return result
    else:
        return time.strftime(format)


import time,os,random
l = ['ios','android','nginx','tomcat','python','blog','apache','mysql','redis']
for i in l:
    p = os.path.join('logs',i)
    os.makedirs(p)
    for j in range(30):
        t = int(time.time())-86400*j
        time_str = timestamp_to_str(t,'%Y-%m-%d')
        log_name = '%s_%s.log'%(i,time_str)
        abs_file_path = os.path.join('logs',i,log_name)
        fw = open(abs_file_path, 'w', encoding='utf-8')
        if random.randint(1,10)%2==0:
            fw.write('胜多负少防守打法双方都')
        fw.close()