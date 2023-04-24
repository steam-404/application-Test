from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('')
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.NAME, '用户名').send_keys('XTGLY')
driver.find_element(By.ID, '密码').send_keys('123456')
driver.find_element(By.TAG_NAME, '登录').click()
driver.find_element(By.XPATH, '禁用').click()
driver.switch_to.alert.accept()
driver.get_screenshot_as_file('D:\\test_accept01.png')

