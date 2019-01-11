#import sys
#sys.path.append(r"E:\Users\dongf\PycharmProjects\BaiDeom\Selenium_Testing")
import random
from time import sleep

from PIL import Image
from selenium import webdriver

from Selenium_Testing.ShowapiRequest import ShowapiRequest
from base.find_element import Find_Element


class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)
    #获取driver并且打开url
    def get_driver(self,url,i):
        if i==1:
            driver = webdriver.Chrome()
        elif i==2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    #输入用户信息
    def send_user_info(self,key,data):
        self.get_uesr_element(key).send_keys(data)

    #获取用户的定位信息element
    def get_uesr_element(self,key):
        find_element = Find_Element(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample("1234567asdf", 5))
        return user_info

    # 获取图片
    def get_code_image(self,file_name):
        code_element = self.get_uesr_element("code_image")
        self.driver.save_screenshot(file_name)
        left = code_element.location['x']
        top = code_element.location['y']
        wide = code_element.size["width"] + left
        high = code_element.size["height"] + top
        im = Image.open(file_name)
        img = im.crop((left, top, wide, high))
        img.save(file_name)

    # 解析图片
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "81856", "3fe29039df2841c5b3c9804156a2dc31")
        r.addBodyPara("img_base64", "")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "1")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        return text

    def main(self):
        get_range = self.get_range_user()
        user_email = get_range + "@asd.com"
        file_name = "E:\\im2.png"
        #code_text = self.code_online(file_name)
        self.send_user_info("user_email", user_email)
        self.send_user_info("user_name", get_range)
        self.send_user_info("password", "123456")
        self.send_user_info("code_text",111111)
        self.get_uesr_element("register_button").click()
        code_error = self.get_uesr_element("code_text_error")
        if code_error==None:
            print("注册成功")
        else:
            user_address = get_range+".png"
            self.driver.save_screenshot("E:\\wenjian\\user_address")
        sleep(3)
        self.driver.close()


if __name__ == "__main__":
    for i in range(3):
        run_main = RegisterFunction("http://www.5itest.cn/register?goto=/",i)
        run_main.main()



