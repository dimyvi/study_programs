f = set(int(i) for i in input().split(' '))
s = set(int(i) for i in input().split(' '))
t = set(int(i) for i in input().split(' '))

d = f.intersection(s).difference(t)
n = sorted(d)
print(*n[::-1])
