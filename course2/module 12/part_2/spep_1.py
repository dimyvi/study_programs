from random import randint
def generate_ip():
    s = '.'.join([str(randint(0, 255)) for _ in range(4)])
    return s

