from random import randint
hidden_number = randint(1, 100)
while hidden_number:
    user_num = int(input('Угадай число от 1 до 100: '))
    if user_num > hidden_number:
        print('Слишком много, попробуйте еще раз')
        continue
    elif user_num < hidden_number:
        print('Слишком мало, попробуйте еще раз')
        continue
    else:
        print('Вы угадали, поздравляем!')
        break


