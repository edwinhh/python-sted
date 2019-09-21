#集合天生去重
s = {1,2,3,1,2,3}
s2 = set() #空集合

l = [1,2,2,3,4,5,4]
print(set(l))
print(s)

#关系测试
#集合是无序的
a = {1,2,3}
b = {3,4,5}

# print(a & b) #取交集
# print(a.intersection(b)) #取交集

# print(a.union(b)) #并集,把两个集合合并到一起，然后取掉重复的
# print(a|b)#并集

# print( a - b ) #差集，在a集合里面存在，但是在b集合里面没有的
# print( a.difference(b))#差集
a.add('123')#增加，
a.remove('232')#删除
