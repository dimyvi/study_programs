matrix = []
for _ in range(int(input())):
    row = [int(num) for num in input().split()]
    matrix.append(row)

new_list = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (i >= j and i <= len(matrix) - 1 - j) or (i <= j and i >= len(matrix) - 1 - j):
            new_list.append(matrix[i][j])
print(max(new_list))
