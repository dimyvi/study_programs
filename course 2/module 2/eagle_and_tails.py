string = input().upper() + ' '
count = 1
out = 0
for i in range(len(string)):
    if string[i] == 'Р' and string[i+1] == 'Р':
        count += 1
        out = max(count, out)
    elif string[i] == 'О':
        count = 1
        out = max(count, out)

z = 0
for g in string:
    if g.upper() != 'Р':
        z += 1
    if z == len(string):
        out = 0
print(out)