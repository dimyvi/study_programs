nm = input().split()

mx = [["." for _ in range(int(nm[1]))] for _ in range(int(nm[0]))]

for i in range(int(nm[0])):
    for j in range(int(nm[1])):
        if i % 2 == 0 and j % 2 != 0:
            mx[i][j] = "*"
        elif i % 2 != 0 and j % 2 == 0:
            mx[i][j] = "*"

for k in mx:
    print(*k)
