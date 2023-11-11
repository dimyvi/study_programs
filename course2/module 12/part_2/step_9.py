import string
from random import *


def generate_password(length):
    a = string.digits + string.ascii_lowercase + string.ascii_uppercase
    alf = [i for i in a if i not in '01LIOlio']
    password = ''
    while len(password) != length:
        for k in sample(alf, length):
            if k in string.digits:
                password += k
            if k in string.ascii_lowercase:
                password += k
            if k in string.ascii_uppercase:
                password += k



def generate_passwords(count, length):
    ls = []
    while len(ls) != count:
        ls.append(generate_password(length))
    print(*ls, sep='\n')


n, m = int(input()), int(input())
generate_passwords(n, m)
