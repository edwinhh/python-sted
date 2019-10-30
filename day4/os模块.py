import os

# os.remove()
# os.rename()
# os.mkdir('case')#创建文件夹
#os.makedirs('case/login') #创建文件夹
#files = os.listdir(r'/Users/nhy/PycharmProjects/mjz/day1')
#print(os.path.isdir(r'/Users/nhy/PycharmProjects/mjz/day3'))
#print(os.path.isfile(r'/Users/nhy/PycharmProjects/mjz/day3'))
os.chdir(r'/Users/nhy/PycharmProjects/mjz/day3')
#print(os.listdir())
#print(os.getcwd())#获取当前路径
#name = '.mp4'
# def search_file(path,name):
#     for cur_dir,dirs,files in os.walk(path):
#         for file in files:
#             if name in file:
#                 abs_path = os.path.join(cur_dir,file)
#                 print('找到%s文件，路径是%s'%(file,abs_path))
#
# search_file('/',name)

#os.system('ifconfig') #执行操作系统命令
#result = os.popen('ifconfig').read()
#print('result...',result)



# print(os.path.getsize('products.json'))
# print(os.path.exists('products.json'))#是否存在
# print(os.path.getatime('products.json'))#最近一次的访问时间
# print(os.path.getctime('products.json'))#createtime
# print(os.path.getmtime('products.json'))#modiyftime
# print(os.path.split(r'/Users/nhy/PycharmProjects/mjz/day4/products.json'))
#print(os.path.dirname(r'/Users/nhy/PycharmProjects/mjz/day4/os模块.py'))#获取父目录

#print(os.path.abspath(__file__))#根据相对路径获取绝对路径

#os.rmdir()#删除空文件夹
#os.removedirs()#删除空文件夹