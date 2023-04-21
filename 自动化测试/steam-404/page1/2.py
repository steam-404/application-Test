from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.CLASS_NAME, '用户名').send_keys('XTGLLY')
        self.driver.find_element(By.NAME, '密码').send_keys('123456')
        self.driver.find_element(By.ID, '登录').click()

    def test_denglu02(self):
        self.driver.find_element(By.NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.ID, '密码').send_keys('123456')
        self.driver.find_element(By.TAG_NAME,'登录').click()
        self.driver.find_element(By.XPATH, '新增').click()
        self.driver.get_screenshot_as_file("denglu_02.png")

if __name__ == '__main__':
    unittest.main()