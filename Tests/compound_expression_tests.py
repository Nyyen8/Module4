"""
Program: compound_expression_tests.py
Author: Paul Elsea
Last Modified: 06/10/2020

Tests 5 compound expressions.
"""
import unittest

class MyTestCase(unittest.TestCase):
    '''Tests to see if y is more than MAX'''
    def test_y_greater_than_MAX_true(self):
        y = 17
        MAX = 10
        self.assertTrue(y > MAX)
    '''Tests to see if y is less than MIN'''
    def test_y_less_than_MIN_false(self):
        y = 17
        MIN = 0
        self.assertFalse(y < MIN)
    '''Tests to see if x is between MIN and MAX without being equal to either'''
    def test_x_between_MIN_MAX_true(self):
        x = 8
        MIN = 0
        MAX = 10
        self.assertTrue(MIN < x < MAX)
    '''Tests to see if x is from MIN to MAX without being equal to MAX'''
    def test_x_from_MIN_to_MAX_but_not_equal_true(self):
        x = 8
        MIN = 0
        MAX = 10
        self.assertTrue(MIN <= x < MAX)
    '''Tests to see if x is from MIN to MAX without being equal to MIN'''
    def test_x_not_MIN_to_MAX_equal_true(self):
        x = 8
        MIN = 0
        MAX = 10
        self.assertTrue(MIN < x <= MAX)

if __name__ == '__main__':
    unittest.main()
