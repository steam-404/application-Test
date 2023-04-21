import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def test_denglu01(self):
        self.driver.find_element('用户名').send_keys('XTGLY')
        self.driver.find_element('密码').send_keys('123456')
        self.driver.find_element('登录').click()

    def test_denglu02(self):
        self.driver.find_element('用户名').send_keys('XTGLY')
        self.driver.find_element('密码').send_keys('123456')
        self.driver.find_element('登录').click()
        self.driver.find_element_by_partial_link_text('客户xx').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()