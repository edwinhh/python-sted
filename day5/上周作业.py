#删掉三天前的日志
    #1、获取到所有的日志文件， os.walk
    #2、获取文件时间 android 2019-09-27 log，并转成时间戳
    #3、获取3天前的时间 time.time() - 60 * 60 *24 *3
    #4、判断文件的时间戳如果小于3天前的时间戳删除
    #5、文件为空删除  os.path.getsize()

import os,time
import random


def str_to_timestamp(string=None,format='%Y-%m-%d %H:%M:%S'):
    '''格式化好的字符串转时间戳，默认返回当前时间戳'''
    if string:
        time_tuple = time.strptime(string, format)  # 格式化好的时间，转时间元组的
        result = time.mktime(time_tuple)  # 把时间元组转成时间戳
    else:
        result = time.time()
    return int(result)

def clean_logs(path,days=3):
    if not os.path.isdir(path):
        print("传入的不是一个文件夹")
        return
    for cur_dir,dirs,files in os.walk(path):
        for file in files:
            if file.endswith('.log'):
                # file_time = file.split('.')[0].split('_')[-1]
                prefix=file.split('.')[0]
                file_time = prefix.split('_')[-1]
                file_time_stamp = str_to_timestamp(file_time,'%Y-%m-%d')
                three_day_ago = time.time() - 60 * 60 * 24 * days
                file_path = os.path.join(cur_dir,file)
                if file_time_stamp < three_day_ago or os.path.getsize(file_path)==0:
                    os.remove(file_path)


#作业2：
    #产生大乐透号码
    #前区 1-32，5 后区 1-12，2
    #1、前区从1-32中级取5个，后区再从1-12里面取2个

    #01 02 03 04
def dlt():
    all_front = [ str(num).zfill(2) for num in range(1,33) ]
    all_back = [ str(num).zfill(2) for num in range(1,13) ]
    front = random.sample(all_front,5)
    front.sort()
    back = random.sample(all_back,2)
    back.sort()
    temp = front + back
    result = ' '.join(temp)
    return result

nums = set()
num = input("请输入产生几注：").strip()
if num.isdigit():
    while len(nums)!=int(num):
        haoma = dlt()
        nums.add(haoma+'\n')
    else:
        with open('dlt.txt','w') as fw:
            fw.writelines(nums)
else:
    print('请输入正确的数字')