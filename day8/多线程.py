import threading
import time
#进程是多个资源的集合。
#线程是就是进程里面具体干活的。
#线程和线程之间是互相独立的。

def down_load():
    time.sleep(5)
    print("运行完了")

def movie():
    time.sleep(1)
    print('movie')

# threading.Thread(target=down_load,args=('name','abfd'))
start_time = time.time()
# for i in range(10):
#     t = threading.Thread(target=down_load)
#     t.start()
#     t.join()

# thread_list = []
# for i in range(5):
#     t = threading.Thread(target=movie)
#     t.start()
#     thread_list.append(t)
#
# print('thread_list',thread_list)
#
# for thread in thread_list:
#     thread.join() #主线程等待子线程结束

for i in range(5):
    t = threading.Thread(target=movie)
    t.start()

while threading.activeCount()!=1:
    pass

print(threading.activeCount()) #查看当前线程数
print(threading.current_thread())#查看当前线程

end_time = time.time()
print(end_time - start_time)
