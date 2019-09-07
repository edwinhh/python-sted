'''
print('hello world!')
print("hello world!")
print("let's go")
print(' 春光长得"很帅"  ')
'''
#print( """ ''' let's go,春光长得"很帅" ''' """)

name = 'xiaohe' #字符串，string
age = 18 #整数，int
score = 1000 #浮点数,float
user ='wangqingzhu'

#条件判断

if score>=90 and score<=100 : #>= <= == !=
    print('优秀')
elif score<90 and score>=80:
    print('良好')
elif score<80 and score>=60:
    print('及格')
elif score<60 and score>0:
    print('不及格')
else:
    print('分数不合法')

