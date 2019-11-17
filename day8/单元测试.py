import unittest
def add(a,b):
    return a+b

#python  unittest
#java junit
#php phpunit

class AddTest(unittest.TestCase):
    def test_normal(self):
        result = add(1,1)
        self.assertEqual(2,result)

    def test_error(self):
        result = add(1,1)
        self.assertEqual(1,result,'结果计算错误')

unittest.main()

