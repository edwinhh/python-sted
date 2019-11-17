#主线程结束，守护线程立马死掉。
import threading,time

def down_load():
    time.sleep(5)
    print("运行完了")

for i in range(10):
    t = threading.Thread(target=down_load)
    t.setDaemon(True) #设置子线程为守护线程
    t.start()


print('over')