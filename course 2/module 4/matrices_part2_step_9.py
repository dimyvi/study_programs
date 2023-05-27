def sum_over_columns_and_rows(ls):
    sum_i, sum_j = 0, 0
    full_i, full_j = 0, 0
    full_lis = []

    for i in range(len(ls)):
        for j in range(len(ls)):
            sum_i += int(str(ls[i][j]))
            full_i += int(str(ls[i][j]))

            sum_j += int(str(ls[j][i]))
            full_j += int(str(ls[j][i]))

        full_lis.append(sum_j)
        full_lis.append(sum_i)
        sum_j, sum_i = 0, 0

    return len(set(full_lis)) == 1 and full_j == full_i


def full_numbers(ls):
    static_list = [int(i) for i in range(1, len(ls) ** 2 + 1)]
    ls_n = []
    for i in range(len(ls)):
        for j in range(len(ls)):
            ls_n.append(ls[i][j])
    ls_n.sort()
    return ls_n == static_list


mx = [[int(i) for i in input().split()] for _ in range(int(input()))]
first_function = (sum_over_columns_and_rows(mx))
second_function = (full_numbers(mx))

if first_function and second_function:
    print('YES')
else:
    print('NO')
