from base.find_element import Find_Element
class RegisterPage(object):
    def __init__(self,driver):
        self.fd = Find_Element(driver)
    #获取邮箱的定位信息
    def get_email_element(self):
        return self.fd.get_element("user_email")

    #获取用户名的定位信息
    def get_name_element(self):
        return self.fd.get_element("user_name")

    #获取密码的定位信息
    def get_password_element(self):
        return self.fd.get_element("password")

    #获取验证码的定位信息
    def get_code_element(self):
        return self.fd.get_element("code_text")

    #获取注册的定位信息
    def get_button_element(self):
        return self.fd.get_element("register_button")

    #获取邮箱错误的信息
    def get_email_element_error(self):
        return self.fd.get_element("user_email_error")

    #获取用户名的错误的信息
    def get_name_element_error(self):
        return self.fd.get_element("user_name_error")

    #获取密码错误的信息
    def get_password_element_error(self):
        return self.fd.get_element("password_error")

    #获取验证码错误的信息
    def get_code_element_error(self):
        return self.fd.get_element("code_text_error")
