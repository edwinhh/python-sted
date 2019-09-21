students = ['zoucuncai','gaotianming','limingmin']
stu2 = [
    ['zoucuncai','未知',38,'北京',182325242],
    ['zoucuncai','未知',38,'北京',182325242],
    ['zoucuncai','未知',38,'北京',182325242],
]

#字典key - value

d = {
      'name':'zoucuncai',
      'idcard_no':3242424,
      'sex':'未知',
      'addr':'北京',
      '手机号':110
}

#取值
# print(d['money'])#取不存在的key会报错
# print(d.get('money',0))#，取不存在的key返回none

#增加key
#
# d['sex'] = 500 #如果key存在，就修改它的值
# d.setdefault('car','bmw')   #如果key存在，那就不管了。

#修改
# d['sex'] = '女' #修改
#删除
# d.pop('sex')#删除指定的key,会返回删除的值
# del d['sex'] #删除指定的key

# d.clear() #清空字典
print(d.keys()) #字典里面所有的key
print(d.values()) #字典里面所有的value

print(d)

