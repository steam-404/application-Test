import csvv
from ddt import data, ddt, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


@ddt
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @data(csvv.read_file())
    @unpack
    @unpack
    def test(self, value1, value2):
        self.driver.find_element(By.ID, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.NAME, '密码').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, '登录').click()
        self.driver.find_element(By.LINK_TEXT, '商品分类').click()
        self.driver.find_element(By.XPATH, '新增').click()
        self.driver.find_element(By.CLASS_NAME).send_keys(value1)
        alert_text = self.driver.switch_to.alert.text
        try:
            self.assertEqual(alert_text, value2)
        except:
            self.driver.get_screenshot_as_file('')
        finally:
            pass
