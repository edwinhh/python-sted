import yagmail,threading
def send_mail():
    smtp = yagmail.SMTP(host='smtp.163.com',
                        user='uitestp4p@163.com',
                        password='houyafan123'
                        )
    smtp.send(to='niuhanyang@163.com',cc=['niuhanyang@163.com','17966033@qq.com'],subject='标题',
              contents='正文',attachments=[r'/Users/nhy/PycharmProjects/mjz/day6/jsonpath模块.py']
              )

def async_send_mail():
    t = threading.Thread(target=send_mail)
    t.start()

