import yagmail
import traceback
#import pythoncom
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.setting import email_info, email_cc, email_to, log,email_template
import os

def send_mail(subject, content, files=None):
    try:
        smtp = yagmail.SMTP(**email_info)
        smtp.send(subject=subject, contents=content,
                  to=email_to, cc=email_cc, attachments=files)
    except Exception as e:
        log.error("发送邮件失败+%s" % traceback.format_exc())



def send_foxmail(subject, content, file):
    name=os.path.basename(file)
    aa='attachment; filename="%s"' %name
    print(aa)
    message = MIMEMultipart()  # 内容, 格式, 编码
    message['From'] = "{}".format(email_to[0])
    message['To'] = ",".join(email_cc)
    message['Subject'] = subject
    message.attach(MIMEText(content, 'plain', 'utf-8'))
    att = MIMEText(open(file, 'rb').read(),'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    message.attach(att)
    try:
        server = smtplib.SMTP()
        server.connect(email_info.get("host"))
        # server.starttls()
        server.login(email_info.get("user"), email_info.get("password"))  # XXX为用户名，XXXXX为密码
        server.sendmail(email_to[0], email_cc, message.as_string())
        server.quit()
        log.debug('邮件发送成功')
        print("发送成功")
    except Exception as e:
        log.error("发送邮件失败+%s" % traceback.format_exc())
        
        

#outlook
# def send_mail_to_notify(sit_mode,usr_to_lc,send_mail,stripmac,strAk,md5Value):
#     pythoncom.CoInitialize()
#     outlook = win32.Dispatch('outlook.application')
#     mail = outlook.CreateItem(0)
#     mail.Recipients.Add("tervor@sf-express.com") # 提醒人邮箱设置h
#     user_list = send_mail.split(",")
#     for ii in user_list:
#         mail.Recipients.Add(ii)
#
#     subject = ""
#     if(sit_mode == "1"):
#         subject = 'SIT测试环境地理编码授权文件'.decode("utf-8").encode("gbk")
#     else:
#         subject = '生产环境地理编码授权文件'.decode("utf-8").encode("gbk")
#     mail.Subject = subject
#     mail_Attach = mail.Attachments
#     mail_Attach.Add(usr_to_lc)
#
#     strinfo = "你好，对以下机器{}进行授权文件的生成！！\r\n".format(stripmac).decode("utf-8").encode("gbk")
#     strinfo +="binary md5:" + md5Value
#     if(len(strAk) > 0):
#         strinfo += "Ak:" + strAk
#
#     mail.Body = strinfo
#     mail.Send()
#     return  0
# subject='a'
# content='b'
# send_mail(subject, content)
