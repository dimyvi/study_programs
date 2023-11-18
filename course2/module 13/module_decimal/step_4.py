from decimal import Decimal as D

d = D(input())
print(D(d.exp()) + D(d.log10()) + D(d.ln()) + D(d.sqrt()))
