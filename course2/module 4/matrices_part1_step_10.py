n = int(input())
matrix = []
count = 0
for _ in range(n):
    row = [int(k) for k in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i == j:
            count += matrix[i][j]
print(count)
