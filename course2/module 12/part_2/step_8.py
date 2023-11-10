import string
from random import *


def generate_password(length):
    a = string.digits + string.ascii_lowercase + string.ascii_uppercase
    alf = [i for i in a if i not in '01LIOlio']
    ret_password = ''
    for k in sample(alf, length):
        ret_password += k
    return ret_password


def generate_passwords(count):
    ls = []
    while len(ls) != count:
        ls.append(generate_password(m))
    print(*ls, sep='\n')


n, m = int(input()), int(input())
generate_passwords(n)