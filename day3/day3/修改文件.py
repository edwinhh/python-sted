#1、简单直接粗暴的方法

# f = open('a.txt','a+',encoding='utf-8')
# f.seek(0)
# result = f.read()
# new_result = result.replace('abc','ABC')
# f.seek(0)
# f.truncate() #清空文件内容
# f.write(new_result)
# f.close()

#2、第二种是逐行修改
import os
# f1 = open('a.txt',encoding='utf-8')
# f2 = open('a2.txt','w',encoding='utf-8')
# for line in f1:
#     new_line = line.replace('一','1')
#     f2.write(new_line)
# f1.close()
# f2.close()
# os.remove('a.txt')
# os.rename('a2.txt','a.txt')

# with open('a.txt',encoding='utf-8') as f1,open('a2.txt','w',encoding='utf-8') as f2:
#     for line in f1:
#         new_line = line.replace('一', '1')
#         f2.write(new_line)
#     os.remove('a.txt')
#     os.rename('a2.txt','a.txt')


# with open('a2.txt','w') as fw:
#     fw.write('123')
#     fw.flush()#刷新缓冲区，直接写到磁盘里面
#


#非空即真，非0即真
# 布尔
a = 1
b = 2
# s=''
# l = []
# d = {}
# s1 = set()
# t = ()
# result = f.read()

# if result:
#     print('')

username = input('user:').strip()
if username:
    print('欢迎登陆%s'%username)
else:
    print('用户名不能为空')
