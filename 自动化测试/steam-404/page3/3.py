from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from ddt import ddt, unpack, data
import csv


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @data(*csv.reader(open('testdata.csv')))
    @unpack
    def test(self,value):
        self.driver.find_element(By.ID, 'XTGLY')
        self.driver.find_element(By.NAME,'123456')
        self.driver.find_element(By.TAG_NAME,'登录').click()
        self.driver.find_element(By.LINK_TEXT, '商品分类').click()
        self.driver.find_element(By.XPATH,'新增').click()
        self.driver.find_element(By.CLASS_NAME,'商品分类名称').send_keys(value)
        self.driver.find_element(By.XPATH,'保存').click()
        assertMessage=self.driver.find_element(By.LINK_TEXT,'提示信息').click()
        assertMessage=assertMessage.text
        self.assertEquals(assertMessage,'预期值')

if __name__ == '__main__':
    unittest.main()