from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.ID, '用户名').send_keys('XTGLY')
driver.find_element(By.ID, '密码').send_keys('123456')
driver.find_element(By.TAG_NAME, '登录').click()
driver.find_element(By.LINK_TEXT, '供应商').click()
driver.find_elements(By.LINK_TEXT, '查看')[0].click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
sleep(3)
driver.get_screenshot_as_file('D:\\test_handles.png')
driver.find_element('查看供应商x').click()
