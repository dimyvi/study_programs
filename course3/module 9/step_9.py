names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

for i in range(len(budgets)):
    box_offices[i] -= budgets[i]
ans_ls = list(zip(names, box_offices))
ans_ls.sort()
for a in ans_ls:
    print(f'{a[0]}: {a[1]}$')