import csvv
from ddt import data, ddt, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


@ddt()
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @data(csvv.read_file())
    def test(self, value1, value2):
        self.driver.find_element(By.NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, '密码').send_keys('123456')
        self.driver.find_element(By.ID, '登录').click()
        self.driver.find_element(By.LINK_TEXT, '商品单位').click()
        self.driver.find_elements(By.TAG_NAME, '新增')[0].click()
        self.driver.find_element(By.CLASS_NAME, '商品单位名称').send_keys(value1)
        self.driver.find_element(By.XPATH, '保存').click()
        alert = self.driver.switch_to.alert.text
        try:
            self.assertEqual(alert, value2)
        except:
            self.driver.get_screenshot_as_file('error.png')
        finally:
            pass


if __name__ == '__main__':
    unittest.main()
