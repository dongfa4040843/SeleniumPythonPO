import unittest
        # 深度优化测试用例
class StringReplaceTestcase(unittest.TestCase):

    def setUp(self):
        """定义原字符串"""
        self.source = "selenium"

    def testBlank(self):
        """测试空字符串的替换"""
        expect = "selenium"
        result = self.source.replace("", "")
        self.assertEqual(expect, result)
    # @unittest.skipUnless(2>3,"火影忍者")#如果条件为真那么执行，相反条件为假不执行
    # @unittest.skipIf(4>3,"123") 如果条件为真就不执行，相反条件为假时，执行用例
    # @unittest.skip("它不会被执行了")
    def testBlankOrd(self):
        """测试空字符串的替换常规字符*"""
        expext = "se*le*n*ium"
        result = self.source.replace("","*")
        self.assertEqual(expext,result)

    def testOrdBlank(self):
        """测试常规字符串替换空字符串"""
        expext = "seleni"
        result = self.source.replace("um", "")
        self.assertEqual(expext, result)

    def testOrd(self):
        """测试常规字符串替换"""
        expext = "selenium"
        result = self.source.replace("m","mm")
        self.assertEqual(expext,result)
