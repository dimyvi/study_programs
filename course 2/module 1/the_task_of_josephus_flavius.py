number_of_people = int(input())
shift = int(input())

list_of_people = [number for number in range(1, number_of_people+1)]
print(list_of_people)

while len(list_of_people) > 1:
    for i in list_of_people:
        print(list_of_people[shift-1])
        del list_of_people[shift-1]
        print(list_of_people)