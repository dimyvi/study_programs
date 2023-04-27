from random import *

word_list = ['Cлово']


def get_word():
    random_word = choice(word_list).upper()
    return random_word


def play(word):
    word_completion = '_' * len(word)
    guessed_letters = set()
    guessed_words = []
    tries = 6

    while tries > 0 and word_completion != word:
        print(display_hangman(tries))
        print('отгаданные буквы:', *guessed_letters)
        print(word_completion)

        user_text = input('сюда ')

        while user_text in guessed_letters:
            user_text = input('сюда ')

        guessed_letters.add(user_text)

        if user_text in word:
            print('Yes')
            new_completion = ''
            for i in range(len(word)):
                if user_text == word[i]:
                    new_completion += user_text
                else:
                    new_completion += word_completion[i]
            word_completion = new_completion
        else:
            print('No')
            tries -= 1

    if tries == 0:
        print(display_hangman[tries])
        print('end')
    else:
        print('all', word)


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
