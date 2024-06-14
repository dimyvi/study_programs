import json

with open('data1.json', 'r', encoding='utf-8') as file1, open('data2.json', 'r', encoding='utf-8') as file2:
    data1, data2 = json.load(file1), json.load(file2)
all_data = data1
for d in data2:
    all_data[d] = data2[d]
with open('data_merge.json', 'w', encoding='utf-8') as ans_file:
    json.dump(all_data, ans_file, indent=3)
