f = open('numbers.txt', encoding='utf-8').readlines()


def g(x):
    return int(x.rstrip())


print(sum(map(g, f)))
