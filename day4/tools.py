name = 'tools文件'
import random
import redis,xlrd,xlutils,xlwt,pymysql
def test():
    print('test函数')
    return 'abc'

# if __name__ == '__main__':
#
#     test()
#     print(name)

def dlt():
    ft=[str(num).zfill(2) for num in range(1,33)]
    bt=[str(num).zfill(2) for num in range(1,13)]
    f=random.sample(ft,5)
    f.sort()
    b=random.sample(bt,5)
    b.sort()
    temp=f+b
    result=' '.join(temp)
    return result

print(dlt())
nums=set()
num=2
while len(nums)!=int(num):
    k=dlt()
    nums.add(k)
print(nums)
