def f(ls):
    return sum([int(i) for i in str(ls)])


numbers = sorted([int(i) for i in input().split()])
print(*sorted(numbers, key=f))
