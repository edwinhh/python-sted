# l = [1,2,3,4,5,6,7,8,9,10]
#
# #切片就是对list一个范围的取值
# s='abc1234'
# L2 = l[::-1]  #顾头不顾尾 0 1 2,步长,如果不是取全部的元素，步长为负数的时候，前面的下标也得是负数
# L3 = l[::1]  #顾头不顾尾 0 1 2,步长
# print(L2)
# print(L3)
#

#元组
l = [1,2,3,4]
l2 = (1,2,3,4) #元组，元组里面的数据不可以修改
s='abc'
print('upper',s.upper())
print('s',s)

# s[0]='A'

# db_info = ['192.158.1.1',3306,'root','123456','db1']

# db_info = ('192.158.1.1',3306,'root','123456','db1')

# s3 = ('abc',)
# print(type(s3))

#可变数据类型
    #list、dict
#不可变量数据类型
    #tuple、str、float、int


#1、不要循环删list，因为会导致下标错乱
# l = [1,1,2,3,4,5,6,7,8,9,10]
# l2 = l
# for i in l2:
#     if i%2!=0:
#         l.remove(i)
# print(l)
# import copy
# l = [1,2,3,4,5,6]
# # l2 = l
# l2 = copy.deepcopy(l)  #深拷贝
#
# print('l的内存地址',id(l))
# print('l2的内存地址',id(l2))
#
# l.append('吴慧丽')
# l2.remove(1)
# print('l',l)
# print('l2',l2)

#浅拷贝、深拷贝
#浅拷贝内存地址不变，深拷贝的话，内存地址会变

import copy
l=[1,2,3,4,['a','b','c']]
# l2 = copy.deepcopy(l) #只有这一种才是深拷贝
# l2 = l[:]#浅拷贝
# l2 = l#浅拷贝
# l2 = l.copy()#浅拷贝
# copy.copy(l1)#浅拷贝
# print('l',id(l))
# print('l2',id(l2))
# l[-1].append('abc')
# l2.insert(0,'A')
# l.append('!!!!!!')
# print('l',l)
# print('l2',l2)


