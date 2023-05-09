ls = [i for i in input().split(' ')]
ls_output = []
for idx in range(len(ls) + 1):
   new_ls = []
   if ls[idx] == ls[idx + 1]:
       new_ls.append(ls[idx])
   print(new_ls)


