n = int(input())
ls = []
for i in range(0, n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = ls[i - 1][j - 1] + ls[i - 1][j]
    ls.append(row)

for r in ls:
    print(*r)
