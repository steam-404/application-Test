from selenium import webdriver
from ddt import ddt, data, unpack
import unittest
import csv


@ddt()
class Test(unittest.TestCase):
    def setUpClass(cls):
        pass

    def tearDownClass(cls):
        pass

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @data(*csv.reader(open('testdata.csv')))
    @unpack
    def test01(self,value):
        self.driver.find_element_by_class_name('用户名').send_keys('XTGLY')
        self.driver.find_element("密码").send_keys('123456')
        self.driver.find_element_by_tag_name('登录').click()
        self.driver.find_elements_by_tag_name('新增').click()
        self.driver.find_element_by_class_name("商品品牌名称").send_keys(value)
        self.driver.find_element_by_xpath('保存').click()
        获取的信息=self.driver.find_element_by_class_name("获取信息")
        if(self.assertEquals(获取的信息,'期望值' == False)):
            self.driver.get_screenshot_as_png()

if __name__ == '__main__':
    unittest.main()

