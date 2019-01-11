import unittest
from selenium import webdriver
from  time import sleep

# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("火影忍者")
# driver.find_element_by_xpath("//input[@id='su']").click()
# driver.quit()
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//input[@id='kw']").send_keys("火影忍者")
        driver.find_element_by_xpath("//input[@id='su']").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()