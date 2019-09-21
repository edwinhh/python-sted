# 作业：
#     1、写一个登录的程序，
#         1、最多登陆失败3次    while for
#         2、登录成功，提示欢迎xx登录，今天的日期是xxx，程序结束  break
#         3、要检验输入是否为空,账号和密码不能为空  s.strip()
#         4、账号不区分大小写  .lower  .upper
#     2、写一个随机产生138开头手机号的程序
#         1、输入一个数量，产生xx条手机号
#             prefix = '138'
#         2、产生的这些手机号不能重复

import datetime
u = 'niuhanyang'
today = datetime.datetime.today()
for i in range(3):
    username =  input('username:').strip()
    password =  input('password:').strip()
    if username =='' or password =='':
        print('账号/密码不能为空')
    elif username.lower() == u.lower() and password =='123456':
        print('登录成功，欢迎%s登录，今天的日期是%s'%(username,today))
        break
    else:
        print('账号/密码错误！')
else:
    print('登录失败次数过多')


##     2、写一个随机产生138开头手机号的程序
#         1、输入一个数量，产生xx条手机号  10 while  for
#             prefix = '138'  138 + randint(10000000,99999999)
#1381323414
#         2、产生的这些手机号不能重复 s='13812348765,1381323414'
import random
number = input('请输入：')
number = int(number)
all_phone_number = [] #存放所有的手机的
for i in range(number):
    prefix= '138'
    end = str(random.randint(10000000,99999999))
    phone_number = prefix+end #电话号码
    if  all_phone_number.count(phone_number)==0:#判断电话号码是否存在
        all_phone_number.append(phone_number)
        print(phone_number)
print(all_phone_number)






