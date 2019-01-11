import unittest
class FirstCase(unittest.TestCase):
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

    def testfirst01(self):
        print("这个是第一条case")

    @unittest.skip("跳过这条case")
    def testfirst02(self):
        print("这个是第二条case")

    def testfirst03(self):
        print("这个是第三条case")

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("testfirst02"))
    suite.addTest(FirstCase("testfirst03"))
    suite.addTest(FirstCase("testfirst01"))
    unittest.TextTestRunner().run(suite)


