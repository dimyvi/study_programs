from math import log
n = int(input())
if int(log(n, 2)) != 2**int(log(n, 2)) != n:
    print(int(log(n, 2))+1)
else:
    print(int(log(n, 2)))
