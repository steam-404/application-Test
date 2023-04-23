from csvv import ReadFile
import unittest
from selenium import webdriver
from ddt import data, ddt, unpack, file_data
from selenium.webdriver.common.by import By

dataMessage = ReadFile()


@ddt
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @data(*dataMessage)
    @unpack
    @unpack
    # 需要解包两次 艹
    def test(self, value):
        print(value)
        self.driver.find_element(By.ID, 'kw').send_keys(value)
        self.driver.find_element(By.ID, 'su').click()


if __name__ == '__main__':
    unittest.main()
