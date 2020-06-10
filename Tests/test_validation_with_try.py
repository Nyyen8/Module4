"""
Program: test_validation_with_try.py
Author: Paul Elsea
Last Modified: 06/10/2020

The purpose of this program is to test the
functions in validation_with_try.py.
"""

import unittest
import unittest.mock as mock
from input_validation import validation_with_try as avg


class FunctionTestCase(unittest.TestCase):

    def test_average_negative_first_input(self):
        with mock.patch('builtins.input', side_effect=[-85, 90, 95]):
            with self.assertRaises(ValueError):
                avg.average()
        '''This test checks to see if the average func throws a valueError if the first entry is negative'''

    # def test_average_negative_second_input(self):
    #     with mock.patch('builtins.input', side_effect=[85, -90, 95]):
    #         self.assertRaises(ValueError)
    #     '''This test checks to see if the average func throws a valueError if the second entry is negative'''
    #
    # def test_average_negative_third_input(self):
    #     with mock.patch('builtins.input', side_effect=[85, 90, -95]):
    #         self.assertRaises(ValueError)
    #     '''This test checks to see if the average func throws a valueError if the third entry is negative'''
    #
if __name__ == '__main__':
    unittest.main()