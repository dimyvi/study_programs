from random import *

word_list = ['Cлово']


def get_word():
    random_word = choice(word_list).upper()
    return random_word


def play(word):
    word_completion = '_' * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(display_hangman(tries))
    print(word_completion)

    while word_completion.isalpha() == False:
        user_text = input('Введи слово или букву: ').upper()
        if user_text.isalpha():
            if user_text in guessed_words or user_text in guessed_letters:
                print('эта буква или слово уже были')
                continue
        else:
            continue

        if user_text.isalpha() and len(user_text) == 1:
            guessed_letters.append(user_text)
            if user_text not in word:
                tries -= 1
                print(display_hangman(tries))
                if tries == 0:
                    print('Вы проиграли')
                    break
                print('вас осталось', tries, 'попыток')
                continue

            else:
                for i in range(len(word)):
                    if word[i] == user_text:
                        list_output = list(word_completion)
                        list_output[i] = user_text
                        word_completion = "".join(list_output)
                print("Вы угадали букву")
                print(word_completion)
                if word_completion.isalpha():
                    print('Поздравляем, вы выиграли')
                continue

        elif user_text.isalpha() and len(user_text) > 1:
            guessed_words.append(user_text)
            if user_text == word:
                print('Вы угадали слово: ', word)
                word_completion = word
                print('Поздравляем, вы выиграли')
            else:
                tries -= 1
                print(display_hangman(tries))
                if tries == 0:
                    print('Вы проиграли')
                    break
                print(f'Вы не угадали слово, у вас осталось {tries} попыток')

    a = input('Сыграть еще раз? да/нет)\n').lower()
    if a == 'да':
        play(get_word())


def display_hangman(tries):
    stages = [
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / /
        |
        |

        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |     
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    
        |     
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     
        |    
        |       
        |  
        '''
    ]
    return stages[tries]


random_word = get_word()
play(random_word)
