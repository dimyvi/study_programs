n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]

s_i = 0
full_i = 0
s_j = 0
full_j = 0
for i in range(len(mx)):
    for j in range(len(mx)):
        s_i += int(str(mx[i][j]))
        full_i += int(str(mx[i][j]))
        s_j += int(str(mx[j][i]))
        full_j += int(str(mx[j][i]))
    print(s_j)
    s_j = 0
    print(s_i)
    s_i = 0


print()

print(full_i)
print(full_j)
