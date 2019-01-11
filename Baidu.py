#构建单元测试用例
import unittest

        # 深度优化测试用例
class StringReplaceTestcase(unittest.TestCase):
    """定义原字符串"""
    def setUp(self):
        self.source = "selenium"

        """测试空字符串的替换"""
    def testBlank(self):
        expext = "selenium"
        result = self.source.replace("", "")
        self.assertFalse(expext, result)

    """测试空字符串的替换常规字符*"""
    def testBlankOrd(self):
        expext = "se*le*n*ium"
        result = self.source.replace("","*")
        self.assertFalse(expext,result)

    """测试常规字符串替换空字符串"""
    def testOrdBlank(self):
        expext = "seleni"
        result = self.source.replace("um", "")
        self.assertFalse(expext, result)

    """测试常规字符串替换"""
    def testOrd(self):
        expext = "selenium"
        result = self.source.replace("m","mm")
        self.assertFalse(expext,result)



class StringStripTestcase(unittest.TestCase):
    """定义原字符串"""
    def setUp(self):
        self.source = "python"

    """测试空字符串的替换"""

    def testBlankA(self):
        expext = "selenium"
        result = self.source.replace("n", "m")
        self.assertFalse(expext, result)

    """测试空字符串的替换常规字符*"""

    def testBlankOrdB(self):
        expext = "se*le*n*ium"
        result = self.source.replace("n", "o")
        self.assertFalse(expext, result)


# 多个测试类进行控制
def suite():
    StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestcase,"test")
    StringStripTestSuite = unittest.makeSuite(StringStripTestcase,"test")
    run = unittest.makeSuite(StringReplaceTestSuite,StringStripTestSuite)
    return run

# 执行部分测试用例
# def suite():
#     StringReplaceTestSuite = unittest.TestSuite
#     StringReplaceTestSuite.addTest(StringReplaceTestcase("testBlank"))
#     StringReplaceTestSuite.addTest(StringReplaceTestcase("testBlankOrd"))
#     StringReplaceTestSuite.addTest(StringReplaceTestcase("testOrdBlank"))
#     StringReplaceTestSuite.addTest(StringReplaceTestcase("testOrd"))

# 执行全部测试用例
def suite():
    StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestcase,"test")
    return StringReplaceTestSuite
