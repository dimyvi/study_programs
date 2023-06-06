s1 = set(i for i in input().split(' '))
s2 = set(i for i in input().split(' '))

print(*sorted(s1 | s2))