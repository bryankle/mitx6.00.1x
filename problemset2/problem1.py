# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
ub = balance - monthlyPaymentRate * balance
b = balance
p = b * monthlyPaymentRate
r = annualInterestRate
for i  in range(0, 13):
    print('Month ',i)
    print('--------------')
    print('Balance: ',b)
    print('Minimum Payment: ', p)
    print('Unpaid Balance: ',ub)
    print('Interest: ', ub * (r/12))

    ub = b - p
    b = ub + ((r / 12) * ub)
    p = b * monthlyPaymentRate