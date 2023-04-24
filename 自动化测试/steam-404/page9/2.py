from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, '密码').send_keys('123456')
        self.driver.find_element(By.XPATH, '登录').click()

    def test_denglu02(self):
        self.driver.find_element(By.ID, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, '密码').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, '登录').click()
        self.driver.find_element(By.LINK_TEXT, '供应商信息').click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])
        self.driver.get_screenshot_as_file('error.png')


if __name__ == '__main__':
    unittest.main()
