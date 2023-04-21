from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from ddt import ddt, data, unpack
import csv


@ddt()
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @data(*csv.reader(open('testdata.csv')))
    @unpack
    def test(self, value):
        self.driver.find_element(By.CLASS_NAME, '用户名').send_keys('XTGLY')
        self.driver.find_element(By.ID, '密码').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, '登录').click()
        self.driver.find_elements(By.PARTIAL_LINK_TEXT, '商品品牌')[0].click()
        self.driver.find_elements(By.TAG_NAME, '新增')[0].click()
        self.driver.find_element(By.CLASS_NAME, '商品品牌名称').send_keys(value)
        self.driver.find_element(By.XPATH, '保存').click()
        self.driver.find_element(By.CLASS_NAME, '提示信息').click()
        alertMessage = self.driver.switch_to_alert()
        alertMessage = alertMessage.text
        self.assertEquals(alertMessage, '预期结果')
