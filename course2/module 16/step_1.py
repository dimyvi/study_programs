s = input()
f = open(s,  'r', encoding='utf-8')
for i in f:
    print(i.rstrip())
f.close()