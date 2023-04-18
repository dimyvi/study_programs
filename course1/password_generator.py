from random import *

dights = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
cg = 'il1Lo0O'
chars = ''

number_of_passwords = int(input('How many passwords to generate? '))
lenght_of_one_password = int(input('How long is the paassword? '))

nubers = input('Will there benumbers in the password? yes/no: ')
if nubers.lower() == 'yes':
    chars += dights
capital = input('Will there be capital letters in the password? yes/no: ')
if capital.lower() == 'yes':
    chars += uppercase_letters
lowercase = input('Will there be lowercase letters in the password? yes/no: ')
if lowercase.lower() == 'yes':
    chars += lowercase_letters
spacial_symbols = input('Will there be spacial symbols in the password? yes/no: ')
if spacial_symbols.lower() == 'yes':
    chars += punctuation
what = input("Should ambiguous characters be excluded? 'il1Lo0O?' yes/no: ")
if what.lower() == 'yes':
    chars += cg

print('Password options:')
for _ in range(number_of_passwords):
    print(*sample(chars, lenght_of_one_password), sep='')
