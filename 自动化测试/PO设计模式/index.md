### BasePage.py

```python
class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.baidu.com/')

    def find_element(self, loc):
        return self.driver.find_element(*loc)

    def send_keys(self, loc, text):
        self.find_element(loc).send_keys(text)

    def click(self, loc):
        self.find_element(loc).click()
```

### Search.py

```python
from PO_test02.Page.BasePage import BasePage
from selenium.webdriver.common.by import By


class Search(BasePage):
    input_value = (By.ID, 'kw')
    click_search = (By.ID, 'su')

    def input_messae(self, value):
        self.send_keys(self.input_value, value)

    def clickSearch(self):
        self.click(self.click_search)

    def search(self, value):
        self.open()
        self.input_messae(value)
        self.clickSearch()
```

### switch

```python
from PO_test02.Page.BasePage import BasePage
from selenium.webdriver.common.by import By


class SwitchPage(BasePage):
    images = (By.PARTIAL_LINK_TEXT, '图片')
    tieba = (By.PARTIAL_LINK_TEXT, '贴吧')
    video = (By.PARTIAL_LINK_TEXT, '视频')

    def click_images(self):
        self.find_element(self.images).click()

    def click_tieba(self):
        self.find_element(self.tieba).click()

    def click_video(self):
        self.find_element(self.video).click()

    def click_all(self):
        self.click_images()
        self.click_tieba()
        self.click_video()
```

### main.py

```python
import unittest

from PO_test02.Page.Search import Search
from PO_test02.Page.AddPage import AddPage
from selenium import webdriver


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.search = Search(cls.driver)
        cls.addPage = SwitchPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01(self):
        self.search.search('sb')

    def test02(self):
        self.addPage.click_all()


if __name__ == '__main__':
    unittest.main()
```