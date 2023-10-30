n = int(input())
m = int(input())

st = set(input() for _ in range(n))
ls = [input() for _ in range(m)]


for i in ls:
    if i in st:
        print('YES')
    else:
        print('NO')