from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get('https://wwww.baidu.com/')
driver.implicitly_wait(5)

driver.find_element(By.ID, '用户名').send_keys('XTGLY')
driver.find_element(By.NAME).send_keys('123456')

login_button = driver.find_element(By.TAG_NAME, '登录')
action.click(login_button).perform()
driver.find_element(By.ID, '请输入商品编号').send_keys('test001')
action.double_click().perform()
