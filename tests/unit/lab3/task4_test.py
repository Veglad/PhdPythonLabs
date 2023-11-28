import unittest

from lab3.task4 import sorted_by_direction


class TestSumOfBinaryOnes(unittest.TestCase):

    def test_ascending_true(self):
        self.assertTrue(sorted_by_direction([1, 2, 3], 'ascending'))

    def test_ascending_false(self):
        self.assertFalse(sorted_by_direction([1, 2, 3, 0], 'ascending'))

    def test_descending_true(self):
        self.assertTrue(sorted_by_direction([3, 2, 1], 'descending'))

    def test_descending_false(self):
        self.assertFalse(sorted_by_direction([3, 2, 1, 10], 'descending'))


if __name__ == '__main__':
    unittest.main()
