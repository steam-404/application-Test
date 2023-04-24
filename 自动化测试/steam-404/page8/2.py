import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.CLASS_NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.TAG_NAME, '密码').send_keys('123456')
        self.driver.find_element(By.NAME, '登录').click()

    def test_denglu02(self):
        self.driver.find_element(By.NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, '密码').send_keys('123456')
        self.driver.find_element(By.ID, '登录').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '供应商信息').click()


if __name__ == '__main__':
    unittest.main()
