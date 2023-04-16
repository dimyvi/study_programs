import random
def start():
    print('Введи верхнюю границу цисла для игры')
    limit = int(input())
    global rand_num
    rand_num = random.randint(1, limit)
    print('Добро пожаловать в числовую угадайку!\nВведи число [1:', limit,']', sep = '')

def is_valid(number):
    return number.isdigit() and 1 <= int(number) <= 100

def not_right():
    while True:
        numm = input()
        if is_valid(numm):
            return int(numm)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def again():
    while True:
        answer = input()
        if answer == 'yes':
            start()
            normal()
        elif answer == 'no':
            print('оченнь жаль, пока')
            break
        else:
            print("Напиши 'no' если не хочешь играть зоново, 'yes' если хочешь")
def normal():
    count = 0
    while True:
        number = not_right()
        if number < rand_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif number > rand_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        else:
            count += 1
            print('Вы угадали, поздравляем!')
            print('Общее количество попыток:', count)
            print('хочешь еще сыграть? yes/no')
            break

start()
normal()
again()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
