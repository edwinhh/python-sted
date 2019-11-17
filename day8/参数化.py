import parameterized
import unittest,BeautifulReport

#数据驱动
#代码驱动
#关键字驱动
data = [
    ['admin','123456',True,'正常登录'],
    ['admin','1122',False,'冻结用户登录'],
    ['sdfsdf','1111',False,'黑名单用户登录']
]
data2 = [
    ['admin','123456',True],
    ['admin','1122',False],
    ['sdfsdf','1111',False]
]
def login(user,password):
    if user=='admin' and password=='123456':
        return True
    return False


class LoginTest(unittest.TestCase):

    @parameterized.parameterized.expand(data)
    def test_login(self,user,password,expect,desc):
        self._testMethodDoc = desc #自己指定
        result = login(user,password)
        self.assertEqual(expect,result)

    @parameterized.parameterized.expand(data2)
    def test_login2(self,user,password,expect):
        '''登录'''
        result = login(user,password)
        self.assertEqual(expect,result)

bf = BeautifulReport.BeautifulReport(unittest.makeSuite(LoginTest))
bf.report(filename='11-17测试报告',description='接口测试报告')



