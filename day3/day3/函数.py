#就是把一段代码封装起来

def say_hello(msg):
    print(msg)

#告诉文件名和内容
def write_file(file_name,content):
    f = open(file_name,'w')
    f.write(content)
    f.close()

#函数里面定义的变量都是局部变量,只在函数里面可以用，出了函数就不能用了
def read_file(file_name):
    with open(file_name,encoding='utf-8') as fr:
        result = fr.read()
        return result,

content = read_file('users')
# print(content)




# result = get_today_data()
#1、函数不写返回值的情况下返回的是什么
#2、返回多个值的时候,返回的是什么
#函数里面遇到return函数立即结束运行
