score = input('请输入你的分数:') #raw_input() python2里面
print('socre的类型',type(score)) #type看一个变量的数据类型
score = int(score) #类型转换
print('转换之后的socre的类型',type(score)) #type看一个变量的数据类型
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