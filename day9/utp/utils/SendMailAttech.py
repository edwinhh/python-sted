#coding:utf-8

# import win32com.client as win32
# import pythoncom
# import sys
# from Crypto.Cipher import AES
# from Crypto.Hash import MD5
from binascii import b2a_hex, a2b_hex
import  struct
import time

import hashlib


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def md5sum(filename):
    fd = open(filename)
    fcont = fd.read()
    fd.close()
    fmd5 = hashlib.md5(fcont)
    return fmd5.hexdigest()





#send_mail：接收邮件人列表（即使用license的客户列表）
def send_mail_to_notify(sit_mode,usr_to_lc,receiver_mail,stripmac,strAk,md5Value,limit_datetime,product, sender_mail, sender_pwd):
    
    server_host = "lsmtp.sf-express.com"
    my_mail_box = sender_mail
    my_mail_pwd = sender_pwd
    
    #创建一个带附件的实例
    msg = MIMEMultipart()
    
    
    subject = ""
    if(sit_mode == "1"):
        if product=='0':
            subject = '测试环境逆地理编码(RGEO)授权文件'.decode("utf-8").encode("gbk")
        elif product=='1':
            subject = '测试环境搜索产品(MSS)授权文件'.decode("utf-8").encode("gbk")
        elif product=='2':
            subject = '测试环境POIS授权文件'.decode("utf-8").encode("gbk")
        elif product=='3':
            subject = '测试环境调度系统输入提示授权文件'.decode("utf-8").encode("gbk")
        else:
            subject = '测试环境授权文件'.decode("utf-8").encode("gbk")
    else:
        if product=='0':
            subject = '生产环境逆地理编码(RGEO)授权文件'.decode("utf-8").encode("gbk")
        elif product=='1':
            subject = '生产环境搜索产品(MSS)授权文件'.decode("utf-8").encode("gbk")
        elif product=='2':
            subject = '生产环境POIS授权文件'.decode("utf-8").encode("gbk")
        elif product=='3':
            subject = '生产环境调度系统输入提示授权文件'.decode("utf-8").encode("gbk")
        else:
            subject = '生产环境授权文件'.decode("utf-8").encode("gbk")
    
    
    strinfo = "你好，对以下机器{}进行授权文件的生成！！\r\n".format(stripmac).decode("utf-8").encode("gbk")
    strinfo +="binary md5:" + md5Value
    if(len(strAk) > 0):
        strinfo += "AK:" + strAk
    
    st = time.localtime(limit_datetime)
    str_limit_ymd = time.strftime('%Y-%m-%d', st)
    strinfo += "\r\n"
    strinfo += "授权到期时间截止：".decode("utf-8").encode("gbk")
    strinfo += str_limit_ymd
    
    
    txt = MIMEText(strinfo,'plain','gbk')    
    msg.attach(txt)
    #构造附件1
    att1 = MIMEText(open(usr_to_lc, 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="binary.dat"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)
    
    #加邮件头
    msg['to'] = receiver_mail
    msg['from'] = sender_mail
    msg['cc'] = sender_mail
    msg['subject'] = subject
    

    #发送邮件
    try:
        server = smtplib.SMTP()
        server.connect(server_host)
        #server.starttls()
        server.login(my_mail_box, my_mail_pwd)#XXX为用户名，XXXXX为密码
        server.sendmail(msg['from'], msg['to'],msg.as_string())
        server.quit()
        print ('发送成功')
    except Exception as e:
        print (str(e))
        
    return  0

'''
#send_mail：接收邮件人列表（即使用license的客户列表）
def send_mail_to_notify(sit_mode,usr_to_lc,send_mail,stripmac,strAk,md5Value,limit_datetime,product):
    pythoncom.CoInitialize()
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.Recipients.Add("BingZhang@sf-express.com") #添加一个邮件接收人（一般是颁发许可证的负责人）
    user_list = send_mail.split(",")
    for ii in user_list:
        mail.Recipients.Add(ii)

    subject = ""
    if(sit_mode == "1"):
        if product=='0':
            subject = '测试环境逆地理编码(RGEO)授权文件'.decode("utf-8").encode("gbk")
        elif product=='1':
            subject = '测试环境搜索产品(MSS)授权文件'.decode("utf-8").encode("gbk")
        elif product=='2':
            subject = '测试环境POIS授权文件'.decode("utf-8").encode("gbk")
        elif product=='3':
            subject = '测试环境调度系统输入提示授权文件'.decode("utf-8").encode("gbk")
        else:
            subject = '测试环境授权文件'.decode("utf-8").encode("gbk")
    else:
        if product=='0':
            subject = '生产环境逆地理编码(RGEO)授权文件'.decode("utf-8").encode("gbk")
        elif product=='1':
            subject = '生产环境搜索产品(MSS)授权文件'.decode("utf-8").encode("gbk")
        elif product=='2':
            subject = '生产环境POIS授权文件'.decode("utf-8").encode("gbk")
        elif product=='3':
            subject = '生产环境调度系统输入提示授权文件'.decode("utf-8").encode("gbk")
        else:
            subject = '生产环境授权文件'.decode("utf-8").encode("gbk")
    mail.Subject = subject
    mail_Attach = mail.Attachments
    mail_Attach.Add(usr_to_lc)

    strinfo = "你好，对以下机器{}进行授权文件的生成！！\r\n".format(stripmac).decode("utf-8").encode("gbk")
    strinfo +="binary md5:" + md5Value
    if(len(strAk) > 0):
        strinfo += "AK:" + strAk
    
    
    st = time.localtime(limit_datetime)
    str_limit_ymd = time.strftime('%Y-%m-%d', st)
    strinfo += "\r\n"
    strinfo += "授权到期时间截止：".decode("utf-8").encode("gbk")
    strinfo += str_limit_ymd

    mail.Body = strinfo
    mail.Send()
    return  0
'''

def decrypt_reg_info(sit_mode,usr_to_lc,receiver_mail,product, sender_mail, sender_pwd):
    
    strkey=""
    if product=='0':
        strkey = "QWE!@#rty456za24xs*&ui3s9iWM<3.e";
    elif product=='1':
        strkey = "QWE!@#rty44456z9iWM<l43.eaxs*&us"
    elif product=='2':
        strkey = "?:P)MJU&^YHN45#$s^vfr4!@#WBGT#3c"
    elif product=='3':
        strkey = "$HG9*j7L90:le56efJU-;@#DE451sh32"
    else:
        strkey=""
    
    m = MD5.new()
    m.update(strkey)
    strpwdkey = m.digest()
    ###注：生成的摘要只有16位，需要补齐至32位
    strpwdkey += "0000000000000000"
    pc = prpcrypt(strpwdkey)  # 初始化密钥

    with open(usr_to_lc) as of:
        reg_info = of.read()

        stripmac = ""
        strak    = ""
        size = len(reg_info)
    
        if (size == 10272):
            strdata = pc.decrypt(reg_info)
            dataLen = len(strdata)
            #reserve:30 bytes, limit_datetime: 8 bytes
            a = struct.unpack("L", strdata[30:34])
            mode = struct.unpack("L", strdata[46:50])[0]
            limit_datetime = a[0]

            
            if (mode==4):
                #mac
                mac = struct.unpack("2048s", strdata[2110:4158])[0]
                stripmac = mac.split("|")[0]
            
            if (mode==5):
                #ip
                ip = struct.unpack("2048s", strdata[62:2110])[0]
                stripmac = ip.split("|")[0]
            
            if (mode==7):
                #ip
                ip = struct.unpack("2048s", strdata[62:2110])[0]
                stripmac = ip.split("|")[0]
                #mac
                mac = struct.unpack("2048s", strdata[2110:4158])[0]
                stripmac = mac.split("|")[0]
            
            #todo: 带ak的解析逻辑
            '''
            strakinfo = struct.unpack("4096s",strdata[9268:13364])[0]
            npos = strakinfo.rfind(":4,")
            strak = strakinfo[0:npos+2]
            '''
            
        #发送邮件
        md5value = md5sum(usr_to_lc)
        send_mail_to_notify(sit_mode,usr_to_lc,receiver_mail,stripmac,strak,md5value,limit_datetime,product, sender_mail, sender_pwd)



if __name__ == '__main__':
    lc_file    = sys.argv[1]
    receiver_mail  = sys.argv[2]
    sit_mode   = sys.argv[3]
    product    = sys.argv[4]
    sender_mail = sys.argv[5]
    sender_pwd = sys.argv[6]
    decrypt_reg_info(sit_mode,lc_file,receiver_mail,product,sender_mail,sender_pwd)
    