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
geo_path=os.path.join(data_path,'geo.txt')
class TestAddress(unittest.TestCase):
    url = urljoin(host,'/wx/address/save')
    url_geo='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'

    # @classmethod
    # def setUpClass(cls):
    #     token = tools.WxLogin(**test_user).get_token() #登录获取token
    #     cls.header = {'X-Litemall-Token':token} #拼header
    
    @parameterized.parameterized.expand(GetTestData.data_for_txt(geo_path))
    def test_geo(self,address,city):
        '''测试geo地址返回'''
        data = {'address':address, \
                'opt': '', \
                'city': city, \
                'ak':"70231a4fa9c047d381cc55c8ff75e0bf"}
        res=MyRequest(self.url_geo,data)
        self.assertEqual(0,res.response.get('status'),msg="返回失败")
        
        

    # @parameterized.parameterized.expand(GetTestData.data_for_excel(address_data_path))
    # def test_create(self,name,tel,isDefault):
    #     '''测试添加收货地址'''
    #     is_default = True if isDefault=='1' else False
    #     data = {
    #         "name": name,
    #         "tel": "%d"%tel,
    #         "country": "",
    #         "province": "北京市",
    #         "city": "市辖区",
    #         "county": "东城区",
    #         "areaCode": "110101",
    #         "postalCode": "",
    #         "addressDetail": "西二旗",
    #         "isDefault": is_default
    #     }
    #     req = MyRequest(self.url,'post',data=data,headers=self.header)
    #     self.assertEqual(0,req.response.get('errno'),msg='添加失败')
    #     address_id = req.response.get('data')
    #     sql = 'select name from litemall_address where id = %s;'%address_id
    #     db_data = mysql.execute_one(sql)
    #     self.assertIsNotNone(db_data,msg='litemall:查询地址不存在')
    #     self.assertEqual(db_data.get('name'),name)



