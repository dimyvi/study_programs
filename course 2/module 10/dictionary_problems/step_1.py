dictionary = {}
for _ in range(int(input())):
    s = input().split(':')
    dictionary.setdefault(str(s[0]).lower(), str(s[1]).lstrip())

for _ in range(int(input())):
    s1 = input().lower()
    if s1 in dictionary:
        print(dictionary[s1])
    else:
        print('Не найдено')

