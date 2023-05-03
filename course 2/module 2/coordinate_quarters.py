first_quarter = 0
second_quarter = 0
third_quarter = 0
fourth_quarter = 0
for i in range(1, int(input()) + 1):
    coordinate = [int(number) for number in input().split(' ')]
    if coordinate[0] > 0 and coordinate[1] > 0:
        first_quarter += 1
    elif coordinate[0] < 0 and coordinate[1] > 0:
        second_quarter += 1
    elif coordinate[0] < 0 and coordinate[1] < 0:
       third_quarter += 1
    elif coordinate[0] > 0 and coordinate[1] < 0:
        fourth_quarter += 1
print('Первая четверть:', first_quarter)
print('Вторая четверть:', second_quarter)
print('Третья четверть:', third_quarter)
print('Четвертая четверть:', fourth_quarter)