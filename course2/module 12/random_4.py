from random import *

seet = set()
while len(seet) != 7:
    seet.add(randint(1, 49))
print(*sorted(seet))
