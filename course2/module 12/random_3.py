from random import *

s = ''
for i in range(int(input())):
    ls = [randint(65, 90),randint(97, 122)]
    s += (str(chr(ls[randint(0, 1)])))
print(s)