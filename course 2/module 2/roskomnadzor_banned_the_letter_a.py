sentence = input() + ' запретил букву'
alphabet = [chr(i) for i in range(1072, 1104)]
for letter in alphabet:
    if letter in sentence:
        print(sentence, letter)
        sentence = sentence.replace(letter, '').replace('  ', ' ').strip()
