import unittest

from parameterized import parameterized

from lab2.task1 import inside_specified_zone


class TestPointWithinZone(unittest.TestCase):

    @parameterized.expand([
        (3, 3),
        (3, 1),
        (1, 3),
        (-3, -3),
        (-3, -1),
        (-1, -3),
    ])
    def test_outside_zone(self, x, y):
        self.assertFalse(inside_specified_zone(x, y))

    @parameterized.expand([
        (2, 2),
        (-2, 2),
        (-2, -2),
        (2, -2)
    ])
    def test_square_boundary(self, x, y):
        self.assertTrue(inside_specified_zone(x, y))

    @parameterized.expand([
        (2, 1),
        (-1, 2),
        (1.5, 1.5),
        (1.2, -1.9)
    ])
    def test_square_zone(self, x, y):
        self.assertTrue(inside_specified_zone(x, y))

    @parameterized.expand([
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ])
    def test_rhomboid_boundary(self, x, y):
        self.assertFalse(inside_specified_zone(x, y))

    @parameterized.expand([
        (0, 0),
        (0.5, 0),
        (-0.5, -0.5),
        (0.1, 0.1)
    ])
    def test_rhomboid_space(self, x, y):
        self.assertFalse(inside_specified_zone(x, y))


if __name__ == '__main__':
    unittest.main()
