from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.NAME,'用户名').send_keys('XTGLY')
driver.find_element(By.ID,'密码').send_keys('123456')
driver.find_element(By.TAG_NAME,'登录').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'商品品牌').click()
alert1=driver.switch_to_alert()
alert1.dismiss()
driver.find_elements(By.TAG_NAME,'商品品牌禁用')[0].click()
alert2=driver.switch_to_alert()
alert2.accept()
