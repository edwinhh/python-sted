import requests,time,threading
from hashlib import md5
result_list = {}
def down_load_pic(url):
    req = requests.get(url)
    m = md5(url.encode())
    file_name = m.hexdigest()+'.png'
    with open(file_name ,'wb') as fw:
        fw.write(req.content)
    # return file_name
    result_list[file_name] = threading.current_thread()




url_list = ['http://www.nnzhp.cn/wp-content/uploads/2019/10/f410afea8b23fa401505a1449a41a133.png',
            'http://www.nnzhp.cn/wp-content/uploads/2019/11/481b5135e75c764b32b224c5650a8df5.png',
            'http://www.nnzhp.cn/wp-content/uploads/2019/11/b23755cdea210cfec903333c5cce6895.png',
            'http://www.nnzhp.cn/wp-content/uploads/2019/11/542824dde1dbd29ec61ad5ea867ef245.png']

# start_time = time.time()
# for url in url_list:
#     down_load_pic(url)
# end_time = time.time()
#
# print(end_time - start_time)

start_time = time.time()
for url in url_list:
    t = threading.Thread(target=down_load_pic,args=(url,))
    t.start()

while threading.activeCount()!=1:
    pass

end_time = time.time()
print(end_time - start_time)
print(result_list)
#4c
#GIL全局解释器锁
#cpu 上下文切换
#多进程
#CPU有几个核心就只能同时运行几个任务（线程）
#锁、守护线程、线程池






