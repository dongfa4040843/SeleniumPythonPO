from PIL import Image
from Selenium_Testing.ShowapiRequest import ShowapiRequest
from time import sleep
class GetCode(object):
    def __init__(self,driver):
        self.driver = driver
    #获取图片
    def get_code_image(self,file_name):
        code_element = self.driver.find_element_by_id("getcode_num")
        self.driver.save_screenshot(file_name)
        left = code_element.location['x']
        top = code_element.location['y']
        wide = code_element.size["width"] + left
        high = code_element.size["height"] + top
        im = Image.open(file_name)
        img = im.crop((left, top, wide, high))
        img.save(file_name)
        sleep(3)

    #解析图片
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