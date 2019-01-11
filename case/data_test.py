import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这个是每个case的前置条件")

    def tearDown(self):
        print("这个是每个case的后置条件")
    #邮箱、用户名，密码，验证码、错误定位信息元素、错误定位信息
    @ddt.data(
        [1,2,3,4,5,6],
        [3,4],
        [5,6]
    )
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)

if __name__ == "__main__":
    unittest.main()