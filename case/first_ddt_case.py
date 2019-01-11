#邮箱、用户名，密码，验证码、错误定位信息元素、错误定位信息
import ddt
import os
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.split(curPath)[0]
print(rootPath)
pt = sys.path.append(rootPath)
print(pt)

from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner

from time import sleep
from util.excel_util import ExcelUtil
from log_001.user_log import UserLog
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    #     cls.file_name = r"E:\Users\dongf\PycharmProjects\BaiDeom\case\report\test002.png"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register?goto=/")
        self.logger.info("thes is log")
        self.login = RegisterBusiness(self.driver)
    def tearDown(self):
        sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        #print("这个是case的后置条件")
        """
    @ddt.data(
        ["12","dongfa123","1234567","111111","user_email_error","请输入有效的电子邮件地址"],
        ["123@163.com","dongfa123","1234567","111111", "user_name_error",  "字符长度必须大于等于4，一个中文字算2个字符"],
        ["1234@163.com","dongfa123","1234567","111111", "password_error", "最少需要输入 5 个字符"]

    )
    @ddt.unpack
        """
    @ddt.data(*data)
    #@ddt.unpack
    def test_register_case(self,data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
        self.assertFalse(email_error,"case失败")

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd() + "/report/" + "first_case2.html")
    f = open(file_path, "wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="用例的测试报告1", description="测试报告详情1", verbosity=2)
    runner.run(suite)
