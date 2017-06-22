# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:37:30 2017

@author: Bryan
"""
balance = 3329
annualInterestRate = 0.2
b = balance
p = 0

while b > 0:
    p = p + 10
    ub = balance - p
    b = balance
    r = annualInterestRate
    for i  in range(0, 12):
        ub = b - p
        b = ub + ((r / 12) * ub)
        
    if b < 0:
        print(p)
 