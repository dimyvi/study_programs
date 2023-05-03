list_of_numbers = [int(number) for number in input().split(' ')]
count = 0
for i in range(len(list_of_numbers) - 1):
    if list_of_numbers[i] < list_of_numbers[i + 1]:
        count += 1
print(count)
