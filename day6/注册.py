import tools


for i in range(3):
    username = input('username:').strip()
    pwd = input('pwd:').strip()
    cpwd = input('cpwd:').strip()
    if username=='' or pwd=='' or cpwd=='':
        print('不能为空')
    elif pwd!=cpwd:
        print('两次输入的密码不一致')
    else:
        sql='select username from app_myuser where username="%s";'%username
        if tools.op_mysql(sql):
            print('已被注册过')
        else:
            new_password = tools.md5(pwd)
            insert_sql = 'insert into app_myuser (username,password) values ("%s","%s");'%(username,new_password)
            tools.op_mysql(insert_sql)
            print('注册成功！')
            break

