import unittest
import parameterized
import os
from urllib.parse import urljoin
from projects.litemall.const import host,test_user,data_path
from projects.litemall import tools
from utils.request import MyRequest
from utils.mysql_util import mysql
from utils.utils import GetTestData

address_data_path = os.path.join(data_path,'address.xlsx')

class TestAddress(unittest.TestCase):
    url = urljoin(host,'/wx/address/save')

    @classmethod
    def setUpClass(cls):
        token = tools.WxLogin(**test_user).get_token() #登录获取token
        cls.header = {'X-Litemall-Token':token} #拼header

    @parameterized.parameterized.expand(GetTestData.data_for_excel(address_data_path))
    def test_create(self,name,tel,isDefault):
        '''测试添加收货地址'''
        is_default = True if isDefault=='1' else False
        data = {
            "name": name,
            "tel": "%d"%tel,
            "country": "",
            "province": "北京市",
            "city": "市辖区",
            "county": "东城区",
            "areaCode": "110101",
            "postalCode": "",
            "addressDetail": "西二旗",
            "isDefault": is_default
        }
        req = MyRequest(self.url,'post',data=data,headers=self.header)
        self.assertEqual(0,req.response.get('errno'),msg='添加失败')
        address_id = req.response.get('data')
        sql = 'select name from litemall_address where id = %s;'%address_id
        db_data = mysql.execute_one(sql)
        self.assertIsNotNone(db_data,msg='litemall:查询地址不存在')
        self.assertEqual(db_data.get('name'),name)



