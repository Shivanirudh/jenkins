#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from add import add

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 35]
        result = add(data)
        self.assertEqual(result, 55)

if __name__ == '__main__':
    unittest.main()
