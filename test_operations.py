import unittest

import operations


class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(operations.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(operations.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(operations.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(operations.divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            operations.divide(10, 0)

    def test_power(self):
        self.assertEqual(operations.power(2, 10), 1024)

    def test_modulus(self):
        self.assertEqual(operations.modulus(10, 3), 1)

    def test_modulus_by_zero(self):
        with self.assertRaises(ValueError):
            operations.modulus(10, 0)


if __name__ == "__main__":
    unittest.main()
