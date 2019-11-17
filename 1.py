import time,os
import HTMLTestRunner,unittest
import BeautifulReport as bfr


def add(a,b):
    return a+b

class AddTest(unittest.TestCase):
    def test_normal(self):
        result = add(1,1)
        self.assertEqual(2,result)

    def test_error(self):
        result = add(1,1)
        self.assertEqual(1,result)

test_suite=unittest.makeSuite(AddTest)
report=bfr.BeautifulReport(test_suite)
report.report(filename='brf_report.html',description="测试报告",)