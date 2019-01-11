#显示等待与隐式等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from UnitTest.ShowapiRequest import ShowapiRequest
from time import sleep
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
import random


driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register?goto=/")
driver.maximize_window()
print(EC.title_contains("注册"))
driver.save_screenshot("E:\\wenjian\\picture.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("E:\\wenjian\\picture.png")
img = im.crop((left,top,right,height))
img.save("E:\\wenjian\\picture1.png")

r = ShowapiRequest("http://route.showapi.com/184-4","81856","3fe29039df2841c5b3c9804156a2dc31" )
r.addBodyPara("img_base64", "35")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"E:\\wenjian\\picture1.png") #文件上传时设置
res = r.post()
text = res.json()["showapi_res_body"]["Result"]
print(text)
driver.find_element_by_id("captcha_code").send_keys(text)
# for i in range(5):
#     user_email = ''.join(random.sample("1234567asdf", 5))+"@.163.com"
#     driver.find_element_by_id("register_email").send_keys(user_email)
#     driver.find_element_by_id("register_email").clear()
#     print(user_email)

sleep(3)

# locator = (By.CLASS_NAME,"controls")
# WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator))
# email_element = driver.find_element_by_id("register_email")
# print(email_element.get_attribute("placeholder"))
# email_element.send_keys("dongfa1234567@163.com")
# print(email_element.get_attribute("value"))
driver.close()

# driver.find_element_by_id("register_email").send_keys("dongfa1234567@163.com")
# user_name_element = driver.find_elements_by_class_name("controls")[1]
# user_element = user_name_element.find_element_by_class_name("form-control")
# user_element.send_keys("dongfa")
# driver.find_element_by_name("password").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")
sleep(3)














































