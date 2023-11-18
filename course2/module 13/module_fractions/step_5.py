from fractions import Fraction as F
n = int(input())
summ = 0
for i in range(1, n+1):
    summ += F(1,i**(2))
print(summ)
