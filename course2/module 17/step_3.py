from random import choice
f = open('lines.txt', encoding='utf-8').readlines()
print(choice(f).rstrip())