#1、随机从所有的字符随机取7位
#2、再分别和所有大小写字母、数字、特殊字母取交集


#1、第二种思路
# 从大写字母 upper_Case ='A-Z'   lower_Case = 'a-z'  digits='0-9'  puc='23$@$@$'

import random
import string
num = input('请输入要产生多少条密码:').strip()
passwords = []
if num.isdigit():
    num = int(num)
    while len(passwords) != num:
        p1 = random.sample(string.ascii_letters+string.digits+string.punctuation,7) #随机取7位
        print(p1)
        if set(p1) & set(string.ascii_lowercase) and set(p1) & set(string.ascii_uppercase) \
            and set(p1) & set(string.digits)  and set(p1) & set(string.punctuation):
            password = ''.join(p1)#把密码变成字符串
            if password not in passwords:
                passwords.append(password)
else:
    print('请输入数字')

f = open('passwrods.txt','w')
for p in passwords:
    f.write(p+'\n')
f.close()