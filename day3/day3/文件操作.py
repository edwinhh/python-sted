# f = open('a.txt',encoding='utf-8')
# print('readline',f.readline())
# print('readlines',f.readlines()) #把文件每一行的内容放到list里面
# print('read',f.read())
#
# f.close()
#文件指针

# stus = ["xiaohei",'xiaobai','xiaolan']
# f  = open('b.txt','w')
# f.write('sdfsdf\n') #只能写字符串
# f.writelines(stus)
# f.close()

#1、先读和后读写的位置不一样
# f = open('a.txt','r+',encoding='utf-8')
# # print(f.read())
# f.write('AAAA')
# f.close()


#1、写完之后读不到东西
# f = open('a.txt','w+',encoding='utf-8')
# f.write('r+模式22222')
# print(f.read())
# f.close()

#1、读不到东西
# f = open('a.txt','a+',encoding='utf-8')
# f.seek(0)
# print(f.read())
# f.write('a+模式22222')
# f.close()


