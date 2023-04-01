### 强制等待

```python
import time

time.sleep("second")
```



### 隐式等待

```python
from selenium import webdriver

driver=webdriver.Chorme()
driver.get("url")
driver.implicitly_wait("second")
# 设置一个等待时间，如果在这个等待时间内，网页加载完成，则执行下一步；否则一直等待时间截止，然后再执行下一步。这样也就会有个弊端，程序会一直等待整个页面加载完成，直到超时，但有时候我需要的那个元素早就加载完成了，只是页面上有个别其他元素加载特别慢，我仍要等待页面全部加载完成才能执行下一步。
```



### 显示等待

```
from selenium.webdriver.support.wait import WebDriverWait
```

