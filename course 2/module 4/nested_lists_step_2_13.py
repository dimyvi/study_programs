def chunked(n, string):
    ls = [i for i in string.split()]
    num = 0
    new = []
    if len(ls) % n == 0:
        num = len(ls) // n
    else:
        num = len(ls) // n + 1

    for j in range(num):
        new.append(ls[:n])
        del ls[:n]
    print(new)

st = input()
number = int(input())
chunked(number, st)
