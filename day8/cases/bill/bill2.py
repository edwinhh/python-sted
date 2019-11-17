import unittest
class Test2(unittest.TestCase):
    def test1(self):
        self.assertTrue(False,msg='Test2里面测试出错了')
    def test2(self):
        self.assertEqual(1,1)
