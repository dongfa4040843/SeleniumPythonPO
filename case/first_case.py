from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
from time import sleep
from log_001.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name = r"E:\Users\dongf\PycharmProjects\BaiDeom\case\report\test001.png"
        cls.log = UserLog()
        cls.logger = cls.log.get_log()


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register?goto=/")
        self.logger.info("这个是日志")
        self.login = RegisterBusiness(self.driver)
    def tearDown(self):
        sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
        print("这个是case的后置条件")
        # 邮箱、用户名，密码，验证码、错误定位信息元素、错误定位信息
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_login_email_error(self):
        email_error = self.login.login_email_error("456","d123456","df123456",self.file_name)
        self.assertFalse(email_error,"case失败")
        # if email_error == True:
        #     print("注册成功，此条case失败")

    def test_login_username_error(self):
        name_error = self.login.login_name_error("123456@163.com","f12345","123456",self.file_name)
        self.assertFalse(name_error)
        # if name_error == True:
        #     print("注册成功，此条case失败")

    def test_login_password_error(self):
        password_error = self.login.login_password_error("123456@163.com", "d123456", "1234567",self.file_name)
        self.assertFalse(password_error)
        # if password_error == True:
        #     print("注册成功，此条case失败")

    def test_login_code_error(self):
        code_error = self.login.login_code_error("123456@163.com", "d12345678", "df1234567",self.file_name)
        self.assertFalse(code_error)
        # if code_error == True:
        #     print("注册成功，此条case失败")

    def test_login_success(self):
        test_success = self.login.user_base("123456@163.com", "de123456", "dgf123456",self.file_name)
        success = self.login.error_base()
        self.assertFalse(test_success)
"""
def main():
    first = FirstCase()
    first.test_login_email_error()
    first.test_login_username_error()
    first.test_login_password_error()
    first.test_login_code_error()
    first.test_login_success()
"""
if __name__ == "__main__":
    suite = unittest.TestSuite()
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,"wb")
    suite.addTest(FirstCase("test_login_email_error"))
    suite.addTest(FirstCase("test_login_username_error"))
    suite.addTest(FirstCase("test_login_password_error"))
    suite.addTest(FirstCase("test_login_code_error"))
    suite.addTest(FirstCase("test_login_success"))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="用例的测试报告",description="测试报告详情",verbosity=2)
    runner.run(suite)


