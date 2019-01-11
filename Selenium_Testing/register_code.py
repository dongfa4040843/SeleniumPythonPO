from selenium import webdriver
from time import sleep
import random
from PIL import Image
from Selenium_Testing.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
#初始化浏览器
def driver_init():
    driver.get("http://www.5itest.cn/register?goto=/")
    driver.maximize_window()
    sleep(2)

#获取element的信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#获取随机数
def get_range_user():
    user_info = ''.join(random.sample("1234567asdf", 5))
    return user_info

#获取图片
def get_code_image(file_name):
    code_element = driver.find_element_by_id("getcode_num")
    driver.save_screenshot(file_name)
    left = code_element.location['x']
    top = code_element.location['y']
    wide = code_element.size["width"] + left
    high = code_element.size["height"] + top
    im = Image.open(file_name)
    img = im.crop((left, top, wide, high))
    img.save(file_name)

#解析图片
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "81856", "3fe29039df2841c5b3c9804156a2dc31")
    r.addBodyPara("img_base64", "")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "1")
    r.addFilePara("image", file_name)  # 文件上传时设置
    res = r.post()
    text = res.json()["showapi_res_body"]["Result"]
    return text

#主程序
def run_main():
    driver_init()
    get_range = get_range_user()
    user_email = get_range+"@asd.com"
    file_name = "E:\\im2.png"
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(get_range)
    get_element("register_password").send_keys("123456")
    get_code_image(file_name)
    image = code_online(file_name)
    get_element("captcha_code").send_keys(image)
    sleep(3)
    driver.close()
run_main()





