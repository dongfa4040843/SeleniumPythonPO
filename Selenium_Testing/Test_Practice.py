from selenium import webdriver
from time import sleep,ctime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
from PIL import Image
import pytesseract
from Selenium_Testing.ShowapiRequest import ShowapiRequest


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.5itest.cn/register?goto=/")
sleep(2)
test_title = driver.title
print("5itetst的title是：%s"%(test_title))
actual_title = "注册 - 乐学 - 乐学，让学习更有效 - Powered By EduSoho"
if test_title==actual_title:
    print(True)
else:
    print(False)

code_element = driver.find_element_by_id("getcode_num")
driver.save_screenshot("E:\\im.png")
print(code_element.location)#{'x':123,'y':456}
left = code_element.location['x']
top = code_element.location['y']
wide = code_element.size["width"]+left
high = code_element.size["height"]+top
im = Image.open("E:\\im.png")
img = im.crop((left,top,wide,high))
img.save("E:\\im2.png")

r = ShowapiRequest("http://route.showapi.com/184-4","81856","3fe29039df2841c5b3c9804156a2dc31" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "1")
r.addFilePara("image", r"E:\\im2.png") #文件上传时设置
res = r.post()
text = res.json()["showapi_res_body"]["Result"]
print(text) # 返回信息
driver.find_element_by_id("captcha_code").send_keys(text)
#driver.close()

