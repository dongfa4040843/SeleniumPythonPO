from selenium import webdriver
from base.find_element import Find_Element
from time import sleep
driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register?goto=/")
fe = Find_Element(driver)
email_ele = fe.get_element("user_email")
#email_element = driver.find_element_by_id("register_email")
#print(email_element.get_attribute("placeholder"))
email_ele.send_keys("222")
driver.find_element_by_id("register_nickname").send_keys("123456")
element = driver.find_element_by_id("register_email-error")
print(element.text)

sleep(4)
driver.close()


