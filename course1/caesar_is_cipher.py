def cipher(text: str):
    new = []
    for latter in text.split():
        new_latt = ''
        word_lenght = len([c for c in latter if c.isupper() or c.islower()])
        for i in latter:
            if i.isupper():
                new_latt += chr((ord(i) + word_lenght - 65) % 26 + 65)
            elif i.islower():
                new_latt += chr((ord(i) + word_lenght - 97) % 26 + 97)
            else:
                new_latt += i
        new.append(new_latt)
    return ' '.join(new)


text = input()
print(cipher(text))
