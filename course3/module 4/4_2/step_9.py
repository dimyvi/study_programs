import csv

with open('titanic.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))

    male = []
    female = []

    for human in data:
        if int(human['survived']) == 1 and float(human['age']) < 18:
            if human['sex'] == 'male':
                male.append(human['name'])
            elif human['sex'] == 'female':
                female.append(human['name'])

    for i in male:
        print(i)
    for j in female:
        print(j)


