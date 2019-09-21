# 账号密码存在文件里面的

#1、获取到所有的用户，存成一个字典
#2、 {"xiaohei":"123456","abc","123",'xiaobai':"123"}


#s=xiaohei,12346\nxiaobai,12\nabc,123
#1、按照\n分隔
import pprint
f = open('users.txt')
result = f.read()
f.close()
user_list = result.split('\n')
users  = {}
pprint.pprint(user_list)
for user in user_list:
    tmp = user.split(',')
    username = tmp[0]
    password = tmp[1]
    #username,password = user.split(',') #这一行代码和前面3行一样的
    users[username] = password


for i in range(3):
    username = input('username:').strip()
    pwd = input('pwd:').strip()
    cpwd = input('cpwd:').strip()
    if username=='' or pwd=='' or cpwd=='':
        print('不能为空')
    elif username in users:
        print('用户已注册')
    elif pwd!=cpwd:
        print('两次输入的密码不一致')
    else:
        users.setdefault(username,pwd)
        print('注册成功')
        print(users)

f  = open('users.txt','w')

for key in users:
    p = '%s,%s\n'%(key,users.get(key))
    f.write(p)
f.close()
