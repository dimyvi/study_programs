import csv

with open('salary_data.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    sorted_data_company = sorted(data, key=lambda x: x['company_name'])

    company = []
    for name in sorted_data_company:
        if name['company_name'] not in company:
            company.append(name['company_name'])

    dict_all = {}
    for com in company:
        dict_all[com] = [0, 0]

    for n1 in dict_all:
        for n2 in sorted_data_company:
            if n2['company_name'] == n1:
                dict_all[n1][0] += int(n2['salary'])
                dict_all[n1][1] += 1

    for i in dict_all:
        dict_all[i] = dict_all[i][0]/dict_all[i][1]
    dict_all = sorted(dict_all.items(), key=lambda item: item[1])
    for comp in dict_all:
        print(comp[0])