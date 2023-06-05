f = set(int(i) for i in input().split(' '))
s = set(int(i) for i in input().split(' '))
t = set(int(i) for i in input().split(' '))

a = set(i for i in range(11))
print(*sorted(a - (f | s | t)))
