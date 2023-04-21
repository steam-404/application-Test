from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('xxxxxx')
driver.find_element_by_name('username').send_keys('XTGLY')
driver.find_element_by_name('passwpord').send_keys('123456')
driver.find_element_by_class_name('login').click()
driver.find_element_by_partial_link_text('user-message').click()
driver.find_element_bys_link_text()
sleep(2)
driver.save_screenshot('test_target01.png')
driver.find_element("查看客户弹窗").click()

