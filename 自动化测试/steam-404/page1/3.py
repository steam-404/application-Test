import csv
import unittest
from ddt import ddt, data, unpack


@ddt()
class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass
        # print('setUp')

    def tearDown(self) -> None:
        pass
        # print('tearDown')

    @data(*csv.reader(open('testdata.csv')))
    @unpack
    def test01(self, value):
        print(value)


if __name__ == '__main__':
    unittest.main()
