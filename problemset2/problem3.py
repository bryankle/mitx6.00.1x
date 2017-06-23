# Paste your code into this box
import math
r = annualInterestRate

upper = balance * (1 * math.pow(1 + (r / 12), 12)) / 12
lower = balance / 12
b = 1
found = False;
while found == False:
  b = balance
  p = (upper + lower) / 2
  ub = balance - p
 
  for i  in range(0, 12):
    ub = b - p
    b = ub + ((r / 12) * ub)
    if round(b) == 0:
      print(round(p, 2))
      found = True
  if b > 0:
    lower = (upper + lower) / 2
    continue
  if b < 0:
    upper = (upper + lower) / 2
    continue
  