from page.register_page import RegisterPage
from util.get_code import GetCode
class RegisterHandle(object):
    #输入邮箱
    def __init__(self,driver):
        self.driver = driver
        self.get_code_text = GetCode(self.driver)
        self.register_p = RegisterPage(self.driver)
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_name(self,name):
        self.register_p.get_name_element().send_keys(name)

    # 输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

   # 输入验证码
    def send_user_code(self,code):
        #code = self.get_code_text.code_online(file_name)
        self.register_p.get_code_element().send_keys(code)

    #获取文字信息
    def send_user_text(self,info,user_info):
        try:
            if info == "user_email_error":
                text = self.register_p.get_email_element_error().text

            elif info == "user_name_error":
                text = self.register_p.get_name_element_error().text
            elif info == "password_error":
                text = self.register_p.get_password_element_error().text
            else:
                text = self.register_p.get_code_element_error().text
        except:
            text = None
        return text
    #获取注册按钮的定位xinxi
    def click_register_button(self):
        self.register_p.get_button_element().click()

    #获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text