f = set(int(i) for i in input().split(' '))
s = set(int(i) for i in input().split(' '))
t = set(int(i) for i in input().split(' '))

d = t.difference(f | s)
n = sorted(d)
print(*n[::-1])