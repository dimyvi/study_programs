from math import sin


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


def root(n):
    return n ** 0.5


def abss(n):
    return abs(n)


def sinn(n):
    return sin(n)


nn = int(input())
ss = input()
commands = {'квадрат': square, 'куб': cube, 'корень': root, 'модуль': abss, 'синус': sinn}
print(commands[ss](nn))
