nm = input().split()

mx = [[0 for _ in range(int(nm[1]))] for _ in range(int(nm[0]))]
ls = [int(l) for l in range(1, int(nm[1]) + 1)]
count = 1
for i in range(int(nm[0])):
    for j in range(int(nm[1])):
        if i == 0 or i % 2 == 0:
            mx[i][j] = count
            count += 1
        elif i % 2 != 0:
            mx[i][j] = count
            count += 1

for k in range(int(nm[0])):
    if k % 2 != 0:
        mx[k].reverse()

for r in range(int(nm[0])):
    for c in range(int(nm[1])):
        print(str(mx[r][c]).ljust(3), end='')
    print()
