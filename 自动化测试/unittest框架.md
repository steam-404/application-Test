### unittest

`TestCase`测试用例

`TestSuite`测试套件&`TestRunner`测试执行

`TestLoader`测试加载

`Fixture`测试夹具

```python
import unittest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(测试用例))
run = unittest.TextTestRunner()
run.run(suite)
```





测试夹具

```python
def setUpClass(cls):
     print('setUpClass')

def tearDownClass(cls):
    print('tarDownClass')
# 每个测试类前/后执行
    
    
def setUp(self):
    print('setup')

def tearDown(self):
    print('teardown\n')
# 每个测试方法前/后执行        
        
```





等待

```
```





断言

```python
self.assertEqual(a,b)
# 判断a,b是否相等

self.assertIn(a,b)
# b是否包含a

self.assertTrue(message)
# message是否为True
```





跳过

```python
@unittest.skip()
# 直接跳过

@unittest.skipIf(True,"")
# 表达式为真时跳过

@unittest.skipUnless(False, "")
# 表达式为假时跳过

@unittest.expectedFailure
# 我也没搞懂是什么
```



数据驱动

```python
from ddt import ddt,data,unpack

@ddt()
class Test(unittest.TestCase):

    # data添加参数
    @data('message1', 'message2')
    def test01(self, value):
        print(value)
	
    # unpack解包
    @data(['message1', 'message2'])
    @unpack
    def test02(self, value1, value2):
        print(value1, value2)
```





测试报告

```
```

