import datetime
user = '金爽'
today = datetime.datetime.today()
msg = '欢迎'+user+','+'今天的日期是'+ str(today)
msg2 = '欢迎 %s登录，今天的日期是 %s' % (user,today) #占位符
msg3 = '欢迎%s登录' % user
age = 18
score = 95.3

# msg4 = '你的名字是 %s ,你的年龄是 %d ，你的分数是 %.2f ' %(user,age,score)
#msg4 = '你的名字是 %s ,你的年龄是 %s ，你的分数是 %s ' %(user,age,score)
msg5 = '你的名字是{name},年龄是{nianling}'.format(name=user,nianling=age)
msg6 = '你的名字是{},年龄是{}'.format(user,age)
print(msg6)
#print(msg4)

username2='jinshuang'
password2='122324'
role2='1'
email2='jinshuang@qq.com'
phone2='18623241323'



#sql='insert into user (username,password,role,email,phone) values (%s,%s,%s,%s,%s);'%(password,username,role,email,phone)
sql = 'insert into user (username,password,role,email,phone) values ({username},{password},{role},{email},{phone})'.format(phone=phone2,email=email2,password=password2,username=username2,role=role2)
print(sql)

