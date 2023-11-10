import random
s = [str(i) for i in input()]
random.shuffle(s)
print(*s, sep='')

