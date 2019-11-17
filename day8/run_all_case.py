import unittest,BeautifulReport,os
#
# test_suite = unittest.defaultTestLoader.discover('cases',
#                                     '*.py')
#
# bf = BeautifulReport.BeautifulReport(test_suite)
# bf.report('report2.html','哈哈哈测试报告')


# all_suite = unittest.TestSuite()
# for cur_dir,dirs,files in os.walk('cases'):
#     for dir in dirs:
#         if not dir.startswith('__'):
#             abs_path = os.path.join(cur_dir,dir)
#             test_suite = unittest.defaultTestLoader.discover(abs_path,'*.py')
#             all_suite.addTests(test_suite)
# print(all_suite)

# test_suite = unittest.defaultTestLoader.discover('cases/bill', '*.py')
# print(test_suite)
#思考一下，如果是多层级的目录，应该怎么查找测试用例