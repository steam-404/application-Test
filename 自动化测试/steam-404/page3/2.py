from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def testdenglu01(self):
        self.driver.find_element(By.NAME,'用户名').send_keys('XTGLY')
        self.driver.find_element(By.XPATH,'登录').click()
    def testdenglu02(self):
        self.driver.find_element(By.NAME,'用户名').send_keys('XTGLY')
        self.driver.find_element(By.ID,'密码').send_keys('123456')
        self.driver.find_element(By.TAG_NAME,'登录').click()
        self.driver.find_element(By.LINK_TEXT,'客户信息').click()
        self.driver.find_elements(By.LINK_TEXT,'数据')[0].clear()
        look=self.driver.find_element(By.ID,'查看')
        self.driver.get_screenshot_as_file('')

if __name__ == '__main__':
    unittest.main()