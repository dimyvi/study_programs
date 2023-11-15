import random

n = 10**6
s0 = 2**4
k = 0

for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
        k += 1

print((k/n)*s0)