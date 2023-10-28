ls = [i.strip('.,!?:;-') for i in input().lower().split()]
ls2 = []
result = {}
ls.sort()

for x in ls:
    if x not in result:
        ls2.append(ls.count(x))
result = dict(zip(ls, ls2))

ans = []
gg = min(result.values())
for k, g in result.items():
    if g == gg:
        ans.append(k)
print(ans[0])
