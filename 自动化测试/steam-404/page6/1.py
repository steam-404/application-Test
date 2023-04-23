from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(3)
driver.maximize_window()

driver.find_element(By.NAME, '用户名').send_keys('XTGLY')
driver.find_element(By.ID, '密码').send_keys('123456')
driver.find_element(By.CLASS_NAME, '登录').click()
driver.find_element(By.TAG_NAME, '新增').click()
select = Select(driver.find_element(By.XPATH, '商品分类'))
select.select_by_value('测试')
driver.get_screenshot_as_file('D:\\test_Select01.png')
