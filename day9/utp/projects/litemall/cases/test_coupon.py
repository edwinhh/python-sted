import unittest
from urllib.parse import urljoin
from projects.litemall.const import host,test_admin_user
from projects.litemall import tools
from utils.request import MyRequest
from utils.utils import get_value

class TestCoupon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = tools.AdminLogin(**test_admin_user).get_token() #登录获取token
        cls.header = {'X-Litemall-Admin-Token':token} #拼header


    def add_coupon(self):
        url = urljoin(host, '/admin/coupon/create')
        name = 'Python自动化测试优惠券'
        data = {
            "name": name,
            "desc": "介绍",
            "total": "29",
            "discount": "1",
            "min": "999",
            "limit": 1,
            "type": 0,
            "status": 0,
            "goodsType": 0,
            "goodsValue": [],
            "timeType": 0,
            "days": "1",
            "startTime": None,
            "endTime": None
        }
        req = MyRequest(url, 'post', data=data, headers=self.header)
        print(req.response)
        self.assertEqual(0, req.response.get('errno'), msg='添加失败')
        coupon_id = get_value(req.response,'id')
        return name,coupon_id

    def test_coupon(self):
        '''测试添加优惠券后，在首页是否查到'''
        url = urljoin(host, '/wx/coupon/list')
        name,id = self.add_coupon() #添加优惠券
        req = MyRequest(url)
        coupon_list = get_value(req.response,'list')
        tag = False
        for coupon in coupon_list:
            if name  == coupon.get('name') and coupon.get('id') == id:
                tag = True
        self.assertTrue(tag,msg='添加的优惠券查不到')




