import csvv
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import data, ddt, unpack

dataMessage = csvv.read_file()


@ddt
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://411.free.svipss/top/')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @data(dataMessage)
    @unpack
    @unpack
    def test(self, value):
        self.driver.find_element(By.CLASS_NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.ID, '密码').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, '登录').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '商品品牌').click()
        self.driver.find_elements(By.TAG_NAME, '新增')[0].click()
        self.driver.find_element(By.CLASS_NAME, '品牌输入框').send_keys(value)
        self.driver.find_element(By.XPATH, '保存').click()
        alert_text = self.driver.switch_to.alert.text
        try:
            self.assert_(alert_text, '预期结果')
        except:
            self.driver.get_screenshot_as_file("{}.png".format(value))


if __name__ == '__main__':
    unittest.main()
