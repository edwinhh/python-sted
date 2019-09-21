#1、输入账号、密码、确认密码来注册
#2、如果账号不存的话，可以注册
#3、两次密码输入一致，可以注册

# stus = [ { 'username':'wangyujian','password':'123456' }, { 'username':'wangyujian2','password':'123456' } ]

stus2 = { 'wangyujian':'123456','lihong':'456789' }
for i in range(3):
    username = input('username:').strip()
    pwd = input('pwd:').strip()
    cpwd = input('cpwd:').strip()
    if username=='' or pwd=='' or cpwd=='':
        print('不能为空')
    elif username in stus2:
        print('用户已注册')
    elif pwd!=cpwd:
        print('两次输入的密码不一致')
    else:
        # stus2[username] = pwd
        stus2.setdefault(username,pwd)
        print('注册成功')
        print(stus2)

