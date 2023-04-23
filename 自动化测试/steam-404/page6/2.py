import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.ID, '密码').send_keys('123456')
        self.driver.find_element(By.CLASS_NAME, '登录').click()

    def test_denglu02(self):
        self.driver.find_element(By.NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, '密码').send_keys('123456')
        self.driver.find_element(By.ID, '登录').click()
        select = Select(self.driver.find_element(By.NAME, '商品品牌'))
        select.select_by_visible_text('测试')


if __name__ == '__main__':
    unittest.main()
