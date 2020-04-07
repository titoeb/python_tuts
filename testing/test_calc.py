import unittest
from unittest.mock import patch
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15) 
        self.assertEqual(calc.add(5, -5), 0)
        self.assertEqual(calc.add(-10, -5), -15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5) 
        self.assertEqual(calc.subtract(5, -5), 10)
        self.assertEqual(calc.subtract(-10, -5), -5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50) 
        self.assertEqual(calc.multiply(5, -5), -25)
        self.assertEqual(calc.multiply(-10, -5), 50)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2) 
        self.assertEqual(calc.divide(5, -5), -1)
        self.assertEqual(calc.divide(-10, -5), 2)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertRaises(ValueError, calc.divide, 10, 0)

    def test_get_website_1(self):
        with patch('calc.requests.get') as mocket_get:
            mocket_get.return_value.ok = True
            mocket_get.return_value.text = 'Success'

            schedule = calc.get_website()
            mocket_get.assert_called_with('http://company.com/tim/1')
            self.assertEqual(schedule, 'Success')

if __name__ == "__main__":
    unittest.main()