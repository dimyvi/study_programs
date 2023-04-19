def cipher(text: str):
    new = []
    for latter in text.split():
        new_lett = ''
        word_lenght = len([c for c in letter if c.isupper() or c.islower()])
        for i in letter:
            if i.isupper():
                new_lett += chr((ord(i) + word_lenght - 65) % 26 + 65)
            elif i.islower():
                new_lett += chr((ord(i) + word_lenght - 97) % 26 + 97)
            else:
                new_lett += i
        new.append(new_lett)
    return ' '.join(new)


text = input()
print(cipher(text))
