import csv, json

with open('playgrounds.csv', 'r', encoding='utf-8') as file:
    table = list(csv.DictReader(file, delimiter=';'))

data = {}
for row in table:
    adm_area = row['AdmArea']
    district = row['District']
    address = row['Address']

    if adm_area not in data:
        data[adm_area] = {}
    if district not in data[adm_area]:
        data[adm_area][district] = []
    data[adm_area][district].append(address)

with open('addresses.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=3)