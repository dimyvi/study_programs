nm = input().split()
mx = [[0 for _ in range(int(nm[1]))] for _ in range(int(nm[0]))]

ls = [int(l) for l in range(1, int(nm[1]) + 1)]

for i in range(int(nm[0])):
    mx[i] = ls
    print(*mx[i])
    ls.append(ls[0])
    del ls[0]
