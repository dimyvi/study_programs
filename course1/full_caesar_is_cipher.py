english_alphabet = [chr(i) for i in range(65, 91)]
eng_alf = [chr(j) for j in range(97, 123)]
russian_alphabet = [chr(l) for l in range(1040, 1072)]
rus_alph = [chr(k) for k in range(1072, 1104)]


def encryption(up_lett, loww_lett, step, txt):
    lenght_alph = len(up_lett)
    ls = ''
    for letter in txt:
        if letter.isalpha() and letter == letter.upper():
            ls += up_lett[((up_lett.index(letter) + step) % lenght_alph)]
        elif letter.isalpha() and letter == letter.lower():
            ls += loww_lett[((loww_lett.index(letter) + step) % lenght_alph)]
        else:
            ls += letter
    return ls


def decryption(dec_up_lett, dec_loww_lett, dec_step, dec_txt):
    ls = ''
    lenght_alph2 = len(dec_up_lett)
    for letter in dec_txt:
        if letter.isalpha() and letter == letter.upper():
            ls += dec_up_lett[((dec_up_lett.find(letter) - dec_step) % lenght_alph2)]
        elif letter.isalpha() and letter == letter.lower():
            ls += dec_loww_lett[((dec_loww_lett.find(letter) - dec_step) % lenght_alph2)]
        else:
            ls += letter
    return ls


def start(lng, dir):
    if dir == 'шифровка':
        if lng == 'английский':
            return encryption(english_alphabet, eng_alf, shear_step, text)
        elif lng == 'русский':
            return encryption(russian_alphabet, rus_alph, shear_step, text)
        else:
            return 'произошла ошибка'

    elif dir == 'дешифровка':
        if lng == 'английский':
            return decryption(english_alphabet, eng_alf, shear_step, text)
        elif lng == 'русский':
            return decryption(russian_alphabet, rus_alph, shear_step, text)
        else:
            return 'произошла ошибка'


direction = input('Шифровка или дешифровка? ').lower()
alphabet_language = input('Какой алфавит использовать: русский или английский? ').lower()

shear_step = int(input('Введи шаг сдвига: '))
text = input('Введи текст, который нужно зашифрофать/дешифровать: ')

print(start(alphabet_language, direction))
