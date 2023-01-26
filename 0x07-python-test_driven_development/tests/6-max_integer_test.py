#!/usr/bin/python3
"""unit test"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unit test class"""

    def test_docstrings(self):
        """module documentation"""
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)
        """function documentation"""
        self.assertTrue(len((max_integer).__doc__) > 1)

    def test_valid(self):
        """positive integers"""
        self.assertEqual(max_integer([1, 4, 3, 10, 2]), 10)
        """negative integers"""
        self.assertEqual(max_integer([-14, -1, -27]), -1)
        """floats"""
        self.assertAlmostEqual(max_integer([1.3, 5, 9.1]), 9.1)
        """single length list"""
        self.assertEqual(max_integer([9]), 9)
        """only a string"""
        self.assertEqual(max_integer("things"), "t")

    def test_invalid(self):
        """string"""
        self.assertRaises(TypeError, max_integer, [1, "hello", 4, 10])
        """nothing"""
        self.assertEqual(max_integer([]), None)
        """integer not list"""
        self.assertRaises(TypeError, max_integer, 9)


if __name__ == '__main__':
    unittest.main()
