import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.CLASS_NAME, '用户名').send_keys('XTGLY')
        self.driver.find_elements(By.TAG_NAME, '密码')[0].send_keys('123456')
        self.driver.find_element(By.ID, '登录').click()

    def test_denglu02(self):
        self.driver.find_element(By.CLASS_NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.ID, '密码').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, '登录').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '仓库信息').click()
        self.driver.find_element(By.XPATH, '禁用').click()
        self.driver.switch_to.alert.accept()

if __name__ == '__main__':
    unittest.main()
