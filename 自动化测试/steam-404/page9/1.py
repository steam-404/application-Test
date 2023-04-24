from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.find_element(By.ID, '用户名').send_keys('XTGLY')
driver.find_element(By.CLASS_NAME, '密码').send_keys('123456')
driver.find_elements(By.TAG_NAME, '新增')[0].click()
select = Select(driver.find_element(By.ID, '商品分类'))
select.select_by_value('测试')
select = Select(driver.find_elements(By.TAG_NAME, '商品品牌')[0])
select.select_by_visible_text('测试')
driver.get_screenshot_as_file('D:\\test_Select01.png')
