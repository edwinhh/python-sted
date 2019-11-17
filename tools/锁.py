#多个线程操作同一个数据的时候，就得加锁
import threading

num = 0

lock = threading.Lock() #申请一把锁

def add():
    global num
    # lock.acquire()#加锁
    # num+=1
    # lock.release()#解锁  #死锁
    with lock:#简写，用with也会帮你加锁，解锁
        num+=1



for i in range(20):
    t = threading.Thread(target=add,)
    t.start()

while threading.activeCount() !=1:
    pass

print(num)
