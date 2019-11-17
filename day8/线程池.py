import threadpool
import requests,time,threading
from hashlib import md5
def down_load_pic(url):
    print(threading.current_thread())
    req = requests.get(url)
    m = md5(url.encode())
    with open( m.hexdigest()+'.png','wb') as fw:
        fw.write(req.content)
url_list = ['http://www.nnzhp.cn/wp-content/uploads/2019/10/f410afea8b23fa401505a1449a41a133.png',
            'http://www.nnzhp.cn/wp-content/uploads/2019/11/481b5135e75c764b32b224c5650a8df5.png',
            'http://www.nnzhp.cn/wp-content/uploads/2019/11/b23755cdea210cfec903333c5cce6895.png',
            'http://www.nnzhp.cn/wp-content/uploads/2019/11/542824dde1dbd29ec61ad5ea867ef245.png']

pool = threadpool.ThreadPool(20)#实例化一个线程池
reqs = threadpool.makeRequests(down_load_pic,url_list)#分配数据
[pool.putRequest(req) for req in reqs]
# for req in reqs:
#     pool.putRequest(req)
print(threading.activeCount())
pool.wait() #等待
print('end')
