from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.ID, '用户名').send_keys('XTGLY')
driver.find_element(By.NAME, '密码').send_keys('123456')
driver.find_element(By.CLASS_NAME, '登录').click()
driver.find_element(By.NAME, '上传图片').send_keys('路径')
driver.get_screenshot_as_file('test_picyure.png')
