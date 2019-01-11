import unittest
from UnitTest.StringReplace import StringReplaceTestcase
from HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    suite = unittest.TestSuite()

    # 运行部分测试用例1
    # suite.addTest(StringReplaceTestcase("testBlank"))
    # suite.addTest(StringReplaceTestcase("testOrd"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # 运行部分测试用例2
    # tests = [StringReplaceTestcase("testBlank"),StringReplaceTestcase("testOrd")]
    # suite.addTests(tests)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    #运行全部测试用例1
    # tests = [StringReplaceTestcase("testBlank"), StringReplaceTestcase("testOrd"),StringReplaceTestcase("testBlankOrd"),StringReplaceTestcase("testOrdBlank")]
    # suite.addTests(tests)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # 运行全部测试用例2
    alltests = unittest.makeSuite(StringReplaceTestcase,"test")
    f = open("E:\\result.html","wb")
    runner = HTMLTestRunner(stream=f,
                            title="测试结果",
                            description="测试用例的执行情况")
    # runner = unittest.TextTestRunner(verbosity=2)
    runner.run(alltests)