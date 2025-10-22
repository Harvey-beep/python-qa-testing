import unittest
from utils import add # Import the function we want to test

class TestMathFunctions(unittest.TestCase):

    # Test method names MUST start with 'test_'
    def test_add_positive_numbers(self):
        print("Running test_add_positive_numbers...")
        expected = 10
        actual = add(5, 5)
        self.assertEqual(expected, actual, "The sum was not correct")

    def test_add_negative_numbers(self):
        print("Running test_add_negative_numbers...")
        self.assertEqual(add(-5, -5), -10)

    def test_add_mixed_numbers(self):
        print("Running test_add_mixed_numbers...")
        self.assertEqual(add(6, -3), 3)

if __name__ == "__main__":
    unittest.main()