import csv
import unittest
from ddt import ddt, data, unpack
from csvv import read_file

dataMessage = read_file()


@ddt()
class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass
        # print('setUp')

    def tearDown(self) -> None:
        pass
        # print('tearDown')

    @data(*dataMessage)
    @unpack
    @unpack
    def test01(self, value):
        print(value)


if __name__ == '__main__':
    unittest.main()
