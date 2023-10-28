result = {}
string = input().split(' ')
ls = []
for x in string:
    if x not in result:
        result.setdefault(x, [j for j in range(string.count(x))])

ls_ans = []
for k in string:
    for k1 in result.items():
        if k == k1[0]:
            if k1[1][0] != 0:
                ls_ans.append(str(k1[0]) + '_' + str(k1[1][0]))
            else:
                ls_ans.append(k1[0])
            del k1[1][0]
print(*ls_ans)