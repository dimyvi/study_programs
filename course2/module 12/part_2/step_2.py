from random import *


def generate_index():
    s = ''
    for i in range(2):
        if i == 0:
            s += (str(chr(randint(65, 90))) + str(chr(randint(65, 90))) + str(randint(0, 99)))
        else:
            s += ('_' + str(randint(0, 99)) + str(chr(randint(65, 90))) + str(chr(randint(65, 90))))
    return s
print(generate_index())