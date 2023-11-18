from decimal import *

num1 = str(Decimal(input()))
ls = [i for i in num1 if i.isdigit()]
print(Decimal(max(ls)) + Decimal(min(ls)))
