    from random import *

    n = int(input())
    for _ in range(n):
        m = randrange(2)
        if m == 0:
            print('Орел')
        else:
            print('Решка')