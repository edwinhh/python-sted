import datetime

s  = {
      "id": 315,
      "name": "矿泉水",
      "sex": "女",
      "age": 27,
      "addr": "上海",
      "grade": "摩羯座",
      "phone": "18317155664",
      "gold": 100
    }



# for k,v in s.items():
#     print(k,v)


#效率更高
# for k in s:
#     print(k,s[k])

#登录逻辑，从字典获取账号密码


#登录
# stus={"a":'123456',"b":'123456',"c":'123456'}
#
# t=datetime.datetime.today()
# for i in range(3):
#     u=input("usrname:").strip()
#     p=input('password:').strip()
#     if u=='' or p=='':
#         print('输入不能为空')
#     elif u.lower() not in stus:
#         print("账号不存在")
#     elif u in stus and p!=stus[u]:
#         print("密码不正确")
#     #elif u in stus and p == stus[u]:
#     else:
#         print("登录ok,日期是{}".format(t))
#         break
# else:
#     print("失败超过次数")


#注册
stus={"a":'123456',"b":'123456',"c":'123456'}

t=datetime.datetime.today()
for i in range(3):
    u=input("usrname:").strip()
    p=input('password:').strip()
    p2=input('password agin:').strip()
    if u=='' or p=='' or p2=='':
        print('输入不能为空')
    elif u.lower() in stus:
        print("账号已存在")
    elif p!=p2:
        print("密码不一致")
    else:
        stus.setdefault(u,p)
        print("注册成功,日期是{}".format(t))





s='abc key'
print(s.upper())
stus={"a":'123456',"b":'123456',"c":'123456'}
stus.popitem()
print(stus)
#print(s.index('c'))
print(s.find('c'))
print(s.capitalize())

l=[1,2,3,4,5,6]
l2=[str(i) for i in l]
print(''.join(l2))

l3=[i for i in range(10) if (i%2==0)]#这个和下面4行代码一致

l3=[]
for i in range(10):
    if i%2==0:
        l3.append(i)

l2=[str(i) for i in l]#这个和下面2行代码一致

for i in l:
    l2.append(str(i))

file='D:/文档/pycharm账号密码txt.txt'
with open(file,'a+') as f:
    f.write("写入str"+'\n')

t1=set(['a','b','c'])
t2=set(['a','b','v'])

#取交集
print(t1&t2)
print(t1.intersection(t2))



#取并集,两个集合结合并，然后去除重复的
print(t1.union(t2))
print(t1|t2)


#差集，在t1集合存在，但是在t2集合没有的
print(t1-t2)
print(t1.difference(t2))