#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from add import addition

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 45]
        result = addition(data)
        self.assertEqual(result, 65)

if __name__ == '__main__':
    unittest.main()
