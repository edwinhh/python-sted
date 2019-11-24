import xlwt,xlrd
import pymysql,os
import datetime,time
import hashlib

ip = '118.24.3.40'
user = 'jxz'
password = '123456'
db = 'jxz'
port = 3306#默认端口号，可以不指定，需要改的话要传
charset = 'uft8'

def op_mysql(sql):
    db_info = {'user': 'jxz', 'password': '123456',
            'host': '118.24.3.40', 'db': 'jxz', 'port': 3306, 'charset': 'utf8',
            'autocommit': True}
    conn = pymysql.connect(**db_info)  # 建立连接
    cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标
    cur.execute(sql)  # 执行sql语句，insert 、update 、delete
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
sql="select * from app_myuser"



def mysqltoexcl(stus,sheetname,savefile):
    tmp={}
    book = xlwt.Workbook()
    sheet = book.add_sheet(sheetname)
    for stu in stus:#控制行
        print(stu)
        for k,v in stu.items():
            tmp.setdefault(k, []).append(v)
    cnum=0
    for k,v in tmp.items():
        sheet.write(0,cnum,k)

        for i in range(len(v)):
            sheet.write(i+1,cnum,v[i])
        cnum +=1
    book.save(savefile)

#mysqltoexcl(op_mysql(sql),'1','app_myuser.xls')









#作业2

reg={}


def read_mysql(sql,u):
    db_info = {'user': 'jxz', 'password': '123456',
            'host': '118.24.3.40', 'db': 'jxz', 'port': 3306, 'charset': 'utf8',
            'autocommit': True}
    conn = pymysql.connect(**db_info)  # 建立连接
    cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标

    cur.execute(sql,u)  # 执行sql语句，insert 、update 、delete
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


reg_check="select * from user where username=%s"
reg_insert="insert into user (username,password,error_count) values (%(username)s,%(password)s,%(error_count)s)"




def register():
    t=datetime.datetime.today()
    error_count=0
    while 1:
        u = input("usrname:").strip()
        if read_mysql(reg_check,u):
            print("账号已存在")

        else:
            break
    p=input('password:').strip()
    p2=input('password agin:').strip()
    if u=='' or p=='' or p2=='':
        print('输入不能为空')
    elif p!=p2:
        print("密码不一致")
    else:
        m = hashlib.md5( p.encode() )
        result = m.hexdigest() #获取加密后的结果
        reg.setdefault("username",u)
        reg.setdefault("password",result)
        reg.setdefault("error_count", 0)
        print(reg)
        read_mysql(reg_insert, reg)
        print("注册成功,日期是{}".format(t))

#register()



#作业3
reg_update="UPDATE user SET error_count=%(error_count)s WHERE username=%(username)s"

def check(u,p):
    m = hashlib.md5(p.encode())
    p = m.hexdigest()
    a = read_mysql(reg_check, u)
    for i in a:
        if p==i['password']:
            return 1

        else:
            return 0


stus={}
def sign():
    error_count=0
    t=datetime.datetime.today()
    for i in range(5-error_count):
        u=input("usrname:").strip()
        p=input('password:').strip()
        if u=='' or p=='':
            print('输入不能为空')
            error_count+=1
        elif not read_mysql(reg_check,u):
            print("账号不存在")
            error_count += 1

        elif not check(u,p):
            print("密码不正确")
            error_count += 1
        else:
            print("登录ok,日期是{}".format(t))
            stus.setdefault("username", u)
            stus.setdefault("error_count", error_count)
            print(stus)
            read_mysql(reg_update, stus)
            break
    else:
        print("失败超过次数")
#sign()
# dstus={'username': 'dd', 'error_count': 2}
# read_mysql(reg_update, dstus)