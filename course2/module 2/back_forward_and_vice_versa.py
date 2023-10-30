list_of_numbers = [int(number) for number in input().split(' ')]
new_list = []
if len(list_of_numbers) % 2 == 0:
    for num in range(1, len(list_of_numbers) + 1):
        new_list.append(list_of_numbers[1])
        new_list.append(list_of_numbers[0])
        del list_of_numbers[:2]
        if len(list_of_numbers) == 0:
            break
    print(*new_list)
else:
    for num in range(1, len(list_of_numbers) - 1):
        new_list.append(list_of_numbers[1])
        new_list.append(list_of_numbers[0])
        del list_of_numbers[:2]
        if len(list_of_numbers) == 1:
            break
    print(*new_list, *list_of_numbers, sep=' ')
