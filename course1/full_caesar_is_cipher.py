english_alphabet = [chr(i) for i in range(65, 91)]
eng_alf = [chr(j) for j in range(97, 123)]
ruassian_alphabet = [chr(l) for l in range(1040, 1072)]
rus_alph = [chr(k) for k in range(1073, 1104)]


def encryption(up_lett, loww_lett, step, txt):
    lenght_alph = len(up_lett)
    ls = ''
    for letters in txt:
        if letters.isalpha() and letters == letters.upper():
            ls += letters + letters[((up_lett.index(letters) + step) % lenght_alph)]
        elif letters.isalpha() and letters == letters.lower():
            ls += letters + letters[((loww_lett.index(letters) + step) % lenght_alph)]
        else:
            ls += letters
    return ls


def decryption(dec_up_lett, dec_loww_lett, dec_step, dec_txt):
    ls2 = ''
    lenght_alph2 = len(dec_up_lett)
    for letters2 in dec_txt:
        if letters2.isalpha() and letters2 == letters2.upper():
            ls2 += letters2 + letters2[((dec_up_lett.index(letters2) - dec_step) % lenght_alph2)]
        elif letters2.isalpha() and letters2 == letters2.lower():
            ls2 += letters2 + letters2[((dec_loww_lett.index(letters2) - dec_step) % lenght_alph2)]
        else:
            ls2 += letters2
    return ls2


def start(lng, dir):
    if dir == 'шифровка':
        if lng == 'английский':
            encryption(english_alphabet, eng_alf, shear_step, text)
        elif lng == 'русский':
            encryption(ruassian_alphabet, rus_alph, shear_step, text)
        else:
            print('произошла ошибка')

    elif dir == 'дешифровка':
        if lng == 'английский':
            decryption(english_alphabet, eng_alf, shear_step, text)
        elif lng == 'русский':
            decryption(ruassian_alphabet, rus_alph, shear_step, text)
        else:
            print('произошла ошибка')


diraction = input('Шифровка или дешифровка? ').lower()
alphabet_language = input('Какой алфавит использовать: русский или английский? ').lower()

shear_step = int(input('Введи шаг сдвига: '))
text = input('Введи текст, который нужно зашифрофать/дешифровать: ')

start(alphabet_language, diraction)
print(ls)
print(ls2)
