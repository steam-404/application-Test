import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.ID, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.ID, '密码').send_keys('123456')
        self.driver.find_element(By.CLASS_NAME, '登录').click()
        sleep(1)

    def test_denglu02(self):
        self.driver.find_element(By.NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.NAME, '密码').send_keys('123456')
        self.driver.find_element(By.CLASS_NAME, '登录').click()
        sleep(1)
        self.driver.find_element(By.LINK_TEXT, '仓库信息').click()


if __name__ == '__main__':
    unittest.main()
