from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """
    BasePage封装了所有页面的公共的方法，比如driver  find_element等
    """
    #实例化BasePage类时，让其最先执行__init__方法。该方法的参数就是BasePage的参数（入参）
    #__init__方法不能有返回值。
    def __init__(self,selenium_driver,base_url):
        self.driver = selenium_driver
        self.base_url = base_url

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def _open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def open(self):
        self._open(self.base_url,self.pagetitle)

    #定位元素
    #*loc 任意数量的位置参数
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未能找到 %s 元素"%(self,loc))

    def script(self,scr):
        self.driver.excute_script(scr)

    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            loc = getattr(self," %s"%loc)#getattr相当于实现了self.loc
            if click_first:
                self.find_element(*loc).click()
            if click_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s y页面中未找到 %s 元素"%(self,loc))



