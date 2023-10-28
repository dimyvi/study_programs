s = sorted(input())
dct1 = dict(zip(range(len(s)), s))

d = sorted(input())
dct2 = dict(zip(range(len(d)), d))

if dct1 == dct2:
    print('YES')
else:
    print('NO')