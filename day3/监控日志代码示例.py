#1、监控服务器日志，找出每分钟访问超过100次的ip地址
#分析：
    #1、读取文件，获取到文件里面的所有ip地址
    #2、把ip地址存起来,用字典存，key是ip地址，value是次数
    #3、循环字典，判断value大于100的

import time
point = 0
while True:
    ips = {}  # 存放所有的ip地址以及它出现的次数
    f = open('access.log')
    f.seek(point)
    for line in f:
        if line.strip()!='':#判断不为空行的时候
            ip = line.split()[0]
            if ip not in ips:
                ips[ip] = 1
            else:
                ips[ip] = ips[ip]+1
    point = f.tell() #当前文件指针的位置
    for ip in ips:
        if ips.get(ip) >= 100:
            print('超过100次的ip是:%s'%ip)
    time.sleep(60)
