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
        assert(coupon.calculate_price(5, 5, 10), 90)
    def test_price_under_10_5_cash_15_percent(self):
        assert(coupon.calculate_price(5, 5, 15), 90)
    def test_price_under_10_5_cash_20_percent(self):
        assert(coupon.calculate_price(5, 5, 20), 90)
    def test_price_under_10_10_cash_10_percent(self):
        assert(coupon.calculate_price(5, 10, 10), 90)
    def test_price_under_10_10_cash_15_percent(self):
        assert(coupon.calculate_price(5, 10, 15), 90)
    def test_price_under_10_10_cash_20_percent(self):
        assert(coupon.calculate_price(5, 10, 20), 90)

    def test_price_under_10_5_cash_10_percent(self):
        assert(coupon.calculate_price(5, 5, 10), 90)
    def test_price_under_10_5_cash_15_percent(self):
        assert(coupon.calculate_price(5, 5, 15), 90)
    def test_price_under_10_5_cash_20_percent(self):
        assert(coupon.calculate_price(5, 5, 20), 90)
    def test_price_under_10_10_cash_10_percent(self):
        assert(coupon.calculate_price(5, 10, 10), 90)
    def test_price_under_10_10_cash_15_percent(self):
        assert(coupon.calculate_price(5, 10, 15), 90)
    def test_price_under_10_10_cash_20_percent(self):
        assert(coupon.calculate_price(5, 10, 20), 90)

if __name__ == '__main__':
    unittest.main()
