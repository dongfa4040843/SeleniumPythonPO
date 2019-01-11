from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

import smtplib
import unittest
import time
import os

#==============发送邮件================
def sendReport(file_new):
    with open(file_new,"rb")as f:
        mail_body = f.read()

    #构造MIMEtext对象，作为邮件以内容的形式进行附加
    msg = MIMEText(mail_body,"html","utf-8")
    msg["Subject"] = Header("Baidu自动化测试脚本报告","utf-8")
    msg["From"] = "dongfa1234567@163.com"#发送地址
    msg["to"] = "dongfa1234567@163.com"#收件地址

    smtp = smtplib.SMTP("smtp.163.com")
    smtp.login("dongfa1234567@163.com","dongfa4040843")#邮箱的账户和密码（授权码）
    smtp.sendmail(msg["From"],msg["to"].split(";"),msg.as_string())

    smtp.quit()
    print("The Html Report is send out!!!")

def newReport(testReport):
    lists = os.listdir(testReport)
    lists2 = sorted(lists)#获得排序后的测试报告
    file_new = os.path.join(testReport,lists2[-1])#获取最新的html报告
    print(file_new)
    return file_new

#====================运行======================
if __name__ == "__main__":
    test_dir = "E:\\Users\\dongf\\PycharmProjects\\BaiDeom\\Email" #测试用例的路径
    test_report = "E:\\Users\\dongf\\PycharmProjects\\BaiDeom\\Email\\Result" #测试报告的路径

    discover = unittest.defaultTestLoader.discover(test_dir,pattern="Baidu.py")

    now = time.strftime("%Y-%m-%d %H%M%S") #获取当前时间
    filename = test_report + "\\" + now + "result.html" #拼接出测试报告名称

    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,title="测试报告",description="测试脚本执行情况")
    runner.run(discover)
    fp.close()

    new_report = newReport(test_report)  #获取最新的测试报告
    print(new_report)
    sendReport(new_report) #发送测试报告邮件

