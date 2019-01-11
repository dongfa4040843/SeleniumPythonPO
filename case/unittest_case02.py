import unittest
class FirstCase02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这个是全部case的前置条件")

    @classmethod
    def tearDownClass(cls):
        print("这个是全部case的后置条件")

    def setUp(self):
        print("这个是case的前置条件")

    def tearDown(self):
        print("这个是case的后置条件")

    def testfirst001(self):
        print("这个是第一条01_case")

    @unittest.skip("跳过这条case")
    def testfirst002(self):
        print("这个是第二条02_case")

    def testfirst003(self):
        print("这个是第三条03_case")

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02("testfirst002"))
    suite.addTest(FirstCase02("testfirst003"))
    suite.addTest(FirstCase02("testfirst001"))
    unittest.TextTestRunner().run(suite)


