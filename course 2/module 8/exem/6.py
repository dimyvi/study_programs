s1 = set(int(i) for i in input().split(' '))
s2 = set(int(i) for i in input().split(' '))

if s1.isdisjoint(s2):
    print('BAD DAY')
else:
    print(*sorted(s1 & s2, reverse=True))