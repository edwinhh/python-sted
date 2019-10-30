import os,time,datetime,random

#1、写一个清理日志的程序，把三天前的日志和为空的日志都删掉

def str_to_timestamp(string=None,format='%Y-%m-%d %H:%M:%S'):
    '''格式化好的字符串转时间戳，默认返回当前时间戳'''
    if string:
        time_tuple = time.strptime(string, format)  # 格式化好的时间，转时间元组的
        result = time.mktime(time_tuple)  # 把时间元组转成时间戳
    else:
        result = time.time()
    return int(result)

path=r'D:\python sted\day4\logs'

def get_logtimestamp(file):
    name=file.split('.')[0]
    time1=name.split('_')[1]
    timestamp1=str_to_timestamp(time1,format='%Y-%m-%d')
    return timestamp1

def getfilesize(file):
    size=os.path.getsize(file)
    if size:
        return 1
    else:
        return 0

def interval_time(file,t):
    t1=get_logtimestamp(file)
    t2=str_to_timestamp(time.strftime('%Y-%m-%d'),format='%Y-%m-%d')
    if t2-t1>int(t):
        return 1
    else:
        return 0

def check_logs(dir,t):
    for cur_dir,dirs,files in os.walk(path):
        for file in files:
            if interval_time(file,t) or not getfilesize(os.path.join(cur_dir,file)):
                print(file)
                os.remove(os.path.join(cur_dir, file))


t=60*60*24*3
# check_logs(path,t)


#写一个生成大乐透号码的程序

def suiji(k,n,m):
    a = []
    for i in range(k):
        while(1):
            front = random.sample(range(n, m), 1)
            if front[0] not in a:
                a.append(front[0])
                break
    a1 = sorted(a)
    a2=[str(i) for i in a1]
    for i in range(len(a2)):
        if len(a2[i])==1:
            a2[i]='0'+a2[i]

    return a2

def daletou():
    a1=suiji(5,1,35)
    b1=suiji(2, 1, 12)
    with open("大乐透.txt",'a+',encoding='utf-8') as f:
        a=[','.join(str(i) for i in a1)]
        b = [','.join(str(i) for i in b1)]
        f.write(a[0])
        f.write('  ')
        f.write(b[0])
        f.write('\n')






for i in range(100):
    daletou()

