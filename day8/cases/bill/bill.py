import unittest
class Test1(unittest.TestCase):
    def test1(self):
        self.assertTrue(False,msg='bill里面测试出错了')
    def test2(self):
        self.assertEqual(1,1)
