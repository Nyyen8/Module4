"""
Program: if_elif.py
Author: Paul Elsea
Last Modified: 06/10/2020

Program to ask which level of a subscription service they want to sign up for.
"""
import unittest
from store import coupon_calculations as coupon


class MyTestCase(unittest.TestCase):
    def test_price_under_10_5_cash_10_percent(self):
        assert round(coupon.calculate_price(14.99, 5, 10), 2) == 15.84
    def test_price_under_10_5_cash_15_percent(self):
        assert round(coupon.calculate_price(14.99, 5, 15), 2) == 15.31
    def test_price_under_10_5_cash_20_percent(self):
        assert round(coupon.calculate_price(14.99, 5, 20), 2) == 14.78
    def test_price_under_10_10_cash_10_percent(self):
        assert round(coupon.calculate_price(14.99, 10, 10), 2) == 11.07
    def test_price_under_10_10_cash_15_percent(self):
        assert round(coupon.calculate_price(14.99, 10, 15), 2) == 10.8
    def test_price_under_10_10_cash_20_percent(self):
        assert round(coupon.calculate_price(14.99, 10, 20), 2) == 10.54

    def test_price_between_10_and_30_5_cash_10_percent(self):
        assert round(coupon.calculate_price(29.99, 5, 10), 2) == 15.84
    def test_price_between_10_and_30_5_cash_15_percent(self):
        assert round(coupon.calculate_price(29.99, 5, 15), 2) == 15.31
    def test_price_between_10_and_30_5_cash_20_percent(self):
        assert round(coupon.calculate_price(29.99, 5, 20), 2) == 14.78
    def test_price_between_10_and_30_10_cash_10_percent(self):
        assert round(coupon.calculate_price(29.99, 10, 10), 2) == 11.07
    def test_price_between_10_and_30_10_cash_15_percent(self):
        assert round(coupon.calculate_price(29.99, 10, 15), 2) == 10.8
    def test_price_between_10_and_30_10_cash_20_percent(self):
        assert round(coupon.calculate_price(29.99, 10, 20), 2) == 10.54

if __name__ == '__main__':
    unittest.main()
