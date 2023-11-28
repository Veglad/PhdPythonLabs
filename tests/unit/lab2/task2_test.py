import unittest

from parameterized import parameterized

from lab2.task2 import compute_expression


class TestPointWithinZone(unittest.TestCase):

    @parameterized.expand([
        (1, -1, -2),
        (-10, -10, -1580),
        (-3, -3, -138),
        (10, -10, -380),
    ])
    def test_compute_when_x_is_less_or_equal_to_minus_6a(self, x, a, result):
        self.assertEqual(compute_expression(x, a), result)

    @parameterized.expand([
        (3, 3, -6.468438123802524),
        (10, -1, 2.2460977456566953),
        (10, 10, -36.669380616522616),
        (2, 2, -6.291000067617227),
    ])
    def test_compute_when_x_is_greater_than_minus_6a(self, x, a, result):
        self.assertEqual(compute_expression(x, a), result)


if __name__ == '__main__':
    unittest.main()
