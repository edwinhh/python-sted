import unittest
def add(a,b):
    return a+b
import HTMLTestRunner
import BeautifulReport as bfr
class AddTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):#所有用例执行之前执行它
        print('setUpClass')
    @classmethod
    def tearDownClass(cls):#所有用例执行之后执行它
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        #每条用例执行之前都会执行它
    def tearDown(self):
        print('tearDown')
        #每条用例执行之后都会执行它

    def test_normal(self):
        result = add(1,1)
        self.assertEqual(2,result)
        print('test_normal')

    def test_error(self):
        print('test_error')
        result = add(1,1)
        self.assertEqual(1,result,'结果计算错误')

# unittest.main() #这个是
#testcase
#testsuite #用例集合
#testrunner #运行测试用例
#testloader #查找测试用例
test_suite = unittest.makeSuite(AddTest)
report = bfr.BeautifulReport(test_suite)
report.report(filename='bf_report.html',description='bf测试报告',log_path='/Users/nhy/Desktop')

print(report.failure_count) #失败次数
print(report.success_count) #通过次数

#htmltestruner产生测试报告
# file = open('report.html','wb')
# runner = HTMLTestRunner.HTMLTestRunner(file,title='测试报告')
# runner.run(test_suite)
# file.close()