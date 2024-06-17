import json, csv

with open('students.json', 'r', encoding='utf-8') as file:
    data_st = json.load(file)
    ls_ans = []
    for student in data_st:
        ls_st = []
        if student['age'] >= 18 and student['progress'] >= 75:
            ls_st.append([student['name'], student['phone']])
        if len(ls_st) != 0:
            ls_ans.extend(ls_st)
    ls_ans.sort()

columns = ['name', 'phone']
with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(ls_ans)