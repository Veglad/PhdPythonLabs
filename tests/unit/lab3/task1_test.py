import unittest

from parameterized import parameterized

from lab3.task1 import sum_of_ones_from_binary_representation


class TestSumOfBinaryOnes(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sum_of_ones_from_binary_representation(0), 0)

    def test_one(self):
        self.assertEqual(sum_of_ones_from_binary_representation(1), 1)

    def test_seven(self):
        self.assertEqual(sum_of_ones_from_binary_representation(7), 3)

    def test_eleven(self):
        self.assertEqual(sum_of_ones_from_binary_representation(11), 3)

if __name__ == '__main__':
    unittest.main()
