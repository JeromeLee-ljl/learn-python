import unittest


def abs2(num):
    return abs(num)


class Test_f(unittest.TestCase):
    def test_abs2(self):
        self.assertEqual(abs2(-1), 1, 'not equal')

    def test_abs3(self):
        self.assertEqual(abs2(-1), 1, 'not equal')

    def test_abs4(self):
        d = {'e': 1, '2': 2}
        with self.assertRaises(ZeroDivisionError):
            a = 10 / 1


if __name__ == '__main__':
    pass
