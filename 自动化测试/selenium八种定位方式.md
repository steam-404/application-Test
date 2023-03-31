```python
pip install selenium # 安装

from selenium import webdriver	#导入

driver = webdriver.Chrome()
# selenium八种元定位方式

driver.find_element_by_id()
# id选择器

driver.find_element_by_name()
# name选择器

driver.find_element_by_class_name()
# class选择器

driver.find_element_by_tag_name()
# 标签选择器

driver.find_element_by_css_selector()
# css选择器

driver.find_element_by_xpath()
# xpath定位

driver.find_element_by_link_text()
# 链接选择器(链接需要写全)

find_element_by_partial_link_text()
# 链接选择器(链接不需要写全)
```