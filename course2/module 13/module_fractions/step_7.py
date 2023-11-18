from fractions import *
from math import gcd
n = int(input())
ls = []
for chis in range(1, n + 1):
    for znam in range(1, n + 1):
        if chis + znam == n and chis > znam and (chis + znam) and gcd(chis, znam) % 2 != 0:
            ls.append(Fraction(znam, chis))
print(max(ls))