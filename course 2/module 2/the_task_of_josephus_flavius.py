number_of_people = int(input())
shift = int(input())

list_of_people = [number for number in range(1, number_of_people + 1)]
while len(list_of_people) > 1:
    for i in range(0, shift - 1):
        list_of_people.append(list_of_people[i])
    del list_of_people[0:shift]
print(*list_of_people)
