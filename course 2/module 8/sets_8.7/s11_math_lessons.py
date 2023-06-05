f = set(int(i) for i in input().split(' '))
s = set(int(i) for i in input().split(' '))
t = set(int(i) for i in input().split(' '))

print(*sorted((f | s | t) - (f & s & t)))