import datetime,os
stus={}
reg={}
#file='D:\\python sted\\day2\\信息.txt'

dir=os.getcwd()
name='信息.txt'
file=os.path.join(dir,name)




def readtxt(dict):
    with open(file,'r') as f:
        for line in f:
            if line:
                u,p=line.strip().split(',')
                dict.setdefault(u,p)


#注册

def register():
    t=datetime.datetime.today()
    reg.clear()
    readtxt(reg)
    for i in range(3):
        u=input("usrname:").strip()
        p=input('password:').strip()
        p2=input('password agin:').strip()
        if u=='' or p=='' or p2=='':
            print('输入不能为空')
        elif u.lower() in reg:
            print("账号已存在")
        elif p!=p2:
            print("密码不一致")
        else:
            reg.setdefault(u,p)
            with open(file, 'a+') as f:
                for i in reg:
                    f.write(i+','+reg[i]+'\n')

            print("注册成功,日期是{}".format(t))


#登录
def sign():
    stus.clear()
    readtxt(stus)
    t=datetime.datetime.today()
    for i in range(2):
        u=input("usrname:").strip()
        p=input('password:').strip()
        if u=='' or p=='':
            print('输入不能为空')
        elif u.lower() not in stus:
            print("账号不存在")
        elif u in stus and p!=stus[u]:
            print("密码不正确")
        #elif u in stus and p == stus[u]:
        else:
            print("登录ok,日期是{}".format(t))
            break
    else:
        print("失败超过次数")

#register()
sign()