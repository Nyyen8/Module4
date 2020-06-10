"""
Program: if_elif.py
Author: Paul Elsea
Last Modified: 06/10/2020

Program to ask which level of a subscription service they want to sign up for.
"""
TAX_RATE = 1.06
UNDER_10_SHIPPING = 5.95
UNDER_30_SHIPPING = 7.95
UNDER_50_SHIPPING = 11.95

def calculate_price(price, cash_coupon, percent_coupon):
    global TAX_RATE
    global UNDER_10_SHIPPING
    global UNDER_30_SHIPPING
    global UNDER_50_SHIPPING

    running_total = (price - cash_coupon) * ((100 - percent_coupon)/100)
    if running_total <= 10.00:
        final_total = (running_total + UNDER_10_SHIPPING) * TAX_RATE
        return final_total
        if 30 > running_total >= 10:
            final_total = (running_total + UNDER_30_SHIPPING) * TAX_RATE
            return final_total

if __name__ == '__main__':
    print(round(calculate_price(14.99, 5, 10), 2))
    print(round(calculate_price(14.99, 5, 15), 2))
    print(round(calculate_price(14.99, 5, 20), 2))
    print(round(calculate_price(14.99, 10, 10), 2))
    print(round(calculate_price(14.99, 10, 15), 2))
    print(round(calculate_price(14.99, 10, 20), 2))
