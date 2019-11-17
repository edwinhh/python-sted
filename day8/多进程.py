import multiprocessing,time
def down_load():
    time.sleep(5)
    print("运行完了")

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=down_load)
        p.start()

    while len(multiprocessing.active_children())!=0:#等待子进程结束
        pass

    print(multiprocessing.current_process())

    print('end')