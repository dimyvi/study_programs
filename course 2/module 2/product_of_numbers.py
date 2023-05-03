first_num = int(input())
numbers = []
for i in range(1, first_num + 1):
    numbers.append(int(input()))

num = int(input())

answer = 0
for c in numbers:
    for k in numbers:
        if c * k == num:
            answer += 1

if answer > 0:
    print('ДА')
elif answer == 0:
    print('НЕТ')
