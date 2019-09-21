import random,string


pwds = []
for i in range(100):
    num = random.sample(string.digits,2) #随机取1位数字
    #sc = random.choice(scs)  # 随机取1位
    sc = random.sample(string.punctuation,1)  # 随机取1位
    lower = random.sample(string.ascii_lowercase,1) #随机取1位小写字母
    upper = random.sample(string.ascii_uppercase,1) #随机取1位大写字母
    res = num+sc+lower+upper #产生的5位密码
    pwd = ''.join(res)+'\n'
    if pwd not in pwds: #判断是否重复
        pwds.append(pwd)
    print(pwd)
with open('password.txt','a+') as f:
    f.writelines(pwds)