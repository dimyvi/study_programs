ls = []
for _ in range(int(input())):
    st = set(input().lower())
    ls.append(len(st))
print(*ls, sep='\n')
