n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
a = []

for i in range(n):
    for j in range(n):
        if j == n - 1 - i or (i <= j and i >= n - 1 - j) or (i >= j and i >= n - 1 - j):
            a.append(mx[i][j])
print(max(a))
