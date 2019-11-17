import unittest
class TestOrder(unittest.TestCase):
    def test1(self):
        self.assertTrue(False,msg='TestOrder1里面测试出错了')
    def test2(self):
        self.assertEqual(1,1)
