import tools,datetime
for i in range(3):
    username = input('username:').strip()
    pwd = input('pwd:').strip()
    if username=='' or pwd=='' :
        print('不能为空')
    else:
        new_password = tools.md5(pwd)
        sql='select username,password,error_count from app_myuser where username="%s";'%(username)
        result = tools.op_mysql(sql,False)
        if result:
            if result.get('error_count')>5:
                print('错误次数大于5，账号被冻结')
                break
            elif new_password == result.get('password') :
                print('登录成功 today is %s'%datetime.datetime.today())
                up_sql = 'update app_myuser set error_count=0 where username="%s";' % username
                tools.op_mysql(up_sql)
                break
            else:
                up_sql = 'update app_myuser set error_count=error_count+1 where username="%s";' % username
                tools.op_mysql(up_sql)
                print('密码错误！')
        else:
            print('用户不存在')

