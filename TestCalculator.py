import unittest
import yonatan_team_calculator as calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(calculator.divide(6, 2), 3)

        # test division by zero
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(6, 0)


if __name__ == '__main__':
    unittest.main()
