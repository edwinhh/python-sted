import datetime,json

file="products.json"

def check_price(price):
    price=str(price)
    if price.isdigit() and int(price) > 0:
        return True
    elif price.count('.') == 1:
        left, right = price.split('.')
        if left.isdigit() and right.isdigit() and int(right) > 0:
            return True
    return False

def check_id_io(id):
    products=read(file)
    if id in products:
        return 0
    else:
        return 1

def check_id(id,products):
    if id in products:
        return 0
    else:
        return 1

def read(file):
    products={}
    with open(file,'r',encoding='utf-8') as f:
        products=json.load(f)
    return products


def write(file,dict):
    try:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(dict,f,ensure_ascii=False)

    except Exception as e:
        print(e)


def input_info():
    name=input('name:')
    color=input('color:')
    price=input('price:')
    if name and check_price(price) and color:
        dict = {}
        product={}
        dict["color"] = color
        dict["price"] = price
        product.setdefault("name", name)
        product.setdefault("dict", dict)
        return product
    else:
        return 0


def add_product():
    product=input_info()
    products=read(file)
    if product:
        if check_id(product.get('name'), products):
            products.setdefault(product.get('name'), product.get("dict"))
            write(file, products)
            print("添加成功")
        else:
            print("商品已经存在或者价格，无法添加")
            return 0

    else:
        print("商品名称，价格，或者颜色输入异常或者为空,请重新输入")




def show_product():
    products = read(file)
    print(products)

    pass
def del_product():
    product=input_info()
    products=read(file)
    if product:
        if check_id(product.get('name'), products) is 0:
            del products[product.get('name')]
            write(file, products)
            print("删除成功")
        else:
            print("商品不存在，无法删除")
    else:
        print("商品名称，价格，或者颜色输入异常或者为空,请重新输入")

def update_product():
    product=input_info()
    products=read(file)
    if product:
        if check_id(product.get('name'), products) is 0:
            products[product.get('name')]=product.get("dict")
            write(file, products)
            print("修改成功")
        else:
            print("商品不存在，无法修改")
    else:
        print("商品名称，价格，或者颜色输入异常或者为空,请重新输入")



choice = input('请输入你的选择：1、添加2、查看 3、修改 4、删除\n')
if choice=='1':
    add_product()
elif choice=='2':
    show_product()
elif choice=='3':
    update_product()
elif choice == '4':
    del_product()
