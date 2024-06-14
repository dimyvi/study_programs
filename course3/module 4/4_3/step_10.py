import json

with open('countries.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    religions = []
    for country in data:
        if country['religion'] not in religions:
            religions.append(country['religion'])

    ans = {}
    for name_rel in religions:
        ans[name_rel] = [i['country'] for i in data if i['religion'] == name_rel]

with open('religion.json', 'w', encoding='utf-8') as file_answer:
    json.dump(ans, file_answer, indent=3)