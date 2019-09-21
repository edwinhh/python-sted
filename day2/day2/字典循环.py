d  = {
      "id": 315,
      "name": "矿泉水",
      "sex": "女",
      "age": 27,
      "addr": "上海",
      "grade": "摩羯座",
      "phone": "18317155664",
      "gold": 100
    }

# for k in d:#直接循环字典，每次取的是字典里面的key
#     value = d.get(k) #循环的时候同时取到key和value
#     print(k,value)
#
print(d.items())
print(d.keys())

# for key,value in d.items():  #第二种方式
#     print(key,value)

#if 'id' in d: #如果字典用in来判断的话，它判断的是key存在不存在

#if 'id' in d.keys()

s2={'x1':'1','x2':'2','x3':'3'}
for i in range(3):
    username=input('username').strip()
    password=input('password').strip()


    if username=='' or password=='':
        print("账号/密码不能为空")
    elif username in s2:
        print('登陆的用户名在注册中')
        if password==s2[username]:
            print("账号/密码正确")
        else:
            print("账号/密码错误")
    else:
        print('账号不存在')

else:
    print("超过了次数")