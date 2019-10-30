#coding=utf-8
# input()
# print()
# len()
# type()
# str()
# tuple()
# set()
# dict()
# list()
#l='asdfgwert3r'
#sorted(l) #排序
#print(all([1,2,3,4,'']))#如果list里面都为真的就返回true
#print(any([0,0,0,1]))#判断可迭代的对象里面的值是否有一个为真
#print(bin(10))#十进制转二进制
# print(bool(0))#把一个对象转换成布尔类型
# print(chr(66))#打印数字对应的ascii
# print(ord('B'))#打印字符串对应的ascii码
# print(dict(a=1,b=2))#转换字典
#s='a'
# print(dir(s))#打印传入对象的可调用方法



# print(eval('[]'))#执行python代码，只能执行简单的，定义数据类型和运算
# print(exec('def a():pass'))#执行python代码
# print(filter(lambda x:x>5,[12,3,12,2,1,2,35]))#把后面的迭代对象根据前面的方法筛选
# print(map(lambda x:x>5,[1,2,3,4,5,6]))
#print(max([12,3,4,5]))#取最大值
#min([12,3,4,5])
#print(oct(9))#把数字转换成8进制
#print(round(3.1415926,3))#取几位小数


#print(eval('[]'))#执行python代码，只能执行简单的，定义数据类型和运算
# print(exec('def a():pass'))#执行python代码
# print(filter(lambda x:x>5,[12,3,12,2,1,2,35]))#把后面的迭代对象根据前面的方法筛选
# print(map(lambda x:x>5,[1,2,3,4,5,6]))
#zip()

#s = "[1,2,3,4]"

# print(eval(s))

# func_str = '''
# import time
# def fun():
#     return 'func_name'
# '''
# exec(func_str)
# result = fun()

#print(result)

# f = open('作业.py',encoding='utf-8')
# result = f.read()
# exec(result)

l = [1,2,3,4,5,6,7,8,9,10]

def t(num):
    if num % 2 == 0:
        return True

#l2 = list( filter(t,l) )
# l3 = list( map(t,l) )
# print(l3)
# print(l2)

# l1=[1,2,3,4]
# l2=['a','b','c','d']
# l3=['a','b','c','d','f']
# for k1,k2,k3 in zip(l1,l2,l3):
#     print(k1,k2,k3)

