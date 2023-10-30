cod = 'anton'
n = int(input())
out = []
for i in range(1, n + 1):
    word = input()
    new = ''
    for letter in cod:
        if letter in word:
            new += letter
            word = word[word.find(letter):]

    if new == 'anton':
        out.append(i)
        continue
print(*out)
