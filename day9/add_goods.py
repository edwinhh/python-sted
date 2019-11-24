import unittest, parameterized
from utils.request import MyRequest

with open('goods.txt',encoding='utf-8') as fr:
    data = []
    for line in fr:
        if line.strip():
            line_data = line.strip().split(',')
            data.append(line_data)

def get_token():

    #1、每次需要token 的时候都要调用登录接口获取token
    #2、其实只需要一次就ok了
    with open('token.txt','w') as fw:
        fw.write('773ae10d-40e9-4be7-a6cc-f470b7285f80')
    #1、先判断有没有token.txt文件，
    #2、如果有，读文件内容，获取token
    #3、如果没有，调用登录接口获取token
    #4、运行完所有用例删除token文件


class GoodsTest(unittest.TestCase):
    @parameterized.parameterized.expand(data)
    def test_add_goods(self, good_sn, name, p1, p2):
        token = get_token()
        header = {'X-Litemall-Admin-Token':token}
        data = {
            "goods": {"picUrl": "http://www.nnzhp.cn/wp-content/uploads/2019/08/adaef5a4fc7b26a532f5d3ddc2ce0249.png",
                      "gallery": [], "goodsSn": good_sn, "name": name, "counterPrice": p1,
                      "retailPrice": p2}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": 0, "number": 0, "url": ""}], "attributes": []}
        req = MyRequest('http://proxy.nnzhp.cn/admin/goods/create', 'post',
                        data=data, is_json=True,headers=header)
        print(req.response)
        self.assertEqual(0,req.response.get('errno'),msg='商品添加失败')


