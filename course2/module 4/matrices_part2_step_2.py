n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

max_num = matrix[0][0]
mx_i = 0
mx_j = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > int(max_num):
            max_num = matrix[i][j]
            mx_i = i
            mx_j = j
print(mx_i, mx_j)
