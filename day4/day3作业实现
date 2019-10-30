import json
FILE_NAME = 'products.json'

def op_file(file_name,content=None):
    if content:
        with open(file_name,'w',encoding='utf-8') as fw:
            json.dump(content,fw,ensure_ascii=False,indent=4)
    else:
        with open(file_name,'a+',encoding='utf-8') as fr:
            fr.seek(0)
            result = fr.read().strip()
            if result:
                dic = json.loads(result)
            else:
                dic = {}
        return dic

#1、添加商品
    #1、获取所有的商品信息
        #add
        #name、price、color
        #校验名称是否存在，价格是否合法
        #update
        #删除
        #查看

def is_price(s):
    s = str(s)
    if s.isdigit():
        return True
    if s.count('.') == 1:
        left, right = s.split('.')
        if left.isdigit() and right.isdigit():
            return True
    return False

def get_product_info():
    while True:
        name = input('product_name:').strip()
        price = input('price:').strip()
        color = input('color:').strip()
        if name and price and color:
            if is_price(price):
                return name,price,color
            else:
                print('价格不合法')
        else:
            print('不能为空')


def add():
    print('add')
    all_products = op_file(FILE_NAME)
    name,price,color = get_product_info()
    if name in all_products:
        print('ycz')
    else:
        all_products[name] = {'price':float(price),'color':color}
        print('success ')
        op_file(FILE_NAME,all_products)

def update():
    print('update')
    all_products = op_file(FILE_NAME)
    name,price,color = get_product_info()
    if name not in all_products:
        print('bycz')
    else:
        all_products[name] = {'price':float(price),'color':color}
        print('success ')
        op_file(FILE_NAME,all_products)

def delete():
    print('detlete')
    all_products = op_file(FILE_NAME)
    name = input('product_name:').strip()
    if name and name not in all_products:
            print('商品不存在')
    else:
        all_products.pop(name)
        print('success ')
        op_file(FILE_NAME, all_products)

def show():
    print('show')
    all_products = op_file(FILE_NAME)
    name = input('product_name:').strip()
    if name=='all':
        print(all_products)
    elif name not in all_products:
        print('不存在')
    else:
        print(all_products.get(name))



func_map = { '1':add,'2':update,'3':delete,'4':show,'q':quit }
for i in range(4):
    choice = input('1、add 2、update 3、delete 4、show q 退出：\n').strip()
    if choice in func_map:
        func_map[choice]()
    else:
        print('输入有误！')
#函数即变量