import yagmail
username='qingfengerya@163.com' # 发件人的邮箱
password='softtest_798'#生成授权码，qq、163、126都是授权码   发件人的密码
# qq = 'lnryhkmepprqbcdg'

mail_server = 'smtp.163.com' # 163的服务
# mail_server = 'smtp.qq.com'
# mail_server = 'smtp.126.com'

m = yagmail.SMTP(user=username,password=password,host=mail_server)


to = ['923465313@qq.com','qingfengerya@hotmail.com'] #发给谁
cc = ['qingfengerya@163.com'] #抄送


m.send(to=to,cc=cc, # to 发送给谁，cc 抄送给谁
       subject='今天吃了吗',#标题
       contents='今天吃鱼肉了吗，吃饱没', #正文
       attachments='1.py') #附件，多个附件传一个list

