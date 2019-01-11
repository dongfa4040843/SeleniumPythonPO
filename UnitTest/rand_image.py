import pytesseract
from PIL import Image
from UnitTest.ShowapiRequest import ShowapiRequest
# image = Image.open("E:\\imooc1.png")
# text = pytesseract.image_to_string(image)
# print(text)
r = ShowapiRequest("http://route.showapi.com/184-4","81856","3fe29039df2841c5b3c9804156a2dc31" )
r.addBodyPara("img_base64", "35")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"E:\\imooc1.png") #文件上传时设置
res = r.post()
text = res.json()["showapi_res_body"]["Result"]
print(text) # 返回信息
