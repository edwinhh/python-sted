s='123'
# s.strip()
# s.lstrip()
# s.rstrip()
# s.lower()
# s.upper()
# s.count('a')
# print(s.index('d')) #找字符串的下标
# print(s.find('d')) #找字符串的下标
name = '小黑'
# s='你的名字是{}'.format(name)
# s='你的名字是{name}'
# print(s.format_map({'name':'小白'}))
# print(s.isupper()) #判断是不是都是大写字母
# print(s.islower()) #判断是不是都是小写字母
# print(s.isdigit()) #判断是否为数字
# s = 'img.jpg'

# print(s.startswith('1')) #判断以xx开头
# print(s.endswith('jpg')) #判断以xx结尾
#s.isspace('        ') #是不是空格
# s='title abc'
# print(s.isalpha()) #如果是字母和汉字的话返回true
# print(s.isalnum()) #如果是字母、汉字和数字的返回true,只要不包含特殊字符都返回true
# print(s.capitalize())#首字母大写
# print(s.title()) #多个单词首字母大写


# s='150'
# print(s.center(50,'*'))
# print(s.zfill(5)) #补零
# s='aaaaaabc'
# s = s.replace('a','A') #Abc
# print(s)


# s='gaotianming,zoucuncai,choulihong,suhong'
# result = s.split("")#不能传空的字符串,这样是不对的，会报错
# result = s.split(',')
# print(result)
import pprint
l=['a','b','c']  #abc
s='hahaha'
t1 = ('a','b','c')
d = {'name':'xiaohei','sex':'男'}


pprint.pprint(''.join(l))#abc,连接字符串的，

# pprint.pprint(str(l))





# print(s.startswith('1')) #判断以xx开头
# print(s.endswith('jpg')) #判断以xx结尾
# print(s.isdigit()) #判断是否为数字
# s.lower()
# s.upper()
# s.count('a')
# s.strip()
# s.replace('a','A')
# s.zfill(5)



# number = input('请输入要产生几条：')
# if not number.isdigit():
#     print('请输入整数！')
# else:
#     number = int(number)