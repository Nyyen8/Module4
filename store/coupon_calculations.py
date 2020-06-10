"""
Program: if_elif.py
Author: Paul Elsea
Last Modified: 06/10/2020

Program to ask which level of a subscription service they want to sign up for.
"""
'''These are the global variables used by the calculate_price func'''
TAX_RATE = 1.06
UNDER_10_SHIPPING = 5.95
UNDER_30_SHIPPING = 7.95
UNDER_50_SHIPPING = 11.95

'''This func calculates a total price taking into consideration cost, two types of discounts,
shipping taxes and sales tax, then returns it.'''
def calculate_price(price, cash_coupon, percent_coupon):
    global TAX_RATE
    global UNDER_10_SHIPPING
    global UNDER_30_SHIPPING
    global UNDER_50_SHIPPING

    '''This is the initial cost calculation before shipping and sales tax'''
    running_total = (price - cash_coupon) * ((100 - percent_coupon)/100)

    '''These nested if statements determine the cost before shipping and apply the proper
    amount of shipping cost then applies sales tax to the result'''
    if running_total < 50:
        if running_total < 30:
            if running_total < 10:
                final_total = (running_total + UNDER_10_SHIPPING) * TAX_RATE
                return final_total
            final_total = (running_total + UNDER_30_SHIPPING) * TAX_RATE
            return final_total
        final_total = (running_total + UNDER_50_SHIPPING) * TAX_RATE
        return final_total
    else:
        final_total = running_total * TAX_RATE
        return final_total

if __name__ == '__main__':
    calculate_price(10,10,10)

