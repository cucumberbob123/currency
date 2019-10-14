import unittest
from conversion import formatMoney, getSymbol


class TestFormatter(unittest.TestCase):
    def testNormal(self):
        self.assertEqual(formatMoney(3.1234123), '3.12')

    def testZero(self):
        self.assertEqual(formatMoney(0.458128), '0.46')

    def testEdge(self):
        self.assertEqual(formatMoney(1.445), '1.45')


class TestSymbolGetter(unittest.TestCase):
    def testNormal(self):
        self.assertEqual(getSymbol("GBP"), "£")
        self.assertEqual(getSymbol('hKd'), "$")

    def testNotFound(self):
        self.assertEqual(getSymbol("FOO"), "FOO ")

    def testErroneous(self):
        with self.assertRaises(TypeError):
            getSymbol(5)
        with self.assertRaises(TypeError):
            getSymbol("E")


if __name__ == '__main__':
    unittest.main()
