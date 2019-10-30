#递归，就是函数自己调用自己

def func():
    num = int(input('num:'))
    if num % 2 ==0:
        print('是偶数')
        return
    else:
        func()

f = lambda x,b:str(x+b)

# result = f(1,2)
# print(result)


# def f(x):
#     return str(x).zfill(2)
#
# result = list(map(lambda x:str(x).zfill(2),range(1,30) ))
#
# result = list(map(f,range(1,30) ))
#
# print(result)
# def f(x):
#     return x+1

l = ['id', 'name', 'sex', 'age', 'addr', 'grade', 'phone', 'gold']
for index,value in enumerate(l):
    print('%s=>%s '%(index,value))