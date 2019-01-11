import unittest
from PODome.BasePage import BasePage
from PODome.Search import SearchPage
from time import sleep
from selenium import webdriver

class TestRun(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        sleep(2)
        self.driver.implicitly_wait(30)
        self.url = "http://www.baidu.com"
        sleep(2)
        self.content = "火影忍者"

    def test_search(self):
        baidu_page = SearchPage(self.driver,self.url)
        baidu_page.open()
        baidu_page.search_content(self.content)
        baidu_page.btn_click()
        sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()





