from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.find_element(By.NAME,'用户名').send_keys('XTGLY')
driver.find_element(By.ID,'密码').send_keys('123456')
driver.find_element(By.TAG_NAME,'登录').click()
driver.find_element(By.LINK_TEXT,'仓库信息').click()
driver.find_elements(By.TAG_NAME)[0].click()
alert=driver.switch_to_alert()
alert.accept()
driver.get_screenshot_as_file('D:\\test_accept01.png')
