import unittest

from lab3.task5 import update_if_sorted


class TestSumOfBinaryOnes(unittest.TestCase):

    def test_ascending_true(self):
        self.assertEqual(update_if_sorted([1, 2, 3], 'ascending'), [1, 3, 5])

    def test_ascending_false(self):
        self.assertEqual(update_if_sorted([1, 2, 3, 0], 'ascending'), [1, 2, 3, 0])

    def test_descending_true(self):
        self.assertEqual(update_if_sorted([3, 2, 1], 'descending'), [3, 3, 3])

    def test_descending_false(self):
        self.assertEqual(update_if_sorted([3, 2, 1, 10], 'descending'), [3, 2, 1, 10])


if __name__ == '__main__':
    unittest.main()
