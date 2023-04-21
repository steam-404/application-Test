from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_elements(By.TAG_NAME,'用户')[0].send_keys('XTGLY')
        self.driver.find_elements(By.TAG_NAME, '密码')[0].send_keys('123456')
        self.driver.find_element(By.NAME,'登录').click()

    def test_denglu02(self):
        self.driver.find_element(By.CLASS_NAME,'用户名').send_keys('XTGLY')
        self.driver.find_element(By.NAME,'密码').send_keys('123456')
        self.driver.find_element(By.ID,'登录').click()
        商品分类=self.driver.find_element(By.ID,'商品分类')
        select=Select(商品分类)
        select.select_by_value('测试')

if __name__ == '__main__':
    unittest.main()

