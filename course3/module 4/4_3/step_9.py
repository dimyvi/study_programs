import json

with open('people.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    all_list = []
    for people in data:
        if len(people) == 8:
            for n in people:
                all_list.append(n)
            break

    for a in data:
        for k in all_list:
            if k not in a:
                a[k] = None

with open('updated_people.json', 'w', encoding='utf-8') as ans_file:
    json.dump(data, ans_file, indent=3)