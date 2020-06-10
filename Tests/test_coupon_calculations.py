"""
Program: if_elif.py
Author: Paul Elsea
Last Modified: 06/10/2020

Program to ask which level of a subscription service they want to sign up for.
"""
import unittest
from store import coupon_calculations as coupon


class MyTestCase(unittest.TestCase):
    '''This test set check for proper final price using a value under $10'''
    def test_price_under_10_5_cash_10_percent(self):
        assert round(coupon.calculate_price(14.99, 5, 10), 2) == 15.84
    def test_price_under_10_5_cash_15_percent(self):
        assert round(coupon.calculate_price(14.99, 5, 15), 2) == 15.31
    def test_price_under_10_5_cash_20_percent(self):
        assert round(coupon.calculate_price(14.99, 5, 20), 2) == 14.78
    def test_price_under_10_10_cash_10_percent(self):
        assert round(coupon.calculate_price(14.99, 10, 10), 2) == 11.07
    def test_price_under_10_10_cash_15_percent(self):
        assert round(coupon.calculate_price(14.99, 10, 15), 2) == 10.80
    def test_price_under_10_10_cash_20_percent(self):
        assert round(coupon.calculate_price(14.99, 10, 20), 2) == 10.54

    '''This test set check for proper final price using a value under $30'''
    def test_price_between_10_and_30_5_cash_10_percent(self):
        assert round(coupon.calculate_price(29.99, 5, 10), 2) == 32.27
    def test_price_between_10_and_30_5_cash_15_percent(self):
        assert round(coupon.calculate_price(29.99, 5, 15), 2) == 30.94
    def test_price_between_10_and_30_5_cash_20_percent(self):
        assert round(coupon.calculate_price(29.99, 5, 20), 2) == 29.62
    def test_price_between_10_and_30_10_cash_10_percent(self):
        assert round(coupon.calculate_price(29.99, 10, 10), 2) == 27.50
    def test_price_between_10_and_30_10_cash_15_percent(self):
        assert round(coupon.calculate_price(29.99, 10, 15), 2) == 26.44
    def test_price_between_10_and_30_10_cash_20_percent(self):
        assert round(coupon.calculate_price(29.99, 10, 20), 2) == 25.38

    '''This test set check for proper final price using a value under $50'''
    def test_price_between_30_and_50_5_cash_10_percent(self):
        assert round(coupon.calculate_price(49.99, 5, 10), 2) == 55.59
    def test_price_between_30_and_50_5_cash_15_percent(self):
        assert round(coupon.calculate_price(49.99, 5, 15), 2) == 53.20
    def test_price_between_30_and_50_5_cash_20_percent(self):
        assert round(coupon.calculate_price(49.99, 5, 20), 2) == 50.82
    def test_price_between_30_and_50_10_cash_10_percent(self):
        assert round(coupon.calculate_price(49.99, 10, 10), 2) == 50.82
    def test_price_between_30_and_50_10_cash_15_percent(self):
        assert round(coupon.calculate_price(49.99, 10, 15), 2) == 48.70
    def test_price_between_30_and_50_10_cash_20_percent(self):
        assert round(coupon.calculate_price(49.99, 10, 20), 2) == 46.58

    '''This test set check for proper final price using a value over $50'''
    def test_price_over_50_5_cash_10_percent(self):
        assert round(coupon.calculate_price(75, 5, 10), 2) == 66.78
    def test_price_over_50_5_cash_15_percent(self):
        assert round(coupon.calculate_price(75, 5, 15), 2) == 63.07
    def test_price_over_50_5_cash_20_percent(self):
        assert round(coupon.calculate_price(75, 5, 20), 2) == 59.36
    def test_price_over_50_10_cash_10_percent(self):
        assert round(coupon.calculate_price(75, 10, 10), 2) == 62.01
    def test_price_over_50_10_cash_15_percent(self):
        assert round(coupon.calculate_price(75, 10, 15), 2) == 58.57
    def test_price_over_50_10_cash_20_percent(self):
        assert round(coupon.calculate_price(75, 10, 20), 2) == 55.12

if __name__ == '__main__':
    unittest.main()
